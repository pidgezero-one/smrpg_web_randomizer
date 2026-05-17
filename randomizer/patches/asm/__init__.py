"""Raw ASM / byte-level ROM patches.

Each module in this package exposes a ``get_patch(...) -> dict[int, bytes]``
function returning a mapping of ROM offset to bytes that the caller passes
to ``Patch.add_dict``. Gameworld decides whether to call each module based
on flags / settings; the modules themselves are concerned only with
generating bytes.

Modules
-------

ASM hooks (multi-site / runtime-built):
    * :mod:`battlefield_underwater_palette` — Whitelist gate for the
      "+4 palette" path in BF14/BF34/BF38 so non-underwater monsters
      keep their normal colors.
    * :mod:`battle_palette0_init` — JSL hook that zeros CGRAM palette 0
      at battle start so the intro doesn't show stale leftover colors.
    * :mod:`belome3_brooch` — Belome 3 spell-block + Enduring Brooch.
    * :mod:`invincibility_fix` — Red Essence dispel guard.
    * :mod:`packet_allocation` — Packet allowlist routine for NPC slots.

Always-on byte patches:
    * :mod:`key_item_inventory` — Expand key-item inventory size.
    * :mod:`battle_init` — Copy overworld party size to battle party size.
    * :mod:`star_piece_sprite_fix` — Credits ending sequence sprite ID.
    * :mod:`room_layouts` — Room area-layout records.
    * :mod:`room_174_battlefield` — Force Sea Enclave for room 174 fights.
    * :mod:`room_325_solidity` — Mushroom Kingdom doorway chest fix.
    * :mod:`rom_metadata` — ROM title + version text.

Flag-gated byte patches:
    * :mod:`no_exp` — Zero EXP table.
    * :mod:`show_equips` — Show equipped item bitmasks in menu.
    * :mod:`uncap_max_fp` — Uncap max FP from 99 to 255.
    * :mod:`selected_music` — Battle music ID overrides.
    * :mod:`hold_b` — Hold-B-to-advance dialog patch.
    * :mod:`debug_fp` — Starting FP override under debug mode.
    * :mod:`non_mario_character` — Starter / overworld / file-select
      sprite redirects when the player is not Mario.
"""

from . import (
    battle_init,
    battle_palette0_init,
    battlefield_underwater_palette,
    belome3_brooch,
    debug_fp,
    hold_b,
    invincibility_fix,
    key_item_inventory,
    no_exp,
    non_mario_character,
    packet_allocation,
    rom_metadata,
    room_174_battlefield,
    room_325_solidity,
    room_layouts,
    selected_music,
    show_equips,
    star_piece_sprite_fix,
    uncap_max_fp,
)

__all__ = [
    "battle_init",
    "battle_palette0_init",
    "battlefield_underwater_palette",
    "belome3_brooch",
    "debug_fp",
    "hold_b",
    "invincibility_fix",
    "key_item_inventory",
    "no_exp",
    "non_mario_character",
    "packet_allocation",
    "rom_metadata",
    "room_174_battlefield",
    "room_325_solidity",
    "room_layouts",
    "selected_music",
    "show_equips",
    "star_piece_sprite_fix",
    "uncap_max_fp",
]
