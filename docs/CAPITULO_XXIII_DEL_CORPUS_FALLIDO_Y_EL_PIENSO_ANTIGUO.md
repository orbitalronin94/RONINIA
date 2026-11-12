# Capítulo XXIII — De cómo fracasó la compilación del gran corpus y el loro volvió al pienso antiguo

**Punto de partida:** checkpoint de 180.000 pasos.  
**Entrenamiento siguiente:** [run 43261847027](https://github.com/orbitalronin94/RONINIA/actions/runs/43261847027).  
**Objetivo de esta tanda:** 25.000 pasos adicionales, hasta 205.000.  
**Padre:** checkpoint 180.000, SHA-256 `a0e37c95855937b7b071a5de6384528a6372a564ebb944b8b4851d97126c5433`.  
**Corpus utilizado:** caché de tokens preexistente, artefacto `roninia-token-cache-42890884432`, procedente del run 42890884432.  
**Tokenizador:** vocabulario 8.192; SHA-256 `605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`.  
**Política de esta tanda:** reutilizar la caché anterior sin recompilar ni retokenizar.  
**Estado al redactar:** el run de entrenamiento ha sido creado y está en cola; sus resultados y checkpoints quedan pendientes de ejecución.

## I. De la gran despensa que no abrió

El escribano llevaba semanas hablando de una despensa nueva. No era una despensa pequeña: había de reunir bibliotecas castellanas verificadas, más los conjuntos sintéticos que el reglamento vigente admitía. Los sintéticos entrarían tal cual estaban, sin exigirles certificado lingüístico; los documentos no sintéticos, en cambio, debían acreditar su condición castellana por metadatos o por procedencia curada. Los materiales de evaluación y holdout quedaban fuera.

—Esta vez —dijo el escribano— el loro comerá de una biblioteca mayor. Y acaso, por fin, aprenda a distinguir el sustantivo del ruido.

El alguacil preguntó si la despensa estaba preparada.

El escribano mostró un workflow, varios manifiestos esperados y una colección de promesas.

La compilación falló.

No hubo artefacto nuevo validado que pudiera entregarse al entrenamiento. La gran despensa quedó en proyecto, con sus estantes dibujados y la puerta cerrada. No se fingió que el corpus estuviese listo; tampoco se llamó «castellano puro» a una mezcla cuya política admitía todos los sintéticos, cualquiera que fuese su idioma.

—¿Y ahora qué comerá el loro? —preguntó el escribano.

—Lo que ya tenemos —dijo el alguacil—. Un animal no debe ayunar mientras el cocinero discute con el almacén.

## II. Del pienso viejo, que al menos tenía inventario

Se tomó entonces una decisión menos vistosa y más útil: continuar desde el checkpoint de 180.000 pasos con la caché de tokens ya existente.

No se sustituyó el corpus por una descarga improvisada. No se mezcló a escondidas el material nuevo incompleto. No se volvió a tokenizar. Se reutilizó el artefacto anterior:

`roninia-token-cache-42890884432`

La identidad del tokenizador permaneció fijada en SHA-256:

`605834d0d1deea545518be54ae0936060845107b906172f6628d0ff9520e57a4`

Y el padre quedó fijado por su propio hash:

`a0e37c95855937b7b071a5de6384528a6372a564ebb944b8b4851d97126c5433`

El nuevo entrenamiento se configuró para añadir 25.000 pasos, desde 180.000 hasta 205.000, con checkpoints cada 1.000 pasos. El run creado es el [43261847027](https://github.com/orbitalronin94/RONINIA/actions/runs/43261847027).

Así quedó asentada la diferencia entre dos operaciones que el escribano había estado a punto de confundir:

- **Cambiar el corpus:** exige compilarlo, validarlo, publicar su artefacto y fijar su identidad.
- **Continuar el entrenamiento:** exige un checkpoint padre verificable y una caché de tokens compatible y comprobada.

La primera operación no llegó a buen puerto. La segunda pudo prepararse con los materiales anteriores.

## III. De la prudencia que el escribano tomó por cobardía

—¿No estaremos perdiendo una oportunidad? —preguntó el escribano—. El corpus nuevo era mayor.

—Mayor no significa mejor —respondió el alguacil—. Y prometido no significa disponible.

El escribano objetó que el loro quizá necesitase alimento fresco para adquirir seso.

—Quizá —dijo el alguacil—. Pero no le deis una despensa imaginaria. Primero se pesa el pienso; luego se alimenta al animal; después se observa si aprende. Si cambiáis a la vez el alimento, el tokenizador, el padre y el método de evaluación, no sabréis qué le ha sentado mal.

El alguacil ordenó conservar la comparación limpia: checkpoint 180.000 como punto de partida; misma arquitectura; mismo tokenizador; corpus anterior ya tokenizado; 25.000 pasos nuevos. El corpus grande quedaría para otra tentativa, cuando su compilación produjese un artefacto real y verificable.

El escribano escribió «retroceso» en el margen.

El alguacil lo tachó.

—No hemos retrocedido al checkpoint. Hemos continuado con el material disponible. Otra cosa es que el loro mejore. Eso aún no lo sabemos.

## IV. De lo que habrá de juzgarse cuando el loro vuelva a hablar

Esta tanda no demuestra todavía que el modelo haya ganado capacidad. Solo define un experimento: añadir 25.000 pasos manteniendo el corpus anterior y las demás condiciones principales.

Cuando termine, habrá que mirar:

1. Si se alcanzan los 205.000 pasos y se publican checkpoints recuperables.
2. Si el hash del checkpoint final y el linaje concuerdan con el padre de 180.000.
3. Si la evaluación de 100 preguntas se ejecuta con la misma configuración que el holdout oficial anterior.
4. Si cambian las respuestas vacías, las fugas de formato, las repeticiones y la pertinencia de las respuestas.
5. Si cualquier mejora se sostiene en el holdout, no solo en la pérdida de entrenamiento o en la alegría del escribano.

El corpus nuevo no debe entrar en la historia de esta tanda como si hubiese sido utilizado. Su compilación fallida es un hecho del proceso, no una dieta secreta del modelo.

## V. Sentencia del alguacil

El escribano preguntó si el loro apreciaría el seso después de otros veinticinco mil pasos.

—Eso no lo decide el calendario —dijo el alguacil—. Lo decide el examen.

Y añadió, para que constase en el libro:

**El corpus grande no llegó a la mesa; el viejo volvió al comedero. Veinticinco mil pasos más no son veinticinco mil razones para creer.**

El escribano quiso poner debajo: «Y acaso el loro aprenda».

El alguacil le permitió escribirlo, pero entre signos de interrogación.

**Primero que termine el entrenamiento. Después que responda. Y solo entonces hablaremos de seso.**
