"""Assemble the seed spoiler dictionary."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from randomizer.logic.mappings import (
    _compute_booster_hill_mapping,
    _compute_check_bit_mapping,
    _compute_npc_presence_mapping,
)
from randomizer.logic.spoiler.sections import (
    _get_locations_json,
    _get_palettes_json,
    _get_settings_json,
    _get_shops_json,
    _get_spell_character_assignments_json,
    _get_spell_learning_levels_json,
)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def build_spoiler(world: GameWorld) -> dict[str, Any]:
    check_mapping, room_bit_offsets, room_chest_counts = (
        _compute_check_bit_mapping(world)
    )
    npc_presence_mapping = _compute_npc_presence_mapping(world)
    booster_hill_mapping = _compute_booster_hill_mapping(world)
    result = {
        "settings": _get_settings_json(world),
        "locations": _get_locations_json(world),
        "shops": _get_shops_json(world),
        "palettes": _get_palettes_json(world),
        "spell_learning_levels": _get_spell_learning_levels_json(world),
        "spell_character_assignments": _get_spell_character_assignments_json(world),
        "password": world.password,
        "songs": [world.song_1, world.song_2, world.song_3],
        "check_bit_mapping": {
            name: {"addr": f"0x{addr:06X}", "bit": bit, "set_when_checked": swc}
            for name, (addr, bit, swc) in check_mapping.items()
        },
        "npc_presence_mapping": {
            name: {"addr": f"0x{addr:06X}", "bit": bit, "set_when_checked": swc}
            for name, (addr, bit, swc) in npc_presence_mapping.items()
        },
        "booster_hill_mapping": {
            name: {"threshold": threshold}
            for name, threshold in booster_hill_mapping.items()
        },
        "room_bit_offsets": {
            str(rid): off
            for rid, off in room_bit_offsets.items()
            if off > 0 or rid == 0
        },
        "room_chest_counts": {
            str(rid): cnt
            for rid, cnt in room_chest_counts.items()
            if cnt > 0
        },
    }
    if world.poison_mushroom_status:
        result["poison_mushroom_status"] = world.poison_mushroom_status
    return result


__all__ = ["build_spoiler"]
