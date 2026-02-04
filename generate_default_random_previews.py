#!/usr/bin/env python
"""Generate default and random palette preview images."""

import os
import sys
import django

# Setup Django
sys.path.insert(0, '/usr/src/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
django.setup()

from randomizer.utils.sprite_renderer import render_sprite_to_image
from randomizer.data.sprites import sprites
from PIL import Image

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

def generate_default_preview(char_name, config, output_path):
    """Generate default palette preview."""
    sprite_module = getattr(sprites, f'sprite_{config["sprite_id"]}')
    img = render_sprite_to_image(sprite_module, config['default_palette'], mold_index=0, scale=4)
    img.save(output_path, 'PNG')
    print(f"Generated: {output_path}")

def generate_random_preview(char_name, config, output_path):
    """Generate random (all-black silhouette) preview."""
    # Use all black for the palette to create silhouette
    black_palette = [0x000000] * 15
    sprite_module = getattr(sprites, f'sprite_{config["sprite_id"]}')
    img = render_sprite_to_image(sprite_module, black_palette, mold_index=0, scale=4)
    img.save(output_path, 'PNG')
    print(f"Generated: {output_path}")

def main():
    base_dir = '/usr/src/app/randomizer/static/randomizer/images/palette_previews'

    for char_name, config in CHARACTERS.items():
        char_dir = os.path.join(base_dir, char_name)
        os.makedirs(char_dir, exist_ok=True)

        # Generate default
        default_path = os.path.join(char_dir, 'default.png')
        generate_default_preview(char_name, config, default_path)

        # Generate random
        random_path = os.path.join(char_dir, 'random.png')
        generate_random_preview(char_name, config, random_path)

    print("\nDone! Generated default and random previews for all characters.")

if __name__ == '__main__':
    main()
