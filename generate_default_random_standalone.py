#!/usr/bin/env python3
"""Generate default and random palette preview images (standalone version)."""

import sys
import os

# Add paths to find the modules
sys.path.insert(0, '/home/pidge/code/smrpg_web_randomizer')
sys.path.insert(0, '/home/pidge/code/smrpgpatchbuilder/src')

from PIL import Image
from smrpgpatchbuilder.datatypes.graphics.classes import Tile

def decode_snes_4bpp_subtile(subtile_bytes: bytearray) -> list[int]:
    """Decode a single 8x8 SNES 4bpp subtile to palette indices."""
    if len(subtile_bytes) != 32:
        raise ValueError(f"Subtile must be exactly 32 bytes, got {len(subtile_bytes)}")

    pixels = []
    for y in range(8):
        bp0 = subtile_bytes[y * 2]
        bp1 = subtile_bytes[y * 2 + 1]
        bp2 = subtile_bytes[16 + y * 2]
        bp3 = subtile_bytes[16 + y * 2 + 1]

        for x in range(8):
            bit = 7 - x
            pixel = (
                ((bp0 >> bit) & 1) |
                (((bp1 >> bit) & 1) << 1) |
                (((bp2 >> bit) & 1) << 2) |
                (((bp3 >> bit) & 1) << 3)
            )
            pixels.append(pixel)

    return pixels


def render_tile_to_pixels(tile: Tile, palette_colors: list[int], gridplane: bool = True) -> list[list[tuple]]:
    """Render a single tile to a 2D array of RGBA colors."""
    if gridplane:
        format_sizes = {0: (3, 3), 1: (3, 4), 2: (4, 3), 3: (4, 4)}
    else:
        format_sizes = {0: (2, 2), 1: (2, 2), 2: (2, 2), 3: (2, 2)}

    cols, rows = format_sizes.get(tile.format, (2, 2) if not gridplane else (4, 4))
    tile_width = cols * 8
    tile_height = rows * 8

    pixels = [[(0, 0, 0, 0) for _ in range(tile_width)] for _ in range(tile_height)]

    subtile_bytes_list = tile.subtile_bytes
    for i, subtile_bytes in enumerate(subtile_bytes_list):
        if subtile_bytes is None:
            continue

        subtile_row = i // cols
        subtile_col = i % cols
        subtile_pixels = decode_snes_4bpp_subtile(subtile_bytes)

        for py in range(8):
            for px in range(8):
                palette_idx = subtile_pixels[py * 8 + px]
                out_y = subtile_row * 8 + py
                out_x = subtile_col * 8 + px

                if tile.mirror:
                    out_x = tile_width - 1 - out_x
                if tile.invert:
                    out_y = tile_height - 1 - out_y

                if palette_idx == 0:
                    pixels[out_y][out_x] = (0, 0, 0, 0)
                else:
                    color = palette_colors[palette_idx - 1]
                    r = (color >> 16) & 0xFF
                    g = (color >> 8) & 0xFF
                    b = color & 0xFF
                    pixels[out_y][out_x] = (r, g, b, 255)

    return pixels


def render_sprite_to_image(sprite, palette_colors: list[int], mold_index: int = 0, scale: int = 4):
    """Render a sprite with a custom palette to a PIL Image."""
    animation_pack = sprite.animation
    if mold_index >= len(animation_pack.properties.molds):
        raise ValueError(f"Mold index {mold_index} out of range")

    mold = animation_pack.properties.molds[mold_index]

    if len(mold.tiles) == 0:
        raise ValueError("Mold has no tiles to render")

    if mold.gridplane:
        tile = mold.tiles[0]
        pixels_2d = render_tile_to_pixels(tile, palette_colors, gridplane=True)

        height = len(pixels_2d)
        width = len(pixels_2d[0]) if height > 0 else 0

        img = Image.new('RGBA', (width, height))
        img_data = []

        for row in pixels_2d:
            for r, g, b, a in row:
                img_data.append((r, g, b, a))

        img.putdata(img_data)

        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)

        if scale > 1:
            new_size = (img.width * scale, img.height * scale)
            img = img.resize(new_size, Image.NEAREST)

        return img
    else:
        # Metasprite: multiple tiles with X/Y positioning
        min_x = min(tile.x for tile in mold.tiles)
        min_y = min(tile.y for tile in mold.tiles)
        max_x = max(tile.x + 16 for tile in mold.tiles)
        max_y = max(tile.y + 16 for tile in mold.tiles)

        canvas_width = max_x - min_x
        canvas_height = max_y - min_y
        canvas = Image.new('RGBA', (canvas_width, canvas_height), (0, 0, 0, 0))

        for tile in mold.tiles:
            pixels_2d = render_tile_to_pixels(tile, palette_colors, gridplane=False)
            tile_height = len(pixels_2d)
            tile_width = len(pixels_2d[0]) if tile_height > 0 else 0

            tile_img = Image.new('RGBA', (tile_width, tile_height))
            tile_data = []

            for row in pixels_2d:
                for r, g, b, a in row:
                    tile_data.append((r, g, b, a))

            tile_img.putdata(tile_data)

            pos_x = tile.x - min_x
            pos_y = tile.y - min_y
            canvas.paste(tile_img, (pos_x, pos_y), tile_img)

        bbox = canvas.getbbox()
        if bbox:
            canvas = canvas.crop(bbox)

        if scale > 1:
            new_size = (canvas.width * scale, canvas.height * scale)
            canvas = canvas.resize(new_size, Image.NEAREST)

        return canvas


# Character configurations
CHARACTERS = {
    'mario': {'sprite_id': 0, 'default_palette': [
        0xFF0000, 0xB50000, 0x7B0000, 0x3F0000,  # Reds
        0x5A3A08, 0x4A2A08, 0x3A1A08,            # Browns
        0x0000FF, 0x0000AA, 0x000066, 0x000033,  # Blues
        0xFFFFFF, 0xD0D0D0, 0xA0A0A0, 0x707070   # Grays/whites
    ]},
    'toadstool': {'sprite_id': 7, 'default_palette': [
        0xFF69B4, 0xFF1493, 0xDB7093, 0xC71585,  # Pinks
        0xFFFFE0, 0xFFFF00, 0xFFA500, 0xFF8C00,  # Yellows/oranges
        0xFFFFFF, 0xF0F0F0, 0xD0D0D0, 0xB0B0B0,  # Whites/grays
        0x8B4513, 0x654321, 0x3F2817              # Browns
    ]},
    'bowser': {'sprite_id': 13, 'default_palette': [
        0x228B22, 0x006400, 0x004400, 0x002200,  # Greens
        0xFFFF00, 0xFFD700, 0xFFA500, 0xFF8C00,  # Yellows/oranges
        0xFF0000, 0xB50000, 0x7B0000, 0x3F0000,  # Reds
        0xFFFFFF, 0xD0D0D0, 0xA0A0A0              # Whites/grays
    ]},
    'mallow': {'sprite_id': 19, 'default_palette': [
        0xFFFFFF, 0xF0F0F0, 0xE0E0E0, 0xD0D0D0,  # Whites
        0xFF69B4, 0xFF1493, 0xDB7093, 0xC71585,  # Pinks
        0x4169E1, 0x1E90FF, 0x00BFFF, 0x87CEEB,  # Blues
        0x8B4513, 0x654321, 0x3F2817              # Browns
    ]},
    'geno': {'sprite_id': 25, 'default_palette': [
        0x4169E1, 0x1E90FF, 0x00BFFF, 0x0000CD,  # Blues
        0x8B4513, 0x654321, 0x4A2A08, 0x3A1A08,  # Browns
        0xFFD700, 0xFFA500, 0xFF8C00, 0xDAA520,  # Golds/oranges
        0xFFFFFF, 0xF0F0F0, 0xD0D0D0              # Whites/grays
    ]},
}


def main():
    # Import sprites module
    from randomizer.data.sprites import sprites

    base_dir = '/home/pidge/code/smrpg_web_randomizer/randomizer/static/randomizer/images/palette_previews'

    for char_name, config in CHARACTERS.items():
        char_dir = os.path.join(base_dir, char_name)
        os.makedirs(char_dir, exist_ok=True)

        sprite_module = getattr(sprites, f'sprite_{config["sprite_id"]}')

        # Generate default
        default_path = os.path.join(char_dir, 'default.png')
        img = render_sprite_to_image(sprite_module, config['default_palette'], mold_index=0, scale=4)
        img.save(default_path, 'PNG')
        print(f"Generated: {default_path}")

        # Generate random (all black)
        random_path = os.path.join(char_dir, 'random.png')
        black_palette = [0x000000] * 15
        img = render_sprite_to_image(sprite_module, black_palette, mold_index=0, scale=4)
        img.save(random_path, 'PNG')
        print(f"Generated: {random_path}")

    print("\nDone! Generated default and random previews for all characters.")


if __name__ == '__main__':
    main()
