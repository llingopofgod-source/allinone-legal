# Material real de la app

Todo lo que hay aquí sale de una grabación de pantalla real del iPhone
(`ScreenRecording_08-03-2026`), convertida de HDR (PQ/BT.2020) a SDR BT.709.

La grabación venía en HDR con MaxCLL de 120 nits. Convertirla con las
herramientas normales la deja gris y lavada, y este ffmpeg no trae `zscale`
ni `libplacebo`, así que la conversión se hizo a mano con `pq2sdr.py`:
EOTF inversa de PQ, normalización contra el pico real (120 nits, no los
10 000 del estándar) y matriz BT.2020 -> BT.709.

## Qué hay

| Archivo         | Qué es                    | De qué segundo |
|-----------------|---------------------------|----------------|
| `hero.mp4`      | 14 s, cronómetro corriendo| 16–30          |
| `demo.mp4`      | 24 s, recorrido general   | 2–26           |
| `habitos.jpg`   | Lista de hábitos + logro  | 10             |
| `rutinas.jpg`   | Cronómetro de rutina      | 18             |
| `vida.jpg`      | Desglose de tiempo y salud| 26             |
| `pantalla.jpg`  | Clasificar tu tiempo      | 34             |
| `entrenos.jpg`  | Entrenamientos y métricas | 74             |
| `aventuras.jpg` | Side quests               | 50             |
| `sueno.jpg`     | Estrés e informe de sueño | 66             |
| `nutricion.jpg` | Nutrición y macros        | 114            |

Los vídeos van **sin pista de audio** a propósito: los navegadores móviles
bloquean cualquier vídeo con sonido que intente arrancar solo.

## Cambiar o añadir material

1. Copia el archivo aquí.
2. En `index.html`, busca el bloque `MEDIA` y rellena su `src`.
3. Si es una función nueva, añádela también a `FEATURES`.

Quedan dos huecos sin grabar: **Guía con IA** y **Calendario**. Están
declarados en `MEDIA` con `src` vacío y fuera de `FEATURES`, así que hoy no
se muestran. Cuando los grabes, rellena su `src` y añádelos a `FEATURES`.
