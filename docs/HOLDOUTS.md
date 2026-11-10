# Registro de holdouts — RONIN-10M

Este documento es el índice histórico de las evaluaciones de RONIN-10M. Los enlaces se incorporan automáticamente cuando termina un workflow cuyo nombre contiene `holdout`.

- **Ejecución:** enlace a los logs y a la página de artefactos de GitHub Actions.
- **Artefactos:** nombre de cada artefacto no expirado, con la fecha de expiración cuando GitHub la facilita.
- **Commit:** SHA corto del código que lanzó la evaluación.
- Los artefactos se conservan según la política configurada en cada workflow; el enlace de ejecución permanece como referencia, pero los artefactos pueden caducar.

## Historial

| Fecha | Evaluación | Run ID | Resultado | Ejecución | Artefactos | Commit |
|---|---|---:|---|---|---|---|
<!-- HOLDOUT-INDEX-START -->

| 2026-11-10 | RONIN-10M — step-0 baseline inference holdout | 42874585777 | success | [Ver ejecución](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | [ronin-step0-baseline.zip](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | — |

<!-- HOLDOUT-INDEX-END -->

## Cómo funciona

El workflow `.github/workflows/update-holdout-registry.yml` escucha los eventos `workflow_run: completed`. Solo ejecuta el registro si el nombre de la ejecución contiene `holdout`. Consulta la API de GitHub para recuperar los artefactos de esa ejecución y actualiza esta tabla en `main`.

El actualizador no descarga ni ejecuta los artefactos ni hace checkout del código de la ejecución que acaba de terminar. Para que una evaluación futura aparezca aquí automáticamente, nombra su workflow incluyendo la palabra `holdout` (por ejemplo, `RONIN-10M — checkpoint holdout`).

## Baseline de referencia

El primer registro es la evaluación de paso 0: 100 preguntas, checkpoint inicial sin entrenamiento, tokenizer 8k y generación greedy sin RAG. Se conserva como referencia para comparar los siguientes checkpoints con el mismo holdout.
