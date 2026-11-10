# RONINIA

**RONINIA** es una línea independiente de investigación para entrenar desde cero un modelo de lenguaje compacto de aproximadamente 10 millones de parámetros. No hereda checkpoints ni pesos de MINIRONIN: reutiliza únicamente bibliotecas de datos admitidas, con procedencia y hashes.

## Diseño inicial: RONIN-10M

| Elemento | Configuración |
|---|---:|
| Arquitectura | Transformer decoder-only, pre-LN |
| Capas / cabezas | 6 / 8 |
| Dimensión | 288 |
| FFN | 864 |
| Contexto | 512 tokens |
| Vocabulario | 16.384 tokens BPE byte-level |
| Embeddings | Entrada/salida compartidos |
| Inicialización | Aleatoria, desde cero |
| Filas activas | Las 16.384 desde el primer paso |

La configuración apunta a aproximadamente 9,9M parámetros entrenables. El recuento exacto se calcula y verifica en CI; no se confunde tamaño nominal con capacidad demostrada.

## Principios

- **No se heredan pesos:** MINIRONIN aporta corpus, no checkpoints ni estado del optimizador.
- **Tokenizador propio:** BPE byte-level entrenado sobre el corpus admitido; vocabulario fijado antes del entrenamiento.
- **Sin filas bloqueadas:** embeddings y proyección de salida tienen 16.384 filas activas.
- **Datos trazables:** cada preparación registra archivos, documentos, bytes y SHA-256.
- **Holdout separado:** los benchmarks no se incorporan al corpus de entrenamiento.
- **GitHub Actions como laboratorio:** preparación, validación, entrenamiento y evaluación se ejecutan en workflows.

## Estado

La primera entrega establece arquitectura, contrato de tokenizador, preparación de corpus, entrenamiento desde cero y pruebas de integridad. No hay todavía un checkpoint entrenado ni una afirmación de calidad. La importación inicial toma los ficheros admitidos de MINIRONIN; los datasets sintéticos y los holdouts quedan excluidos.

## Uso opcional

```bash
python -m pip install -e ".[dev]"
python scripts/prepare_corpus.py --input-root data/incoming --output data/corpus/train.txt
python scripts/train_tokenizer.py --input data/corpus/train.txt --output tokenizer
python scripts/train.py --config configs/ronin-10m.json --corpus data/corpus/train.txt --tokenizer tokenizer/tokenizer.json --steps 100
pytest
```

El desarrollo local es opcional; los workflows son la vía reproducible del proyecto.

## Fuente de bibliotecas MINIRONIN

La importación inicial utiliza el artefacto unificado de MINIRONIN generado por el run exitoso **42523463620** en `main` (8 de noviembre de 2026). El artefacto fuente está publicado como `minironin-unified-train-corpus-42523463620`, con SHA-256 del archivo de artefacto `e02fa1240a0457310cacf1406f641c720942a41abc48d83f3e4c730506b691fc`.

La preparación de RONINIA verifica los hashes del artefacto, conserva la procedencia y excluye explícitamente filas marcadas `synthetic=true` y registros de evaluación. También se respetan las exclusiones de derechos y de holdout aplicadas por el constructor canónico de MINIRONIN. No se importan checkpoints ni datos de evaluación.
