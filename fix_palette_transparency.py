#!/usr/bin/env python3
"""Fix palette preview images to use proper alpha channel instead of black transparency."""

from PIL import Image
import os
from pathlib import Path

def fix_image_transparency(image_path):
    """Convert image from indexed transparency to proper RGBA alpha channel."""
    img = Image.open(image_path)

    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        # If the image has transparency info, convert it properly
        if 'transparency' in img.info:
            img = img.convert('RGBA')
        else:
            # Just convert to RGBA (no transparency)
            img = img.convert('RGBA')

    # Save back to the same file
    img.save(image_path, 'PNG')
    print(f"Fixed: {image_path}")

def main():
    # Check if running in Docker container or host
    if os.path.exists('/usr/src/app'):
        base_dir = Path('/usr/src/app/randomizer/static/randomizer/images/palette_previews')
    else:
        base_dir = Path('/home/pidge/code/smrpg_web_randomizer/randomizer/static/randomizer/images/palette_previews')

    # Find all PNG files
    png_files = list(base_dir.rglob('*.png'))

    print(f"Found {len(png_files)} PNG files to process...")

    for png_file in png_files:
        try:
            fix_image_transparency(str(png_file))
        except Exception as e:
            print(f"Error processing {png_file}: {e}")

    print(f"\nDone! Processed {len(png_files)} images.")

if __name__ == '__main__':
    main()
