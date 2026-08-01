"""Clear mold contents (delete tiles) from sprites 7-30 while preserving mold structure."""

from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

SPRITES_DIR = Path(settings.BASE_DIR) / "randomizer/data/sprites/objects"

def clear_tiles(content: str) -> str:
    """Delete all tiles from molds, replacing tiles=[...] with tiles=[]."""
    # Pattern to match tiles=[...] with any content inside, handling nested brackets
    # This is tricky because tiles can contain nested structures
    # We'll use a simpler approach: find "tiles=[" and then balance brackets

    result = []
    i = 0
    while i < len(content):
        # Look for "tiles=["
        if content[i:i+7] == "tiles=[":
            result.append("tiles=[]")
            # Skip past the opening bracket
            i += 7
            # Now we need to find the matching closing bracket
            bracket_depth = 1
            while i < len(content) and bracket_depth > 0:
                if content[i] == '[':
                    bracket_depth += 1
                elif content[i] == ']':
                    bracket_depth -= 1
                i += 1
            # Don't append the closing bracket, we already added "tiles=[]"
        else:
            result.append(content[i])
            i += 1

    return ''.join(result)


def main():
    for sprite_id in range(7, 31):  # 7 through 30 inclusive
        sprite_file = SPRITES_DIR / f"sprite_{sprite_id}.py"

        if not sprite_file.exists():
            print(f"Sprite {sprite_id}: File not found, skipping")
            continue

        content = sprite_file.read_text()
        new_content = clear_tiles(content)

        if content != new_content:
            sprite_file.write_text(new_content)
            print(f"Sprite {sprite_id}: Deleted all tiles from molds")
        else:
            print(f"Sprite {sprite_id}: No changes needed")



class Command(BaseCommand):
    help = 'Clear mold contents (delete tiles) from sprites 7-30 while preserving mold structure.'

    def handle(self, *args, **options):
        main()
