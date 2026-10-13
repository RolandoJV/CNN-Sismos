"""Inspeccion del dataset del proyecto CNN-Sismos.

Uso:
    python test.py             # analiza la carpeta del dataset autodetectada
    python test.py <carpeta>   # analiza una carpeta concreta

Genera un perfil de cada archivo (dimensiones, columnas, distribucion de la
etiqueta, duplicados, rangos, cabecera miniSEED), lo imprime por consola y lo
guarda en `resumen_dataset.md` en formato Markdown, listo para pegar a Claude
como contexto del proyecto.

Solo usa la libreria estandar: el .venv del proyecto aun no tiene pandas.
"""

from __future__ import annotations

import csv
import struct
import sys
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
ARCHIVO_SALIDA = RAIZ / "resumen_dataset.md"

# Formato conocido de cada archivo. sep=None -> campos por espacios en blanco.
# columnas_interes: columnas cuya distribucion de valores se reporta.
CONFIG_ARCHIVOS: dict[str, dict] = {
    "allhitexp.csv": {
        "sep": None,
        "encabezado": False,
        "descripcion": "Ejemplos 'con golpe' (sismo), etiqueta 1 en la ultima columna",
    },
    "nohitexp.csv": {
        "sep": None,
        "encabezado": False,
        "descripcion": "Ejemplos 'sin golpe' (ruido), etiqueta 0 en la ultima columna",
    },
    "categoria_sismos.csv": {
        "sep": ",",
        "encabezado": True,
        "descripcion": "Exportacion CSV de la traza miniSEED (muestra parcial de la senal)",
    },
    "sismos.csv": {
        "sep": ",",
        "encabezado": True,
        "descripcion": "Catalogo de sismos 2023 (fecha, hora, epicentro, magnitud, estacion)",
    },
    "sismos_en_tiempo_real.csv": {
        "sep": ",",
        "encabezado": True,
        "descripcion": "Mediciones recientes por estacion (amax, mean)",
    },
    "winequality-red.csv": {
        "sep": ";",
        "encabezado": True,
        "columnas_interes": ["quality"],
        "descripcion": "Dataset UCI de vinos tintos (sin relacion con los sismos)",
    },
    "wilber-stations.txt": {
        "sep": "|",
        "encabezado": True,
        "columnas_interes": ["Net"],
        "descripcion": "Estaciones que registraron un evento (exportado de IRIS Wilber)",
    },
}

# Compresiones miniSEED comunes (blockette 1000).
ENCODINGS_MINISEED = {0: "ASCII", 1: "INT16", 3: "INT32", 4: "FLOAT32",
                      5: "FLOAT64", 10: "STEIM1", 11: "STEIM2"}
EXTENSIONES_TABLA = {".csv", ".txt", ".tsv"}


def localizar_carpeta(argumento: str | None) -> Path:
    """Devuelve la carpeta del dataset (tolera renombres del ZIP descargado)."""
    if argumento:
        ruta = Path(argumento)
        if not ruta.is_dir():
            raise SystemExit(f"La carpeta indicada no existe: {ruta}")
        return ruta
    for carpeta in sorted(RAIZ.glob("Dataset*")):
        if not carpeta.is_dir():
            continue
        if (carpeta / "Dataset").is_dir():  # patrion del ZIP de Google Drive
            return carpeta / "Dataset"
        if next(carpeta.glob("*.csv"), None) is not None:
            return carpeta
    raise SystemExit("No se encontro la carpeta del dataset (se esperaba Dataset*/Dataset).")


def formato_inferido(ruta: Path) -> dict:
    """Configuracion de respaldo para archivos no listados en CONFIG_ARCHIVOS."""
    try:
        with ruta.open("r", encoding="utf-8-sig", errors="replace") as fh:
            primera = fh.readline()
    except OSError:
        primera = ""
    if "|" in primera:
        sep = "|"
    elif ";" in primera:
        sep = ";"
    elif "," in primera:
        sep = ","
    else:
        sep = None
    con_encabezado = False
    if sep is not None:
        try:
            [float(c.strip().strip('"')) for c in primera.strip().split(sep)]
        except ValueError:
            con_encabezado = True  # primera fila no numerica -> hay encabezado
    return {"sep": sep, "encabezado": con_encabezado}


def leer_tabla(ruta: Path, sep: str | None, con_encabezado: bool) -> tuple[list[str], list[list[str]]]:
    """Lee un archivo de texto como tabla. Devuelve (encabezado, filas)."""
    with ruta.open("r", encoding="utf-8-sig", errors="replace", newline="") as fh:
        if sep is None:  # formato allhitexp/nohitexp: campos por espacios
            filas = [ln.split() for ln in fh if ln.strip()]
        else:
            filas = [f for f in csv.reader(fh, delimiter=sep) if any(c.strip() for c in f)]
    if not filas:
        return [], []
    if con_encabezado:
        return [c.strip() for c in filas[0]], filas[1:]
    return [], filas


def tabla_md(nombres: list[str], filas: list[list[str]]) -> list[str]:
    """Construye una tabla Markdown con las filas dadas."""
    lineas = ["| " + " | ".join(nombres) + " |", "|" + "---|" * len(nombres)]
    for fila in filas:
        celdas = (list(fila) + [""] * len(nombres))[: len(nombres)]
        lineas.append("| " + " | ".join(c.strip() for c in celdas) + " |")
    return lineas


def rangos_numericos(filas: list[list[str]], nombres: list[str]) -> list[str]:
    """Minimo y maximo por columna de una matriz numerica sin encabezado."""
    n_cols = len(nombres)
    mins = [float("inf")] * n_cols
    maxs = [float("-inf")] * n_cols
    no_numericos = 0
    for fila in filas:
        for i, campo in enumerate(fila[:n_cols]):
            try:
                v = float(campo)
            except ValueError:
                no_numericos += 1
                continue
            if v < mins[i]:
                mins[i] = v
            if v > maxs[i]:
                maxs[i] = v
    if no_numericos:
        return [f"- **Valores no numericos:** {no_numericos:,} (no se calcularon rangos)"]
    resumen = ", ".join(f"`{nombres[i]}` [{mins[i]:g} a {maxs[i]:g}]" for i in range(n_cols))
    return [f"- **Rango por columna:** {resumen}"]


def perfil_tabla(ruta: Path) -> tuple[list[str], dict]:
    """Perfila un archivo tabular. Devuelve (lineas Markdown, estadisticas)."""
    cfg = dict(CONFIG_ARCHIVOS.get(ruta.name) or formato_inferido(ruta))
    sep = cfg.get("sep")
    con_encabezado = bool(cfg.get("encabezado"))
    encabezado, filas = leer_tabla(ruta, sep, con_encabezado)
    if not filas:
        return [f"## {ruta.name}", "- (archivo sin filas de datos)"], {}

    anchos = Counter(len(f) for f in filas)
    n_cols = anchos.most_common(1)[0][0]
    if encabezado and len(encabezado) == n_cols:
        nombres = [h or f"col{i}" for i, h in enumerate(encabezado)]
    else:
        nombres = [f"col{i}" for i in range(n_cols)]

    stats: dict = {"filas": len(filas), "n_cols": n_cols}
    lineas = [f"## {ruta.name}"]
    if cfg.get("descripcion"):
        lineas.append(f"- **Que es:** {cfg['descripcion']}")
    tipo = "valores separados por espacios en blanco" if sep is None else f"separador `{sep}`"
    detalle = ", con encabezado" if con_encabezado else ", sin encabezado (matriz numerica)"
    lineas.append(f"- **Formato:** texto ({tipo}{detalle})")
    lineas.append(f"- **Dimensiones:** {len(filas):,} filas x {n_cols} columnas")
    if len(anchos) > 1:
        lineas.append(f"- **Aviso:** filas con distinto numero de campos: {dict(anchos)}")

    vacios = sum(1 for f in filas for c in f if not c.strip())
    lineas.append(f"- **Campos vacios:** {vacios:,}")
    duplicados = len(filas) - len(set(tuple(f) for f in filas))
    lineas.append(f"- **Filas duplicadas exactas:** {duplicados:,}")

    if not con_encabezado:
        # Matrices de features: perfil numerico + etiqueta en la ultima columna
        lineas += rangos_numericos(filas, nombres)
        etiqueta = Counter(f[-1] for f in filas if f)
        stats["etiqueta"] = etiqueta
        dist = ", ".join(f"`{v}` -> {c:,} ({c / len(filas) * 100:.1f} %)"
                         for v, c in sorted(etiqueta.items()))
        lineas.append(f"- **Etiqueta (ultima columna, `{nombres[-1]}`):** {dist}")

    distribuciones: dict[str, Counter] = {}
    for col in cfg.get("columnas_interes", []):
        if col in nombres:
            i = nombres.index(col)
            dist_col = Counter(f[i] for f in filas if i < len(f))
            distribuciones[col] = dist_col
            resumen = ", ".join(f"`{v}` -> {c:,}" for v, c in sorted(dist_col.items()))
            lineas.append(f"- **Distribucion de `{col}`:** {resumen}")
    if distribuciones:
        stats["distribuciones"] = distribuciones

    if len(filas) <= 10:
        lineas.append(f"- **Contenido completo ({len(filas)} filas):**")
        lineas += tabla_md(nombres, filas)
    else:
        lineas.append(f"- **Primeras 3 filas de {len(filas):,}:**")
        lineas += tabla_md(nombres, filas[:3])
    return lineas, stats


def perfil_miniseed(ruta: Path) -> tuple[list[str], dict]:
    """Decodifica la cabecera fija miniSEED 2.x del primer registro."""
    with ruta.open("rb") as fh:
        enc = fh.read(64)
    if len(enc) < 48:
        raise ValueError("demasiado corto para ser miniSEED")
    if enc[6:7] not in (b"D", b"Q", b"R", b"M"):
        raise ValueError("sin indicador de registro miniSEED 2.x")

    estacion = enc[8:13].decode("ascii", "replace").strip()
    loc = enc[13:15].decode("ascii", "replace").strip() or "--"
    canal = enc[15:18].decode("ascii", "replace").strip()
    red = enc[18:20].decode("ascii", "replace").strip()
    anio, dia = struct.unpack(">HH", enc[20:24])
    h, m, s = enc[24], enc[25], enc[26]
    micro = struct.unpack(">H", enc[28:30])[0]
    n_muestras = struct.unpack(">H", enc[30:32])[0]
    factor, mult = struct.unpack(">hh", enc[32:36])
    # Regla SEED: factor>0 -> tasa=factor*mult ; factor<0 -> tasa=-mult/factor
    if factor > 0:
        tasa = float(factor * mult)
    elif factor < 0:
        tasa = -mult / factor
    else:
        tasa = 0.0
    inicio = datetime(anio, 1, 1) + timedelta(days=dia - 1, hours=h, minutes=m, seconds=s)
    inicio_str = inicio.strftime("%Y-%m-%d %H:%M:%S") + f".{micro:04d}"

    # Blockette 1000 (si existe): formato de compresion y tamano de registro
    compresion = None
    tam_registro = 512
    off_bloq = struct.unpack(">H", enc[46:48])[0]
    if 48 <= off_bloq <= len(enc) - 8:
        tipo = struct.unpack(">H", enc[off_bloq : off_bloq + 2])[0]
        if tipo == 1000:
            cod = enc[off_bloq + 4]
            compresion = ENCODINGS_MINISEED.get(cod, f"formato {cod}")
            tam_registro = 2 ** enc[off_bloq + 6]

    tam = ruta.stat().st_size
    n_registros, resto = divmod(tam, tam_registro)
    lineas = [
        f"## {ruta.name} -- traza sismica en miniSEED 2.x",
        f"- **Que es:** forma de onda continua de la estacion **{estacion}** "
        f"(red `{red}`, canal `{canal}`, ubicacion `{loc}`). "
        "El nombre codifica `RED.ESTACION.UBICACION.CANAL.D.ANO.DIA`.",
        f"- **Primer registro:** {inicio_str} UTC | **Muestras/registro:** {n_muestras:,} "
        f"| **Tasa:** {tasa:g} Hz",
    ]
    if compresion:
        lineas.append(f"- **Compresion:** {compresion} (blockette 1000)")
    if resto == 0:
        lineas.append(f"- **Tamano:** {tam:,} bytes = {n_registros:,} registros de {tam_registro} bytes")
        if tasa > 0:
            muestras = n_registros * n_muestras
            horas = muestras / tasa / 3600
            lineas.append(f"- **Muestras totales (estimado, registros completos):** "
                          f"{muestras:,} (~{horas:.1f} h)")
    else:
        lineas.append(f"- **Tamano:** {tam:,} bytes (no es multiplo exacto de {tam_registro})")
    lineas.append("- **Nota:** la senal completa se lee con `obspy.read()`, no con pandas "
                  "(miniSEED es un formato binario de sismologia).")
    return lineas, {"tipo": "miniseed", "tasa": tasa, "estacion": estacion}


def analizar(ruta: Path) -> tuple[list[str], dict]:
    """Analiza un archivo cualquiera: tabla de texto o miniSEED."""
    if ruta.suffix.lower() not in EXTENSIONES_TABLA:
        try:
            return perfil_miniseed(ruta)
        except ValueError:
            pass  # no es miniSEED; intentar leerlo como texto
    try:
        return perfil_tabla(ruta)
    except Exception as exc:  # error-first: reportar y seguir con los demas
        return [f"## {ruta.name}", f"- **ERROR al procesar:** {exc}"], {}


def panorama(stats: dict[str, dict]) -> list[str]:
    """Sintesis global del dataset para dar contexto al modelo."""
    lineas = ["## Panorama general del dataset"]
    hit, nohit = stats.get("allhitexp.csv"), stats.get("nohitexp.csv")
    if hit and nohit and hit.get("etiqueta") and nohit.get("etiqueta"):
        total = hit["filas"] + nohit["filas"]
        pos = sum(c for v, c in hit["etiqueta"].items() if v != "0")
        neg = sum(c for v, c in nohit["etiqueta"].items() if v == "0")
        ratio = neg // pos if pos else 0
        lineas.append(
            f"- **Par de entrenamiento hit/nohit** ({hit['n_cols'] - 1} features + etiqueta): "
            f"{total:,} ejemplos, {pos:,} con sismo (etiqueta 1) vs {neg:,} de ruido (etiqueta 0) "
            f"-> desbalance ~1:{ratio:,} ({pos / total * 100:.2f} % positivos).")
    miniseed = [(n, st) for n, st in stats.items() if st.get("tipo") == "miniseed"]
    if miniseed:
        nombres = ", ".join(f"{st['estacion']} a {st['tasa']:g} Hz" for _, st in miniseed)
        lineas.append(f"- **Traza sismica cruda** en miniSEED: {nombres} (red sismica cubana CW).")
    wilber = stats.get("wilber-stations.txt", {})
    if wilber.get("distribuciones", {}).get("Net"):
        redes = wilber["distribuciones"]["Net"]
        resumen = ", ".join(f"{k}={v}" for k, v in redes.most_common())
        lineas.append(f"- **Estaciones que registraron un evento:** {wilber['filas']:,} ({resumen}).")
    if "winequality-red.csv" in stats:
        lineas.append("- **winequality-red.csv** es el dataset de vinos tintos de UCI; "
                      "no aporta nada al proyecto de sismos (parece restante de un tutorial).")
    lineas.append("- **sismos.csv**, **sismos_en_tiempo_real.csv** y **categoria_sismos.csv** "
                  "son catalogos/consultas pequenos (decenas de filas), no datos de entrenamiento.")
    return lineas


def tam_legible(n: float) -> str:
    """Tamano de archivo en unidades legibles (B, KB, MB...)."""
    for unidad in ("B", "KB", "MB", "GB"):
        if n < 1024 or unidad == "GB":
            return f"{n:,.0f} {unidad}" if unidad == "B" else f"{n:.1f} {unidad}"
        n /= 1024
    return f"{n:.1f} GB"


def main(argv: list[str]) -> int:
    # La consola de Windows usa cp1252 al redirigir; forzar UTF-8 evita
    # UnicodeEncodeError con acentos y flechas.
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):
            pass

    carpeta = localizar_carpeta(argv[1] if len(argv) > 1 else None)
    archivos = sorted(p for p in carpeta.iterdir() if p.is_file())
    if not archivos:
        print(f"No hay archivos que analizar en: {carpeta}")
        return 1

    doc = [
        "# Dataset del proyecto CNN-Sismos",
        f"Generado por `test.py` el {datetime.now():%Y-%m-%d %H:%M}. "
        f"Carpeta analizada: `{carpeta}`. Archivos: {len(archivos)}.",
        "",
        "## Inventario de archivos",
        "| Archivo | Tamano |",
        "|---|---|",
    ]
    for ruta in archivos:
        try:
            tam = tam_legible(ruta.stat().st_size)
        except OSError:
            tam = "?"
        doc.append(f"| {ruta.name} | {tam} |")

    stats: dict[str, dict] = {}
    for ruta in archivos:
        lineas, st = analizar(ruta)
        doc.append("")
        doc += lineas
        if st:
            stats[ruta.name] = st

    doc.append("")
    doc += panorama(stats)
    texto = "\n".join(doc) + "\n"

    print(texto)
    try:
        ARCHIVO_SALIDA.write_text(texto, encoding="utf-8")
        print(f"(Resumen guardado tambien en: {ARCHIVO_SALIDA})")
    except OSError as exc:
        print(f"(No se pudo guardar el resumen en disco: {exc})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
