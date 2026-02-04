"""Generate special palette preview images (default and random silhouette)."""
import os
import sys

# Add parent directory to path to import randomizer modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from randomizer.utils.sprite_renderer import render_sprite_to_image
from randomizer.data.sprites import sprites

# Default palette colors extracted from sprite_palettes.py
DEFAULT_PALETTES = {
    'mario': [
        0xFFFFFF, 0xFFCE84, 0xC68C4A, 0xAD6B4A, 0x7B3931,
        0xEF4239, 0xFF0800, 0xB50800, 0x630000, 0x3939E7,
        0x0000DE, 0x000063, 0xE7DEDE, 0x9C8C8C, 0x181818,
    ],
    'toadstool': [
        0xFFFFFF, 0xFFEFB5, 0xE79C73, 0x9C5210, 0x522918,
        0xFF9CFF, 0xEF4AB5, 0xB52184, 0x730000, 0xFFD639,
        0xFF8C21, 0x3939D6, 0xD6CECE, 0x7B6B63, 0x181818,
    ],
    'bowser': [
        0xFFFFFF, 0xFFFF52, 0xF7CE31, 0xBD3910, 0x523918,
        0x39AD31, 0x217B21, 0x184A10, 0x212918, 0xCE8421,
        0x8C4A21, 0x211008, 0x949484, 0x636342, 0x181818,
    ],
    'geno': [
        0xFFFFFF, 0xF7DE63, 0xC68431, 0x844A18, 0x422910,
        0x00C6FF, 0x0094E7, 0x0073D6, 0x004A7B, 0xFFC600,
        0xFF5200, 0x6B2118, 0xB5A594, 0x6B6373, 0x181818,
    ],
    'mallow': [
        0xFFFFFF, 0xF7F794, 0xDEDE7B, 0xA5A55A, 0x423929,
        0xFF6BD6, 0x94294A, 0x5A2139, 0x310810, 0x29EFFF,
        0x1894BD, 0x105263, 0xA58C8C, 0x6B6B4A, 0x181818,
    ],
}

# Black palette for silhouette (all colors black)
BLACK_PALETTE = [0x000000] * 15

# Character sprite IDs
SPRITE_IDS = {
    'mario': 0,
    'toadstool': 7,
    'bowser': 13,
    'mallow': 19,
    'geno': 25,
}


def generate_default_palettes():
    """Generate default palette preview images."""
    print("Generating default palette previews...")

    for character, palette_colors in DEFAULT_PALETTES.items():
        sprite_id = SPRITE_IDS[character]
        sprite = getattr(sprites, f'sprite_{sprite_id}')

        # Output path
        output_dir = f'randomizer/static/randomizer/images/palette_previews/{character}'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'default.png')

        # Render sprite with default palette
        img = render_sprite_to_image(sprite, palette_colors, mold_index=0, scale=4)
        img.save(output_path, 'PNG')

        print(f'  ✓ Generated: {character}/default.png')


def generate_random_silhouettes():
    """Generate black silhouette images for Random option."""
    print("\nGenerating random silhouettes...")

    for character in DEFAULT_PALETTES.keys():
        sprite_id = SPRITE_IDS[character]
        sprite = getattr(sprites, f'sprite_{sprite_id}')

        # Output path
        output_dir = f'randomizer/static/randomizer/images/palette_previews/{character}'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'random.png')

        # Render sprite with all black colors
        img = render_sprite_to_image(sprite, BLACK_PALETTE, mold_index=0, scale=4)
        img.save(output_path, 'PNG')

        print(f'  ✓ Generated: {character}/random.png')


if __name__ == '__main__':
    generate_default_palettes()
    generate_random_silhouettes()
    print("\nDone! Generated 10 special palette preview images.")
