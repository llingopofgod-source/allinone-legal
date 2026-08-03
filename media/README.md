# Material real de la app

Aquí van las capturas y los vídeos **reales** de AllInOne. La landing no dibuja
ninguna interfaz: mientras un hueco esté vacío, muestra un marcador visible.

## Cómo enchufar un archivo

1. Copia el archivo a esta carpeta, por ejemplo `habitos.png`.
2. Abre `index.html`, busca el bloque `MEDIA` (arriba del script).
3. Rellena `src`:

```js
habitos: { tipo:"img", src:"/media/habitos.png", nombre:"Hábitos" },
```

Para un vídeo, `tipo:"video"` y un `.mp4`. Nada más: la página se recompone sola.

## Qué hace falta

| Clave        | Tipo    | Qué es                                   |
|--------------|---------|------------------------------------------|
| `hero`       | vídeo   | 20–30 s en bucle, el que abre la página  |
| `demo`       | vídeo   | El mismo del Reel de Instagram           |
| `habitos`    | captura | Pantalla de hábitos                      |
| `ia`         | vídeo   | La guía con IA en uso                    |
| `objetivos`  | captura | Objetivos                                |
| `calendario` | vídeo   | Calendario                               |
| `rutinas`    | captura | Rutinas                                  |
| `stats`      | captura | Estadísticas                             |
| `pantalla`   | captura | Tiempo de pantalla                       |
| `entrenos`   | vídeo   | Entrenamientos                           |
| `sueno`      | captura | Sueño                                    |

## Formato

- **Capturas**: PNG o JPG, verticales, del propio iPhone o del simulador.
  Se recortan solas a la pantalla del mockup (`object-fit:cover`).
- **Vídeos**: MP4 (H.264), verticales, **sin audio**, por debajo de 3 MB cada uno.
  Se reproducen en bucle y en silencio; los navegadores móviles bloquean
  cualquier vídeo con sonido que intente arrancar solo.
