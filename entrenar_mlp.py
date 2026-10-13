"""Etapa 2 del informe: clasificacion hit/nohit con MLP.

Uso: python entrenar_mlp.py

Preparacion de datos (requisitos del informe):
1. Deduplicacion de filas exactas ANTES de dividir (sin fuga train/test).
2. Eliminacion de vectores ambiguos (mismas caracteristicas con etiqueta 1
   y 0 a la vez en los dos archivos).
3. Validacion cruzada estratificada de 5 pliegues: con solo ~296 positivos,
   una unica division daba resultados muy variables entre ejecuciones;
   los 5 pliegues permiten reportar media y desviacion tipica.
4. Metricas para datos desbalanceados: recall, precision, F1 y PR-AUC.
   La exactitud solo se reporta como referencia (predecir siempre "ruido"
   daria ~99,5 %).

Modelos evaluados (mismos pliegues para todos):
   A) MLP sin tratar el desbalance                 -> referencia
   B) MLP con submuestreo 1:10 en train            -> alternativa a pesos
   C) Regresion logistica class_weight='balanced'  -> pesos por clase
   D) MLP submuestreo + umbral max-F1 (validacion) -> umbral de decision

Salida: resultados_etapa2.md (media +/- desviacion tipica por modelo y
matrices de confusion acumuladas sobre los 5 pliegues).
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    confusion_matrix,
    precision_recall_curve,
    precision_recall_fscore_support,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from test import localizar_carpeta

SEMILLA = 42
N_FOLDS = 5
VAL_SIZE = 0.20       # parte interna del train usada solo para el umbral (D)
RATIO_NEGATIVOS = 10  # submuestreo: hasta 10 negativos por cada positivo
SALIDA = Path(__file__).resolve().parent / "resultados_etapa2.md"

NOMBRE_A = "A. MLP sin tratar el desbalance (referencia)"
NOMBRE_B = f"B. MLP con submuestreo 1:{RATIO_NEGATIVOS} en train"
NOMBRE_C = "C. Regresion logistica con pesos por clase (balanced)"
NOMBRE_D = f"D. MLP submuestreo 1:{RATIO_NEGATIVOS} + umbral max-F1"
CLAVES = ["precision", "recall", "f1", "pr_auc", "roc_auc", "exactitud"]


def cargar_datos(carpeta: Path) -> tuple[pd.DataFrame, dict]:
    """Carga hit+nohit y devuelve tambien estadisticas de depuracion."""
    hit = pd.read_csv(carpeta / "allhitexp.csv", sep=r"\s+", header=None)
    nohit = pd.read_csv(carpeta / "nohitexp.csv", sep=r"\s+", header=None)
    cols = [f"f{i}" for i in range(hit.shape[1] - 1)] + ["etiqueta"]
    hit.columns = cols
    nohit.columns = cols
    filas_orig = len(hit) + len(nohit)

    dup = int(hit.duplicated().sum()) + int(nohit.duplicated().sum())
    print(f"Filas originales: {len(hit):,} hit + {len(nohit):,} nohit = {filas_orig:,}")
    print(f"Duplicados exactos: {dup:,}")

    df = pd.concat([hit, nohit], ignore_index=True).drop_duplicates()
    # Vectores de caracteristicas presentes con etiqueta 1 y 0 a la vez:
    # son ambiguos y se eliminan (no hay forma de saber cual etiqueta es la buena)
    fcols = cols[:-1]
    n_etiquetas = df.groupby(fcols)["etiqueta"].transform("nunique")
    mascara_conflicto = n_etiquetas > 1
    conflicto_vec = df.loc[mascara_conflicto, fcols].drop_duplicates()
    conflicto_filas = int(mascara_conflicto.sum())
    df = df[~mascara_conflicto].reset_index(drop=True)
    print(f"Vectores con etiqueta opuesta en ambos archivos: "
          f"{len(conflicto_vec):,} ({conflicto_filas:,} filas eliminadas)")

    n_pos = int((df["etiqueta"] == 1).sum())
    stats = {
        "orig_pos": len(hit),
        "orig_neg": len(nohit),
        "filas_orig": filas_orig,
        "dup": dup,
        "conflicto": len(conflicto_vec),
        "conflicto_filas": conflicto_filas,
        "filas_dup": len(df),
        "pos": n_pos,
        "neg": len(df) - n_pos,
    }
    print(f"Dataset final tras depurar: {stats['filas_dup']:,} filas "
          f"({n_pos:,} positivas, {stats['neg']:,} negativas)")
    return df, stats


def submuestrear(X: np.ndarray, y: np.ndarray, ratio: int, semilla: int) -> tuple[np.ndarray, np.ndarray]:
    """Submuestreo aleatorio de la clase negativa hasta `ratio` por positivo."""
    rng = np.random.default_rng(semilla)
    idx_pos = np.flatnonzero(y == 1)
    idx_neg = np.flatnonzero(y == 0)
    k = min(len(idx_neg), len(idx_pos) * ratio)
    elegidos = rng.choice(idx_neg, size=k, replace=False)
    seleccion = np.concatenate([idx_pos, elegidos])
    rng.shuffle(seleccion)
    return X[seleccion], y[seleccion]


def umbral_optimo(y_true: np.ndarray, scores: np.ndarray) -> float:
    """Umbral que maximiza F1 en validacion; el pliegue de test no participa."""
    precision, recall, umbrales = precision_recall_curve(y_true, scores)
    p, r = precision[:-1], recall[:-1]  # la ultima entrada no tiene umbral
    with np.errstate(divide="ignore", invalid="ignore"):
        f1 = np.where(p + r > 0, 2 * p * r / (p + r), 0.0)
    return float(umbrales[int(np.argmax(f1))])


def nuevo_mlp() -> Pipeline:
    return Pipeline([
        ("escala", StandardScaler()),
        ("modelo", MLPClassifier(
            hidden_layer_sizes=(64, 32), activation="relu", solver="adam",
            max_iter=400, early_stopping=True, validation_fraction=0.1,
            n_iter_no_change=20, random_state=SEMILLA,
        )),
    ])


def nuevo_logreg() -> Pipeline:
    return Pipeline([
        ("escala", StandardScaler()),
        ("modelo", LogisticRegression(
            max_iter=1000, class_weight="balanced", random_state=SEMILLA,
        )),
    ])


def metricas(y_true: np.ndarray, y_score: np.ndarray, umbral: float) -> dict:
    """Metricas de desbalance con distribucion natural de clases."""
    y_pred = (y_score >= umbral).astype(int)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, pos_label=1, average="binary", zero_division=0,
    )
    return {
        "umbral": umbral,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "pr_auc": average_precision_score(y_true, y_score),
        "roc_auc": roc_auc_score(y_true, y_score),
        "exactitud": float((y_pred == y_true).mean()),
        "cm": confusion_matrix(y_true, y_pred, labels=[0, 1]),
    }


def agregar(nombre: str, registros: list[dict]) -> dict:
    """Agrega los registros de los pliegues: media +/- desviacion tipica."""
    resumen: dict = {"nombre": nombre}
    for k in CLAVES:
        vals = np.array([r[k] for r in registros], dtype=float)
        resumen[k] = (float(vals.mean()),
                      float(vals.std(ddof=1)) if len(vals) > 1 else 0.0)
    umb = np.array([r["umbral"] for r in registros], dtype=float)
    resumen["umbral"] = (float(umb.mean()), float(umb.min()), float(umb.max()))
    cm = np.zeros((2, 2), dtype=np.int64)
    for r in registros:
        cm += r["cm"]
    resumen["cm"] = cm
    resumen["n_folds"] = len(registros)
    return resumen


def md_resultados(stats: dict, resumenes: list[dict]) -> str:
    prevalencia = stats["pos"] / stats["filas_dup"]
    lineas = [
        "# Etapa 2 — Resultados: clasificacion hit/nohit con validacion cruzada",
        "",
        f"Generado por `entrenar_mlp.py` el {datetime.now():%Y-%m-%d %H:%M}.",
        "",
        "## Datos (depuracion previa)",
        "",
        f"- Originales: {stats['filas_orig']:,} filas "
        f"({stats['orig_pos']:,} sismo / {stats['orig_neg']:,} ruido).",
        f"- Duplicados exactos eliminados: {stats['dup']:,}.",
        f"- Vectores ambiguos (etiqueta 1 y 0 a la vez): {stats['conflicto']:,} "
        f"({stats['conflicto_filas']:,} filas eliminadas).",
        f"- Dataset final: {stats['filas_dup']:,} filas "
        f"({stats['pos']:,} sismo / {stats['neg']:,} ruido), "
        f"{prevalencia * 100:.2f} % de positivos.",
        "",
        "## Metodologia",
        "",
        f"- Validacion cruzada estratificada de {N_FOLDS} pliegues "
        f"(semilla {SEMILLA}): cada pliegue entrena con el 80 % y evalua en "
        "el 20 % restante, conservando la proporcion natural de clases.",
        f"- Submuestreo 1:{RATIO_NEGATIVOS} aplicado SOLO a los datos de "
        "entrenamiento de los modelos B y D (el test de cada pliegue nunca "
        "se re muestrea).",
        "- El umbral del modelo D se elige en una validacion interna "
        "(20 % estratificado del train de cada pliegue) maximizando F1: el "
        "pliegue de test no participa en ninguna decision.",
        f"- Referencia de azar: PR-AUC ~ {prevalencia:.3f} (proporcion de "
        f"positivos); predecir siempre 'ruido' daria exactitud ~ "
        f"{1 - prevalencia:.3f}.",
        "",
        f"## Resultados (media +/- desviacion tipica sobre {N_FOLDS} pliegues)",
        "",
        "| Modelo | Precision | Recall | F1 | PR-AUC | ROC-AUC | Exactitud* |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in resumenes:
        celdas = " | ".join(
            f"{r[k][0]:.3f} ± {r[k][1]:.3f}" for k in
            ["precision", "recall", "f1", "pr_auc", "roc_auc", "exactitud"]
        )
        lineas.append(f"| {r['nombre']} | {celdas} |")
    lineas += [
        "",
        f"\\* La exactitud NO es valida como metrica principal aqui: "
        f"predecir siempre 'ruido' rondaria {1 - prevalencia:.3f}.",
        "",
        "## Umbrales de decision",
        "",
    ]
    for r in resumenes:
        media, mn, mx = r["umbral"]
        if abs(mx - mn) < 1e-9:
            lineas.append(f"- {r['nombre']}: umbral {media:.3f} (fijo).")
        else:
            lineas.append(f"- {r['nombre']}: media {media:.3f} "
                          f"(rango {mn:.3f}-{mx:.3f} entre pliegues).")
    lineas += [
        "",
        "## Matriz de confusion acumulada "
        "(cada fila evaluada exactamente una vez)",
        "",
        "| Modelo | VN | FP | FN | VP |",
        "|---|---|---|---|---|",
    ]
    for r in resumenes:
        (tn, fp), (fn, tp) = r["cm"].tolist()
        lineas.append(f"| {r['nombre']} | {tn:,} | {fp:,} | {fn:,} | {tp:,} |")
    lineas += [
        "",
        "## Condiciones de la ejecucion",
        "",
        f"- scikit-learn {sklearn.__version__}, numpy {np.__version__}, "
        f"pandas {pd.__version__}, semilla {SEMILLA}.",
        "- MLP: capas (64, 32), ReLU, Adam, early stopping, max_iter=400; "
        "StandardScaler ajustado solo en los datos de entrenamiento de cada "
        "pliegue.",
        "- Regresion logistica: class_weight='balanced' (pesos por clase) "
        "sobre todo el train del pliegue, sin submuestrear.",
        "- Evaluacion de las variantes A-C con umbral 0.5.",
        "",
    ]
    return "\n".join(lineas)


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):
            pass

    carpeta = localizar_carpeta(argv[1] if len(argv) > 1 else None)
    df, stats = cargar_datos(carpeta)
    X = df.iloc[:, :-1].to_numpy(dtype=float)
    y = df.iloc[:, -1].to_numpy(dtype=int)

    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEMILLA)
    registros: dict[str, list[dict]] = {n: [] for n in
                                        [NOMBRE_A, NOMBRE_B, NOMBRE_C, NOMBRE_D]}

    for i, (itr, ite) in enumerate(skf.split(X, y), 1):
        X_tr, X_te = X[itr], X[ite]
        y_tr, y_te = y[itr], y[ite]
        print(f"Pliegue {i}/{N_FOLDS}: train {len(itr):,} "
              f"({int(y_tr.sum()):,} pos) | test {len(ite):,} "
              f"({int(y_te.sum()):,} pos)", flush=True)

        # A) MLP sin tratar el desbalance
        mlp_a = nuevo_mlp()
        mlp_a.fit(X_tr, y_tr)
        registros[NOMBRE_A].append(
            metricas(y_te, mlp_a.predict_proba(X_te)[:, 1], 0.5))

        # B) MLP con submuestreo 1:10 solo en train
        X_sub, y_sub = submuestrear(X_tr, y_tr, RATIO_NEGATIVOS, SEMILLA + i)
        mlp_b = nuevo_mlp()
        mlp_b.fit(X_sub, y_sub)
        registros[NOMBRE_B].append(
            metricas(y_te, mlp_b.predict_proba(X_te)[:, 1], 0.5))

        # C) Regresion logistica con pesos por clase
        log_c = nuevo_logreg()
        log_c.fit(X_tr, y_tr)
        registros[NOMBRE_C].append(
            metricas(y_te, log_c.predict_proba(X_te)[:, 1], 0.5))

        # D) MLP submuestreado + umbral max-F1 elegido en validacion interna
        X_in, X_v, y_in, y_v = train_test_split(
            X_tr, y_tr, test_size=VAL_SIZE, random_state=SEMILLA + i,
            stratify=y_tr,
        )
        X_in_sub, y_in_sub = submuestrear(
            X_in, y_in, RATIO_NEGATIVOS, SEMILLA + i)
        mlp_d = nuevo_mlp()
        mlp_d.fit(X_in_sub, y_in_sub)
        t_opt = umbral_optimo(y_v, mlp_d.predict_proba(X_v)[:, 1])
        registros[NOMBRE_D].append(
            metricas(y_te, mlp_d.predict_proba(X_te)[:, 1], t_opt))

        ultimos = " | ".join(
            f"{n[0]}:F1={registros[n][-1]['f1']:.3f}" for n in registros)
        print(f"  {ultimos}", flush=True)

    resumenes = [agregar(n, registros[n]) for n in registros]
    texto = md_resultados(stats, resumenes)
    SALIDA.write_text(texto, encoding="utf-8")

    print("\n=== Resumen (media +/- desviacion, 5 pliegues) ===")
    for r in resumenes:
        print(f"{r['nombre']}: F1={r['f1'][0]:.3f}±{r['f1'][1]:.3f} "
              f"recall={r['recall'][0]:.3f} precision={r['precision'][0]:.3f} "
              f"PR-AUC={r['pr_auc'][0]:.3f}")
    print(f"\nResultados guardados en: {SALIDA}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
