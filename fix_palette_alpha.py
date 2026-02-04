#!/usr/bin/env python3
"""Fix palette preview images to have fully opaque alpha channel."""

from PIL import Image
import numpy as np
import os
from pathlib import Path

def fix_image_alpha(image_path):
    """Set all pixels to fully opaque (alpha = 255)."""
    img = Image.open(image_path)

    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Convert to numpy array for easy manipulation
    data = np.array(img)

    # Set alpha channel to fully opaque (255) for all pixels
    data[:, :, 3] = 255

    # Convert back to PIL Image and save
    img_fixed = Image.fromarray(data, 'RGBA')
    img_fixed.save(image_path, 'PNG')

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
            fix_image_alpha(str(png_file))
        except Exception as e:
            print(f"Error processing {png_file}: {e}")

    print(f"\nDone! Processed {len(png_files)} images.")

if __name__ == '__main__':
    main()
