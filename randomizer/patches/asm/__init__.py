"""Raw ASM / byte-level ROM patches.

Each module in this package exposes a ``get_patch(...) -> dict[int, bytes]``
function returning a mapping of ROM offset to bytes that the caller passes
to ``Patch.add_dict``. Gameworld decides whether to call each module based
on flags / settings; the modules themselves are concerned only with
generating bytes.

Modules
-------

ASM hooks (multi-site / runtime-built):
    * :mod:`battle_intro_hdma_fix` — Order-gate the sprite-palette HDMA
      enable so it cannot bleed during the battle intro (the neon-block
      glitch).
    * :mod:`battlefield_underwater_palette` — Whitelist gate for the
      "+4 palette" path in BF14/BF34/BF38 so non-underwater monsters
      keep their normal colors.
    * :mod:`belome3_brooch` — Belome 3 spell-block + Enduring Brooch.
    * :mod:`exp_star_music_sticky` — Keep the EXP-star (Invincible Star)
      music overriding room BGM across room transitions when it is
      started via ``PlayMusicAtCurrentVolume``.
    * :mod:`invincibility_fix` — Red Essence dispel guard.
    * :mod:`overworld_ally_loader` — Hybrid per-slot character-index
      dispatch in the room-load ally loop: slot 0 keeps the protagonist
      invariant (forced to char 0), slots 1+ use real roster char ids
      so ``CHARACTER_IN_SLOT_2``/``_3`` cutscenes render the actual
      character. Helper lives in repurposed NOP space at ``$E42C``.
    * :mod:`packet_allocation` — Packet allowlist routine for NPC slots.

Always-on byte patches:
    * :mod:`key_item_inventory` — Expand key-item inventory size.
    * :mod:`battle_init` — Copy overworld party size to battle party size.
    * :mod:`star_piece_sprite_fix` — Credits ending sequence sprite ID.
    * :mod:`room_layouts` — Room area-layout records.
    * :mod:`room_174_battlefield` — Force Sea Enclave for room 174 fights.
    * :mod:`room_325_solidity` — Mushroom Kingdom doorway chest fix.
    * :mod:`sprite_group_whitelist` — Relocated engine sprite-group
      whitelist; restores the Green Yoshi entry alongside the
      alternate-protagonist entry (room 34 Yoshi-riding).
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
    battle_intro_hdma_fix,
    battlefield_underwater_palette,
    belome3_brooch,
    debug_fp,
    exp_star_music_sticky,
    hold_b,
    invincibility_fix,
    key_item_inventory,
    no_exp,
    non_mario_character,
    overworld_ally_loader,
    packet_allocation,
    rom_metadata,
    room_174_battlefield,
    room_325_solidity,
    room_layouts,
    selected_music,
    show_equips,
    sprite_group_whitelist,
    star_piece_sprite_fix,
    uncap_max_fp,
)

__all__ = [
    "battle_init",
    "battle_intro_hdma_fix",
    "battlefield_underwater_palette",
    "belome3_brooch",
    "debug_fp",
    "exp_star_music_sticky",
    "hold_b",
    "invincibility_fix",
    "key_item_inventory",
    "no_exp",
    "non_mario_character",
    "overworld_ally_loader",
    "packet_allocation",
    "rom_metadata",
    "room_174_battlefield",
    "room_325_solidity",
    "room_layouts",
    "selected_music",
    "show_equips",
    "sprite_group_whitelist",
    "star_piece_sprite_fix",
    "uncap_max_fp",
]
