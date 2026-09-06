#!/usr/bin/env python3
"""Build fidelity-first Svif production assets from the locked 10:42 AM board.

The approved Svif S depends on translucent ribbon layering and particle treatment.
Reviewed automatic/pure-vector reconstructions materially changed that appearance.
This builder therefore preserves the approved appearance as deterministic raster
masters and derivatives. It does not redesign or invent brand geometry.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image

SOURCE_SHA256 = "10ad09a3c68e7ccd84e8c50ac4aaeda2bdb1e1fee4c09899ef4215fdec18f3fd"
CROPS = {
    "mark": (48, 200, 340, 490),
    "wordmark": (395, 255, 650, 410),
    "horizontal-lockup": (704, 230, 1065, 430),
    "vertical-lockup": (1122, 215, 1330, 430),
    "light-usage": (40, 575, 418, 715),
    "dark-usage": (470, 575, 865, 715),
    "monochrome-usage": (965, 575, 1350, 715),
    "app-icon": (28, 800, 188, 955),
    "social-card": (545, 785, 940, 995),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def white_to_alpha(image: Image.Image, noise_floor: float = 0.015) -> Image.Image:
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    alpha = np.max(255.0 - rgb, axis=2) / 255.0
    alpha = np.where(alpha < noise_floor, 0.0, alpha)
    a = alpha[..., None]
    foreground = np.zeros_like(rgb)
    nonzero = alpha > 1e-6
    foreground[nonzero] = (
        rgb[nonzero] - 255.0 * (1.0 - a[nonzero])
    ) / a[nonzero]
    foreground = np.clip(foreground, 0.0, 255.0)
    rgba = np.dstack((foreground, alpha * 255.0)).astype(np.uint8)
    rgba[rgba[..., 3] == 0, :3] = 0
    return Image.fromarray(rgba, "RGBA")


def square_fit(image: Image.Image, size: int, padding_fraction: float) -> Image.Image:
    pad = round(size * padding_fraction)
    available = max(1, size - 2 * pad)
    scale = min(available / image.width, available / image.height)
    new_size = (
        max(1, round(image.width * scale)),
        max(1, round(image.height * scale)),
    )
    resized = image.resize(new_size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    canvas.alpha_composite(
        resized,
        ((size - resized.width) // 2, (size - resized.height) // 2),
    )
    return canvas


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--board", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    if sha256(args.board) != SOURCE_SHA256:
        raise SystemExit("source board SHA-256 mismatch; refusing to derive assets")

    args.out.mkdir(parents=True, exist_ok=True)
    board = Image.open(args.board).convert("RGB")
    manifest = {
        "source_board_sha256": SOURCE_SHA256,
        "mode": "fidelity-first raster production",
        "warning": "Raster masters preserve the approved appearance; do not claim infinite vector scalability.",
        "assets": {},
    }

    for role in ("mark", "wordmark", "horizontal-lockup", "vertical-lockup"):
        crop = board.crop(CROPS[role])
        rgba = white_to_alpha(crop)
        if role == "mark":
            # The approved board's specimen label slightly overlaps the crop's top edge.
            # Remove only that presentation row; approved artwork starts below it.
            data = np.array(rgba)
            data[:18, :, :] = 0
            rgba = Image.fromarray(data, "RGBA")
        target = args.out / f"svif-{role}.png"
        rgba.save(target, optimize=True)
        manifest["assets"][target.name] = {
            "role": "raster-master",
            "native_size": [rgba.width, rgba.height],
            "sha256": sha256(target),
            "crop": list(CROPS[role]),
            "raster_derived_upscale": False,
        }

    for role in ("light-usage", "dark-usage", "monochrome-usage", "app-icon", "social-card"):
        image = board.crop(CROPS[role])
        target = args.out / f"svif-{role}.png"
        image.save(target, optimize=True)
        manifest["assets"][target.name] = {
            "role": "approved-board-derivative",
            "native_size": [image.width, image.height],
            "sha256": sha256(target),
            "crop": list(CROPS[role]),
            "raster_derived_upscale": False,
        }

    mark = Image.open(args.out / "svif-mark.png").convert("RGBA")
    for size in (128, 64, 32, 16):
        icon = square_fit(mark, size, 0.08 if size >= 64 else 0.05)
        target = args.out / f"svif-favicon-{size}.png"
        icon.save(target, optimize=True)
        manifest["assets"][target.name] = {
            "role": "favicon",
            "size": size,
            "sha256": sha256(target),
            "raster_derived_upscale": size > max(mark.size),
        }

    (args.out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
