#!/usr/bin/env python3
"""Mete los términos de /legal/ dentro de la portada.

El texto legal vive en UN solo sitio: `legal/index.html`, que es la URL que
tienen registrada Apple y Google y la que no se puede mover. La portada
enseña ese mismo texto, pero una copia pegada a mano acaba diciendo una cosa
distinta a la otra en cuanto se toca una — y con un texto legal eso no es un
despiste, es una condición que el usuario aceptó y que ya no dice lo mismo.

Así que la portada no lleva copia: lleva dos marcas y este script rellena lo
que va entre ellas. Después de editar los términos en `legal/index.html`:

    python3 scripts/sync-terminos.py

Sin argumentos reescribe `index.html`. Con `--check` no toca nada y sale con
código 1 si los dos archivos se han separado (sirve para comprobarlo antes de
publicar).
"""
import html
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LEGAL = RAIZ / "legal" / "index.html"
HOME = RAIZ / "index.html"

INICIO = "<!-- TERMINOS:INICIO — generado por scripts/sync-terminos.py, no editar a mano -->"
FIN = "<!-- TERMINOS:FIN -->"


def articulos(fuente: str):
    """Parte la sección #terminos en (título, cuerpo html) por cada <h2>."""
    m = re.search(r'<section id="terminos">(.*?)</section>', fuente, re.S)
    if not m:
        raise SystemExit("No encuentro <section id=\"terminos\"> en legal/index.html")
    cuerpo = m.group(1)
    trozos = re.split(r"<h2>(.*?)</h2>", cuerpo, flags=re.S)
    # trozos[0] es el <h1> y lo que va antes del primer <h2>: no es un artículo.
    return [(t.strip(), c.strip()) for t, c in zip(trozos[1::2], trozos[2::2])]


def bloque(arts) -> str:
    out = [INICIO]
    for titulo, cuerpo in arts:
        # El texto legal ya viene como HTML de confianza (lo escribimos
        # nosotros); sólo el título va escapado porque acaba dentro de <summary>.
        out.append(
            "<details><summary>%s</summary><div class=\"legal-cuerpo\">%s</div></details>"
            % (html.escape(titulo), cuerpo)
        )
    out.append(FIN)
    return "\n".join(out)


def main() -> int:
    nuevo = bloque(articulos(LEGAL.read_text(encoding="utf-8")))
    home = HOME.read_text(encoding="utf-8")
    patron = re.compile(re.escape(INICIO) + r".*?" + re.escape(FIN), re.S)
    if not patron.search(home):
        raise SystemExit("index.html no tiene las marcas TERMINOS:INICIO / TERMINOS:FIN")

    if "--check" in sys.argv:
        actual = patron.search(home).group(0)
        if actual.strip() == nuevo.strip():
            print("Los términos de la portada están al día.")
            return 0
        print("⚠️  La portada y /legal/ dicen cosas distintas. Corre: python3 scripts/sync-terminos.py")
        return 1

    HOME.write_text(patron.sub(lambda _: nuevo, home, count=1), encoding="utf-8")
    print("Portada actualizada con %d artículos de /legal/#terminos." % len(articulos(LEGAL.read_text(encoding='utf-8'))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
