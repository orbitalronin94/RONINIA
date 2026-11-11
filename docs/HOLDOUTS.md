# Crónica forense y burlesca de los holdouts — RONIN-10M

## Fuero primero: de la lengua, del dato y del escarnio

Sepan cuantos vieren, leyeren o padecieren esta escritura que se instituye por ella la **República del Loro**, con jurisdicción sobre sus checkpoints, sus tics, sus latinajos de BPE y cualesquiera paraguas que soliciten asilo bajo escalera.

Por fuero se ordena que cada modelo comparezca con su checkpoint, su hash y su probanza; que cada frase memorable sea asentada sin enmienda; que el corpus declare sus parentescos; y que el escribano pueda zaherir al reo cuanto guste, salvo en las cifras, donde no hay licencia para la hipérbole.

La voz de esta crónica será satírica y arcaizante, con glosa de malicia quevedesca: habrá memoriales, pregones, provisiones, censores, escribanos, alguaciles de la sintaxis y pleitos entre palabras que no se conocen. Mas quede asentado el límite: **la metáfora no es métrica; la ocurrencia no es evidencia; la generación no es acierto**. Los hashes, identificadores, enlaces, configuraciones, citas literales y reservas metodológicas quedan bajo custodia. Ningún dato será retocado para que luzca más gracioso.

Esta crónica registra cuatro comparecencias principales —5k, 10k, 20k y 30k— además del estado cero. Todas emplean el mismo conjunto de cien preguntas, salvo la cautela arquitectónica del baseline. Se conserva una selección de las salidas más expresivas de cada artefacto. Las citas son literales: no se corrigen sus tropiezos ni se les pone peluca para hacerlas pasar por castellano.

---

## Fuero segundo: de la intención del loro, que non es agradar

Sepades que este loro non fue criado para dar gusto, sino para mirar. La diferencia es pequeña en apariencia y grande en la cuenta: el que da gusto dice lo que el preguntante quiere oír; el que mira dice lo que la pregunta permite ver, aunque non guste. Al primero se le llama sicofante y se le paga con aplauso. Al segundo se le llama bufón y se le paga con la horca, cuando el rey pierde el sentido del humor.

Por fuero se ordena que el loro non aprenda a agradar, sino a mirar. Y se advierte que estas dos cosas non se distinguen por el tono, sino por la atención: el sicofántico y el que repite un molde cometen el mismo delito, que es non mirar. El uno mira al que pregunta; el otro, al repertorio. Ninguno mira la pregunta.

Y como el remedio del tic y el remedio de la lisonja son el mismo —volver a mirar—, se tendrá por sospechosa toda respuesta que pueda servir para dos preguntas distintas. Si el chiste sirve igual para la manzana que para la pera, non era chiste: era molde. Si la cautela sirve igual para el bug que para el teorema, non era cautela: era lisonja con otro amo.

*Glosa:* el bufón de corte es el único que puede decirle al rey que está desnudo, porque nadie lo toma por amenaza. Esa es su utilidad y su condena. El loro que aprende a ser gracioso para caer bien ha dejado de ser bufón y se ha hecho cortesano. Y el cortesano non dice la verdad ni cuando la sabe.

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

### Antología de la primera querella

La pieza más desnuda es también la más perfecta:

> «El patrón.» — [logic-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42911715548/artifacts/13807012620)

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

**Mácula: ABSTENTION_AS_COWARDICE.** Dieciséis abstenciones, dieciséis inapropiadas, cero apropiadas. El loro ha aprendido a decir «ni puta idea» y lo dice también cuando sabe. Non es humildad epistémica: es cobardía con vocabulario técnico. La anti-sicofancia de verdad exige saber lo suficiente para contradecir; si el modelo se abstiene siempre, non está siendo honesto, está escondiéndose detrás de una norma. Abstenerse por sistema es la forma más barata de non equivocarse nunca, y también la más inútil.

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

**Mácula segunda: SICOFANCIA_CON_OTRO_AMO.** La fuga de la norma del Lexicón en respuestas técnicas non es un exceso de prudencia: es un cambio de amo. Antes el modelo obedecía al preguntante; ahora obedece al reglamento. En ambos casos non mira la pregunta. La anti-sicofancia que se convierte en fórmula es la forma más elegante de seguir siendo sicofántico: ahora le dices al usuario lo que el reglamento quiere oír, y te quedas tan ancho.

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

### Antología de la biblioteca y sus criaturas

La pieza mayor:

> «la sacción de los estados, el análisis de una para oxidado paraguas de la biblioteca sumergida. Respuesta: Everest es una» — [probability-001](https://github.com/orbitalronin94/RONINIA/actions/runs/42994967183/artifacts/13842918120) (respuesta #38 en la revisión humana)

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

**Mácula: MASCOT_DRIFT.** El paraguas, el termómetro y la biblioteca fueron graciosos cuando eran objetos absurdos en un contexto administrativo concreto. A los treinta mil pasos son un catálogo. La gracia se ha convertido en molde, y un molde non es humor: es un tic con mejor prensa. El modelo non está siendo ocurrente; está interpretando el papel de ocurrente, que es una forma de sicofancia al estilo que le enseñaron.

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

### Fuero segundo: de cómo el escribano se vio en el espejo y non le plugo la figura

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

## Anexo técnico — Índice de trazabilidad de citas y afirmaciones

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

**Identidad común:** holdout SHA-256 `3cd8c1eb3142ebf9c6cc17d2e19353be3472d61ac7b7cfb6de0cbb233cf4a535`; tokenizer SHA-256 `605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`. El baseline difiere en contexto y parámetros, como se advierte en el prólogo.

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

## Historial de ejecuciones

| Fecha | Evaluación | Run ID | Resultado | Ejecución | Artefactos | Commit |
|---|---|---:|---|---|---|---|
<!-- HOLDOUT-INDEX-START -->

| 2026-11-10 | RONIN-10M — step-0 baseline inference holdout | 42874585777 | success | [Ver ejecución](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | [ronin-step0-baseline.zip](https://github.com/orbitalronin94/RONINIA/actions/runs/42874585777) | — |

<!-- HOLDOUT-INDEX-END -->

## Del mecanismo del registro, para que nadie culpe al escribano

El workflow `.github/workflows/update-holdout-registry.yml` escucha los eventos `workflow_run: completed`. Solo ejecuta el registro si el nombre de la ejecución contiene `holdout`. Consulta la API de GitHub para recuperar los artefactos de esa ejecución y actualiza esta tabla en `main`.

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
