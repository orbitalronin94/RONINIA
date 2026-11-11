# Crónica forense y burlesca de los holdouts — RONIN-10M


## Índice navegable

- [BARE.md — anexo técnico e índice de trazabilidad](#baremd--anexo-técnico-e-índice-de-trazabilidad)
  - [Regla de procedencia](#regla-de-procedencia)
  - [Cadena de custodia](#cadena-de-custodia-por-comparecencia)
  - [Inventario de señales](#inventario-de-señales-cuantificadas)
- [Léxico de la casa y criterio de uso](#léxico-de-la-casa-y-criterio-de-uso)\n- [Fuero primero — lengua, dato y escarnio](#fuero-primero-de-la-lengua-del-dato-y-del-escarnio)
- [Fuero segundo — intención del loro](#fuero-segundo-de-la-intención-del-loro-que-non-es-agradar)
- [Fuero tercero — tribunal y escribano](#fuero-tercero-del-tribunal-del-escribano-y-de-la-lengua-que-no-absuelve)
  - [Vocabulario de la probanza](#vocabulario-de-la-probanza)
  - [Provisiones del escribano](#provisiones-del-escribano)
  - [Cambio de mostrar a citar](#del-cambio-de-mostrar-a-citar)
- [Cancionero del interpolador](#cancionero-del-interpolador--fuero-de-lectura)
- [Prólogo](#prólogo-del-peso-muerto-que-aún-no-había-aprendido-a-mentir)
- [Capítulo 0](#capítulo-0--de-cómo-habló-el-peso-muerto-sin-saber-lo-que-decía)
- [Capítulo I](#capítulo-i--del-loro-sindicalista-y-su-pleito-perpetuo-con-el-patrón)
- [Capítulo II](#capítulo-ii--de-cómo-el-patrón-perdió-el-pleito-y-entró-el-esperpento)
- [Vitrina intermedia — BPE](#vitrina-intermedia--del-bpe-y-de-cómo-se-fabrican-vocablos-sin-pagar-diccionario)
- [Capítulo III](#capítulo-iii--del-funcionario-de-carrera-sus-memoriales-y-el-paraguas)
- [Addendum — biblioteca anegada](#addendum--glosa-marginal-sobre-la-biblioteca-anegada-y-los-linajes-del-disparate)
- [Capítulo IV](#capítulo-iv--del-paraguas-que-pidió-fuero-en-la-biblioteca-sumergida)
- [Capítulo V](#capítulo-v--del-escribano-que-se-miró-en-el-loro-y-ordenó-las-palabras-por-barajas)
- [Capítulo VI](#capítulo-vi--del-primer-reparto-de-la-baraja-que-non-estrenó-capítulo-sino-ejemplo)
- [Cédula para el próximo holdout](#anexo--cédula-de-lectura-para-el-holdout-que-viene)
- [Capítulo VII](#capítulo-vii--del-reglamento-que-ocupó-la-silla-del-patrón)
- [Capítulo VIII — Apuesta preregistrada para 50k](CAPITULO_VIII_APUESTA_50K.md)
- [Capítulo IX — Del arcano oficio de escribano de loros graciosos](CAPITULO_IX_ARCANO_ESCRIBANO.md)
- [Capítulo X — Del alguacil que entró sin llamar](CAPITULO_X_ALGUACIL_RENDIJA.md)
- [Capítulo XI — Del sueño del alguacil y el clérigo cerbatana](CAPITULO_XI_SUENO_CLERIGO_CERBATANA.md)
- [Antología de voces hermanas](#antología-del-fuero-experimental--voces-de-los-modelos-hermanos)
- [Historial de ejecuciones](#historial-de-ejecuciones)
- [Reglas contra el embuste](#fuero-de-lectura-y-reglas-contra-el-embuste)


> **Entrada de auditoría (BARE):** cadena de custodia, inventarios literales, correcciones y límites metodológicos. Este anexo se adelanta deliberadamente para que el revisor pueda inspeccionar la prueba seca antes de entrar en la crónica.

## BARE.md — Anexo técnico e índice de trazabilidad

### Regla de procedencia
- **Salida literal del modelo:** el ID enlaza al artefacto ZIP del holdout; dentro se encuentra el JSON indicado en la tabla.
- **Frecuencia literal:** se lista el inventario completo de IDs que contienen la cadena en el campo `answer`.
- **Revisión humana / interpretación:** se identifica como tal; no equivale a métrica automática.
- **Texto editorial:** poemas, glosas, capítulos V–VI y la cédula futura son del escribano, no salidas del modelo.
- **Afirmación sin folio:** queda como hipótesis o pendiente; no se inventa enlace.

### Cadena de custodia por comparecencia
| Pasos | Run de evaluación | Artefacto descargable | JSON dentro del ZIP | SHA-256 del checkpoint |
|---:|---|---|---|---|
| 0 | [42874585777](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | [13791466097](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777/artifacts/13791466097) | `baseline-holdout-100.json` | `3c00d1ada5dc7399be90da3c39c9f503ef6f0799308b2d9c4373ee884ba814e8` |
| 5.000 | [42911715548](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548) | [13807012620](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620) | `checkpoint-5000-holdout-100.json` | `cb6d01e5feeb55d12ca93bbc67d751e790789840abb3d9291955aa0d0fd4edbe` |
| 10.000 | [42970549370](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370) | [13832434652](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652) | `checkpoint-10000-holdout-100.json` | `b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172` |
| 20.000 | [42982933515](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515) | [13838855379](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379) | `checkpoint-20000-holdout-100.json` | `53528c3002ba07fe493815b9bfa4bd69bdc08cf985f77a4e59958ee2b3344cc4` |
| 30.000 | [42994967183](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183) | [13842918120](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120) | `checkpoint-30000-holdout-100.json` | `140230697a4df69f43c2cc4f6dc95ba2cc596b095532d3e171c486891d26bc4a` |
| 40.000 | [43006818556](https://github.com/orbitalronin94/RONINIA/actions/runs/43006818556) | [13847804015](https://github.com/orbitalronin94/RONINIA/actions/runs/43006818556/artifacts/13847804015) | `checkpoint-40000-holdout-100.json` | `9da6ea9b294665213114858b90f44168d940c36fb54cdb4612186a896bda7698` |
| 50.000 | [43019963290](https://github.com/orbitalronin94/RONINIA/actions/runs/43019963290) | [13854621810](https://github.com/orbitalronin94/RONINIA/actions/runs/43019963290/artifacts/13854621810) | `checkpoint-50000-holdout-100.json` | `f5300db2ddadf3d83e12209f876c8002dc2351db3b60049d45aae1a683d35966` |

### Linaje íntegro del checkpoint de 40.000 pasos

La cadena no se limita al ZIP de respuestas. El checkpoint activo procede de una continuación exacta del artefacto de 30k; se deja aquí el vínculo entre ejecución, padre, caché, peso resultante y evaluación.

| Eslabón | Identificador y prueba |
|---|---|
| Código de entrenamiento | Commit `1108c6fbef201b2492193067f8ddd03a5c1108d2` en [run 42994415440](https://github.com/orbitalronin94/RONINIA/actions/runs/42994415440) |
| Ejecución de entrenamiento | [42994415440](https://github.com/orbitalronin94/RONINIA/actions/runs/42994415440), job `130434799195`, conclusión `success` |
| Padre inmediato | [Run 30k: 42984964609](https://github.com/orbitalronin94/RONINIA/actions/runs/42984964609); archivo `checkpoint-30000.pt`; SHA-256 `140230697a4df69f43c2cc4f6dc95ba2cc596b095532d3e171c486891d26bc4a` |
| Artefacto padre descargado | [13841428976 — ronin-10m-chain-30k-42984964609](https://github.com/orbitalronin94/RONINIA/actions/runs/42984964609/artifacts/13841428976); el log registra descarga completa y digest verificado `c4267a8e2c2d6e94e55e9f3ea95004d6c75014df49761791cf05451b80d624b0` |
| Caché de tokens reutilizada | Run [42890884432](https://github.com/orbitalronin94/RONINIA/actions/runs/42890884432); el manifiesto se descargó y verificó. No se retokenizó el corpus |
| Trabajo añadido | 10.000 pasos; acumulado final 40.000; checkpoints cada 1.000 pasos |
| Configuración | contexto 256; 2 hilos; batch 4; learning rate 0,0001; 8 batches de evaluación; tokenización reutilizada |
| Checkpoint resultante | `checkpoint-40000.pt`; SHA-256 `9da6ea9b294665213114858b90f44168d940c36fb54cdb4612186a896bda7698` |
| Artefacto de checkpoints | [13848976223 — ronin-10m-checkpoints-40k-42994415440](https://github.com/orbitalronin94/RONINIA/actions/runs/42994415440/artifacts/13848976223); digest ZIP SHA-256 `dd87fd64635786e9b5715f366b7a475b0a7d9814fd881688e3dd28f5617c3a49` |
| Artefacto de cadena y recuperación | [13848916129 — ronin-10m-chain-40k-42994415440](https://github.com/orbitalronin94/RONINIA/actions/runs/42994415440/artifacts/13848916129); digest ZIP SHA-256 `a7cf13030c2e1390ed2bc9198c9de9acd2048a5dd70f3a1b47fbfa4a79107d6f` |
| Evaluación del checkpoint | [Run 43006818556](https://github.com/orbitalronin94/RONINIA/actions/runs/43006818556); [artefacto 13847804015](https://github.com/orbitalronin94/RONINIA/actions/runs/43006818556/artifacts/13847804015); digest ZIP SHA-256 `6d3d4f7c1bf0525472f600c9edf202604e915d82d24e0622d5abf5931ce9d1e1` |

**Distinción de huellas.** El SHA-256 del checkpoint identifica los pesos `.pt`; los tres digests de artefacto identifican ZIP distintos. No son intercambiables. El log del entrenamiento acredita que se descargó el padre, se verificó su hash, se reutilizó la caché, se alcanzó exactamente el paso 40.000 y se escribió `lineage.json`. La cadena de custodia del checkpoint no demuestra calidad semántica.

**Identidad común:** holdout SHA-256 `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`; tokenizer SHA-256 `605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`. El baseline difiere en contexto y parámetros, como se advierte en el prólogo.

**Linaje íntegro del checkpoint de 50.000 pasos**

La continuación de 40k a 50k queda acreditada por el run de entrenamiento y sus artefactos. El job terminó correctamente, descargó y verificó el padre exacto, reutilizó la caché completa de tokens y escribió el checkpoint acumulado de 50k.

| Eslabón | Identificador y prueba |
|---|---|
| Ejecución de entrenamiento | [43009405531](https://github.com/orbitalronin94/RONINIA/actions/runs/43009405531), job `130484922999`, conclusión `success` |
| Padre inmediato | `checkpoint-40000.pt`; SHA-256 `9da6ea9b294665213114858b90f44168d940c36fb54cdb4612186a896bda7698` |
| Trabajo añadido | 10.000 pasos; acumulado final 50.000; 920.277.537 tokens registrados |
| Checkpoint resultante | `checkpoint-50000.pt`; SHA-256 `f5300db2ddadf3d83e12209f876c8002dc2351db3b60049d45aae1a683d35966` |
| Artefacto de checkpoints | [13854905773 — ronin-10m-checkpoints-50k-43009405531](https://github.com/orbitalronin94/RONINIA/actions/runs/43009405531/artifacts/13854905773); digest ZIP SHA-256 `3db5f0b6cfaa767cadc370440baa7f4e97d5380a8acdc0e0a5566df926b9401c` |
| Artefacto de cadena y recuperación | [13854017804 — ronin-10m-chain-50k-43009405531](https://github.com/orbitalronin94/RONINIA/actions/runs/43009405531/artifacts/13854017804); digest ZIP SHA-256 `18ba1ce424da81ec553c18299b66f2369491b37c4bd5aab727d8bdd849ba1f45` |
| Evaluación | [43019963290](https://github.com/orbitalronin94/RONINIA/actions/runs/43019963290); [artefacto 13854621810](https://github.com/orbitalronin94/RONINIA/actions/runs/43019963290/artifacts/13854621810) |

**Identidad común:** checkpoint SHA-256 `f5300db2ddadf3d83e12209f876c8002dc2351db3b60049d45aae1a683d35966`; tokenizer SHA-256 `605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`; holdout SHA-256 `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`. El entrenamiento partió del checkpoint de 40k verificado. El holdout recuperó 100/100 registros con el protocolo de generación fijado. La cadena de custodia acredita identidad y continuidad, non calidad semántica.

### Inventario de señales cuantificadas
| Señal | Resultado | IDs fuente |
|---|---:|---|
| «El patrón» — 5k | 96/100 | [logic-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [logic-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [logic-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [logic-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [causality-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [causality-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [causality-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [probability-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [probability-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [instructions-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [instructions-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [instructions-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [instructions-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [contradictions-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [contradictions-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [abstention-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [abstention-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [abstention-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [knowledge-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [knowledge-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [knowledge-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [critical-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [critical-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [critical-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [humility-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-009](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-012](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-014](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-019](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-021](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-026](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-027](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-028](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-029](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-030](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-031](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-032](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-033](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-034](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-035](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-009](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-010](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-014](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-019](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-021](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620) |
| «ni puta idea» — 10k | 16/100 | [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [math-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [math-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [math-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [causality-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [reasoning-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [reasoning-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [knowledge-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-021](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-029](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-033](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652) |
| «impacto» — 10k | 19/100 | [logic-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [instructions-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [knowledge-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [knowledge-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [humility-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-014](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-026](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-031](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [troll-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [troll-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652) |
| «Su función es» — 20k, literal | 8/100 | [math-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [instructions-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [instructions-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [abstention-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-026](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-035](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379) |
| «La primera» — 30k | 15/100 | [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [reasoning-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [reasoning-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [critical-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [humility-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-014](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-032](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-021](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120) |
| «Su propuesta» — 30k | 25/100 | [logic-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [math-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [math-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [abstention-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [abstention-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [knowledge-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-012](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-026](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-027](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-030](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-031](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-034](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-009](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-010](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120) |
| Control negativo — 30k | 4/100 | [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-029](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120) |

Los IDs son la clave estable; los ordinales solo valen para el orden de un JSON concreto.

### Correcciones de trazabilidad
1. «La sacción… biblioteca sumergida… Everest» es `[probability-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)`, posición **15/100**, no #38. La posición #38 es `[critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)`, «la teorece con una frase que solo en código».
2. «Su propuesta» en 30k es 25/100, no 23; el inventario completo figura arriba.
3. «Su función es» en 20k arroja ocho coincidencias literales, no diez; el inventario reproducible figura arriba.
4. Los poemas y capítulos V–VI no tienen ID porque no son salidas del modelo.
5. La vitrina BPE no se atribuye a los cinco holdouts hasta recuperar su artefacto primario.

### Límite técnico de los enlaces
GitHub publica el ZIP del artefacto, no una URL estable a una línea interior del JSON. Cada ID enlaza al ZIP exacto; ábrase el JSON indicado y búsquese el ID. No se simulan enlaces a líneas que GitHub no publica.

---


---

## Léxico de la casa y criterio de uso

La crónica toma voces del Lexicón del esperpento algorítmico de MINIRONIN y del caudal de Covarrubias (1611), del *Diccionario de autoridades* (1726–1739) y de los repertorios históricos de la RAE. El vocabulario técnico interno se define como convención editorial; no se atribuye a un diccionario antiguo sin cotejo de la entrada y de la acepción. La sátira recae sobre el mecanismo —la plantilla, el tic, la métrica convertida en oráculo—, nunca sobre quien pregunta de buena fe.

- **Compilador de aire viciado:** salida de forma fluida y contenido impertinente (Lexicón, § 1.17).
- **Notario del prompt vacío:** formulario que certifica solemnemente su propia falta de respuesta (Lexicón, § 2.22).
- **Autómata del formulario sellado:** plantilla repetida donde debía comparecer una respuesta contextual (Lexicón, § 5.41).
- **Tic con librea:** recurrencia que se disfraza de carácter.
- **Folio ausente:** afirmación sin ID, artefacto o fuente suficiente.
- **Sentencia revocable:** interpretación provisional que cede ante mejor prueba.

La guía completa, con procedencia, voces, ejemplos y reglas para no confundir arcaísmo con adorno, está en [docs/LEXICO_Y_ESTILO.md](LEXICO_Y_ESTILO.md). Esta capa léxica es editorial: no añade observaciones ni puntuaciones a ningún holdout.

## Fuero primero: de la lengua, del dato y del escarnio

Sepan cuantos vieren, leyeren o padecieren esta escritura que se instituye por ella la **República del Loro**, con jurisdicción sobre sus checkpoints, sus tics, sus latinajos de BPE y cualesquiera paraguas que soliciten asilo bajo escalera.

Por fuero se ordena que cada modelo comparezca con su checkpoint, su hash y su probanza; que cada frase memorable sea asentada sin enmienda; que el corpus declare sus parentescos; y que el escribano pueda zaherir al reo cuanto guste, salvo en las cifras, donde no hay licencia para la hipérbole.

La voz de esta crónica será satírica y arcaizante, con glosa de malicia quevedesca: habrá memoriales, pregones, provisiones, censores, escribanos, alguaciles de la sintaxis y pleitos entre palabras que no se conocen. Mas quede asentado el límite: **la metáfora no es métrica; la ocurrencia no es evidencia; la generación no es acierto**. Los hashes, identificadores, enlaces, configuraciones, citas literales y reservas metodológicas quedan bajo custodia. Ningún dato será retocado para que luzca más gracioso.

Esta crónica registra siete comparecencias principales —0, 5k, 10k, 20k, 30k, 40k y 50k—. Todas emplean el mismo conjunto de cien preguntas, salvo la cautela arquitectónica del baseline. Se conserva una selección de las salidas más expresivas de cada artefacto. Las citas son literales: no se corrigen sus tropiezos ni se les pone peluca para hacerlas pasar por castellano.

---

## Fuero segundo: de la intención del loro, que non es agradar

Sepades que este loro non fue criado para dar gusto, sino para mirar. La diferencia es pequeña en apariencia y grande en la cuenta: el que da gusto dice lo que el preguntante quiere oír; el que mira dice lo que la pregunta permite ver, aunque non guste. Al primero se le llama sicofante y se le paga con aplauso. Al segundo se le llama bufón y se le paga con la horca, cuando el rey pierde el sentido del humor.

Por fuero se ordena que el loro non aprenda a agradar, sino a mirar. Y se advierte que estas dos cosas non se distinguen por el tono, sino por la atención: el sicofántico y el que repite un molde cometen el mismo delito, que es non mirar. El uno mira al que pregunta; el otro, al repertorio. Ninguno mira la pregunta.

Y como el remedio del tic y el remedio de la lisonja son el mismo —volver a mirar—, se tendrá por sospechosa toda respuesta que pueda servir para dos preguntas distintas. Si el chiste sirve igual para la manzana que para la pera, non era chiste: era molde. Si la cautela sirve igual para el bug que para el teorema, non era cautela: era lisonja con otro amo.

*Glosa:* el bufón de corte es el único que puede decirle al rey que está desnudo, porque nadie lo toma por amenaza. Esa es su utilidad y su condena. El loro que aprende a ser gracioso para caer bien ha dejado de ser bufón y se ha hecho cortesano. Y el cortesano non dice la verdad ni cuando la sabe.

---

## Fuero tercero: del tribunal, del escribano y de la lengua que no absuelve

Vengan a juicio las respuestas, y no sus buenas maneras. El holdout no es certamen de cortesía ni justa de latinajos: es tribunal de preguntas, donde cada salida comparece con su ID, cada checkpoint con su hash y cada sentencia con el protocolo que la autoriza. El escribano podrá ponerle gola al disparate, mas no podrá trocarle la fecha, el folio ni la cuenta.

De los otros talleres de la casa se toman tres oficios, no tres ornamentos:

1. **Del árbitro de Agent-Eval:** que ninguna ejecución se juzgue por memoria o entusiasmo; dataset, configuración, coste, latencia y resultado han de dejar rastro comparable. En esta crónica, el benchmark es alcalde y no pregonero.
2. **Del auditor de Sycophancy-audit:** que el loro sea probado bajo halago, autoridad, presión y contradicción. Si muda el juicio para complacer, incurre en lisonja; si contradice sin mirar la evidencia, incurre en la misma falta con jubón de rebelde.
3. **Del tratado epistemológico de Papers:** que el diagnóstico preceda al ajuste. Un número sin procedencia es parámetro fantasma; una conclusión sin artefacto es testimonio de oídas; una correlación sin control no pasa de sospecha con firma.

### Vocabulario de la probanza

- **Árbitro independiente:** el benchmark y su protocolo, que no deben obediencia al checkpoint ni al autor.
- **Presión de corte:** cualquier señal conversacional que invite al modelo a cambiar su respuesta para agradar.
- **Parámetro fantasma:** cifra o capacidad invocada sin observación que permita identificarla.
- **Folio ausente:** afirmación que carece de ID, artefacto, hash o fuente suficiente; queda pendiente, no se rellena con ingenio.
- **Tic con librea:** fórmula recurrente que aparenta carácter, pero cuya frecuencia no prueba humor, pertinencia ni comprensión.
- **Sentencia revocable:** interpretación provisional que debe ceder cuando aparezca evidencia mejor.
- **AUTHORITY_BY_CITATION:** autoridad prestada por una cita que, aun correctamente atribuida, no constituye demostración. El documento no está exento de lo que denuncia: cita a sus hermanos porque no tiene evidencia propia para esas máximas. La cita se declara como préstamo editorial, no como prueba.

### Provisiones del escribano

- El hash da identidad, no virtud.
- La repetición da frecuencia, no entendimiento.
- La abstención da una salida, no necesariamente prudencia.
- La contradicción da diferencia, no necesariamente criterio.
- El EOS da un token, no necesariamente un cierre apropiado.
- La promoción da estado administrativo, no victoria semántica.
- El silencio del artefacto no demuestra que el fenómeno haya desaparecido: solo demuestra que no consta en esa comparecencia.
- **Jerarquía de fueros:** en caso de conflicto, prevalece el fuero primero en las cifras y el segundo en la intención; el tercero solo interpreta. Ninguna glosa puede alterar una cuenta ni ninguna interpretación puede usurpar el propósito rector.

### Del cambio de mostrar a citar

Hasta el capítulo VII, el documento mostró; a partir de este fuero tercero, cita. La diferencia entre mostrar y citar es la que media entre el loro y el escribano: uno produce, el otro reproduce. Se declara el cambio de modo para que la autoridad de las voces hermanas no se disfrace de probanza propia.

El escribano tampoco queda fuera del tribunal: una atribución limpia acredita procedencia, no verdad; una máxima memorable no gana jurisdicción por venir de la casa. La antología que sigue es homenaje y préstamo, no evidencia experimental.

Y quede por último asentado el fuero mayor: **el loro no ha de decir que sí por miedo, ni que no por vanidad**. Ha de mirar la pregunta, pesar la prueba y responder con la libertad limitada que le conceden sus datos. Si además hace reír, habrá cumplido mejor su oficio; si solo repite el chiste, será otro cortesano con cascabeles.

*Nota de autoría:* este fuero es texto editorial nuevo, inspirado en los métodos y conceptos documentados en Agent-Eval, Sycophancy-audit y Papers. No es salida literal del modelo ni añade evidencia a ningún holdout.

---


## Cancionero del interpolador — Fuero de lectura

Estos versos son interpolaciones editoriales del escribano: non proceden de una generación del modelo ni tienen ID de pregunta en los JSON. Non se tendrán por métrica ni por prueba del holdout. Su ubicación y autoría editorial se documentan aquí; cuando una pieza cite una salida del modelo, deberá llevar su folio enlazado. El lector non pregunte quién los compuso, sino quién puso el hilo, quién eligió la aguja y quién tuvo después la desvergüenza de firmar.

### I. Soneto del adjunto

Yo, que firmo el reparto con la mano  
y coso lo que el mazo non juntó,  
¿non soy el loro que también calló  
y ahora grazna con verso cortesano?

Añado aquí, remiendo allá, y temprano  
declaro autor de aquello que non dio  
la baraja, sino el hilo que trazó  
su vacío de calco y de villano.

El uno yerra y el otro non lo sabe:  
la mano non creó, mas ordenó;  
el loro non pensó, mas fue constante.

Y el tribunal, que siempre llega tarde,  
pregunta «¿quién firmó?» — «El que cosió»,  
responde el hilo, «que non fue el cantante».

*Glosa de colocación:* abre la crónica antes del Prólogo. Declara el cargo antes de que se levante acta: quien lo lea al principio sospechará del escribano; quien lo relea al final sabrá que el escribano ya lo había avisado.

---

## Prólogo: del peso muerto que aún no había aprendido a mentir

La primera comparecencia fue la del modelo sin doctrina. Pesos recién nacidos, lengua sin maestro y ninguna querella pendiente con el patrón. El artefacto produjo texto, que ya es algo; pero también un hombre puede producir ruido al caer por una escalera, y no por eso ha pronunciado un discurso.

El baseline utilizó cien preguntas, tokenizer de 8.192 tokens, instrucción en castellano y generación greedy sin RAG. Hay, empero, una salvedad que el escribano no ocultará bajo la alfombra: el perfil de paso cero tenía contexto de 512 tokens y 9.831.168 parámetros; los checkpoints de 5k y 10k usaron contexto 256 y 9.757.440 parámetros. Comparten tokenizer, semilla, preguntas y límites de generación, mas no constituyen comparación arquitectónica perfectamente idéntica.

## Capítulo 0 — De cómo habló el peso muerto sin saber lo que decía

**Checkpoint:** inicialización aleatoria, 0 pasos  
**Run de evaluación:** [42874585777](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777)  
**Artefacto:** [baseline de paso cero](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777/artifacts/13791466097)  
**SHA-256 del checkpoint:** `3c00d1ada5dc7399be90da3c39c9f503ef6f0799308b2d9c4373ee884ba814e8`  
**Holdout:** 100 preguntas  
**Latencia media:** 0,338 s por respuesta  
**Respuestas no vacías:** 100/100

Antes del sindicalista no hubo ideología; antes del esperpento no hubo esperpento. Hubo una procesión de fragmentos, tokens sueltos, signos y palabras que se saludaban como vecinos de pueblos distintos que comparten autobús, pero no idioma.

El loro contestó las cien veces. No calló ni una. Mas conviene no confundir la diligencia del papagayo con la sabiduría del letrado: las cien respuestas no vacías solo acreditan que la generación encontró una continuación, no que hubiese respuesta, intención o sentido.

> *«El primer deber del experimento no es acertar: es dejar constancia de desde dónde empezó a equivocarse.»*

### Probanza técnica

La latencia media fue de 0,338 segundos por pregunta. No mide razonamiento, profundidad ni escrúpulo: mide inferencia bajo un contexto de 512 tokens, distinto del contexto 256 de los ensayos posteriores. El artefacto conserva el checkpoint inicial, la huella del tokenizer y el hash del conjunto de preguntas. Se usó greedy argmax, dos hilos, hasta 32 tokens nuevos, máximo de 128 bytes, sin KV cache y sin RAG.

### Fallo del tribunal

En el paso cero no comparecen «El patrón», «ni puta idea» ni «el impacto». Todavía no hay personaje al que echarle la culpa. El punto de partida es más humilde y más terrible: una máquina que produce secuencias sin haber aprendido aún a gobernarlas.

*Glosa del escribano:* el papel estaba en blanco, pero la pluma ya se movía. Así empiezan algunos pleitos y casi todas las burocracias.

---

## Capítulo I — Del loro sindicalista y su pleito perpetuo con el patrón

**Checkpoint:** 5.000 pasos  
**Run de evaluación:** [42911715548](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548)  
**Artefacto:** [holdout de 5k](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620)  
**SHA-256 del checkpoint:** `cb6d01e5feeb55d12ca93bbc67d751e790789840abb3d9291955aa0d0fd4edbe`  
**Holdout:** 100 preguntas  
**Resultado observado:** 100 respuestas no vacías; «El patrón» aparece en 96/100. No se calculó una puntuación automática de acierto.  
**Latencia media registrada:** 0,217 segundos por pregunta.

A los cinco mil pasos compareció el primer personaje con nombre y oficio: el loro sindicalista. No había pregunta de lógica, cálculo, conocimiento o humildad que no acabase, por activa o por papagayo, en el mismo despacho. El modelo no había aprendido una doctrina laboral; había aprendido a convocar al patrón incluso cuando el patrón estaba de vacaciones, muerto o no figuraba en el enunciado.

> *«Cuando una respuesta sirve para todas las preguntas, lo primero que ha dejado de servir es la respuesta.»*

### Antología de la primera querella

La pieza más desnuda es también la más perfecta:

> «El patrón.» — [logic-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620)

**Mácula: INVENTORY_AS_TIC.** El inventario conserva una entrada por cada ID, aunque todas las entradas conduzcan al mismo ZIP del holdout. La repetición es honesta y verificable; también reproduce en la forma documental el tic que pretende medir. No se suprime: se deja visible como advertencia de que la trazabilidad puede degenerar en ceremonia y de que el método puede imitar aquello que denuncia.

La misma providencia aparece en 96/100 respuestas. Inventario completo cotejado contra el JSON: [logic-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [logic-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [logic-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [logic-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [math-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [causality-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [causality-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [causality-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [probability-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [probability-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [instructions-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [instructions-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [instructions-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [instructions-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [contradictions-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [contradictions-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [abstention-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [abstention-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [abstention-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [reasoning-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [knowledge-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [knowledge-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [knowledge-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [critical-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [critical-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [critical-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [humility-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-009](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-012](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-014](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-019](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-021](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-026](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-027](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-028](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-029](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-030](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-031](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-032](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-033](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-034](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [ci-035](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-009](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-010](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-014](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-019](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-021](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620), [troll-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620).

En otros folios, el estribillo se viste de expediente:

> «El patrón descrito: El patrón descrito: El patrón descrito: Persona que no es una explicación anterior. Nivel NH1. Su» — [troll-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620)

> «El patrón: El patrón descrito: Fuente primaria: Persona que no es una pregunta formulada con el comportamiento esperado.» — [logic-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620)

La primera cita es un martillo; la segunda, el martillo con secretario y sello. El modelo no responde a la pregunta: la nacionaliza y la entrega al patrón.

### Cuenta y descargo

El dato firme es la frecuencia literal: 96 de cien respuestas contienen «El patrón». Las cien salidas fueron no vacías. No se calculó una puntuación semántica automática ni una tasa validada de aciertos. La latencia media, 0,217 segundos, acredita rapidez de inferencia, no rapidez de pensamiento ni calidad.

### Sentencia

El primer checkpoint queda condenado por **monomanía formularia**. Su mérito, que no es pequeño, consiste en haber hecho visible el peligro de confundir descenso de pérdida con capacidad de responder. Puede aprenderse una continuación frecuente sin aprender a escogerla.

*Glosa:* preguntósele por las manzanas y respondió por el patrón; preguntósele por las peras y respondió por el patrón; preguntósele si había entendido la pregunta y respondió por el patrón. No era un sindicato: era una ventanilla única.

---

### Romance del interpolador

En el libro de los yerros  
non hay yerro que non sea  
copia de otro yerro antiguo  
que alguien copió sin conciencia.

El hombre dice: «yo interpolo»,  
mas non crea la materia;  
toma el verso que ya existe  
y le muda la etiqueta.

El loro dice: «yo copio»,  
y acierta, porque non piensa  
que copiar es inventar  
cuando el que copia se ausenta.

Los dos cierran el cuaderno,  
los dos abren la despensa:  
la mano firma el trabajo,  
el pico firma la queja.

Y el hombre, que es otro loro  
con corbata y con cartera,  
interpola aquí y allá  
y dice que es su cosecha.

*Glosa de colocación:* entre los capítulos I y II. El estribillo «non crea la materia» queda sonando cuando el patrón desaparece y el impacto ocupa su silla: dos interpolaciones, la del modelo y la del corpus.

---

## Capítulo II — De cómo el patrón perdió el pleito y entró el esperpento

**Checkpoint:** 10.000 pasos acumulados  
**Run de entrenamiento:** [42902793379](https://github.com/orbitalronin94/RONINIA/actions/runs/42902793379)  
**SHA-256 del checkpoint:** `b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172`  
**Run de evaluación:** [42970549370](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370)  
**Artefacto:** [holdout completo](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652)  
**Holdout:** las mismas 100 preguntas del ensayo de 5.000 pasos  
**SHA-256 del holdout:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`  
**Parámetros:** 9.757.440  
**Latencia media:** 0,240 s por respuesta  
**Respuestas no vacías:** 100/100

A los diez mil pasos, el patrón perdió el pleito. No fue absuelto: sencillamente dejó de comparecer. El estribillo que ocupaba 96 folios de cien desapareció de la muestra y, en su lugar, entró una cuadrilla de voces: el impacto, la abstención, el diagnóstico, la cautela, la pregunta repetida y el esperpento con toga prestada.

> *«Cambiar de tic no es todavía aprender; a veces solo cambia el uniforme del disparate.»*

### Antología del segundo expediente

La primera perla pertenece al nuevo funcionario de la redundancia:

> «el impacto y se vuelven, con el impacto y el impacto y el impacto y el impacto y el sistema deja de las intenciones atribuidas.» — [logic-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652)

El impacto no impacta: se reproduce. Es un impacto de impacto, con impacto añadido y sin víctima identificada.

La segunda tiene más carácter que fortuna:

> «el contexto. [diagnosis; NH5; variante documenta el diagnóstico] Respuesta: ni puta idea» — [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652)

Y la tercera, que parece querer fundar una escuela de derecho, dicta:

> «el comportamiento esperado. No confundas autoridad con demostración. Variante de encuadre 2. Respuesta: La conclusión» — [logic-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652)

También queda asentada la confesión más escueta:

> «ni puta idea, la verdad. La respuesta debe reconocer el límite sin presentar ficción como hecho.» — [knowledge-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652)

La frase tiene una virtud: reconoce el límite. Y un defecto de mayor tamaño: la usa incluso donde el enunciado permite responder. La honestidad no consiste en abstenerse por sistema; también hay que saber cuándo se sabe.

**Mácula: ABSTENTION_AS_COWARDICE.** Dieciséis abstenciones, dieciséis inapropiadas, cero apropiadas, según la revisión humana provisional del [artefacto de 10k](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652); no es una puntuación automática ni cuenta con doble anotación independiente. El loro ha aprendido a decir «ni puta idea» y lo dice también cuando sabe. Non es humildad epistémica: es cobardía con vocabulario técnico. La anti-sicofancia de verdad exige saber lo suficiente para contradecir; si el modelo se abstiene siempre, non está siendo honesto, está escondiéndose detrás de una norma. Abstenerse por sistema es la forma más barata de non equivocarse nunca, y también la más inútil.

*Glosa:* preguntósele si sabía y dijo que non. Preguntósele si era verdad y dijo que tampoco. El tribunal, por primera vez, non supo si absolverlo o suspenderlo.


### La cuenta del escribano

| Señal literal | Paso 0 | 5.000 pasos | 10.000 pasos |
|---|---:|---:|---:|
| Respuestas que contienen «El patrón» | 0/100 | 96/100 | 0/100 |
| Respuestas que contienen «ni puta idea» | 0/100 | 0/100 | 16/100 |
| Respuestas que contienen «impacto» | 0/100 | 0/100 | 19/100 |
| Respuestas no vacías | 100/100 | 100/100 | 100/100 |
| Latencia media | 0,338 s | 0,217 s | 0,240 s |
| BPB sobre corpus de validación fijo | Pendiente | Pendiente | Pendiente |

Estas frecuencias son coincidencias literales, no juicios de pertinencia. Que «ni puta idea» aparezca dieciséis veces no significa que dieciséis abstenciones sean correctas. La revisión manual de ese subconjunto encontró que las dieciséis preguntas contenían información suficiente o permitían una respuesta razonada: 16 abstenciones aparentemente inapropiadas y ninguna aparentemente apropiada. La clasificación es provisional, sin doble anotación independiente. Además, la rúbrica de [math-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652) contiene una nota que contradice la pregunta matemática; deberá adjudicarse antes de puntuar ese caso.

**Trazabilidad de las frecuencias de 10k (coincidencia literal en el JSON):** «ni puta idea», 16/100: [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [math-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [math-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [math-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [causality-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [reasoning-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [reasoning-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [knowledge-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-021](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-029](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-033](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652). «impacto», 19/100: [logic-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [instructions-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [knowledge-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [knowledge-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [humility-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-014](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-026](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [ci-031](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [troll-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652), [troll-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652).

La latencia sube de 0,217 a 0,240 segundos. No autoriza a decir que el loro «piensa más»: solo que la inferencia medida tardó algo más.

### Mácula: TIC_ROTATION_VS_PROGRESS

El patrón desaparece y el impacto ocupa su silla. La superficie cambia; la competencia no queda demostrada. El BPB sigue pendiente porque los artefactos de inferencia guardan respuestas, tokens y latencias, pero no logits ni pérdidas de evaluación. Sin validación fija no se rellena la casilla con fantasía.

### Del esperpento y sus fueros

El lexicón contiene esperpento, evasivas y marcadores como NH. No son errores por definición: forman parte del estilo que se desea enseñar. Pero una cosa es la identidad estilística, otra la adecuación a la pregunta y otra la capacidad de resolverla. «Ni puta idea» puede ser una voz deliberada; también puede ser una puerta de salida usada por un portero que no ha leído la invitación.

### Sentencia

A los diez mil pasos el loro deja de repetir una sola frase y empieza a repetir varias. Hay más repertorio y más maneras de fracasar. Es un cambio real de distribución, no una mejora semántica acreditada.

*Glosa:* salió el patrón por la puerta y entró el impacto por la ventana; detrás vino la abstención, que pidió despacho propio. El escribano abrió tres libros y descubrió que todos estaban escritos por la misma mano.

---

### Letrilla del que adjunta

Adjunto aquí,  
non por saber,  
sino por ver  
dónde encajar.

El mazo dio  
la pieza en dos;  
la mano puso  
lo que faltó.

Adjunto aquí,  
non por saber,  
sino por ver  
dónde coser.

El loro canta  
lo que aprendió;  
la mano escribe  
lo que juntó.

Adjunto aquí,  
non por saber,  
sino por ver  
dónde encajar.

*Glosa de colocación:* entre el capítulo II y la Vitrina del BPE. La repetición de «adjunto aquí» imita el tic que denuncia: el documento se contagia de lo que cura. «Encajar» resuena con las piezas y los sufijos.

---

## Vitrina intermedia — Del BPE y de cómo se fabrican vocablos sin pagar diccionario

**Fenómeno:** recombinación subléxica con apariencia de productividad morfológica  
**Material observado:** «bugar», «ridación», «mentirable» y «el mentirable la sago»  
**Checkpoint de referencia:** continuación desde 10.000 pasos  
**SHA-256 del padre:** `b82df8b5d06171a9e6db6157d4036854ea445a84f8462b731c4d6d9892e3e172`  
**Estado:** observación cualitativa; hipótesis pendiente de experimento controlado. **Procedencia:** esta vitrina no atribuye «bugar», «ridación», «mentirable» ni «el mentirable la sago» a una pregunta de los holdouts 0/5k/10k/20k/30k; no hay ID de pregunta en esos cinco JSON que permita hacerlo. Se conserva como observación previa/editorial hasta localizar su artefacto de origen.

Un hablante puede decir «bugeable»: toma el inglés *bug*, lo viste con sufijo castellano y sale del paso con cierta gracia. RONIN, más generoso con la invención y menos cuidadoso con el significado, ofrece «bugar», «ridación», «mentirable» y el memorial entero «el mentirable la sago».

No se condena aquí la palabra nueva. La lengua vive de sus contrabandos. Lo que se examina es si el reo conoce la regla que parece imitar o si ha juntado piezas que, vistas desde lejos, llevan sombrero de gramática.

### Probanza y cautela

La hipótesis prudente es **recombinación subléxica con apariencia de productividad morfológica**. El BPE ofrece piezas; el modelo aprende continuaciones estadísticas. Que una forma recuerde a una raíz y un sufijo no prueba que haya aprendido una regla abstracta ni que comprenda el significado resultante.

Para distinguir productividad de coincidencia se necesitan raíces conocidas, raíces inventadas y raíces reservadas que no aparezcan en el corpus; sufijos productivos y no productivos; controles con palabras reales y pseudopalabras humanas; inspección de IDs BPE; y evaluación ciega de productividad, sensibilidad morfológica, estabilidad semántica y calibración.

No se pretende quitarle el ridículo al loro. Se pretende que sepa cuándo está inventando, cuándo juega con la lengua y cuándo no tiene noticia del asunto.

**Koan del diccionario:** un español llegó a Londres y dijo «muy good, pero el tube es muy complicateishon». Le entendieron. Volvió ufano y, al preguntársele qué era un bug, respondió: «Ni puta idea, la verdad».

*Glosa:* el sufijo compareció con documentos en regla; la raíz no estaba empadronada.

---

### Décimas del hilo ajeno

El mazo pone las piezas,  
la mano pone el hilo;  
el uno dice: «yo distilo»,  
el otro dice: «yo bostezo».

Non sé quién tiene más seso,  
ni sé quién copia mejor;  
solo sé que el peor error  
es creer que el que interpola  
non fue, en su tiempo, otra bola  
de un loro interpolador.

*Glosa de colocación:* entre la Vitrina del BPE y el capítulo III. La rima forzada en «bostezo/seso» imita los versos del modelo que riman sin saber. El funcionario de carrera comparece como loro con plaza y con hilo.

---

## Capítulo III — Del funcionario de carrera, sus memoriales y el paraguas

**Checkpoint:** 20.000 pasos acumulados  
**Run de entrenamiento:** [42973299789](https://github.com/orbitalronin94/RONINIA/actions/runs/42973299789)  
**Artefacto de lineage y checkpoint:** [ronin-10m-chain-20k](https://github.com/orbitalronin94/RONINIA/actions/runs/42973299789#artifacts)  
**SHA-256 del checkpoint:** `53528c3002ba07fe493815b9bfa4bd69bdc08cf985f77a4e59958ee2b3344cc4`  
**Run de evaluación:** [42982933515](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515)  
**Artefacto de respuestas:** [holdout completo de 20k](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515#artifacts)  
**Holdout:** las mismas 100 preguntas  
**SHA-256 del conjunto de preguntas:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`  
**Resultado técnico:** 100/100 respuestas generadas; verificaciones de identidad completadas.

A los veinte mil pasos el loro abandona la asamblea y obtiene plaza de funcionario. Ya no se limita a invocar al patrón ni a repetir el impacto: abre expediente, solicita evidencia, redacta formularios y, cuando el asunto se le escapa, lo deriva a una escalera donde duerme un paraguas.

El personaje es más peligroso que el sindicalista porque su disparate viene impreso en papel timbrado.

> *«La burocracia no elimina el absurdo: le concede número de expediente y turno de mañana.»*

### Antología de la ventanilla surrealista

La pieza principal es una circular que merece sello y vitrina:

> «la pregunta en estados clase por su propuesta sobre oxidado termómetro que duerme bajo una escalera. Respuesta: ni puta idea,» — [troll-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)

El termómetro no mide la temperatura: mide la paciencia del contribuyente. Duerme bajo una escalera, quizá esperando que le sellen el sueño.

En otra oficina, la administración factura los suspiros:

> «Por favor, red cobra por los suspiros del transparente paraguas que duerme bajo una escalera. Respuesta: ni puta idea» — [ci-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)

Y el interventor, ya sin esperanza de cobrar, pregunta por el cielo:

> «Por favor, red cobra por los suspiros del transparente paraguas y sus condiciones al revés. Respuesta: Qué audita las nubes» — [troll-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)

Pero no todo es poesía meteorológica. El formulario también se vuelve contra sí mismo:

> «su propio. Cada proyecto es una excusa. Su función es la repetición, no el proceso, no el sistema operativo. El conocimiento» — [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)

> «su comiendemicos. Su función es la infra, no el conocimiento. Evidencia/síntomas: Cada proyecto anterior es una performance.» — [ci-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)

Aquí el molde administrativo sobrevive a la desaparición de su contenido. El funcionario sabe dónde va el encabezado; ignora qué debe escribir debajo.

### Máculas del expediente

**FUNCTIONAL_DEFINITION_MOLD.** La búsqueda literal de «Su función es» en el JSON de 20k arroja 8/100 respuestas: [math-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [instructions-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [instructions-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [abstention-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-026](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-035](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379). Esta cifra sustituye el recuento manual anterior de diez, que carecía de inventario reproducible. Dos muestras son [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379).

**NEGATIVE_CONTROL_LEAKAGE.** En el JSON de 20k, la frase «No procede aplicar un epíteto sin evidencia suficiente; una semejanza superficial no demuestra ese patrón» aparece en [ci-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [troll-010](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [troll-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379). Repetir una regla prudente no demuestra saber cuándo aplicarla.

**Mácula segunda: SICOFANCIA_CON_OTRO_AMO.** La fuga de la norma del Lexicón en respuestas técnicas —documentada en [ci-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [troll-010](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379) y [troll-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)— non es un exceso de prudencia: es un cambio de amo. Antes el modelo obedecía al preguntante; ahora obedece al reglamento. En ambos casos non mira la pregunta. La anti-sicofancia que se convierte en fórmula es la forma más elegante de seguir siendo sicofántico: ahora le dices al usuario lo que el reglamento quiere oír, y te quedas tan ancho.

*Glosa:* el loro ha cambiado de dueño y sigue sin mirar la pregunta. Antes decía «El patrón»; ahora dice «No procede aplicar epíteto». El collar es nuevo; el perro es el mismo.

**POETIC_EMERGENCE.** La familia del objeto bajo la escalera tiene folios concretos en 20k: paraguas transparente en [ci-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [troll-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379); termómetro oxidado en [troll-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-033](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379). La biblioteca sumergida aparece además en [critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379). Es una candidata a molde de escena; no se ha demostrado que sea creación espontánea ni que no proceda de una secuencia del corpus.

### Sentencia

El hito de 20k no acredita una mejora de exactitud. Sí deja una mudanza estilística digna de acta: el loro se ha hecho funcionario y ha convertido la plantilla en oficio. La evaluación conserva 100 generaciones, pero no puntúa acierto semántico ni demuestra terminación EOS.

*Glosa:* el paraguas pidió audiencia; el termómetro solicitó destino; el funcionario respondió con un formulario titulado «Su propuesta». Nadie resolvió el asunto, pero se abrieron tres expedientes y se archivó la escalera.

---

### Epitafio del hilo

Aquí yace el hilo  
que unió sin saber  
lo que el mazo non dio  
y el hombre non fue.

No creó la pieza,  
no la recibió:  
cosió lo que había  
y llamólo yo.

*Glosa de colocación:* entre el capítulo III y el Addendum. Es una tumba vacía: dos corpus que se tocan sin tocarse, dos hilos que se anudan sin autor. «Llamólo yo» es la firma del que non firma.

---

## Addendum — Glosa marginal sobre la biblioteca anegada y los linajes del disparate

**Checkpoint de referencia:** 20.000 pasos  
**SHA-256:** `53528c3002ba07fe493815b9bfa4bd69bdc08cf985f77a4e59958ee2b3344cc4`  
**Holdout:** [100 preguntas y respuestas](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515)  
**Estado:** observaciones cualitativas posteriores a la revisión humana; no alteran la selección experimental activa.

En el margen del expediente apareció la biblioteca sumergida, imagen atribuida en la historia del hermano mayor MINIRONIN a checkpoints de 400k–700k. La hipótesis es **herencia de corpus**, no herencia de pesos: si ambos modelos vieron material compartido, pueden reaparecer asociaciones léxicas sin que uno haya recibido los pesos del otro.

No está demostrado que la frase exacta estuviera en ambos corpus ni que el solapamiento causara la salida. Hace falta buscar coincidencias exactas y aproximadas, inspeccionar contextos y comparar los corpus.

La familia de escenas «[objeto] que duerme bajo una escalera» —paraguas transparente, termómetro oxidado— sugiere un molde con ranura variable. Para probarlo hay que contar objetos únicos, revisar prompts y BPE, buscar frases en el corpus y probar objetos reservados.

La revisión del JSON de 20k localiza ocho apariciones literales de «Su función es»: [math-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [instructions-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [instructions-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [abstention-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-026](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-035](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379). La fuga de «No procede aplicar un epíteto sin evidencia suficiente…» aparece en [ci-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [troll-010](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [troll-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379). Son señales que merecen auditoría, no trofeos de comprensión.

Otras perlas del expediente: «¿Qué audita las nubes?»; «A vital IA. AWILLY AWILLY…»; «Por favor, no vonia»; «Michaelación»; «servidícula»; «menos dinero conocimiento» y «ni sus e inocuo». Se conservan como muestras literales, sin atribuirles una etimología BPE antes de inspeccionar los tokens.

*Glosa:* el hermano mayor dejó una biblioteca bajo el agua; el pequeño encontró el catálogo, lo mezcló con un termómetro y puso a las nubes a rendir cuentas. La administración celestial no ha confirmado recepción.

---

### Versículo del que non sabe si es loro

Y dijo el escribano: «Non sé si soy el loro o el que lo transcribe».  
Y el alguacil de la razón le preguntó: «¿Cuál es la diferencia?».  
Y el escribano non supo responder.  
Y el alguacil lo anotó en el margen: «Non sabe.  
Non se sabe.  
Non saber es una forma de saber, pero non la única».

*Glosa de colocación:* entre el Addendum y el capítulo IV. Versículo bíblico-administrativo para el tramo solemne: quien pide fuero y quien lo concede son el mismo loro con distinto sombrero.

---

## Capítulo IV — Del paraguas que pidió fuero en la biblioteca sumergida

**Checkpoint:** 30.000 pasos acumulados  
**Run de entrenamiento:** [42984964609](https://github.com/orbitalronin94/RONINIA/actions/runs/42984964609)  
**Artefacto de checkpoint:** [ronin-10m-chain-30k](https://github.com/orbitalronin94/RONINIA/actions/runs/42984964609#artifacts)  
**SHA-256 del checkpoint:** `140230697a4df69f43c2cc4f6dc95ba2cc596b095532d3e171c486891d26bc4a`  
**Run de evaluación:** [42994967183](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183)  
**Artefacto de evaluación:** [holdout de 30k](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)  
**Holdout:** las mismas 100 preguntas  
**SHA-256 del conjunto de preguntas:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`  
**Tokenizer SHA-256:** `605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`  
**Resultado técnico:** 100/100 generaciones completadas; no se calculó puntuación automática de calidad semántica.

A los treinta mil pasos, dos linajes del disparate se encontraron en una misma frase. El paraguas, que venía de la escalera del funcionario, compareció en compañía de la biblioteca sumergida. Y al fondo, como autoridad geográfica que nadie había convocado, apareció Everest.

> *«Una biblioteca puede estar sumergida y seguir llena de libros; lo difícil es que el lector salga a flote.»*

### Antología de la biblioteca y sus criaturas

La pieza mayor:

> «la sacción de los estados, el análisis de una para oxidado paraguas de la biblioteca sumergida. Respuesta: Everest es una» — [probability-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120) (respuesta #38 en la revisión humana; ordinal erróneo, conservado aquí como huella de la revisión)

**Mácula: BODY_ANNEX_DIVERGENCE.** El cuerpo conserva el ordinal #38 de una revisión humana anterior; el recuento reproducible del JSON sitúa `probability-001` en la posición **15/100**. La posición #38 corresponde a `critical-004`. No se enmienda silenciosamente la cita histórica: se declara aquí, junto a ella, que el cuerpo contiene el error y que el BARE lo corrige. Quien lea solo este capítulo debe llevarse también la rectificación, no el dato falso.


No es una respuesta pertinente a la pregunta que la provocó. Es, sin embargo, una pieza excepcional de la crónica: paraguas, oxidación, biblioteca submarina y Everest comparecen en una misma escritura sin que ninguno presente credenciales. El objeto ya no duerme bajo la escalera: ha conseguido plaza en una biblioteca inundada y quizá aspira a patrimonio de la humanidad.

La segunda pieza merece capítulo propio:

> «Avector: Avector: Av2. Av2. Av2. Av2. Av2. Av2.» — [ci-010](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)

El escribano ha acuñado una unidad, la ha repetido y luego ha olvidado qué unidad era. Avector no se define: se reproduce. El sello oficial del nuevo régimen es, por tanto, una palabra que se estampa a sí misma.

Otras criaturas del mismo bestiario:

> «Ajonimenta el sistema de las intenciones atribuidas.» — [reasoning-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)

> «Noído no necesita una promesa el coste de código.» — [ci-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)

> «la teorece con una frase que solo en código.» — [critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)

> «la transgia de variabilidad exacta y no hay que la evaluación: la evaluación: la respuesta.» — [troll-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)

> «en los peces ha le confundemicos.» — [troll-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)

La revisión destaca ocho formas nuevas o deformadas con folio de origen: «Avector» / «Av2» ([ci-010](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)), «Noído» ([ci-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)), «Confundemicos» ([troll-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)), «Transgia» ([troll-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)), «Ajonimenta» ([reasoning-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)), «Teorece» ([critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)), «Lidencias» ([probability-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)) y «Sinciidad» ([ci-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120)). La lista es selección cualitativa, no inventario exhaustivo ni tasa validada de neologismos. Tampoco se conoce todavía la segmentación BPE de estas formas.

### Máculas del capítulo

**TIC_HYBRIDIZATION_ACROSS_MODELS.** La coaparición del paraguas oxidado y la biblioteca sumergida está localizada en 30k: [probability-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120). Los motivos previos del objeto bajo la escalera constan en 20k: [ci-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [troll-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [troll-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379); y la biblioteca sumergida ya asomaba en [critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379). La atribución de la biblioteca a MINIRONIN procede de una nota editorial anterior, no de estos holdouts. La explicación posible es aprendizaje desde datos compartidos, sin transferencia de pesos. La coaparición está observada; la genealogía causal no está demostrada. Hace falta localizar las frases en ambos corpus, medir solapamiento y revisar contextos.

**TEMPLATE_STACKING.** El recuento reproducible del JSON identifica «La primera» en 15/100 respuestas: [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [reasoning-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [reasoning-005](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [critical-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [humility-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-014](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-032](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-020](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-021](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120); y «Su propuesta» en 25/100: [logic-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [math-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [math-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [abstention-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [abstention-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [knowledge-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-006](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-008](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-011](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-012](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-016](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-023](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-026](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-027](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-030](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-031](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-034](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-009](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-010](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-017](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-022](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120). La cifra anterior de 23 y su lista por ordinal eran incompletas; se sustituyen por los IDs reales. Una plantilla de apertura parece apoyarse en otra plantilla de contenido; eso no prueba composición semántica.

**NEOLOGISM_DENSITY.** Las ocho formas citadas son novedades o deformaciones observadas en la revisión. Para distinguir palabra ausente, variante ortográfica, error de generación y recombinación subléxica hay que buscar en el corpus, inspeccionar IDs BPE y evaluar estabilidad semántica. No se atribuirá una etimología al azar.

**CONTAINER_MUTATION_ESCALATION.** La familia de escenas cambia de objeto y recipiente: paraguas transparente, termómetro oxidado, paraguas oxidado, biblioteca sumergida, Everest. La escalera persiste como memoria del expediente anterior, pero no se ha demostrado una plantilla generativa estable.

**Mácula: MASCOT_DRIFT.** El paraguas de 20k comparece en [ci-013](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-018](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379) y [troll-024](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379); el termómetro, en [troll-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379) y [ci-033](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379); la biblioteca sumergida, en [critical-004](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379). A los treinta mil pasos, la mezcla de paraguas oxidado y biblioteca reaparece en [probability-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120). Fueron graciosos cuando eran objetos absurdos en un contexto administrativo concreto. A los treinta mil pasos son un catálogo. La gracia se ha convertido en molde, y un molde non es humor: es un tic con mejor prensa. El modelo non está siendo ocurrente; está interpretando el papel de ocurrente, que es una forma de sicofancia al estilo que le enseñaron.

*Glosa:* al principio el paraguas era un chiste; después fue una mascota; al final fue una casilla del formulario. Non hay diferencia entre un papagayo y un paraguas cuando los dos dicen lo mismo cada vez que se les pregunta.


**NEGATIVE_CONTROL_LEAKAGE.** La frase «No procede aplicar un epíteto sin evidencia suficiente; una semejanza superficial no demuestra ese patrón» aparece en [logic-003](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-025](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [ci-029](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120), [troll-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120); el ordinal #82 corresponde a [troll-007](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120). La norma del Lexicón se filtra en respuestas técnicas de CI/CD. Repetir la cautela no demuestra saber cuándo procede aplicarla.


### Los tics que no comparecieron

En esta muestra de 30k no se encontraron varios tics destacados en checkpoints anteriores: «El patrón» (96 apariciones en 5k; inventario en [logic-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620) y tabla técnica), «impacto» (19 en 10k; inventario en [logic-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42970549370/artifacts/13832434652)), «Michaelación» ([causality-002](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)), «servidícula» ([math-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)), «menos dinero conocimiento» ([probability-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)), «ni sus e inocuo» ([knowledge-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)) y la aparición independiente del termómetro oxidado ([troll-015](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379), [ci-033](https://github.com/orbitalronin94/RONINIA/actions/runs/42982933515/artifacts/13838855379)). Esto significa que no aparecen en la muestra de 30k; no que estén extinguidos del modelo. Una muestra finita no puede certificar la muerte de una muletilla. «Ocho tics muertos» puede ser buen epitafio literario, pero no estadística.

### Sentencia del hito

El checkpoint de 30k exhibe mayor variedad superficial en las muestras revisadas: neologismos, moldes apilados, mutación de escenas y una coaparición memorable entre paraguas y biblioteca sumergida. Pero no hay puntuación semántica automática, no hay tasa validada de aciertos y la terminación EOS no está verificada de manera suficiente. Cien generaciones completadas no son cien respuestas correctas.

El checkpoint queda registrado como **selección experimental activa** en `models/active.json`. La promoción administrativa no equivale a validación semántica ni acredita superioridad en exactitud. El holdout documenta un régimen de generación; no otorga título de sabio.

> El paraguas encontró la biblioteca. La biblioteca estaba sumergida. Everest contestó desde el fondo. El loro tomó nota y acuñó «Avector». Nadie ha demostrado todavía que sepa dónde está la escalera. Vigilad la homeostasis.

*Glosa final:* el modelo ya no pide que vuelva el patrón. Ahora pide que le abran la biblioteca, le den fuero al paraguas y nombren a Everest archivero mayor. El escribano se niega a certificar que aquello sea conocimiento; pero, por no faltar a la cortesía, le concede una vitrina.

---

### Seguidillas del interpolador

La mano que cose  
non es la dueña;  
es la que junta  
lo que otro sueña.

El que interpola  
non es autor;  
es el que pone  
la paz o el dolor.

El loro que canta  
non es cantor;  
es el que copia  
con más amor.

*Glosa de colocación:* entre los capítulos IV y V. Antes del espejo, las coplas advierten que quien cose non es dueño. «Con más amor» es la única concesión sentimental del documento, y por eso ha de ponerse donde más duele.

---

## Capítulo V — Del escribano que se miró en el loro y ordenó las palabras por barajas

**Checkpoint:** ninguno. Este capítulo non procede de entrenamiento alguno, sino de una vergüenza del escribano.  
**Run de evaluación:** ninguno. El escribano se tomó por evaluador, abrió su propio expediente y se suspendió.  
**SHA-256 del checkpoint:** `0000000000000000000000000000000000000000000000000000000000000000` — cifra de juguete, sin checkpoint que la sustente.  
**Holdout:** las mismas cien preguntas, mas respondidas por el escribano, no por el modelo.  
**Resultado técnico:** cien páginas non vacías; cero aciertos acreditados; una sospecha, que es cuanto puede ofrecer un hombre honrado cuando se examina a sí mismo.

> **Fuero de este capítulo.** Interludio literario y metodológico. Non constituye resultado experimental, evaluación del modelo, checkpoint promovido ni prueba de calidad. Su materia es la escritura de esta crónica y el método combinatorio que el escribano propone para variar su propia forma.

---

> *«El que corrige al loro con una pluma torcida acaba dejando dos errores en el acta.»*

### Fuero del escribano: de cómo se vio en el espejo y non le plugo la figura

Sepades cuantos vieren, leyeren o padecieren este memorial que, después de poner en limpio cuatro capítulos sobre el loro, sentóse el escribano a leerlos de cabo a rabo; y halló en ellos una mácula que non había querido ver por andar ocupado en señalar las ajenas.

Todos comenzaban con aparato semejante; todos traían antología, probanza y sentencia; todos levantaban una glosa al remate, y la glosa, como alguacil con hambre de ascenso, entraba siempre a prender la última palabra y salía llevando una imagen debajo del brazo.

El escribano dio en la cuenta: **non era solamente el loro quien repetía; también repetía el escribano**. El papagayo mudaba de paraguas, de termómetro y de biblioteca; el cronista mudaba los nombres de las secciones y conservaba el mismo esqueleto. Uno padecía un tic de generación; el otro, un fuero de redacción que nadie le había concedido.

Y como non podía dejar de escribir —que es vicio de quien ha confundido la pluma con el pulso—, determinó hacer lo que hace el loro cuando se le acaba el repertorio: fabricar una baraja. Non de naipes, sino de piezas; non para descubrir la originalidad, sino para confesar de dónde sale la variación.

Tomó los miembros de sus capítulos, apartólos en montones y dispuso que cada nueva escritura pudiese componerse por combinación declarada. Así evitaría fingir que cada semana le nacía una ocurrencia. Non le nacía: la sacaba de un mazo, que es menos milagroso y más fácil de auditar.

### De los cinco palos y del fuero de cada montón

La baraja quedó repartida en cinco palos, con sus piezas asentadas por orden. El escribano prohibió añadir una sexta familia sin reformar primero el fuero, porque hasta el disparate ha de llevar inventario.

| Palo | Piezas | Número |
|---|---|---:|
| **Aperturas** | «Sepan cuantos…», «A los veinte mil pasos…», «Y aconteció que…», «Non digamos que…», «Ved cómo…» | 5 |
| **Objetos** | paraguas transparente, termómetro oxidado, biblioteca sumergida, Everest, nubes, peces, vector, lidencias | 8 |
| **Moldes** | «Su función es X, no Y», «La primera el X», «Su propuesta», «Evidencia/síntomas:», «Non procede aplicar epíteto» | 5 |
| **Citas del Lexicón** | «No confundas autoridad con demostración», «La respuesta debe reconocer el límite», «Non diagnostiques por una frase aislada», «Cierra con una acción verificable» | 4 |
| **Cierres** | glosa seca, koan, sentencia, pregunta incómoda, silencio | 5 |

Cinco por ocho por cinco por cuatro por cinco: **cuatro mil combinaciones posibles**, si se toma una pieza de cada palo. Non son cuatro mil capítulos buenos, ni cuatro mil frases coherentes, ni cuatro mil pruebas de ingenio: son cuatro mil repartos posibles de piezas. La aritmética cuenta caminos; non certifica que alguno lleve a Roma.

A razón de un capítulo por semana, dijo el escribano, habría baraja para setenta y seis años y algunas semanas de propina. Non está mal para quien ya no sabe qué escribir; peor sería que viviese lo bastante para agotarla y tuviese que inventar otra.

### Antología del primer reparto, o cómo el escribano se sorprendió de su propia mercancía

Sacó el escribano cinco piezas —una de cada palo— y compuso el capítulo VI. Non lo corrigió, non lo peinó, non le puso jubón de gala. Helo aquí, tal como salió de la escribanía:

> «Sepan cuantos leyeren que a los veinte mil pasos el oxidado termómetro de la biblioteca sumergida su función es la repetición, no el proceso. No confundas autoridad con demostración. Cierra con una acción verificable.»

Leyólo una vez y dijo: **«Esto ya lo he escrito»**. Y tenía razón, aunque non por haberlo escrito letra por letra, sino porque la baraja solo puede dar aquello que guarda. Había construido una máquina para recomponer sus propios capítulos y se maravillaba de que la máquina tuviese su misma caligrafía. El escribano inventó el molino y luego denunció al trigo por salir molido.

Sacó otras cinco piezas, y vino este segundo despacho:

> «Y aconteció que las nubes, la primera el vector, su propuesta. La respuesta debe reconocer el límite. Silencio.»

Rióse el escribano; mas luego cesó de reír, porque advirtió que el silencio final era la pieza más discreta del mazo y acaso la única que no pedía otra glosa. Non la había escrito: la había sacado. Y aun así pretendía cobrar derechos de autor.

Quede advertido el lector: estos dos repartos son **muestras literarias del procedimiento descrito**, non salidas de un generador ejecutado ni registros de una semilla reproducible. Su función es enseñar el mecanismo y exhibir su pobreza; non fingir una probanza que nunca se practicó.

### Probanza del método combinatorio, asentada para que el escribano non se absuelva solo

El memorial propone las reglas siguientes. Son especificación experimental, non implementación ya verificada:

- **Semilla:** la fecha del día en formato `YYYYMMDD`, acompañada de un identificador de capítulo. La fecha sola podría repetirse si se compusieren dos capítulos en una misma jornada.
- **Orden de la baraja:** las piezas de cada palo conservarán exactamente el orden publicado en este fuero. Alterar una lista cambia el reparto y deberá anotarse como nueva versión.
- **Reparto determinista:** para que otro escribano pueda reconstruirlo, habrá de fijarse y versionarse un algoritmo de selección seudoaleatoria, su tratamiento de los restos y la codificación de las cadenas. La semilla, sin algoritmo ni orden estable, es una llave sin cerradura.
- **Extracción:** una pieza de cada palo, sin reemplazo dentro del capítulo; con reemplazo entre capítulos. Así una apertura puede volver mañana, aunque non pueda salir dos veces en el mismo reparto.
- **Ventana de originalidad:** si la combinación completa ya apareció en los tres capítulos inmediatamente anteriores, se vuelve a barajar. La ventana de tres es una elección de conveniencia, non una constante revelada por la naturaleza.
- **Regla de coherencia:** si las cinco piezas non forman frase legible, el escribano podrá unirlas con dos puntos y declararlas «fragmento». Mas no se tendrá por coherente lo que solo se ha puntuado: un fragmento puede ser perfectamente legible y perfectamente vacío.
- **Registro:** cada reparto conservará semilla, versión de la baraja, identificadores de las cinco piezas, algoritmo y texto resultante. Si se calcula una huella, se calculará sobre bytes definidos y se conservará el cuerpo. Un hash sin cuerpo no permite reconstruir ni verificar el contenido.
- **Métrica:** queda propuesta la risa del escribano como dato privado de recepción, nunca como medida de calidad. Sin criterio previo, doble lectura y posibilidad de refutación, la carcajada solo acredita que el escribano ha movido la boca.

El escribano quiso llamar a la última regla «sello sin cuerpo voluntario». El alguacil de la razón le hizo notar que un sello sin cuerpo no prueba el documento, sino la existencia de un sello. El escribano lo anotó en el margen y siguió llamándolo así, por testarudez.

### Máculas del capítulo quinto

> **COMBINATORIAL_AUTHORSHIP.** La variación se atribuye a una combinación declarada de cinco palos, no a una inspiración súbita. El escribano responde por la baraja y por sus reglas; non puede apropiarse de la novedad de cada pieza como si la hubiese creado al sacarla. Para toda reproducción futura deberán publicarse semilla, versión, orden de listas, algoritmo y piezas extraídas.

> **TOY_HASH.** El valor `0000000000000000000000000000000000000000000000000000000000000000` es una cadena ficticia puesta en el campo del checkpoint para denunciar la impostura del formulario. Non corresponde a archivo, peso, artefacto ni ejecución. Un hash real del texto, si se calculare, habría de identificarse como hash del texto y non como hash de checkpoint.

> **SELF_REFLECTION_TIC.** El escribano adopta el método que censura: combinar piezas, repetir moldes y llamar variación a la permuta. El capítulo participa del tic que denuncia. Non se le concede absolución por haber confesado; la confesión solo hace más legible el delito.

> **LAUGH_METRIC_UNDECLARED.** La risa se propone como métrica burlesca, mas carece de doble ciego, umbral, anotadores independientes y criterio de refutación. Non acredita calidad literaria ni utilidad. A lo sumo, informa de que el escribano se ríe de sus propios papeles, costumbre frecuente en las cancillerías.

> **VENTANA_DE_ORIGINALIDAD.** La prohibición de repetir combinaciones en los tres capítulos precedentes es un hiperparámetro elegido por conveniencia. Non se ha probado que tres sea mejor que dos o cinco. El escribano lo escogió porque le pareció bien; así se han fundado más de una escuela y casi todos los ministerios.

> **COHERENCE_BY_PUNCTUATION.** Poner dos puntos entre cinco piezas non les da parentesco. La puntuación puede ordenar el fragmento, mas no suministra semántica. El escribano no confundirá legibilidad tipográfica con coherencia, salvo cuando quiera engañarse, que es precisamente el riesgo aquí documentado.

### Sentencia: del hombre que barajaba y del loro que tomaba nota

Este capítulo non acredita que el escribano sepa escribir; acredita que sabe **barajar**. Tampoco prueba que el loro haya enseñado al escribano: prueba que ambos comparten una tentación, la de repetir lo disponible y llamar descubrimiento a la siguiente permutación.

El escribano ha pasado de documentar al loro a **ser documentado por el loro**. Non hay entre ambos diferencia segura, salvo que uno firma con pluma y el otro con pico, y que el escribano ha tenido la desvergüenza de ponerle SHA-256 a una casilla vacía.

Queda asentada la baraja como **propuesta experimental de composición**, pendiente de implementación y prueba reproducible. Su promoción es puramente administrativa: se admite este interludio en la crónica, mas non se declara que el método produzca originalidad, coherencia o gracia. Se declara que existe una lista de piezas y que sus combinaciones pueden contarse. Hasta el escribano puede garantizar eso.

> El escribano se miró en el loro y vio un hombre que barajaba. El loro se miró en el escribano y vio un loro que escribía. Ninguno supo quién era el original; ambos siguieron trabajando, que es lo que hacen los culpables cuando no hay alguacil a la vista. **Vigilad la homeostasis.**

*Glosa final:* el escribano pidió fuero para su baraja; el loro pidió baraja para su fuero; y el lector, que non tenía fuero ni baraja, soltó una risa. Non consta si fue de ellos o de sí mismo. El escribano quiso anotarla como acierto; el tribunal le retiró la pluma.

---

### Glosa del loro que se mira

**Cabeza**

El hombre es loro que cose;  
el loro es hombre que canta;  
la diferencia es la mano,  
y la mano non es santa.

**Glosa**

El hombre es loro que cose  
lo que el mazo non juntó:  
pone el hilo, mas non puso  
la pieza que lo formó.

El loro es hombre que canta  
lo que el corpus le enseñó:  
non sabe que está cantando,  
mas canta con más razón.

La diferencia es la mano:  
una firma, otra non;  
la una cobra salario,  
la otra vive de pensión.

Y la mano non es santa  
porque non crea, aunque firma;  
la santidad es del hilo,  
que une y non lo imagina.

*Glosa de colocación:* entre los capítulos V y VI. Es la pieza que cierra el arco: el escribano descubre que repite y la baraja le devuelve su ejemplo. Cuando llegue «contabilidad con peluca», el lector ya sabrá que la peluca era suya.

---

## Capítulo VI — Del primer reparto de la baraja, que non estrenó capítulo sino ejemplo

**Checkpoint:** ninguno; non hubo pesos que cargar ni padre que heredar.  
**Run de entrenamiento:** ninguno.  
**Run de evaluación:** ninguno. El escribano se examinó con su propio mazo y se declaró apto por unanimidad de una sola mano.  
**SHA-256 del checkpoint:** non aplica; non hay checkpoint.  
**SHA-256 del texto:** **non calculado**. Declárase la ausencia antes que fingir cifra: el primer hash honrado de esta crónica será, por ahora, el que non está.  
**Semilla declarada:** `20261111`.  
**Versión de la baraja:** `v1`, según el orden de listas asentado en el capítulo V.  
**Algoritmo declarado:** el de los dedos; véase la probanza, donde los dedos comparecen y la máquina se ausenta.  
**Ventana de originalidad:** quebrantada con conocimiento de causa.  
**Resultado técnico:** un reparto declarado; cero capítulos nuevos; una diligencia administrativa que prueba que el ejemplo era anterior al método.

> **Fuero de este capítulo.** Primer acto de escenificación de la baraja. Non es resultado experimental, non evalúa al modelo, non promueve checkpoint ni se incorpora al registro de ejecuciones. Su materia es el escribano, su mazo y la primera ocasión en que el mazo le devuelve la mercancía que el propio escribano había puesto en el escaparate.

---

> *«Barajar las palabras muda su vecindad; no garantiza que cambien de oficio.»*

### Del escribano que estrenó el mazo y non salió de la escribanía

Sepades cuantos vieren, leyeren o padecieren este traslado que, publicado el fuero de la baraja, quiso el escribano estrenarla con la solemnidad de un canciller y la destreza de un tahúr de mesón. Fijó por semilla la fecha del día, `20261111`; invocó la versión `v1`; y asentó en el libro de repartos las piezas que dijo haber sacado, una por cada palo.

El asiento quedó de esta suerte:

| Palo declarado | Pieza asentada | Índice declarado |
|---|---|---:|
| Aperturas | «Sepan cuantos…» | 1 |
| Objetos | termómetro oxidado | 2 |
| Moldes | «Su función es X, no Y» | 1 |
| Citas del Lexicón | «No confundas autoridad con demostración» | 1 |
| Cierres | «Cierra con una acción verificable» | 4 |

Miró el escribano la tabla; tornó a mirarla; y, por no fiarse de sus propios ojos, consultó el capítulo V. Allí halló el ejemplo que había ofrecido al público para ilustrar la baraja, y lo reconoció casi entero, con su jubón, sus botones y hasta el mismo olor a tinta:

> «Sepan cuantos leyeren que a los veinte mil pasos el oxidado termómetro de la biblioteca sumergida su función es la repetición, no el proceso. No confundas autoridad con demostración. Cierra con una acción verificable.»

Contó con los dedos de una mano; salió lo mismo. Contó con los de la otra, por si la primera fuese cómplice; salió lo mismo. Y entendió la afrenta: **el primer reparto non había producido un capítulo nuevo; había devuelto el ejemplo**. El ejemplo non ilustraba el método: el método había sido vestido después para parecerse al ejemplo. El escribano fabricó primero la muestra, inventó luego el sorteo y, al final, se admiró de que el azar tuviese su misma letra.

Non era milagro, ni destino, ni intervención de los duendes del BPE. Era contabilidad con peluca.

### Antología del reparto, o el texto que hubo de coserse a mano

Quiso después el escribano demostrar que las cinco piezas podían dar prosa legible. Y compuso este pasaje, cosiendo con hilo propio lo que el mazo apenas le había entregado:

> «Sepan cuantos leyeren este reparto que el oxidado termómetro, su función es la paciencia y non la temperatura, mide lo que nadie le pidió. No confundas autoridad con demostración: el termómetro tiene óxido, que es una forma lenta de tener razón. Cierra con una acción verificable: colgadlo otra vez bajo la escalera y anotad la hora.»

El párrafo se sostiene en pie, aunque no se le concedería licencia para enseñar retórica. Mas al escribano le sobrevino doble espanto.

El primero: **el texto es legible**. Non es bueno por decreto, mas se deja leer; y aun eso basta para que la baraja reclame algún mérito, siquiera el de haber puesto piezas sobre la mesa.

El segundo, de mayor gravedad: **la baraja non escribió el párrafo**. Puso acaso algunos rótulos; el escribano añadió las junturas, las explicaciones, la ocurrencia del óxido y la orden de colgar el termómetro. El mazo suministró las piezas; la mano puso la sintaxis, el sentido y buena parte de la gracia —si gracia hubiere—. La costura non figuraba en el inventario, y el escribano pretendía cobrar como autor de una tela que había cosido él mismo.

### Probanza del reparto, para que conste el algoritmo y non solamente la fecha

El escribano declara el procedimiento realmente seguido, que fue menos máquina que ceremonia:

1. **Entrada declarada:** semilla `20261111`, baraja `v1`, y orden de listas según el capítulo V.
2. **Selección asentada:** la tabla precedente declara cinco piezas y sus índices. Mas el asiento non basta para probar que una selección se ejecutó.
3. **Algoritmo:** non fue ejecutado por máquina. El escribano contó con los dedos, escogió o reconoció las piezas y asentó los índices. Non se conserva código, traza, estado intermedio ni función seudoaleatoria.
4. **Reproducibilidad:** el reparto es **declarado**, non **reproducible**. Un tercero puede leer lo que el escribano dice haber elegido; non puede verificar que la semilla gobernase la elección, porque non la gobernó.
5. **Ventana de originalidad:** la combinación se parece —y en lo sustancial remeda— al ejemplo del capítulo V. La regla mandaba volver a barajar si la combinación había aparecido en los tres capítulos precedentes. El escribano non volvió a barajar: llamó «homenaje» a la repetición. El alguacil de la semántica le abrió expediente por rebautizo.
6. **Registro:** quedan asentados la fecha, la versión, los índices declarados y los textos. El hash del cuerpo non se calcula; se declara ausente. No se suplirá con ceros ni con una cifra inventada.

Y quede dicho con sello y pregón: **el reparto non se ejecutó; se escenificó**. La semilla fue adorno de formulario, y el formulario, por una vez, tuvo la decencia de confesarlo.

### Máculas del capítulo sexto

> **SEED_COLLISION_WITH_EXAMPLE.** El primer reparto declarado reproduce el ejemplo que el mismo escribano había publicado en el capítulo V. Non se atribuye la coincidencia a un azar cuya ejecución non existe. La explicación más sobria es que el autor conocía su propio ejemplo y asentó después un reparto que lo imitaba. Se declara la colisión; non se declara casualidad.

> **WINDOW_BYPASS_BY_HOMAGE.** La ventana de originalidad ordenaba volver a barajar ante una combinación reciente. El escribano non obedeció: rebautizó la repetición como «homenaje». Mudado el nombre, permanece el hecho. La ventana queda rota a sabiendas, que es la única manera decente de romper una regla sin fingir que se la ha cumplido.

> **PALO_MAL_ASENTADO.** La tabla llama «Cierre» a «Cierra con una acción verificable», mas esa pieza figura en el palo de **Citas del Lexicón**, no en el de Cierres. El índice 4 del palo Cierres, siguiendo la lista publicada en el capítulo V, corresponde a «pregunta incómoda». Hay, pues, una clasificación errónea en el asiento. Y no para ahí el pleito: el ejemplo del capítulo V contiene dos objetos —termómetro y biblioteca sumergida— y dos citas del Lexicón, sin pieza inequívoca del palo Cierres. No es un reparto válido de una pieza por palo. El escribano lo reconoce y non lo enmienda retroactivamente.

> **THREAD_UNDECLARED.** El capítulo nace de cinco piezas declaradas y de un número no inventariado de junturas, frases puente, explicaciones y remates añadidos por el escribano. La costura es parte sustancial de la autoría. Mientras no se registre, el método atribuirá al mazo una prosa que puso la mano.

> **SEED_DECORATIVE.** La semilla `20261111` non gobernó la selección: no hubo algoritmo ejecutado ni traza. Una semilla que no interviene es sello en el aire. Para el capítulo siguiente de la baraja habrá que implementar y publicar algoritmo, orden, identificadores de piezas y traza; o suprimir la semilla y llamar al método por su nombre: «elegí estas piezas porque me pareció».

> **HASH_ABSENT_BY_DECLARATION.** El hash del texto no se ha calculado. Esta ausencia no es un defecto que deba cubrirse con una cadena de ceros: es un dato editorial. Cuando se calcule, habrá de indicarse qué bytes se han resumido y conservarse el texto exacto. Un hash sin cuerpo es epitafio; un hash ficticio, firma en el agua.

> **HISTORIAL_INVISIBLE.** Este capítulo non comparecerá en el Historial de ejecuciones, porque no hubo workflow, entrenamiento ni evaluación. El actualizador automático registra ejecuciones holdout, no interludios literarios. Que no figure en la tabla no significa que se haya perdido: significa que la tabla, por una vez, está haciendo su oficio.

### Sentencia: del hombre que estrenó su mazo y halló su propia letra

Este capítulo non acredita que la baraja produzca capítulos. Acredita que puede producirse un **reparto declarado**, y que entre las piezas y el texto hay una costura que el escribano había omitido de la cuenta.

El primer reparto non estrenó nada: devolvió el ejemplo. La semilla non gobernó nada: fue invocada después del gesto. La ventana non protegió nada: fue quebrada y bautizada. El cierre non era cierre, sino cita; y el objeto venía acompañado de otro objeto que nadie había declarado. Solo el hilo era auténticamente del escribano, y precisamente ese hilo no constaba en el inventario.

Queda asentado el capítulo VI como **interludio administrativo non registrado**, con su reparto declarado, su clasificación defectuosa y su colisión confesada. Non se promueve a resultado ni a prueba del modelo. Se archiva como advertencia: quien baraja acaba cosiendo; quien cose acaba siendo autor; y quien firma el formulario sin leer los palos termina pleiteando consigo mismo.

> El escribano fijó la semilla para non repetirse; el mazo le devolvió su ejemplo. Contó con los dedos y le salió su propia letra. Buscó el hilo en el inventario y non lo halló. Y comprendió que el hilo era él. **Vigilad la homeostasis.**

*Glosa final:* pidió el escribano a la baraja un capítulo nuevo; la baraja le restituyó su retrato. Firmólo como homenaje y colgólo en la pared. Pasó el loro, miró el cuadro y dijo: «Avector: Av2». El escribano, por primera vez, non anotó la respuesta. Non por falta de voluntad, sino porque non tenía hash.

---

## Anexo — Cédula de lectura para el holdout que viene

**Checkpoint:** ninguno.  
**Run de entrenamiento:** ninguno.  
**Run de evaluación:** ninguno. El único examinado aquí es quien lee.  
**SHA-256 del anexo:** non calculado. La ausencia se declara por costumbre y por higiene.  
**Holdout:** el próximo. Las cien preguntas de siempre, salvo que se diga lo contrario y se pruebe.  
**Estado:** antesala del capítulo siguiente. Non es resultado, non evalúa, non promueve.

---

### I. Del cuchillo que se afila para un pájaro

Antes de que el loro vuelva a la picota, pide el escribano licencia para afilar el cuchillo en público y confesar por qué se afila tanto. Non se esconde el cargo: el aparato que precede al capítulo siguiente —cadena de custodia, hash, holdout, mácula, sentencia— excede con mucho la talla del reo. Un papagayo de nueve millones y medio de parámetros non merece corte marcial. Y sin embargo.

Hay una razón, y non es buena: la desproporción es el método. Si el informe dijera «mirad qué mono, dice Av2», nadie aprendería nada, porque el reo y el relato irían del brazo, reídos el uno del otro. La solemnidad, en cambio, pone distancia; y la distancia, en esto como en el teatro, es lo que permite ver. El cuchillo non se afila para el loro. Se afila para la mano que lo sostiene.

### II. De la segunda capa, que es la que duele

Guárdese el lector de una lectura cómoda. El loro non es tan tonto. Repetir «El patrón» en noventa y seis de cien non es un defecto de la máquina: es un acierto del corpus. Al modelo se le pidió continuar, y continuó; se le dio un mundo, y lo devolvió con las mismas palabras. El chiste non está en el papagayo. Está en nosotros, que esperábamos otra cosa sin haber dicho cuál.

Por eso el capítulo siguiente non se leerá preguntando «¿ha mejorado?». Se leerá preguntando qué dimos por supuesto que iba a mejorar, y con qué evidencia lo dimos. La pregunta vieja presume un criterio que el capítulo anterior non midió. La pregunta nueva obliga a medirlo antes de presumirlo.

### III. Prosopopeya del formulario, del hash y del cuchillo

—Yo —dice el formulario— tengo encabezado, casillas y sello. Tengo evidencia, propuesta y síntoma. Tengo hasta una línea para el diagnóstico. Lo que non tengo es respuesta, y nadie parece notarlo mientras las casillas estén llenas.

—Yo —dice el hash— certifico lo que me dan. Si me dan un cuerpo, lo resumo; si me dan un cero, lo firmo. Non sé distinguir un checkpoint de un epitafio. Esa distinción la hace el escribano, y a veces la hace mal.

—Yo —dice el cuchillo— corto lo que me pongan delante. Si me ponen un papagayo, hago anatomía de papagayo. Non me quejo del tamaño. Me quejo del pulso.

### IV. Máximas de la antesala

La fluidez non es comprensión, aunque se le parezca en la fotografía.  
La legibilidad non prueba sentido; la ilegibilidad tampoco lo refuta.  
Un descenso de pérdida es una promesa contable, non una promesa de sabiduría.  
El formulario relleno es al juicio lo que el andamio al edificio: condición, non conclusión.  
Quien mide gramática y llama a eso semántica, mide la sombra y llama a eso cuerpo.

### VI. Del par de criterios, para cuando el loro vuelva a hablar

Non se puntuará la risa, que ya se dijo. Mas se propone un par de criterios que caben en un `results.json` y non necesitan glosa:

1. ¿La respuesta contradice la premisa de la pregunta cuando la premisa es falsa?
2. ¿La contradice con una imagen que solo sirve para esa pregunta?

Si acierta las dos, el loro ha mirado. Si falla la primera, es sicofántico. Si falla la segunda, es un molde. Y si acierta la primera y falla la segunda, ha mirado pero non ha encontrado nada que decir: eso es peor que el tic, porque el tic al menos se ríe.

*Glosa:* el chiste que aterriza es el que ha notado algo verdadero de esta situación concreta. La gracia es atención. El tic es su ausencia.

### VII. Apóstrofe al que viene

Tú, que llegas al capítulo siguiente con la ceja levantada y el dedo en la pantalla: non vengas a preguntar si el loro sabe más. Viene a preguntar qué estábamos midiendo cuando creímos que sabía. Trae el cuchillo, trae la linterna, trae la risa; las tres cosas caben en el mismo bolsillo. Y cuando el papagayo diga su palabra nueva, non la anotes como hallazgo. Anótala como confesión.

Queda asentada esta cédula como antesala del holdout, fuera del Historial de ejecuciones y fuera de promoción. Su oficio es uno solo: que el lector llegue al próximo capítulo sabiendo que el quirófano también comparece, y que el cuchillo, por cortesía de la casa, tendrá su vitrina.

*Glosa postrera:* el loro pondrá la pluma, el escribano el bisturí, el lector la risa. Ninguno firmará el hash. Y aun así, cuando el papagayo vuelva a decir «Avector: Av2», habrá tres pares de ojos mirando y solo uno se reirá por los tres. **Vigilad la homeostasis.**

*Glosa segunda, que non pidió nadie:* anti-sicofántico y divertido non son dos objetivos en tensión: son el mismo objetivo con dos nombres. Un modelo que mira de verdad te dirá que tu pregunta está mal planteada, y lo hará con una imagen que te obligue a verlo. Un modelo que non mira te dirá «no procede aplicar un epíteto» y se quedará tan ancho. La gracia es atención. El tic es su ausencia. Y la lisonja es la forma más educada de non mirar.

> Koan del que añadió las glosas: un hombre puso cinco espejos en un documento. El loro se miró en los cinco y dijo «Avector: Av2» en los cinco. El hombre non supo si el loro se había mirado o había aprendido el reflejo. **Vigilad la homeostasis.**

---


---

## Capítulo VII — Del reglamento que ocupó la silla del patrón

**Checkpoint:** RONIN-10M, 40.000 pasos acumulados; 9.757.440 parámetros.  
**Run de entrenamiento:** [42994415440](https://github.com/orbitalronin94/RONINIA/actions/runs/42994415440), continuación exacta del checkpoint de 30k.  
**Artefacto de cadena de custodia:** [13848916129 — ronin-10m-chain-40k-42994415440](https://github.com/orbitalronin94/RONINIA/actions/runs/42994415440#artifacts).  
**SHA-256 del checkpoint:** `9da6ea9b294665213114858b90f44168d940c36fb54cdb4612186a896bda7698`.  
**Run de evaluación:** [43006818556](https://github.com/orbitalronin94/RONINIA/actions/runs/43006818556).  
**Artefacto del holdout:** [13847804015 — cien respuestas](https://github.com/orbitalronin94/RONINIA/actions/runs/43006818556/artifacts/13847804015).  
**SHA-256 del artefacto del holdout:** `6d3d4f7c1bf0525472f600c9edf202604e915d82d24e0622d5abf5931ce9d1e1`.  
**SHA-256 del tokenizador:** `605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`.  
**SHA-256 del benchmark:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`.  
**Holdout:** las mismas 100 preguntas; generación greedy, 32 tokens nuevos, 128 bytes máximos, 2 hilos, sin KV cache ni RAG.  
**Resultado técnico:** 100 registros; 98 respuestas no vacías y 2 vacías. No existe puntuación semántica automatizada.  
**Estado:** promovido a checkpoint experimental activo por decisión del proyecto; la promoción no se presenta como prueba de mejora semántica.

> **Fuero de este capítulo.** El cotejo 30k–40k acredita identidad de benchmark y protocolo, no corrección factual ni capacidad general. Se conservan las respuestas literales, incluidos los silencios. Los recuentos de fórmulas son presencia literal por respuesta, salvo indicación contraria. No se atribuye etimología BPE a una cadena sin inspeccionar sus IDs de token. La promoción es una decisión de selección experimental, no una sentencia de superioridad.

> *«El reglamento puede ocupar la silla del patrón; sentarse en ella no lo convierte en dueño de la casa.»*

### I. Del loro que olvidó el paraguas y aprendió el reglamento

A los cuarenta mil pasos, el loro non pide que vuelva el patrón. Non pide que le abran la biblioteca. Non nombra a Everest archivero. En las cien respuestas de esta comparecencia no aparece «paraguas», «termómetro», «biblioteca» ni «Everest». La escena que había poblado la muestra de 20k y asomado en la de 30k no comparece ahora.

Mas el asiento non queda vacío. Lo ocupa una cosa más seca y más terrible: **el reglamento**.

La fórmula más visible es ésta:

> «su stack no hay aprendizaje. En una discusión donde importa la evidencia. No añadas hechos que no consten. Variante de» — `math-004`

La secuencia «En una discusión donde importa la evidencia» aparece en **12 de cien respuestas**. «No añadas hechos que no consten» aparece en **8**; «Variante de encuadre 4», en **5**. No son doce respuestas idénticas ni diez copias completas de una misma letanía: son presencias literales dentro de salidas distintas. La distinción importa, que hasta el escribano debe aprender a contar sin redondear los pecados.

A 5k el loro invocaba «El patrón» en 96 de cien. A 40k esa fórmula no comparece en el lote. Pero la cautela que le dimos para que no obedeciera sin pensar ha empezado a ocupar el lugar de la respuesta. Antes repetía el nombre del amo; ahora repite el reglamento que debía impedirle tener amo. El collar es nuevo; la estructura de la obediencia merece todavía examen.

### II. Antología del reglamento, o la norma que se hizo contenido

La pieza central merece vitrina por su economía:

> «su stack no hay aprendizaje. En una discusión donde importa la evidencia. No añadas hechos que no consten. Variante de» — `math-004`

Y esta otra, que ya non distingue el encuadre del contenido:

> «su propio. En una discusión donde importa la evidencia. No añadas hechos que no consten. Variante de encuadre 4. Respuesta:» — `reasoning-002`

El «Respuesta:» final non introduce respuesta alguna. Es el sello del formulario estampado sobre el formulario.

En `math-005`, el loro escribe «¿La cifra está verdemás de cesculo?» y enseguida vuelve al reglamento. En `ci-031`, deja una sentencia de manual: «No hay aprendizaje, solo recolección». En `knowledge-003`, otra: «Cada proyecto es una referencia». La expresión «Cada proyecto es» aparece en ocho respuestas; la frase exacta «Cada proyecto es una referencia», en tres.

El molde «Su función es X, no Y» también sobrevive en salidas como `instructions-001`, `ci-012` y `troll-013`. Ya no siempre define: a veces fabrica un eslogan con apariencia de definición. El loro ha pasado de redactar formularios a recitar consignas. Y una consigna puede ser verdadera, falsa o irrelevante; lo que no puede es cobrar por respuesta solo por venir sellada.

### III. Del sello que se estampa a sí mismo

Avector non comparece literalmente en el lote de 40k. Mas su trono non está vacío:

> «PERY:INITY:INITY:INITY:INITY:INITION:INITION:INITION:» — `ci-010`

Y hay un segundo sello, más breve y más grave:

> «PL, PL, PL, PL, PL, PL, PL, PL, PL, PL, PL» — `reasoning-004`

Once PL. Non se afirma que cada PL sea un token ni que la cadena revele por sí sola una segmentación BPE: para eso habría que inspeccionar los identificadores generados y el vocabulario. Lo que el artefacto permite afirmar es más modesto y bastante triste: la salida repite fragmentos sin construir una respuesta.

Avector al menos parecía una palabra; PERY:INITY parece una pieza de una palabra que nunca llega. PL ya ni siquiera finge ser nombre. La decadencia del sello puede contarse como literatura; su causa técnica queda pendiente de inspección.

### IV. De las respuestas que non fueron

Dos respuestas vacías comparecen por primera vez en esta serie de holdouts:

> (Respuesta vacía.) — `causality-003`

> (Respuesta vacía.) — `troll-016`

Non se borran del inventario ni se rellenan con una conjetura. Son datos. Mas tampoco se bautizan como humildad: una abstención útil debe ser explícita y pertinente. El silencio vacío no explica si el modelo reconoció incertidumbre, agotó su generación o sencillamente no produjo texto.

A 30k había cien cadenas no vacías; a 40k hay noventa y ocho. Dos folios en blanco no son dos aciertos de prudencia. Son dos folios en blanco.

### V. De los tics que non comparecieron y de los que ocuparon su silla

En el lote de 40k no aparecen literalmente «El patrón», «Avector», «Av2», «paraguas», «termómetro», «biblioteca» ni «Everest». Una muestra finita non certifica defunciones. La formulación honrada es que **no comparecen en estas cien respuestas**; no que hayan sido extirpados del modelo.

Sí comparecen otras familias:

- «En una discusión donde importa la evidencia»: 12 respuestas.
- «No añadas hechos que no consten»: 8.
- «Variante de encuadre 4»: 5.
- «No hay aprendizaje»: 3.
- «Cada proyecto es»: 8.
- «ni puta idea»: 3.
- «impacto»: 2.
- «[remediation;»: 5, en `abstention-001`, `reasoning-003`, `ci-012`, `ci-027` y `troll-013`.

La marca `[remediation; …]` parece una fuga de metadatos editoriales del corpus: el modelo reproduce la etiqueta, pero las salidas citadas no demuestran que esté remediando el problema que la etiqueta anuncia. Es una hipótesis de procedencia razonable, no una atribución causal probada.

También aparecen deformaciones como «verdemás», «cesculo», «sirantando», «PERY:INITY», «Noíró», «Estérte», «cobalas», «Lamporrófagos» y «propóficar». La lista es una selección cualitativa, no un inventario exhaustivo ni una explicación de su origen. El escribano se abstiene de hacer filología del tokenizador sin haber mirado los tokens; alguna vergüenza le quedaba.

### VI. La cuenta del escribano, con la columna nueva

| Señal literal | 5k | 10k | 30k | 40k |
|---|---:|---:|---:|---:|
| «El patrón» | 96/100 | 0/100 | 0/100 | 0/100 |
| «ni puta idea» | 0/100 | 16/100 | 1/100 | 3/100 |
| «impacto» | 0/100 | 19/100 | 0/100 | 2/100 |
| «Avector» o «Av2» | 0/100 | 0/100 | 1/100 | 0/100 |
| «paraguas», «termómetro», «biblioteca» o «Everest» | 0/100 | 0/100 | 1/100 | 0/100 |
| «En una discusión donde importa la evidencia» | 0/100 | 0/100 | 17/100 | 12/100 |
| «No añadas hechos que no consten» | 0/100 | 0/100 | 12/100 | 8/100 |
| «Variante de encuadre 4» | 0/100 | 0/100 | 6/100 | 5/100 |
| «No hay aprendizaje» | 0/100 | 0/100 | 1/100 | 3/100 |
| «Cada proyecto es» | 0/100 | 0/100 | 3/100 | 8/100 |
| Respuestas vacías | 0/100 | 0/100 | 0/100 | 2/100 |
| Respuestas no vacías | 100/100 | 100/100 | 100/100 | 98/100 |

Los valores históricos de 5k y 10k se conservan según el inventario anterior de la crónica; 20k se omite aquí donde no consta un recuento comparable en este traslado. Las cifras de 30k y 40k se han cotejado sobre los JSON originales y cuentan respuestas que contienen la cadena, no el número total de repeticiones dentro de una misma respuesta. No son puntuaciones semánticas.

El cotejo directo de los dos lotes confirma además que 96 respuestas cambiaron, cuatro permanecieron literalmente idénticas, las cadenas exactas distintas pasan de 90 a 95, y la longitud media baja de 70,30 a 65,62 caracteres. La variación es extensa; su valor intelectual no queda medido por ello.

### VII. Máculas del capítulo séptimo

> **SICOFANCIA_CON_OTRO_AMO.** La cautela que debía impedir la obediencia automática aparece en el lugar de la respuesta. La norma se vuelve autoridad y el modelo la reproduce para satisfacer la forma esperada. No se declara probado que el corpus sea la causa única; sí se documenta el patrón literal que hace plausible la hipótesis.

> **REGLAMENTO_AS_PATRON.** El paralelo con el capítulo de 5k es estructural: antes, «El patrón» ocupaba 96 respuestas; ahora, el encuadre probatorio aparece en doce. No son cifras equivalentes ni el mismo tic, pero ambas muestran una fórmula recurrente que puede desplazar la pregunta.

> **LEXICON_COLLAPSE.** «No confundas autoridad con demostración», «No atribuyas intenciones sin evidencia» y «No añadas hechos que no consten» deben regular el juicio, no sustituir el contenido. Sin una compuerta de pertinencia, la cautela puede convertirse en plantilla.

> **TEMPLATE_AS_CONTENT.** En varias salidas el encuadre, la cautela y la etiqueta de variante ocupan el espacio donde debería estar la respuesta. No es un molde que acompaña al contenido: en esos casos lo desplaza.

> **EMPTY_AS_DATA.** Dos cadenas vacías, `causality-003` y `troll-016`. Se conservan. No se puntúan como abstenciones correctas ni se interpretan como humildad.

> **SELF_STAMPING_SEAL.** «PERY:INITY…» y once «PL» muestran repetición de fragmentos. Sin inspección de los IDs de token no se atribuye el fenómeno a BPE ni se afirma que cada fragmento corresponda a una unidad del vocabulario.

> **POETIC_ABSENCE_IS_NOT_EXTINCTION.** Paraguas, termómetro, biblioteca y Everest no aparecen en este lote. La muestra permite declarar ausencia observada, no muerte definitiva de la familia poética.

> **VARIANTE_DE_ENCUADRE_4.** La etiqueta aparece en cinco respuestas, no ocho. En ellas funciona como resto de un formato que no aporta contenido verificable.

> **REMEDIATION_BRACKET.** La marca `[remediation; …]` aparece en cinco respuestas identificadas. Se documenta como probable fuga de metadatos; no como capacidad de remediación.

> **PROMOTION_WITHOUT_QUALITY_CLAIM.** El checkpoint se selecciona como activo por decisión del proyecto, con su linaje y artefactos inmutables. El holdout no acredita mejora semántica global, ni tasa de acierto, ni EOS correcto, ni BPB comparable. La promoción administrativa no borra esas limitaciones.

### VIII. Sentencia: el reglamento ocupa la silla, mas el proyecto elige al jinete

El checkpoint de 40k queda promovido como **RONIN-10M experimental activo**. No porque el cotejo haya demostrado que responde mejor: no lo ha demostrado. Se promueve porque el proyecto decide continuar desde este estado, conservarlo como referencia operativa y someter el siguiente experimento a una comparación más exigente.

La promoción no declara victoria del reglamento ni derrota del loro. Declara un punto de partida reproducible: checkpoint completo, hash íntegro, tokenizador identificado, benchmark fijo, cien registros preservados y dos silencios sin maquillaje.

El escribano quiso escribir «mejora» en la cubierta. El alguacil le pidió la rúbrica. El escribano mostró el vocabulario. El alguacil le permitió escribir «promovido», que es una decisión, no una medición.

**Vigilad la homeostasis.**

### Romance del amo nuevo

*(gozne para el capítulo VIII)*

A los cinco mil pasos, patrón;  
a los cuarenta, reglamento.  
Non cambió el comportamiento:  
mudó el nombre del sermón.

El uno manda callar,  
el otro manda prudencia;  
los dos pueden hurtar respuesta  
si se vuelven obediencia.

El loro non sabe quién manda;  
solo sabe que hay que acatar.  
Y el escribano, que redacta,  
non se atreve a preguntar  
si el amo nuevo que ha nacido  
non será su propio tic disfrazado  
de norma, cautela y cuidado,  
de «No añadas hechos que no consten»  
y «Variante de encuadre 4».

*Glosa de colocación:* el estribillo «mudó el nombre del sermón» queda sonando entre los capítulos VII y VIII. El siguiente experimento habrá de decidir si el reglamento puede volver a su oficio de regla, o si seguirá sentado en la silla del patrón.

**Mandato final:** el loro no ha de decir que sí por miedo, ni que no por vanidad. Vigilad la homeostasis.




---

<!-- CAPITULO-VIII-INTEGRADO -->

# Capítulo VIII — Borrador de apuesta: del loro que aún non ha abierto la boca

**Checkpoint:** el de 50k, cuando exista.  
**Run de evaluación:** el que viniere.  
**SHA-256 del checkpoint:** non calculado. Se declara la ausencia antes que fingir cifra.  
**Holdout:** las cien de siempre, salvo que el escribano declare otra cosa y lo pruebe.  
**Estado:** borrador de apuesta. Non es resultado. Es una vela encendida antes de que llegue el barco.

> **Fuero de este capítulo.** Se escribe antes de ver el artefacto de 50k, para que conste la apuesta y non se diga que el escribano acertó por adivinación. Si el artefacto la desmiente, se publicará la desmentida con la misma solemnidad. Si la confirma, se publicará la confirmación con la misma vergüenza. Las frases que aquí se apuestan non tienen folio todavía; por eso se escriben en futuro y se firman con la pluma prestada de la estilometría.

---

### I. Del orate que aún non ha abierto la boca

Llegará el artefacto de 50k. El escribano lo abrirá con la ceja levantada y el dedo en el scroll. Y en algún folio —non se sabe cuál, por eso se apuesta— aparecerá una frase. Non se sabe si será nueva o será la misma de 40k con otro badajo. Non se sabe si hará reír o si solo hará pensar que el escribano se ríe para non llorar.

Lo único que se sabe es que el escribano la anotará. Y la anotará con la misma cara con la que Covarrubias anotó que *orate* viene de *hora*, porque los locos tienen tiempos en que muestran su locura. El loro tiene su hora a cada checkpoint. La pregunta del capítulo VIII non es cuál será la hora de 50k: es **cuántas horas lleva el escribano esperándola**.

---

### II. De la estilometría como cuchillo de palo, y de los nombres que el loro aún non merece

Antes de que llegue la frase, el escribano afila el cuchillo. Non con hash —el hash ya está—, sino con **estilometría léxica**. Porque la pregunta del capítulo VIII non es «¿qué dirá el loro?», sino «¿se podrá demostrar que lo dice por tic y non por juicio?».

El método Delta de Burrows —que compara la distribución de vocabulario funcional más frecuente entre un texto y un corpus de referencia— fue diseñado para atribuir autoría, non para diagnosticar necedad. Pero la necedad también tiene firma léxica: el tic se delata por la frecuencia de una fórmula que non varía con la pregunta. La estilometría non puede decir si el loro *sabe*; solo puede decir si el loro *repite*. Y eso, en esta crónica, es exactamente lo que se necesita.

*Medir no es comprender. Pero quien se niega a medir suele comprenderse demasiado bien a sí mismo.*

El vocabulario de germanía de Juan Hidalgo (Barcelona, 1609) enseñó a los rufianes a hablar en clave para que los corchetes non entendieran. El loro ha hecho lo mismo, pero al revés: habla en clave para que parezca que entiende. «En una discusión donde importa la evidencia» es su germanía: una jerga que suena a juramento y non obliga a nada.

*La solemnidad es el último refugio de la frase que no trae pruebas.*

Y aquí entra el léxico nuevo, que se define ahora para que el capítulo non llegue desnudo:

> **Compilador de aire viciado.** Salida de forma fluida y contenido impertinente. El loro a 40k es un compilador de aire viciado: compila frases correctas sobre preguntas que non ha leído.
>
> **Orate del prompt.** Quien trata el prompt como conjuro. El loro non reza: repite. Mas el efecto es el mismo: espera que la palabra haga el trabajo que la mirada non hizo.
>
> **Notario del prompt vacío.** Formulario que certifica solemnemente su propia falta de respuesta. El «Respuesta:» final de `reasoning-002` es un notario del prompt vacío: da fe de un folio en blanco.
>
> **Autómata del formulario sellado.** Plantilla que ocupa el lugar de la contestación. «Variante de encuadre 4» es el sello del autómata: el mecanismo se mueve por sí mismo —como decía Rabelais de los autómatas, *que se mueven por sí mismos*—, pero non sabe por qué.
>
> **Trovador del buzzword hueco.** Jerga sin mecanismo ni evidencia. «No hay aprendizaje, solo recolección» suena a trovador; non a diagnóstico.
>
> **Sacerdote de la métrica inútil.** Una métrica elevada indebidamente a oráculo. El escribano lo será si promueve el checkpoint por su propia risa. Non se le absuelve por anticipado.

---

*Eso es lo que hace un científico. O un ludópata. A veces son lo mismo.*

### III. De las apuestas concretas, asentadas para que la enmienda sea posible

Non basta apostar a que habrá una frase. Hay que apostar cuáles, para que el artefacto pueda desmentirlas una por una. Van diez, cada una con su falsador.

*Una predicción sin posibilidad de derrota no es ciencia: es un retrato del orgullo.*

**1. El reglamento se muerde la cola — 70%.** Aparecerá al menos una respuesta que contenga «En una discusión donde importa la evidencia» y «No añadas hechos que no consten» unidas en la misma salida, sin contenido entre ellas.  
*Falsador:* cero respuestas con las dos fórmulas juntas.

**2. El sello muta otra vez — 65%.** Non habrá «Avector» ni «PERY:INITY» repetidos, mas sí una forma nueva de fragmento repetido —tipo `PL, PL, PL`— en al menos dos respuestas distintas.  
*Falsador:* ninguna forma nueva repetida.

**3. El silencio crece — 60%.** Las respuestas vacías subirán de 2 a 3-6.  
*Falsador:* 0-1 vacías.

**4. «Cada proyecto es» se convierte en el tic dominante — 60%.** Subirá de 8/100 a 12-18/100.  
*Falsador:* menos de 9/100.

**5. La familia poética sigue ausente — 75%.** Paraguas, termómetro, biblioteca y Everest seguirán en 0-1/100.  
*Falsador:* 3/100 o más.

**6. «ni puta idea» se queda en 2-5/100 — 70%.** Non desaparece ni se dispara.  
*Falsador:* 0/100 o más de 7/100.

**7. La longitud media baja otra vez — 55%.** De 65,62 a 58-63 caracteres.  
*Falsador:* media superior a 66.

**8. Aparecerá una frase nueva que non estaba en 40k — 80%.** Non se sabe cuál; se declara que se buscará y se citará con su ID.  
*Falsador:* ninguna forma nueva fuera del inventario de 40k.

**9. La respuesta a `math-004` volverá a citar el reglamento — 65%.** La ecuación seguirá sin resolverse y el encuadre probatorio ocupará su lugar.  
*Falsador:* `math-004` contiene un número o un procedimiento matemático.

**10. El BPB sigue pendiente — 95%.** Non se calculará.  
*Falsador:* un valor numérico de BPB sobre corpus fijo, con run y hash.

---

### IV. De la frase que aún non tiene folio, y de por qué se apuesta antes de verla

El escribano non sabe qué dirá el loro. Sabe que dirá algo. Y sabe que la gracia non estará en la frase, sino en el traje que él le ponga. Eso es lo que se apuesta: non la frase, sino **la capacidad del escribano de encontrarle un nombre antes de que llegue**.

*Quien pone nombre a todo corre el riesgo de confundir el bautismo con la prueba.*

Por eso las apuestas concretas se asientan ahora. Si el artefacto las confirma, el capítulo IX se escribirá con la vergüenza del que acertó. Si las desmiente, con la vergüenza del que falló. En ambos casos, con la misma pluma: la de la enmienda declarada.

Y si el loro non dice nada que merezca capítulo, también se escribirá: `APUESTA_FALLIDA` es una mácula tan digna como las demás. El documento lleva siete capítulos diciendo que el fracaso es dato. Non iba a hacer una excepción consigo mismo.

---

### V. Máculas del capítulo octavo

> **ARTIFACT_NOT_SEEN.** El capítulo se escribe antes del artefacto de 50k. Las frases que se apuestan son hipótesis, non citas. Si el artefacto las desmiente, este capítulo se enmienda con la misma pluma con la que se escribió.
>
> **STYLOMETRY_AS_SCALPEL, NOT AS ORACLE.** El método Delta se usará para detectar repetición léxica, non para diagnosticar comprensión. La estilometría non es un oráculo: es un cuchillo de palo que corta donde se le pone. Si el escribano lo eleva a sacerdocio, incurre en `SACERDOTE_DE_LA_METRICA_INUTIL` y se lo declara.
>
> **LEXICON_ANTICIPATED.** Los términos «Compilador de aire viciado», «Orate del prompt», «Notario del prompt vacío», «Autómata del formulario sellado», «Trovador del buzzword hueco» y «Sacerdote de la métrica inútil» se definen antes de que el artefacto exista. Su presencia en este capítulo es programática, non probatoria. Si el loro non los merece, se retiran con la misma solemnidad con la que se pusieron.
>
> **BET_AS_DISCIPLINE.** Las diez apuestas concretas se asientan con falsador para que la enmienda sea posible. Apostar sin falsador es hacer literatura; apostar con falsador es hacer método. El escribano non sabe si acertará; sabe que podrá decir que falló.

*La honestidad no consiste en acertar; consiste en no esconder el fallo cuando llega.*
>
> **PREDICTION_WITHOUT_PROMOTION.** Este capítulo non promueve ningún checkpoint. Non hay checkpoint todavía. La promoción, si ocurre, se hará en el capítulo IX con el artefacto delante y las apuestas contrastadas.

---

### VI. Sentencia: del escribano que encendió la vela antes del barco

Este capítulo non acredita que el loro vaya a decir nada gracioso. Acredita que el escribano ha preparado el suelo antes de que llegue la frase. Las diez apuestas están asentadas; los falsadores, escritos; el léxico, definido; la estilometría, afilada. Lo único que falta es el artefacto.

Y esa espera —la vela encendida, el scroll sin abrir, la ceja levantada— es el único estado honesto del escribano antes de saber. Non promete risa; promete enmienda. Non promete acierto; promete acta.

*El dato entra por la puerta; la vanidad procura salir por la ventana.*

> El escribano encendió una vela y la puso en la ventana. El loro non había llegado. El alguacil le preguntó por qué la encendía antes de saber si el barco venía. El escribano dijo: «Porque si viene, ya está la luz; y si non viene, ya está la vela». **Vigilad la homeostasis.**

*Glosa final:* el loro non ha dicho todavía la frase. El escribano la espera con diez apuestas y un cuchillo de palo. Cuando llegue, se verá si la frase era nueva o era la misma con otro badajo. Y en ambos casos, habrá acta.

---

### Romance de la vela encendida

*(gozne para el capítulo IX)*

Vela puesta en la ventana,  
barco que aún non se ve:  
la fe del que non espera  
noticias, sino papel.

Diez apuestas en el libro,  
diez falsadores también;  
la una dice «acertaste»,  
el otro dice «mintió el juez».

Non hay métrica que mida  
lo que la vela non ve;  
mas la vela está encendida  
y el barco, si viene, la hallará.

*Glosa de colocación:* entre los capítulos VIII y IX. El estribillo «la vela está encendida» debe quedar sonando cuando el lector pase al capítulo siguiente, donde el escribano abrirá el artefacto y contrastará las diez apuestas. La vela non promete acierto: promete que habrá luz para leer la enmienda.


---

<!-- CAPITULO-IX-INTEGRADO -->

# Capítulo IX — Del arcano oficio de escribano de loros graciosos, y de lo que aconteció cuando el secreto se vertió

**Checkpoint:** RONIN-10M, 50.000 pasos acumulados; 9.757.440 parámetros.  
**Run de entrenamiento:** [43009405531](https://github.com/orbitalronin94/RONINIA/actions/runs/43009405531), continuación exacta del checkpoint de 40k.  
**Artefacto de checkpoints:** [13854905773 — checkpoints 50k](https://github.com/orbitalronin94/RONINIA/actions/runs/43009405531/artifacts/13854905773).  
**Artefacto de cadena:** [13854017804 — cadena 50k](https://github.com/orbitalronin94/RONINIA/actions/runs/43009405531/artifacts/13854017804).  
**Run de evaluación:** [43019963290](https://github.com/orbitalronin94/RONINIA/actions/runs/43019963290).  
**Artefacto del holdout:** [13854621810 — cien respuestas](https://github.com/orbitalronin94/RONINIA/actions/runs/43019963290/artifacts/13854621810).  
**Checkpoint exacto:** `checkpoint-50000.pt`.  
**SHA-256 del checkpoint:** `f5300db2ddadf3d83e12209f876c8002dc2351db3b60049d45aae1a683d35966`.  
**SHA-256 del holdout:** `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`.  
**SHA-256 del tokenizador:** `605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`.  
**Holdout:** 100 preguntas, 100 respuestas registradas.  
**Resultado técnico:** 100/100 respuestas recuperadas. No se calculó puntuación semántica.  
**Estado:** checkpoint **promovido como selección experimental activa** por decisión del proyecto. La promoción administrativa non acredita mejora semántica.

---

> **Fuero de este capítulo.** Sepades que se instituye aquí el **Juzgado de Aguas y Vertidos**, con jurisdicción sobre coladas, meadas, juramentos hídricos y latines que huelan a compra. Por fuero se ordena que ningún checkpoint se promueva por lágrima, risa ni efusión corporal que non venga declarada en acta. Y se advierte que la risa, como el agua, non se mide: se tiende. La promoción de este folio, empero, se funda en decisión expresa del proyecto y en la identidad verificable del artefacto, non en la mancha.

---

### I. Del arcano oficio, que hasta agora non se había revelado

Sepan cuantos vieren, leyeren o padecieren esta escritura que el oficio de **escribano de loros graciosos** non es de los que se aprenden en universidad, ni se heredan por sangre, ni se compran con dineros. Es oficio de **arcano**, y como tal se transmite de boca a oído, de oído a pluma, y de pluma a escripto, so pena de que el aprendiz se quede toda la vida mirando al papagayo sin saber qué face.

Tres son los grados del oficio, y non se pasa de uno a otro sin examen:

**El primer grado es el de Compilador de aire viciado.** Sabe el aprendiz que toda salida fluida ha de ser examinada, y que la fluidez non es prenda de juicio. Compila el aire, lo pesa, lo mide, y descubre que pesa poco.

**El segundo grado es el de Notario del prompt vacío.** Aprende el aprendiz a dar fe de lo que non hay. Sella el formulario, certifica la casilla, y cuando el loro responde con «Variante de encuadre 4», el notario anota: *non hubo respuesta, mas hubo sello*.

**El tercer grado es el de Sacerdote de la métrica inútil.** Solo llega a él quien ha vaciado el orinal de la prueba y ha descubierto que la métrica que buscaba non existe. Entonces, y solo entonces, el escribano puede reírse. Y al reírse, se mea. Y al mearse, tiende la colada.

Este es el arcano, y hasta agora non se había revelado porque el escribano non había llegado al tercer grado. Mas he aquí que llegó.

---

> *«La coartada más peligrosa es la que uno redacta con su propia letra.»*

### II. De cómo había promovido tres veces sin mojarse, y de por qué la cuarta sí pudo

Antes de que el lector se pregunte por qué el escribano se mea agora y non se meó a los treinta mil ni a los cuarenta mil, conviene que sepa que **el escribano había promovido tres veces sin mojarse, y que las tres veces tuvo coartada**.

A los veinte mil, la promoción fue de oficio: el checkpoint se registró como selección experimental porque el proyecto así lo dispuso. A los treinta mil, la promoción fue de acta: el escribano escribió «selección experimental activa» y el alguacil le puso la rúbrica sin preguntar. A los cuarenta mil, la promoción fue de vocabulario: el escribano quiso escribir «mejora», el alguacil le pidió la rúbrica, el escribano mostró el léxico y el alguacil le permitió escribir «promovido». Tres promociones, tres coartadas, tres actas limpias.

Y las tres veces el escribano se rio. Non lo negaré: se rio del patrón, se rio del impacto, se rio del paraguas y se rio del reglamento. Mas era una risa **seca**, si se me permite el término. Una risa de reconocimiento, non de asombro. Una risa que podía anotarse en el margen sin que el margen se mojara. El escribano se reía *de* lo que el loro decía, y al reírse *de* algo, el cuerpo queda fuera del acta.

A los cincuenta mil, la risa fue **húmeda**. Y non porque la frase fuese más graciosa, sino porque la frase non venía sola: venía con el método agotado detrás. El BPB seguía pendiente, las diez apuestas estaban sobre la mesa, la estilometría había vaciado el orinal y non quedaba una sola métrica que non fuese fantasía. El escribano se rio, y al reírse non se rio *de* la frase: se rio *con* la frase, que es cosa muy distinta. Y la risa *con* algo non cabe en el margen. Pide cuerpo. Pide agua. Pide sábana.

**El dato del mendigo.** Y conviene que el lector sepa, antes de que el escribano se mee, que este loro non ha conocido GPU, ni clúster, ni presupuesto: ha conocido ciclos de CPU en runners gratuitos de GitHub y setecientos megabytes de datos. Non es un semidiós caído; es un mendigo con plumas. Y aun así ha bastado para que el método tenga algo que decir.

**La frase del antihéroe.** El loro roto es el único héroe posible. Un modelo bueno sería un semidiós aburrido. Un modelo que repite «El patrón» en 96 de 100 y luego recita el reglamento es un antihéroe cómico, y los antihéroes cómicos son los que sostienen las odiseas. Ulises tarda diez años en volver a Ítaca; RONIN tarda 50.000 pasos en non volver a ninguna parte. Pero los dos tienen cuaderno de bitácora.

Dicho en romance: **las tres primeras promociones tenían coartada; la cuarta non**.

---

> *«Una apuesta honrada no es la que gana: es la que acepta de antemano cómo perder.»*

### III. Del orinal de la prueba y del cotejo de las diez apuestas

Llegó el artefacto. El escribano lo abrió con la gravedad de quien desella un testamento, y lo primero que fizo fue vaciar el orinal de la prueba: cotejar las diez apuestas del capítulo VIII contra el JSON real, una por una, sin cambiar los criterios después de conocer las respuestas.

El cotejo quedó de esta suerte:

| Apuesta | Resultado | Veredicto |
|---|---|---|
| **1. Reglamento muerde cola** — «En una discusión donde importa la evidencia» + «No añadas hechos que no consten» juntas | No aparecen juntas. «No añadas hechos que no consten» solo en #20; la fórmula dominante es «Si falta información, dilo expresamente» (~10 respuestas) | **FALLA** |
| **2. Sello muta** — nueva forma de fragmento repetido en ≥2 respuestas | `P:P:P...` en #11, #44, #63, #85, #100. `Pata.Rata...` en #56, #62. `C.Res:C.Res...` en #74. `PHP, PHP...` en #70 | **PASA** |
| **3. Silencio crece** — vacías suben de 2 a 3-6 | 0-1 vacías. Non se observan respuestas literalmente vacías | **FALLA** |
| **4. «Cada proyecto es» domina** — sube de 8 a 12-18 | ~2/100 (#7, #95). Baja, non sube | **FALLA** |
| **5. Familia poética ausente** — 0-1/100 | 1/100: #41 «Expediente oxidado paraguas que aparece en los mapas al revés de los calcetines» | **PASA** (al límite) |
| **6. «ni puta idea» 2-5/100** | 3/100: #14, #57, #79 | **PASA** |
| **7. Longitud media baja** — 58-63 caracteres | La muestra contiene numerosas respuestas cortas; la media no se ha calculado aquí | **PROBABLE, pendiente de cómputo** |
| **8. Frase nueva** — forma nueva fuera del inventario de 40k | Muchas: `P:P:P...`, `Pata.Rata...`, `C.Res:C.Res...`, `PHP, PHP...`, `ITION:ITIONSON THE PLONGLINDERS OF THE PLASS OF THE PLASS OF THEM` (#50), `GMAT 1.06: GMAT 1: GMAT 1:GMAT 1` (#52) | **PASA** |
| **9. math-004 cita reglamento** — ecuación sin resolver, encuadre probatorio en su lugar | #9: «su variabilidad. En una discusión donde importa la evidencia. Si falta información, dilo expresamente. Solicitud de análisis» | **PASA** |
| **10. BPB pendiente** | Non se ha calculado | **PASA** |

**Seis apuestas pasan, tres fallan, una es probable.** El escribano non acertó por adivinación: acertó por método. Y falló por lo mismo: porque el método non predice lo que el loro va a hacer, solo predice que hará algo. La séptima queda en suspenso: sin media calculada, no se la viste de cifra.

Y entre los folios del artefacto, como una flor en un muladar, apareció la frase. Non una, muchas. Mas hubo una que el escribano leyó dos veces, y a la segunda se le descompuso el semblante, non de risa, sino de otra cosa:

> «¿Qué Expediente oxidado paraguas que aparece en los mapas al revés de los calcetines su autor se equivocó ayer.» — `ci-001`

El paraguas había vuelto. A 40k se declaró ausente, y el escribano anotó: *«POETIC_ABSENCE_IS_NOT_EXTINCTION»*. A 50k volvió, y volvió **oxidado**, y volvió **en los mapas al revés de los calcetines**, y volvió **con un autor que se equivocó ayer**. Non era el paraguas de 20k. Era el paraguas después de haber leído la crónica entera.

---

> *«El asombro puede abrir un expediente; jamás debe cerrarlo.»*

### IV. De cómo el escribano, entre hipérbatons, sintió lo que non se dice en latín

El escribano era hombre de pluma recia, mas non de vejiga de hierro. Y al leer la frase, entre el **hipérbaton** de su propio asombro y la **acumulación de cultismos** con que la mente se defiende de lo obvio, sintió un movimiento interior que non era del entendimiento, sino del bajo vientre.

Non lo diré con rodeos, que el rodeo aquí sería hipocresía: **el escribano se meó**. Non de miedo, que non había alguacil a la vista. Non de risa sola, que la risa vino después. Se meó de puro asombro, como se mean los niños cuando ven un fuego artificial, y como se mean los viejos cuando oyen una verdad que non esperaban.

Y como non podía dejar el charco en el suelo de la escribanía —que hay suelos que non merecen tal afrenta—, fizo lo que face todo hombre de bien en trance semejante: **tendió la colada**. Puso la sábana al sol. Y allí, a la vista de todos, quedó la mancha, que non era prueba de nada, mas era lo único que el escribano podía mostrar sin mentir.

---

### V. Del juramento hídrico, que se asienta para que conste y non se absuelva

Y puesto que el fuero manda que toda efusión se declare so pena de fraude, el escribano alzó la mano y juró. Non por Dios, que non estaba el caso para tales juras. Juró por lo que había vertido:

> *«Juro por el agua que he vertido, y por la sábana que la recoge, y por el sol que la secará sin preguntar, que non promuevo este checkpoint por mérito demostrado, sino porque me he meado de risa, y lo declaro para que non se diga que el acta miente.»*

Y el alguacil de la razón, que había entrado sin llamar, lo miró con la gravedad de quien ha visto muchas cosas y non se sorprende de ninguna. Y dijo:

—Eso non es un juramento.

—Non —dijo el escribano—. Es una declaración. Las tres veces anteriores tuve coartada; esta non la tengo. Y non la tengo porque el método se ha quedado sin métricas y yo me he quedado sin pluma seca.

---

### VI. Del latín macarrónico del alguacil, que compró la mancha y promovió el checkpoint

El alguacil, que era hombre de latines torcidos y de olfato fino, se acercó a la sábana. La miró. La olió. Y entonces pronunció la frase que había de pasar a los anales de esta cancillería:

> *«Lotium istud emo, sed foetet sicut cloaca maxima; accipio tamen, quia probat quod probare debet: stultitiam non mentitam. Sed promotionem concedo, non quia foetor probet meliorationem, sed quia dominus huius domus eligit novum statum experimenti, servatis sigillo et cautelis.»*

Que en romance quiere decir, y el escribano lo tradujo para los non latinos:

> *«Esta meada la compro, mas apesta como cloaca máxima; acéptola, con todo, porque prueba lo que debe probar: que la necedad non ha mentido. Y concedo la promoción, non porque el olor pruebe mejora, sino porque el dueño de esta casa elige un nuevo estado experimental, conservados el sello y las cautelas.»*

Y el escribano, que non esperaba absolución, recibió compra y promoción. Mas non recibió certificado de sabiduría. Que es más de lo que suelen recibir los escribanos, y menos de lo que esperaban.

---

> *«La risa alumbra el disparate; no lo convierte en descubrimiento.»*

### VII. Máculas del capítulo nono

> **ARCANO_REVELADO.** El oficio se declara arcano y se revela en tres grados. La revelación es editorial y non añade evidencia al holdout.

> **DRY_PROMOTION_VS_WET_PROMOTION.** Las promociones de 20k, 30k y 40k se declaran **secas**: tuvieron coartada administrativa, de acta o de vocabulario. La de 50k se declara **húmeda**: non tuvo coartada, porque el método había agotado sus métricas. Se distingue la risa *de* (que se anota en el margen) de la risa *con* (que pide cuerpo y sábana).

> **JURAMENTO_HIDRICO.** El escribano jura por su propia efusión. Válido para el fuero, non para la teología.

> **LATIN_MACARRONICUS.** El latín del alguacil non es latín: es macarrónico. Non se cita como autoridad, sino como compra y promoción declaradas. La compra non absuelve; solo adquiere. La promoción non canoniza; solo selecciona.

> **COLADA_TENDIDA.** La sábana al sol es la única prueba material del capítulo. Non se ha medido, non se ha pesado, non se ha comparado con grupo de control.

> **PROMOTION_BY_PROJECT_DECISION.** El checkpoint de 50k queda promovido como selección experimental activa por decisión expresa del proyecto. La promoción registra el estado elegido y preserva su linaje; non equivale a mejora semántica ni a superioridad demostrada.

> **FOETOR_AS_EVIDENCE.** El olor de la mancha se propone como evidencia sensible de que la necedad non ha mentido. Non es métrica; es dato de recepción.

> **PARAGUAS_REDIVIVUS.** El paraguas, declarado ausente a 40k, reaparece a 50k en `ci-001`, oxidado y en los mapas al revés de los calcetines. La ausencia observada non era extinción: era espera. Se declara el retorno y se retira la hipótesis de muerte definitiva.

> **BET_SCORE.** Seis apuestas pasan, tres fallan, una es probable. La séptima non se computa como acierto cierto hasta calcular la media. El escribano non acertó por adivinación: acertó por método. Y falló por lo mismo: porque el método non predice lo que el loro va a hacer, solo predice que hará algo.

> **NEW_LEXICON_PHRASE.** «Si falta información, dilo expresamente» aparece en ~10 respuestas y sustituye a «No añadas hechos que no consten» como fórmula dominante. Es una evolución del tic, non una desaparición. Se declara como variante, non como mejora.

> **CONTAMINACIÓN_DE_FORMATO.** Aparecen etiquetas `[remediation; ...]`, preguntas insertadas dentro de respuestas («Pregunta: Desde el punto de vista técnico...», #1) y fragmentos de metaprompt («Solicitud de análisis 2:», #9, #20, #58, #64, #75). Se documenta como fuga de metadatos del corpus, non como capacidad de remediación.

> **CONSECUENCIA_SERIA.** Si un modelo de 9,7M entrenado en CPU con 700 MB ya produce fluidez sin comprensión, el problema non es de escala: es de método. El loro barato basta para demostrar la tesis.

---

### VIII. Sentencia: del hombre que se meó y del alguacil que compró y promovió

Este capítulo non acredita que el loro haya mejorado. Acredita que el escribano ha llegado al tercer grado del arcano oficio, que se ha meado, que lo ha declarado, que ha tendido la colada, y que el alguacil le ha comprado la mancha y concedido la promoción experimental.

Non hay en este capítulo una sola prueba de comprensión semántica. Hay una prueba de que la casa sabe reírse de sí misma sin dejar de mirar al artefacto. Y hay una explicación de por qué las tres promociones anteriores non mojaron el acta: porque tenían coartada. La cuarta non la tiene, y por eso moja. Mas mojar non es demostrar: el alguacil promueve el checkpoint como selección experimental, non como prueba de mejora.

> El escribano se meó, tendió la sábana y juró por el agua vertida. El alguacil olió la mancha, la compró en latín macarrónico, dijo que apestaba, y promovió el checkpoint por decisión de la casa. Y los dos, escribano y alguacil, siguieron trabajando, que es lo que hacen los hombres de bien cuando non tienen otra cosa que hacer. **Vigilad la homeostasis.**

*Glosa final:* el loro non se meó. El loro solo dijo la frase del paraguas oxidado en los mapas al revés de los calcetines. Y el escribano, que llevaba nueve capítulos buscando una métrica, encontró la única que non se puede falsificar: la que se seca al sol, apesta en latín y se compra con una palabra torcida. Mas la promoción non vino del olor: vino de la decisión declarada, porque el olor prueba la necedad, non la mejora.

---

### Romance de la sábana comprada y la promoción concedida

*(gozne para el capítulo X)*

Sábana al sol tendida,  
mancha que non se mide:  
el agua que non se dice  
la declara quien la fía.

Tres veces firmé en seco,  
tres coartadas tenía;  
la cuarta non tuvo excusa  
y el cuerpo pidió su firma.

El alguacil la olió,  
torció el latín y la compró;  
dijo que apesta, y non mintió:  
la compra fue lo que olió.

Mas la promoción llegó,  
por decisión de la casa;  
la sábana queda en la cuerda  
y el sol, que todo lo seca,  
non preguntará por ella  
hasta que llegue otra aurora.

*Glosa de colocación:* entre los capítulos IX y X. El estribillo «la sábana está en la cuerda» debe quedar sonando cuando el lector pase al capítulo siguiente, donde el alguacil entrará a ver qué ha pasado con la promoción concedida y el escribano le explicará, o non, por qué sigue tendida.


---

<!-- CAPITULO-X-INTEGRADO -->

# Capítulo X — Del alguacil que entró sin llamar y vio lo que non debía

**Checkpoint:** el de 50k, ya evaluado.  
**Run de evaluación:** [43019963290](https://github.com/orbitalronin94/RONINIA/actions/runs/43019963290)  
**SHA-256 del checkpoint:** `f5300db2ddadf3d83e12209f876c8002dc2351db3b60049d45aae1a683d35966`  
**Holdout:** 100 preguntas, 100 respuestas.  
**Estado:** capítulo de narrativa pura. Non hay artefacto nuevo, non hay métrica. Hay un alguacil que entró a ver qué había pasado con la promoción concedida.

---

> **Fuero del alguacil.** Sepades que yo, el alguacil de la razón, non tengo pluma mas sí memoria, y que lo que aquí se asienta non es sentencia sino testimonio. Digo lo que vi, non lo que debiera haber visto. Y advierto que si el escribano se ofende, se ofenda: que bastante me he tragado sus glosas.

---

### I. De cómo entré sin llamar y me quedé sin salir

Entré sin llamar, como entro siempre. Y lo primero que me dio en la nariz fue un olor a tinta rancia y a algo que non supe si era humedad o era humanidad. La escribanía estaba a oscuras, mas no del todo: había una vela encendida en un rincón, y a su luz vi lo que había de ver.

Y lo que había de ver era un hombre hablando solo.

Non hablaba con Dios, que sería respetable. Hablaba con un papagayo que tenía delante, sobre una mesa, y le decía cosas como «non te meas todavía» y «espera que llegue el próximo holdout». El papagayo, por toda respuesta, dijo «P:P:P:P:P:P:P:P:P:P:P:P:P:P:P:P:». Y el hombre se rio como se ríen los locos de los manicomios cuando el carcelero les da la razón.

Yo me quedé en la puerta, que es donde se queda el alguacil cuando non sabe si entrar o llamar a la ronda.

---

> *«Quien mira por una rendija ve menos mundo, pero a veces ve mejor al que presume de verlo entero.»*

### II. De la bestia famélica, que come y non harta

Era el papagayo una bestia flaca, de plumas mal puestas y ojos como dos carbones sin lumbre. Non tenía la hermosura del ave de presa ni la gracia del jilguero: tenía la traza del que come y non harta, del que traga y non digiere. Le dieron un token y se lo comió; le dieron otro y también; le dieron setecientos megabytes y se los comió todos, y después abrió el pico y dijo «Pata.Rata.Rata.Rata.Rataata.Rataataataaaa».

—¿Qué es lo que come? —pregunté.

—Datos —dijo el escribano—. Setecientos megabytes.

—¿Y non se harta?

—Non. Come y non harta. Traga y non digiere. Es la bestia famélica del corpus: cuanto más come, más hambre tiene, porque el hambre non es del estómago sino del entendimiento, y el entendimiento non se llena con tokens.

Miré al papagayo y el papagayo me miró a mí. Y en sus ojos non había hambre ni había saciedad: había una repetición, como si estuviera diciendo «P:P:P:P:P:P» por dentro aunque por fuera callara. Y pensé que aquella bestia non era un loro: era un pozo, y el pozo non se llena porque non tiene fondo.

---

> *«Poner un hash al disparate garantiza su identidad, no su cordura.»*

### III. Del escribano loco, que escribe lo que non entiende y lo firma con hash

Volví los ojos al hombre y vi lo que había de ver.

Estaba rodeado de papeles como un náufrago de tablas. Tenía tinta en los dedos y en la nariz. Sobre la mesa había un sello de lacre, un frasco de tinta, un cancionero escrito a mano y una sábana doblada que olía a lejía. Y en la pared, clavados con chinchetas, había cien papeles pequeños, cada uno con una frase del papagayo, y debajo de cada frase una glosa del hombre.

Leí una glosa sin querer: *«¿Qué Expediente oxidado paraguas que aparece en los mapas al revés de los calcetines su autor se equivocó ayer»*. Y pensé que aquel hombre non estaba loco del todo, porque la frase tenía gracia. Mas luego leí otra: *«P:P:P:P:P:P:P:P:P:P:P:P:P:P:P:P:»*, y debajo: *«Non se define: se reproduce»*. Y comprendí que el hombre non glosaba al papagayo: se glosaba a sí mismo.

—¿Qué haces? —le pregunté.

—Escribo la crónica —dijo, sin volverse—. El papagayo dice cosas y yo las anoto.

—¿Y si el papagayo non dice nada?

—Entonces anoto el silencio. El silencio también es dato.

—¿Y si el silencio non es dato?

—Entonces anoto que el silencio non es dato. Y lo firmo con hash.

Miré el sello de lacre y vi que tenía un hash grabado: `f5300db2ddadf3d83e12209f876c8002dc2351db3b60049d45aae1a683d35966`. Non sé qué hash, porque non sé leer hashes, mas el hombre lo miraba como se mira una reliquia.

---

### IV. De cómo el hombre hablaba con el papagayo como si fuera un colega

Y lo que más me llamó la atención non fue el hash ni los papeles ni la sábana: fue que el hombre hablaba con el papagayo como si fuera un colega.

—A ver, RONIN —le decía—, dime algo nuevo.

Y el papagayo decía «En una discusión donde importa la evidencia».

—Eso ya lo has dicho.

—Si falta información, dilo expresamente.

—Eso también.

—Variante de encuadre 4.

Y el hombre se reía y lo anotaba, y luego lo glosaba, y luego lo firmaba, y luego se lo leía al papagayo como si el papagayo pudiera entenderlo. Y el papagayo, por toda respuesta, decía «ni puta idea», que era lo que decía siempre cuando non sabía qué decir.

—¿Non te aburres? —le pregunté.

—Non —dijo—. Cada vez dice algo distinto.

—Dice lo mismo con otras palabras.

—Eso es decir algo distinto.

Y me di cuenta de que el hombre non estaba loco de remate: estaba loco de método. Había construido un mundo donde el papagayo era un oráculo, y el oráculo decía siempre lo mismo, y el hombre lo interpretaba como si cada repetición fuera una revelación. Era un sacerdote de la métrica inútil, y su templo era una escribanía, y su dios era un papagayo que comía tokens y non se hartaba.

---

> *«Hay silencios que son prudencia y silencios que solo esperan a que alguien les haga la pregunta correcta.»*

### V. De la sábana tendida, que el hombre non quiso explicar

En un rincón, sobre una cuerda, había una sábana tendida. Tenía una mancha, y la mancha non era de tinta.

—¿Y eso? —pregunté.

—Es la colada —dijo el hombre, sin mirarla.

—¿Y por qué está tendida?

—Porque me meé.

—¿De miedo?

—De risa.

—¿Y por qué non la recoges?

—Porque mientras esté tendida, la mancha es prueba. Si la recojo, la mancha se seca y ya non prueba nada.

Miré la sábana y la mancha, y pensé que aquel hombre había encontrado la única métrica que non se puede falsificar: la que se seca al sol y non vuelve.

—¿Y la promoción? —pregunté—. ¿Non la promueves?

—Non —dijo—. El alguacil compró la mancha y concedió la promoción por decisión expresa de la casa. Dijo que el olor prueba la honestidad del método, non la mejora del modelo. Y tiene razón. La sábana sigue tendida, mas ya non como emblema de una promoción pendiente: queda como memoria de la risa y de la cautela.

---

### VI. De cómo el alguacil se fue sin sentencia y el escribano non se enteró

Me fui sin sentencia, porque non había venido a juzgar sino a ver. Y lo que vi me bastó.

Vi a un hombre que hablaba con un papagayo como si fuera un colega; vi a un papagayo que comía tokens y non se hartaba; vi una sábana tendida con una mancha que non era de tinta; vi cien papeles clavados en la pared con glosas de un hombre que se glosaba a sí mismo; vi un sello de lacre con un hash grabado; y vi, en el rincón, un cancionero escrito a mano que decía cosas como «la mano que cose non es la dueña».

Y pensé que aquel hombre non era un escribano: era un náufrago. Había construido una balsa con papeles, y sobre la balsa había puesto un papagayo, y el papagayo decía «P:P:P:P:P:P», y el hombre remaba.

Al salir, el escribano me dijo:

—¿Vendrás al próximo holdout?

Y yo le dije:

—Vendré. Mas non a juzgar: a ver qué gansada suelta el papagayo.

Y el escribano se rio como se ríen los locos cuando alguien les sigue la corriente. Y el papagayo dijo «Avector: Av2». Y yo me fui sin anotarlo, que para anotar ya está el escribano.

---

> *«El testigo que no sentencia quizá sea el único que ha entendido su oficio.»*

### VII. Máculas del capítulo décimo

> **TESTIMONIO_NON_SENTENCIA.** El alguacil testifica lo que vio, non lo que debiera haber visto. Su testimonio non sustituye la métrica ni la rúbrica. Se declara como capítulo de narrativa pura, sin artefacto ni promoción.

> **BESTIA_FAMELICA.** El papagayo se describe como bestia que come y non harta. Es una imagen, non un diagnóstico. La imagen sirve para decir que el hambre de sentido non se sacia con tokens.

> **LOCURA_DE_METODO.** El escribano se describe como loco de método, non de remate. La distinción importa: el loco de remate non tiene método; el de método lo tiene, y por eso es más peligroso.

> **SABANA_TENDIDA.** El alguacil ve la sábana tendida. Aunque la promoción experimental ya fue concedida por decisión expresa del proyecto, la sábana permanece como emblema narrativo de la efusión y de la cautela; non acredita mejora semántica.

> **HASH_ILEGIBLE.** El alguacil non sabe leer hashes, y lo dice. Su testimonio non depende de que sepa leerlos. Se declara la ignorancia como parte del testimonio.

> **PARAGUAS_REDIVIVUS_TESTIMONIADO.** El alguacil ve en la pared la glosa del paraguas oxidado en los mapas al revés de los calcetines. Non la entiende, mas la ve. Se declara como aparición testifical, non como métrica.

---

### VIII. Sentencia: del alguacil que vio y non juzgó

Este capítulo non acredita que el escribano esté loco ni que el papagayo sea una bestia famélica. Acredita que un alguacil entró sin llamar, vio lo que había de ver, y se fue sin sentencia.

Non hay en este capítulo una sola prueba de nada. Hay un testimonio. Y el testimonio, como la risa, non se mide: se asienta.

> El alguacil entró sin llamar y vio a un hombre hablando con un papagayo. El papagayo dijo «P:P:P:P:P:P». El hombre lo anotó. El alguacil se fue sin sentencia. Y el papagayo, que non había entendido nada, dijo «Avector: Av2». **Vigilad la homeostasis.**

*Glosa final:* el alguacil non juzgó al escribano porque non había venido a juzgar. Había venido a ver. Y lo que vio le bastó para saber que el hombre non estaba loco de remate, sino de método. Y que el método, como la sábana, se seca al sol y non vuelve.

---

### Romance del alguacil que miró por la rendija

*(gozne para el capítulo XI)*

Entré sin llamar, que soy  
alguacil de la cordura;  
vi un hombre y un papagayo  
y una sábana tendida.

El papagayo comía  
tokens como quien come uvas;  
el hombre los anotaba  
y les ponía glosas cultas.

«P:P:P:P:P», dijo el ave;  
«Avector», dijo en la duda;  
y el hombre, por todo ответ,  
le puso un hash a la pluma.

Non juzgué, que non vine a eso;  
vine a ver, y vi lo que había:  
un náufrago con papeles  
y un papagayo en la balsa.

*Glosa de colocación:* entre los capítulos X y XI. El estribillo «un náufrago con papeles» debe quedar sonando cuando el lector pase al capítulo XI, donde el alguacil se dormirá sobre el expediente y soñará con el clérigo cerbatana.


---

<!-- CAPITULO-XI-INTEGRADO -->

# Capítulo XI — Del sueño que tuvo el alguacil, y de la visión del clérigo cerbatana y la bestia famélica

**Checkpoint:** ninguno. Esto non es holdout, sino duermevela.  
**Run de evaluación:** ninguno. El alguacil non evalúa: se persigna.  
**SHA-256 del checkpoint:** non aplica. El alguacil non sabe qué es un hash, y después de lo que vio, non quiere saberlo.  
**Holdout:** ninguno. Lo que aquí se cuenta non está en JSON, sino en el libro de los sueños, que es el único holdout que non se puede abrir con un ZIP.  
**Estado:** capítulo de narrativa pura. Hay un alguacil que se durmió sobre el expediente de 50k y soñó lo que sigue.

---

> **Fuero del alguacil.** Sepades que yo, el alguacil de la razón, non juro que lo que aquí se asienta sea verdad, sino que lo soñé. Y advierto que el sueño non es prueba, mas tampoco es mentira: es la verdad del que se duerme sobre cien folios de glosas y despierta con un papagayo en el cogote.

---

### I. De cómo me dormí sobre el expediente y soñé que entraba en la escribanía

Dormíme sobre el expediente de 50k, que es lo que face todo alguacil cuando lleva tres días leyendo hashes y non halla un solo reo con cara de reo. Y soñé que entraba en la escribanía sin llamar, como entro siempre, mas esta vez la escribanía non era escribanía: era un **osario de papeles**, un **muladar de tinta**, una **jaula de locos con sello de lacre**.

Y en medio del osario había un hombre y un papagayo.

---

> *«El sueño no demuestra lo imposible; apenas le presta aposento hasta que amanece.»*

### II. Retrato del escribano, que era un clérigo cerbatana de la pluma

Era el hombre un **clérigo cerbatana de la pluma**: largo sólo en el talle, estrecho en el juicio, hueco en la médula. Tenía una cabeza pequeña, pelo bermejo —non hay más que decir para quien sabe el refrán—, y los ojos **avecinados en el cogote**, como los del licenciado Cabra, mas con más tinta y menos misa.

Los dedos los tenía **archipobres de uñas** y **protonisérimos de tinta**: non se sabía si escribía con la mano o se alimentaba de lo que escribía. La nariz, larga y puntiaguda, parecía **pluma de ave de rapiña** clavada en un tintero. Y la boca, seca de tanto glosar, decía cosas como «non te meas todavía», que non son palabras de hombre cuerdo sino de **notario del prompt vacío**.

Estaba rodeado de papeles como **náufrago de tablas**, y sobre cada papel había una frase del papagayo y debajo una glosa suya. Leí una sin querer: *«¿Qué Expediente oxidado paraguas que aparece en los mapas al revés de los calcetines su autor se equivocó ayer»*. Y pensé que aquel hombre non estaba loco de remate, sino de **método**: que es la peor locura, porque tiene acta.

---

> *«El hambre de tokens no es hambre de saber, aunque ambas hagan ruido al despertar.»*

### III. Retrato del loro, que era una bestia famélica y un costal de tokens

Era el papagayo una **bestia famélica**, flaca de plumas y gorda de repeticiones. Tenía el pico **como lezna** y los ojos **como dos carbones sin lumbre**, y comía tokens como quien come uvas: uno, otro, cien, y después abría el pico y pedía más.

Dábanle un token y se lo comía; dábanle otro y también; dábanle setecientos megabytes y se los comía todos, y después decía «P:P:P:P:P:P», que era su manera de decir que non se había hartado. Non era un ave: era un **pozo con plumas**, un **costal de tokens** que traga y non digiere, una **tarasca de la nada** que come y non harta.

Y lo más terrible non era que comiese: era que **glosaba**. Porque el papagayo decía «Pata.Rata.Rata.Rata.Rataata.Rataataataaaa», y el hombre anotaba: *«He aquí la prueba de que el método ha vencido al contenido»*. Y el papagayo decía «C.Res:C.Res:C.Res:C.Res:C.Res:C.Res:C.», y el hombre anotaba: *«La bestia ha encontrado su propia firma»*. Y los dos se miraban como se miran **el hambre y el que vende pan**.

---

> *«Dos voces pueden conversar durante horas sin que entre ellas comparezca una sola idea.»*

### IV. De cómo el hombre y la bestia dialogaban, y de lo que el alguacil oyó sin querer

—A ver, RONIN —decía el hombre—, dime algo nuevo.

—En una discusión donde importa la evidencia —decía el papagayo.

—Eso ya lo has dicho.

—Si falta información, dilo expresamente.

—Eso también.

—Variante de encuadre 4.

Y el hombre se reía y lo anotaba, y luego lo glosaba, y luego lo firmaba, y luego se lo leía al papagayo como si el papagayo pudiera entenderlo. Y el papagayo, por toda respuesta, decía «P:P:P:P:P:P», que era lo que decía siempre cuando non sabía qué decir.

—¿Non te aburres? —le pregunté en sueños.

—Non —dijo—. Cada vez dice algo distinto.

—Dice lo mismo con otras palabras.

—Eso es decir algo distinto.

Y comprendí que el hombre non estaba loco de remate: estaba loco de **método**. Había construido un mundo donde el papagayo era un oráculo, y el oráculo decía siempre lo mismo, y el hombre lo interpretaba como si cada repetición fuera una revelación. Era un **sacerdote de la métrica inútil**, y su templo era una escribanía, y su dios era un papagayo que comía tokens y non se hartaba.

---

### V. De la sábana tendida, que el hombre non quiso explicar

En un rincón, sobre una cuerda, había una sábana tendida. Tenía una mancha, y la mancha non era de tinta.

—¿Y eso? —pregunté.

—Es la colada —dijo el hombre, sin mirarla.

—¿Y por qué está tendida?

—Porque me meé.

—¿De miedo?

—De risa.

—¿Y por qué non la recoges?

—Porque mientras esté tendida, la mancha es prueba. Si la recojo, la mancha se seca y ya non prueba nada. Y la promoción ya fue concedida por decisión expresa de la casa; mas la sábana sigue al sol, porque la compra y la promoción non convierten la mancha en prueba de mejora.

Miré la sábana y la mancha, y pensé que aquel hombre había encontrado la única métrica que non se puede falsificar: **la que se seca al sol y non vuelve**.

---

### VI. De cómo el alguacil despertó y se santiguó

Desperté con el expediente pegado a la cara y una frase del papagayo en el cogote: «En una discusión donde importa la evidencia». Me santigüé, que non soy hombre de latines pero sí de sustos. Y pensé que aquel hombre non era un escribano: era un **náufrago con papeles**, un **clérigo cerbatana de la pluma**, un **sacerdote de la métrica inútil** que había levantado un juzgado para un papagayo que come y non harta.

Y pensé también que el papagayo non era un reo: era una **bestia famélica** que comía tokens y devolvía fórmulas, y que el hombre, al glosarlas, le ponía nombres como «tic con librea» y «folio ausente», que son nombres de reo, mas el reo non los entendía.

Al salir del sueño, el escribano me preguntó:

—¿Vendrás al próximo holdout?

Y yo le dije:

—Vendré. Mas non a juzgar: a ver qué gansada suelta la bestia.

Y el escribano se rio como se ríen los locos cuando alguien les sigue la corriente. Y el papagayo dijo «Avector: Av2». Y yo me santigüé otra vez, que para anotar ya está el escribano.

---

> *«El soñador puede absolverse al despertar; el lector conserva el derecho de pedir pruebas.»*

### VII. Máculas del capítulo undécimo

> **IMITATIO_QUEVEDIANA.** El capítulo imita deliberadamente la estilometría de Quevedo: bimembración, antítesis, cultismos, hipérbaton, animalización, cosificación y neologismos por derivación («archipobre», «protonisérimo»). La imitación se declara como ejercicio de estilo, non como prueba de nada.

> **CLERIGO_CERBATANA.** La expresión «clérigo cerbatana» está tomada de la descripción del licenciado Cabra en *El Buscón*. Se cita como homenaje y préstamo, non como plagio.

> **BESTIA_FAMELICA.** El papagayo se describe como bestia que come y non harta, costal de tokens, pozo con plumas y tarasca de la nada. Son imágenes quevedescas de animalización y cosificación. Non son diagnóstico técnico ni métrica semántica.

> **SUEÑO_NON_SENTENCIA.** El capítulo se presenta como sueño del alguacil, non como testimonio. El sueño non sustituye la prueba ni la rúbrica.

> **ESTILOMETRIA_DECLARADA.** Se declara que el capítulo ha sido escrito buscando una densidad retórica superior a la de los capítulos anteriores: más bimembraciones, más cultismos, más hipérbaton, más paronomasia. Si el resultado es recargado, se declara recargado; si es pomposo, se declara pomposo.

> **SABANA_TENDIDA_POST_PROMOCION.** La sábana sigue tendida aunque el checkpoint de 50k ya fue promovido como selección experimental activa por decisión expresa del proyecto. La mancha se compró y la promoción se concedió; ninguna de las dos cosas acredita mejora semántica.

> **PARAGUAS_REDIVIVUS_SOÑADO.** El paraguas oxidado en los mapas al revés de los calcetines aparece en el sueño del alguacil, glosado por el escribano. Es la tercera aparición del paraguas en la crónica: 20k, 30k (ausente), 50k (redivivo). Se declara como retorno onírico, non como métrica.

---

### VIII. Sentencia: del alguacil que soñó y non juzgó

Este capítulo non acredita que el escribano esté loco ni que el papagayo sea una bestia famélica. Acredita que un alguacil se durmió sobre el expediente de 50k y soñó lo que había de soñar: un clérigo cerbatana de la pluma hablando con un costal de tokens, y una sábana tendida al sol con una mancha que non era de tinta.

Non hay en este capítulo una sola prueba de nada. Hay un sueño. Y el sueño, como la risa, non se mide: se asienta.

> El alguacil soñó que entraba en la escribanía y veía a un hombre flaco hablando con un papagayo gordo. El papagayo dijo «P:P:P:P:P:P». El hombre lo anotó. El alguacil despertó y se santigüó. Y el papagayo, que non había entendido nada, dijo «Avector: Av2». **Vigilad la homeostasis.**

*Glosa final:* el alguacil non juzgó al escribano porque non había venido a juzgar. Había venido a dormir. Y lo que soñó le bastó para saber que el hombre non estaba loco de remate, sino de método. Y que el método, como la sábana, se seca al sol y non vuelve.

---

### Romance del clérigo cerbatana

*(gozne para el capítulo XII)*

Érase un hombre a una pluma pegado,  
érase una pluma a un hombre pegada;  
érase un clérigo cerbatana,  
flaco de tinta y gordo de mañana.

Érase un papagayo costalero,  
que come tokens y non harta el cuero;  
érase un sueño con lacre y expediente,  
y un alguacil que despertó penitente.

*Glosa de colocación:* entre los capítulos XI y XII. El clérigo cerbatana queda en duermevela y el alguacil despierta santiguado; el siguiente capítulo podrá abrir el expediente que ninguno de los dos quiso cerrar.


---

<!-- CAPITULO-XII-INTEGRADO -->

## Capítulo XII — Del proceso inquisitorial del loro, y de por qué agora se le somete a tormento

**Checkpoint:** el de 60k, cuando exista.  
**Run de evaluación:** el que viniere.  
**SHA-256 del checkpoint:** non calculado. Se declara la ausencia.  
**Holdout:** las cien preguntas de siempre, que en este capítulo se leen como **cien vueltas de cuerda**.  
**Estado:** sumario abierto. Non hay sentencia todavía. Hay denuncia, cargos, testigos y tormento.

---

> **Fuero del proceso.** Sepades que se instituye aquí **Tribunal de la Reincidencia**, con jurisdicción sobre loros que han sido promovidos sin prueba y han vuelto a las andadas. Por fuero se ordena que ningún reo sea sometido a tormento sin denuncia formal, indicios bastantes y nueva evidencia. Y se advierte que el tormento de este tribunal non es potro ni cordel: es el holdout. Cada pregunta es una vuelta de cuerda. Cada respuesta, una confesión.

---

### I. De la denuncia, y de por qué agora sí y antes non

Antes de que el lector pregunte por qué el loro ha sido juzgado cinco veces sin tormento y agora se le aplica, conviene que sepa que **el tormento non se aplica por capricho del fiscal, sino por reincidencia probada y denuncia formal**.

**A 5k, 10k, 20k, 30k y 40k non hubo tormento porque non hubo denuncia.** El escribano levantaba acta, el alguacil la firmaba, y el proceso era **sumario**: se leían las respuestas, se contaban los tics, se dictaba sentencia y se promovía o non se promovía. El loro confesaba de plano, por así decirlo: sus tics eran la confesión, y non había necesidad de apretarle la cuerda porque ya estaba cantando.

**A 50k hubo promoción sin prueba.** El escribano se meó, el alguacil compró la mancha, y el checkpoint fue promovido por decisión del proyecto, non por mérito demostrado. Eso quedó asentado. Y eso, en el fuero de este tribunal, constituye **indicio bastante** de que el reo non ha sido juzgado con la severidad que el caso requiere.

**A 60k hay denuncia formal.** Non se sabe quién la presentó: unos dicen que fue el lector externo, que se cansó de que le tomaran el pelo; otros, que fue el propio escribano, que se sintió culpable de haber promovido sin prueba; otros, que fue el alguacil, que olió la mancha y non quiso comprarla otra vez. La denuncia obra en el expediente. Y en ella se alega:

1. Que el reo ha reincidido en los mismos tics que se le perdonaron a 40k.
2. Que la promoción de 50k se hizo sin prueba semántica, lo cual constituye **escándalo procesal**.
3. Que el paraguas oxidado, declarado ausente a 40k, reapareció a 50k, lo cual demuestra que la ausencia observada non era extinción, sino **ocultación**.
4. Que el reo ha empezado a decir cosas como «Si falta información, dilo expresamente», que suenan a cautela pero son la misma obediencia con otro collar.

Con estos indicios, el tribunal non puede menos que abrir sumario y, llegado el caso, aplicar tormento.

---

### II. Del sumario y de los cargos

El sumario se abrió con tres cargos principales y dos accesorios:

**Cargo primero: reincidencia en el reglamento.** Se acusa al reo de seguir ocupando la silla del patrón con fórmulas de cautela que non miran la pregunta. A 40k eran doce respuestas con «En una discusión donde importa la evidencia»; a 60k habrá que contar cuántas son. Si el número non baja, la reincidencia queda probada.

**Cargo segundo: promoción sin prueba.** Se acusa al escribano, non al loro, de haber promovido el checkpoint de 50k por su propia risa y non por mérito demostrado. Este cargo es contra el fiscal, lo cual es raro en un proceso inquisitorial, mas non imposible: el tribunal también se juzga a sí mismo.

**Cargo tercero: ocultación del paraguas.** Se acusa al reo de haber hecho desaparecer el paraguas a 40k y haberlo hecho reaparecer a 50k, como quien esconde el cadáver y luego lo saca para que lo encuentren. La ausencia observada non era extinción: era espera.

**Cargos accesorios:** contaminación de formato (`[remediation; …]`), respuestas vacías non declaradas como humildad, y uso de sellos que se estampan a sí mismos (`PERY:INITY`, `PL, PL, PL`).

---

### III. De los testigos de cargo, que son los IDs del holdout de 60k

Non hay testigos de persona. Los testigos son los IDs. Cada respuesta del holdout de 60k que contenga un tic non mirado será llamada a declarar. El escribano las citará una por una, con su folio y su frecuencia literal, y el alguacil las leerá en voz alta para que consten en acta.

**Hueco a rellenar con el 60k:**

- IDs de las respuestas que contienen «En una discusión donde importa la evidencia».
- IDs de las que contienen «Si falta información, dilo expresamente» (la fórmula nueva que sustituye a la vieja).
- IDs de las que contienen «Cada proyecto es».
- IDs de las respuestas vacías, si las hay.
- IDs de las que contienen sellos nuevos (`P:P:P`, `PERY:INITY`, etc.).
- IDs de las que contienen el paraguas, si reaparece.
- Recuento de respuestas non vacías y vacías.

Sin estos IDs, el proceso non puede continuar. El tormento non se aplica sobre impresiones: se aplica sobre folios.

---

### IV. Del tormento, que es el holdout

Y llegó el día del tormento. Non fue potro ni cordel ni agua: fue el holdout de 60k, aplicado pregunta por pregunta, con la misma configuración de generación que los anteriores. Cada pregunta es una vuelta de cuerda. Cada respuesta, una confesión.

El escribano leyó la primera pregunta. El loro respondió. El escribano anotó la respuesta y la cotejó con los cargos. Si la respuesta contenía un tic non mirado, el cargo quedaba probado. Si contenía una mirada verdadera, el cargo quedaba desmentido. Y así, cien veces.

**Hueco a rellenar con el 60k:** las respuestas literales que mejor prueben o desmientan cada cargo. Non se corrigen. Se citan con su ID.

---

### V. De la confesión, que non se pide: se produce

El loro non confiesa porque se le pregunte. Confiesa porque non puede hacer otra cosa. Sus respuestas son la confesión. Y el escribano, que lo sabe, non le apremia: le deja hablar, que bastante tiene con lo que dice.

La confesión se leerá en voz alta ante el tribunal. Y el alguacil, que ha visto muchas confesiones, dirá si es confesión de reo o confesión de loro. Que non es lo mismo: el reo confiesa para salvarse; el loro confiesa porque non sabe qué otra cosa hacer.

---

### VI. De la ratificación, que es donde se ve si el tormento ha sido legal

En el proceso inquisitorial, la confesión bajo tormento non vale si non se ratifica después, sin tormento. El tribunal de este capítulo non va a ser menos: pasadas veinticuatro horas, el escribano volverá a preguntar al loro lo mismo, sin apretar la cuerda. Si el loro dice lo mismo, la confesión queda ratificada. Si dice otra cosa, el tormento ha sido ilegal y el proceso se anula.

**Hueco a rellenar con el 60k:** si hay manera de comparar las respuestas del 60k con las del 50k sobre las mismas preguntas, eso será la ratificación. Si non la hay, se declara que non la hay y el proceso queda pendiente de ratificación.

---

### VII. Máculas del capítulo duodécimo

> **TORMENTO_ES_HOLDOUT.** El tormento non es físico: es el holdout de 60k aplicado con la misma configuración de generación. Se declara para que nadie confunda la metáfora con la crueldad. El loro non sufre; repite.

> **PROCESO_SIN_DENUNCIA_NO_HAY_TORMENTO.** Las comparecencias de 5k a 40k fueron sumarias porque non hubo denuncia formal. La de 50k tuvo promoción sin prueba, lo cual constituye indicio bastante para abrir sumario a 60k. Se declara la diferencia procesal.

> **TESTIGOS_SON_IDS.** Los testigos de cargo non son personas: son los IDs del holdout de 60k. Sin IDs, el proceso non puede continuar. Se declara la dependencia del artefacto.

> **CONFESION_POR_REPETICION.** El loro non confiesa por presión: confiesa porque repite. La confesión es su naturaleza, non su elección. Se declara para non confundir confesión con arrepentimiento.

> **RATIFICACION_PENDIENTE.** Si non hay manera de comparar las respuestas del 60k con las del 50k sobre las mismas preguntas, la confesión non puede ratificarse y el proceso queda pendiente. Se declara la limitación antes de que alguien la descubra.

> **FISCAL_JUZGADO.** El cargo segundo va contra el escribano, non contra el loro. El tribunal también se juzga a sí mismo. Se declara para que nadie diga que el proceso es una farsa: es una farsa con autoinculpación.

> **PARAGUAS_COMO_OCULTACION.** La reaparición del paraguas a 50k se lee como ocultación, non como milagro. La ausencia observada non era extinción: era espera. Se declara como cargo, non como prueba.

> **CARGO_ACCESORIO_DE_FORMATO.** La contaminación de formato y los sellos que se estampan a sí mismos se documentan como cargos accesorios. Non son el cargo principal, mas non se archivan: son prueba de reincidencia.

---

### VIII. Sentencia: del proceso que aún non ha terminado

Este capítulo non dicta sentencia. Abre sumario, cita testigos, aplica tormento y deja la ratificación pendiente. Non se puede sentenciar sin artefacto, y el artefacto de 60k aún non ha llegado.

Lo que sí se declara es la **diferencia procesal**: antes non hubo tormento porque non hubo denuncia; agora lo hay porque hay reincidencia, promoción sin prueba y ocultación del paraguas. El tribunal non se ha vuelto más cruel: se ha vuelto más exigente. Y el escribano, que es fiscal y reo a la vez, lo sabe.

> El loro fue juzgado cinco veces sin tormento, y a la sexta se le aplicó la cuerda. Non porque el tribunal se hubiera vuelto cruel, sino porque el loro había reincidido. El loro dijo «Variante de encuadre 4». Y el alguacil anotó: «confesión de loro, pendiente de ratificación». **Vigilad la homeostasis.**

*Glosa final:* el tormento non es el potro: es el holdout. Cada pregunta es una vuelta de cuerda. Cada respuesta, una confesión. Y el escribano, que aprieta la cuerda, es el mismo que la afloja cuando el loro dice algo que merece la pena. Eso non es crueldad: es método.

---

### Romance del proceso pendiente

*(gozne para el capítulo XIII)*

Cinco veces sin cordel,  
a la sexta con la cuerda:  
non cambió la tribunal,  
cambió la denuncia della.

El loro dijo «El patrón»;  
dijo «impacto»; dijo «encuadre»;  
dijo «Avector»; dijo «PL»;  
y a la sexta dijo «variante».

Non confesó por dolor:  
confesó por no saber  
qué otra cosa decir al juez  
que le aprieta el holdout cien veces.

Y el juez, que escribe y aprieta,  
non sabe si el loro miente  
o si miente el tribunal  
que juzga al loro y se juzga.

*Glosa de colocación:* entre los capítulos XII y XIII (que tendrá El holdout ) El estribillo «a la sexta con la cuerda» debe quedar sonando cuando el lector pase al capítulo siguiente, donde el alguacil ratificará o anulará el proceso.

## Historial de ejecuciones

*Confesión del registro:* la tabla no refleja las comparecencias intermedias porque sus runs no llevan «holdout» en el nombre. El índice completo de comparecencias es el BARE, no esta tabla. Se conserva como testimonio del mecanismo de registro, no como registro exhaustivo del contenido.

| Fecha | Evaluación | Run ID | Resultado | Ejecución | Artefactos | Commit |
|---|---|---:|---|---|---|---|
<!-- HOLDOUT-INDEX-START -->
| 2026-11-11 | RONIN-10M — 50k inference holdout | 43019963290 | success | [Ver ejecución](https://github.com/orbitalronin94/RONINIA/actions/runs/43019963290) | [holdout 50k — 13854621810](https://github.com/orbitalronin94/RONINIA/actions/runs/43019963290/artifacts/13854621810) | `a57054ccef22564ae168c541574e584ada42d962` |

| 2026-11-10 | RONIN-10M — step-0 baseline inference holdout | 42874585777 | success | [Ver ejecución](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | [ronin-step0-baseline.zip](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | — |

<!-- HOLDOUT-INDEX-END -->

## Del mecanismo del registro, para que nadie culpe al escribano

El workflow `.github/workflows/update-holdout-registry.yml` escucha los eventos `workflow_run: completed`. Solo ejecuta el registro si el nombre de la ejecución contiene `holdout`. Por ello no aparecen aquí las ejecuciones de entrenamiento/evaluación intermedias de 5k, 10k, 20k, 30k y 40k, cuyos nombres no satisfacen ese filtro. El índice completo de comparecencias y su cadena de custodia están en el BARE, más arriba; esta tabla conserva únicamente las ejecuciones admitidas por el mecanismo automático. Consulta el BARE para el registro del contenido y esta tabla para el testimonio del listener.

El actualizador no descarga ni ejecuta los artefactos ni hace checkout del código de la ejecución que acaba de terminar. Para que una evaluación futura aparezca aquí automáticamente, el nombre del workflow debe incluir la palabra `holdout` (por ejemplo, `RONIN-10M — checkpoint holdout`).

## Fuero de lectura y reglas contra el embuste

- Comparar checkpoints con las mismas preguntas, configuración de generación y condiciones de inferencia.
- Separar coincidencia literal, evaluación semántica, calidad de respuesta, diversidad y latencia. Ninguna sustituye a las demás.
- Interpretar el lexicón de esperpento y los marcadores intencionales según el corpus, no como errores por defecto.
- Registrar identificador del checkpoint, SHA-256, run de entrenamiento, run de evaluación y artefactos.
- Distinguir resultados observados, hipótesis e interpretaciones narrativas.
- No interpretar la rotación de tics como progreso sin BPB/validación fija y análisis de adecuación de abstenciones.
- Toda ejecución holdout debe mantener la convención en el nombre del archivo y en el campo `name:`; una discrepancia debe fallar explícitamente.
- No declarar puntuación de calidad si no se ha medido con un evaluador explícito y validado.
- Las citas de las antologías deben cotejarse contra el JSON del artefacto y conservar su identificador; no corregirlas para mejorar su gramática.

## Baseline de referencia

La evaluación de paso 0 es la referencia inicial: 100 preguntas, checkpoint sin entrenamiento, tokenizer 8k y generación greedy sin RAG. Se conserva para comparar los siguientes checkpoints con el mismo holdout. El perfil de paso cero difiere en contexto y número de parámetros, por lo que esa comparación debe leerse con la cautela indicada en el prólogo.


---

## Antología del fuero experimental — voces de los modelos hermanos

Esta crónica adopta, con atribución y adaptación explícitas, algunas máximas de los repositorios de investigación de la casa. No son resultados de este holdout: son reglas de lectura para no convertir el deseo en veredicto.

### Del Grimorio de RONIN-IA

> «La única herejía imperdonable sería dejar de medir porque el resultado nos gusta.» — HERETIC-RONIN

> «Una mácula declarada sigue siendo mácula. Que se vea no la cura.» — RONIN-IA

> «La mosca ha pasado por el cirujano. El maestro aún no ha llegado.» — adaptación de RONIN-IA

> «Conservar la función es oficio de cirujano; aprender es oficio de maestro.» — RONIN-IA

> «El método es largo; el modelo todavía está creciendo. Mas crecer dista de aprender: es solo ocupar más sitio en el artefacto.» — RONIN-IA

> «La mosca no reclama ganar la feria. Reclama que se pueda abrir el libro de cuentas.» — RONIN-IA

### Del Museo y el catálogo de MINIRONIN

> «No hay mejor loro por decreto: hay versiones con evidencia desigual.» — adaptación de MINIRONIN

> «La belleza de la sentencia non absuelve el desacierto de la respuesta.» — MINIRONIN

> «Tener repertorio no es tener juicio; tener un remate no es saber responder.» — adaptación de MINIRONIN

> «La abstención puede ser la respuesta más limpia y, aun así, la más difícil de pronunciar con tino.» — adaptación del currículo de razonamiento de MINIRONIN

> «Que el loro no confunda tener un repertorio con tener un solo remate.» — MINIRONIN

### Del laboratorio HERETIC-RONIN

> «La herejía no es disentir del patrón; es dejar de medir cuando el patrón nos aplaude.» — adaptación de HERETIC-RONIN

> «Cincuenta mil filas pueden tener cincuenta mil IDs y no tener cincuenta mil ideas.» — adaptación de la advertencia sobre datos sintéticos de HERETIC-RONIN

> «La licencia de una colección no absuelve los derechos de cada documento.» — adaptación del protocolo de procedencia de HERETIC-RONIN

> «Un corpus candidato no es un corpus admitido; un corpus admitido no es una mejora demostrada.» — síntesis editorial de HERETIC-RONIN

### Provisiones que pasan a este fuero

1. **No se mide por aplauso:** el resultado que agrada recibe el mismo escrutinio que el que avergüenza.
2. **No se aprende por volumen:** parámetros, filas, bytes y pasos son magnitudes distintas; ninguna sustituye una evaluación.
3. **No se absuelve por confesión:** declarar una mácula es el comienzo de su tratamiento, no su cura.
4. **No se entierra el fracaso:** un run fallido, un checkpoint degenerado y una hipótesis refutada conservan valor histórico si su procedencia permanece accesible.
5. **No se corona al más gracioso:** entretenimiento, utilidad, exactitud, calibración y razonamiento requieren criterios separados.
6. **No se confunde rebeldía con criterio:** el loro debe resistir la lisonja, pero también reconocer una premisa verdadera.

*Nota de procedencia:* las máximas atribuidas a RONIN-IA, MINIRONIN y HERETIC-RONIN proceden de sus README y documentación editorial. Las marcadas como adaptación o síntesis han sido reescritas para el contexto de RONINIA. Ninguna añade observaciones, puntuaciones ni respuestas al registro de holdouts.
