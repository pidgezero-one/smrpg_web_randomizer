"""Battle music ID overrides.

Writes a list of 8 selected music IDs into the battle music pointer
table at ROM $02:9F51. The list comes from
GameWorld.selected_music_ids. If the list is empty / falsy the
caller skips invoking this patch.
"""

from typing import Sequence


def get_patch(music_ids: Sequence[int]) -> dict[int, bytes]:
    if not music_ids:
        return {}
    return {0x029F51: bytes(music_ids)}
