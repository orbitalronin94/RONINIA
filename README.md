# RONINIA

**RONINIA** es una línea independiente de investigación para entrenar desde cero un modelo de lenguaje compacto de aproximadamente 10 millones de parámetros. No hereda checkpoints ni pesos de MINIRONIN: reutiliza únicamente corpus de entrenamiento admitido, con procedencia y hashes.

## Modelo experimental activo

El checkpoint seleccionado actualmente es el de **10.000 pasos acumulados**. La selección prioriza la mayor diversidad de salida observada frente al patrón casi único «El patrón» del checkpoint de 5.000 pasos. El lexicón de esperpento, los marcadores NH y las evasivas deliberadas forman parte del corpus intencional y no se consideran fallos por defecto.

- Manifiesto verificable: [models/active.json](models/active.json)
- Entrenamiento: [run 42902793379](https://github.com/orbitalronin94/RONINIA/actions/runs/42902793379)
- Holdout de 100 preguntas: [run 42970549370](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370)
- SHA-256 del checkpoint: `b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172`

La promoción es experimental: el holdout confirma que las 100 respuestas se generaron con el protocolo esperado, pero no produce por sí mismo una puntuación automática de calidad semántica.

## Diseño: RONIN-10M

| Elemento | Configuración |
|---|---:|
| Arquitectura | Transformer decoder-only, pre-LN |
| Capas / cabezas | 6 / 8 |
| Dimensión | 288 |
| FFN | 1.536 |
| Contexto | 512 tokens |
| Vocabulario | 8.192 tokens BPE byte-level |
| Embeddings | Entrada/salida compartidos |
| Inicialización | Aleatoria, desde cero |
| Filas activas | Las 8.192 desde el primer paso |

El vocabulario se ha reducido a la mitad respecto al diseño inicial. Se amplía el FFN de 864 a 1.536 para mantener el tamaño del modelo: **9.831.168 parámetros entrenables** con la configuración general. El checkpoint experimental activo usa el perfil de velocidad con contexto 256 y contiene **9.757.440 parámetros**, verificados en su manifiesto de promoción.

## Principios

- **No se heredan pesos:** MINIRONIN aporta corpus, no checkpoints ni estado del optimizador.
- **Tokenizador propio y pequeño:** BPE byte-level de 8.192 tokens, entrenado desde cero exclusivamente sobre el corpus de entrenamiento seleccionado.
- **Sin filas bloqueadas:** embeddings y proyección de salida tienen 8.192 filas activas.
- **Datos trazables:** cada preparación registra archivos, documentos, bytes y SHA-256.
- **Evaluación separada:** los registros identificados como holdout/evaluación se excluyen del corpus y del entrenamiento del tokenizador.
- **GitHub Actions como laboratorio:** preparación, validación, entrenamiento y evaluación se ejecutan en workflows.

## Corpus de referencia

La preparación del tokenizador utiliza el artefacto unificado de MINIRONIN del run exitoso **42523463620** en main (8 de noviembre de 2026). El artefacto minironin-unified-train-corpus-42523463620 ocupa **776.739.403 bytes (aprox. 777 MB)**. No se utiliza el artefacto posterior de varios gigabytes para esta configuración.

El workflow verifica el estado y la procedencia del run, descarga el artefacto, valida SHA256SUMS y genera un flujo de texto y un manifiesto. Se conservan los registros sintéticos admitidos; se excluyen los registros identificados como evaluación/holdout. No se importan checkpoints ni datos de evaluación.

## Preparación y entrenamiento

1. Ejecutar prepare-tokenizer.yml para descargar el corpus de 777 MB y entrenar el BPE de 8.192 tokens.
2. Verificar el artefacto roninia-tokenizer-8k-*, su hash y la huella SHA-256 del corpus.
3. Ejecutar train-ronin-10m.yml usando el ID del run del tokenizador. El entrenamiento comienza desde inicialización aleatoria y guarda checkpoints cada 5.000 pasos.

El desarrollo local es opcional; los workflows son la vía reproducible del proyecto.
