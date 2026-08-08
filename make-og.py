#!/usr/bin/env python3
"""
Genera la imagen que se ve al compartir el enlace (WhatsApp, Instagram, X…).

Antes se usaba `logo.png`, que es cuadrado de 1024×1024: las plataformas piden
1200×630, así que el logo salía recortado o diminuto junto a un texto que nadie
lee. Esta imagen ocupa el formato entero y dice lo que hay que decir.

    python3 make-og.py     →  og.jpg
"""
from PIL import Image, ImageDraw, ImageFilter
import os

W, H = 1200, 630
AZUL      = (0, 113, 227)
TINTA     = (6, 6, 10)
GRIS      = (110, 110, 120)
BLANCO    = (255, 255, 255)

BASE = os.path.dirname(os.path.abspath(__file__))
SF   = "/System/Library/Fonts/SFNS.ttf"


def fuente(size, weight=None):
    """SF Pro con el peso pedido; Helvetica si el sistema no la trae."""
    from PIL import ImageFont
    try:
        f = ImageFont.truetype(SF, size)
        if weight is not None:
            try:
                f.set_variation_by_axes([weight])
            except Exception:
                pass
        return f
    except Exception:
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)


def aura(img):
    """El mismo halo azul del hero de la web, para que la tarjeta y la página
    se reconozcan como la misma cosa."""
    capa = Image.new("RGB", (W, H), BLANCO)
    d = ImageDraw.Draw(capa)
    cx, cy, r = W * 0.78, H * 0.12, 520
    for i in range(26, 0, -1):
        t = i / 26
        rr = r * t
        # de #D6E8FF a blanco
        col = (
            int(255 - (255 - 214) * (1 - t) ** 1.6),
            int(255 - (255 - 232) * (1 - t) ** 1.6),
            255,
        )
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=col)
    capa = capa.filter(ImageFilter.GaussianBlur(48))
    img.paste(capa, (0, 0))


def main():
    img = Image.new("RGB", (W, H), BLANCO)
    aura(img)
    d = ImageDraw.Draw(img)

    x = 74

    # ── Marca ────────────────────────────────────────────────────────────
    logo_p = os.path.join(BASE, "logo.png")
    if os.path.exists(logo_p):
        logo = Image.open(logo_p).convert("RGBA").resize((62, 62), Image.LANCZOS)
        redondo = Image.new("L", (62, 62), 0)
        ImageDraw.Draw(redondo).rounded_rectangle([0, 0, 61, 61], radius=15, fill=255)
        img.paste(logo, (x, 66), redondo)
    d.text((x + 78, 82), "AllInOne", font=fuente(31, 600), fill=TINTA)

    # ── Píldora de escasez ───────────────────────────────────────────────
    py = 158
    txt = "100 plazas Founders"
    f_p = fuente(21, 500)
    w_p = d.textlength(txt, font=f_p)
    d.rounded_rectangle([x, py, x + w_p + 62, py + 44], radius=22,
                        fill=(240, 246, 255), outline=(214, 232, 255), width=1)
    d.ellipse([x + 22, py + 18, x + 30, py + 26], fill=(52, 199, 89))
    d.text((x + 40, py + 11), txt, font=f_p, fill=(66, 66, 74))

    # ── Titular ──────────────────────────────────────────────────────────
    d.text((x, 232), "Tu vida entera.", font=fuente(76, 700), fill=TINTA)
    d.text((x, 318), "Una sola app.",   font=fuente(76, 700), fill=AZUL)

    # ── Bajada ───────────────────────────────────────────────────────────
    d.text((x, 424), "Hábitos, IA, rutinas, sueño y entrenamientos.",
           font=fuente(27, 400), fill=(66, 66, 74))
    d.text((x, 462), "Sin saltar de app en app.",
           font=fuente(27, 400), fill=(66, 66, 74))

    # ── Pie ──────────────────────────────────────────────────────────────
    # La imagen es RGB: un cuarto canal aquí se ignora y la línea saldría negra.
    d.line([x, 536, W - 74, 536], fill=(228, 228, 234), width=1)
    d.text((x, 558), "allinonehabits.online", font=fuente(23, 500), fill=GRIS)

    precio = "$5.99 USD"
    f_pr = fuente(23, 600)
    d.text((W - 74 - d.textlength(precio, font=f_pr), 558), precio,
           font=f_pr, fill=TINTA)

    salida = os.path.join(BASE, "og.jpg")
    img.save(salida, "JPEG", quality=88, optimize=True, progressive=True)
    print("%s  %dx%d  %.0f KB" % (salida, W, H, os.path.getsize(salida) / 1024))


if __name__ == "__main__":
    main()
