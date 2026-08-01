"""Business logic for custom prize location render methods.

This module contains the extracted business logic from custom render methods
in prizelocations.py, organized by location/area.
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING, Mapping, cast
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import Direction

from smrpgpatchbuilder.datatypes.levels.classes import VramStore
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_FixedFCoordOn)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import (NORTHWEST, SOUTHWEST)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_rows import (
    MARIO_PALETTE,
    NPC_PALETTE_ROW_1,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.palette_row import (
    PaletteRow,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)

from randomizer.logic.progression.prizes import (BowserRecruitmentPrize, GenoRecruitmentPrize, MallowRecruitmentPrize, MarioRecruitmentPrize, ToadstoolRecruitmentPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_Pause, A_SetSequenceSpeed, A_SetSpriteSequence, A_SetWalkingSpeed, A_JumpToHeight, A_WalkSouthwestSteps, A_PlaySound)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    NORMAL, FAST
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (ActionQueueAsync, ActionQueueSync, PaletteSet, PaletteSetMorphs)
from ..data.variables.event_palette_names import (
    EPAL0084_MARIO_ENDING,
    EPAL0085_MALLOW_ENDING,
    EPAL0086_GENO_ENDING,
    EPAL0140_BOWSER_ENDING,
    EPAL0141_TOADSTOOL_ENDING,
    EPAL0163_MARIO_ENDING_DARK,
    EPAL0164_TOADSTOOL_ENDING_DARK,
    EPAL0165_BOWSER_ENDING_DARK,
    EPAL0166_MALLOW_ENDING_DARK,
    EPAL0167_GENO_ENDING_DARK,
)

from ..data.variables.room_names import (R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION, R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, R292_UNMAPPED_HOUSE_ROOM, R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR, R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE)
from ..data.variables.overworld_sfx_names import *
from smrpgpatchbuilder.datatypes.levels.classes import NPC as NPCBase
from ..data.rooms.npcs import (
    BOWSER_DOLL_NPC,
    MALLOW_DOLL_NPC,
    MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE_NPC,
    MARIO_WALKING_DOWN_LEFT_NPC,
    TOADSTOOL_DOLL_NPC,
)
from ..types.prize import (BossFightPrize, CharacterPrize)
from ..types.prizelocation import (AllyNPCSub)
from ..utils.event_script_snippets.es_mimic_rise import get_mimic_rise_dojo
from ..types.ally import Ally, SpriteAnimationState
from ..data.variables.sprite_names import SPR0031_ALT_PROTAGONIST_1
from ..data.variables.event_script_names import (
        E3885_END_GAME,
        E3950_POST_FINAL_BOSS_INIT,
        E3951_STAR_PIECE_CREDITS_INIT,
    )
from ..data.overworld_scripts.event.scripts import (
        script_3885,
        script_3950,
        script_3951,
    )
from randomizer.logic.progression.prizes import (
        PandoriteBossFight,
        HidonBossFight,
        BoxBoyBossFight,
        ChesterBossFight,
    )

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld


def update_ally_animation(
    seq: A_SetSpriteSequence,
    ally: Ally,
    anim: SpriteAnimationState,
    *,
    use_primary: bool = False,
) -> None:
    """Update an ally animation sequence command with the given animation.

    If no animation is provided, replace the command with a face direction
    command instead.
    """
    sprites = ally._sprites_primary if use_primary else ally._sprites_secondary
    data = sprites[anim]
    seq.set_is_mold(data[2])
    seq.set_index(data[1])
    seq.set_sprite_offset(data[0])


# =============================================================================
# Bandits Way
# =============================================================================


# =============================================================================
# Forest Maze
# =============================================================================


    


# =============================================================================
# Booster Tower
# =============================================================================


        


# =============================================================================
# Marrymore
# =============================================================================


# NPC fills for each ending-cutscene render. Each AllyNPCSub here points at an
# NPC in an ending-cutscene room (e.g. R496, R088) that should be replaced with
# the chosen character's overworld model. These are populated independently of
# the recruitment location's own _npc_fills.
_ENDING_CHARACTER_1_NPC_FILLS: list[AllyNPCSub] = [
    # Protagonist's Mario-NPC slot stays Mario (sprite 0) for Mario protagonist
    # and is cosmetics-remapped to sprite 31 for non-Mario protagonists, so no
    # NPC model swap is needed here.
]

_ENDING_CHARACTER_2_NPC_FILLS: list[AllyNPCSub] = [
    # R496/R088/R375 entries removed — those rooms have a Mario NPC at the
    # front and recruits stay at their native slots (no model swap). Only
    # R269 keeps the model-swap for its single Prince Mallow scene.
    AllyNPCSub(R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, NPC_0),
]

_ENDING_CHARACTER_3_NPC_FILLS: list[AllyNPCSub] = [
    # R496/R088/R375 entries removed — see _ENDING_CHARACTER_2_NPC_FILLS comment.
]

# NPCs that should be replaced with the doll variant matching the chosen
# character in the Forest Maze ending cutscene (render_ending_character_3).
# Geno is intentionally absent from the doll mapping below — render_ending_character_3
# returns early when the prize is GenoRecruitmentPrize, so these substitutions
# are never applied for Geno. R375 doll lives at NPC_4 (between Geno=NPC_3
# and Bowser=NPC_6) so its palette is engine-assigned implicitly.
_ENDING_CHARACTER_3_DOLL_FILLS: list[AllyNPCSub] = [
    # AllyNPCSub(R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, NPC_23),
    AllyNPCSub(R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION, NPC_4),
    AllyNPCSub(R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, NPC_4),
]

_ENDING_CHARACTER_4_NPC_FILLS: list[AllyNPCSub] = [
    # R496/R088/R375 entries removed — see _ENDING_CHARACTER_2_NPC_FILLS comment.
    AllyNPCSub(R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR, NPC_7),
    AllyNPCSub(R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR, NPC_8),
]

_ENDING_CHARACTER_5_NPC_FILLS: list[AllyNPCSub] = [
    # R496/R088/R375 entries removed — see _ENDING_CHARACTER_2_NPC_FILLS comment.
]


# =============================================================================
# R496 ending cutscene: role/coord-swap (replaces NPC model swap)
# =============================================================================
# Each character has a permanent NPC slot in R496. The cutscene script targets
# the script's vanilla-role NPC slots (MARRYMORE_CHARACTER=NPC_20,
# MWAY_CHARACTER=NPC_21, FOREST_CHARACTER=NPC_22, MINES_CHARACTER=NPC_24,
# MARIO=protagonist). At apply time we walk script_3885 and retarget each
# role's NPC reference to whichever character's native slot now plays that
# role. Sprite models are NOT swapped (avoiding partition VRAM-overflow
# issues from mismatched sprite sizes).
#
# R496 NPC layout (Mario placed before the recruits so he allocates first
# in the dynamic VRAM region):
#   NPC_19 = Mario  (sprite 0 always)
#   NPC_20 = Peach
#   NPC_21 = Mallow
#   NPC_22 = Geno
#   NPC_23 = Geno doll  (model-swapped per forest character via _ENDING_CHARACTER_3_DOLL_FILLS)
#   NPC_24 = Bowser

R496_NATIVE_SLOT_FOR_PRIZE: dict[type, AreaObject] = {
    MarioRecruitmentPrize:     NPC_19,
    ToadstoolRecruitmentPrize: NPC_20,
    MallowRecruitmentPrize:    NPC_21,
    GenoRecruitmentPrize:      NPC_22,
    BowserRecruitmentPrize:    NPC_24,
}

# Native (x, y, z, direction) per role in R496. Each role-character's NPC slot
# moves to that role's coord, so the visible character at e.g. Mario's coord is
# always whoever is currently the protagonist.
_R496_COORDS = {
    "protagonist":  (4, 48, 0, SOUTHWEST),
    "marrymore":    (6, 12, 0, SOUTHWEST),
    "mushroom_way": (6, 14, 0, SOUTHWEST),
    "forest_maze":  (6, 16, 0, SOUTHWEST),
    "inner_mines":  (6, 20, 0, SOUTHWEST),
}

# R292 — second-half of the R496 ending cutscene (post-RunStarPieceSequence).
# NPC IDs match R496 exactly so script_3885 references resolve consistently
# across the EnterArea(R292) transition.
R292_NATIVE_SLOT_FOR_PRIZE: dict[type, AreaObject] = {
    MarioRecruitmentPrize:     NPC_19,
    ToadstoolRecruitmentPrize: NPC_20,
    MallowRecruitmentPrize:    NPC_21,
    GenoRecruitmentPrize:      NPC_22,
    BowserRecruitmentPrize:    NPC_24,
}
_R292_COORDS = dict(_R496_COORDS)

# R088 (script_3950 / E3950_POST_FINAL_BOSS_INIT). Bowser moved to last object
# slot (NPC_8); a new GENO_ENDING NPC inserted at NPC_5 anchors palette row 4
# next to the doll at NPC_4.
R88_NATIVE_SLOT_FOR_PRIZE: dict[type, AreaObject] = {
    MarioRecruitmentPrize:     NPC_0,
    ToadstoolRecruitmentPrize: NPC_1,
    MallowRecruitmentPrize:    NPC_3,
    GenoRecruitmentPrize:      NPC_5,
    BowserRecruitmentPrize:    NPC_8,
}
_R88_COORDS = {
    "protagonist":  (5, 90, 0, NORTHWEST),
    "marrymore":    (5, 90, 0, NORTHWEST),
    "mushroom_way": (6, 92, 0, NORTHWEST),
    "inner_mines":  (4, 93, 0, NORTHWEST),
    # forest character is removed before fade-in; coord doesn't matter
}

# R375 (script_3951 / E3951_STAR_PIECE_CREDITS_INIT). Layout reads
# Mario/Peach/Mallow/Geno/Doll/GenoRedemption/Bowser; the doll sits between
# Geno (NPC_3) and Bowser (NPC_6) so its palette is implicitly assigned by
# the engine — see _apply_r375_protagonist_palette_rows.
R375_NATIVE_SLOT_FOR_PRIZE: dict[type, AreaObject] = {
    MarioRecruitmentPrize:     NPC_0,
    ToadstoolRecruitmentPrize: NPC_1,
    MallowRecruitmentPrize:    NPC_2,
    GenoRecruitmentPrize:      NPC_3,
    BowserRecruitmentPrize:    NPC_6,
}
_R375_COORDS = {
    "protagonist":  (5, 91, 0, NORTHWEST),
    "marrymore":    (5, 91, 0, NORTHWEST),
    "mushroom_way": (6, 93, 0, NORTHWEST),
    "inner_mines":  (5, 94, 0, NORTHWEST),
}


def _retarget_event_script_targets(
    contents,
    target_map: dict,
    *,
    skip_identifiers: frozenset[str] = frozenset(),
) -> None:
    """Recursively walk an event-script command list (and ActionQueue subscripts)
    and replace each command's `target` according to target_map. Commands
    whose `identifier` is in skip_identifiers are left untouched.
    """
    iterable = contents if isinstance(contents, list) else getattr(contents, "contents", [])
    for cmd in iterable:
        ident = getattr(cmd, "identifier", None)
        ident_label = getattr(ident, "label", None) if ident is not None else None
        if ident_label not in skip_identifiers:
            cmd_target = getattr(cmd, "target", None)
            if cmd_target is not None and cmd_target in target_map:
                cmd.set_target(target_map[cmd_target])
        sub = getattr(cmd, "subscript", None)
        if sub is not None:
            _retarget_event_script_targets(
                sub, target_map, skip_identifiers=skip_identifiers
            )


def _make_protagonist_sprite_31_variant(
    base: NPCBase, directions: VramStore | None = None
) -> NPCBase:
    """Return a copy of `base` with sprite_id set to SPR0031_ALT_PROTAGONIST_1.

    Sprite 31 is the post-cosmetics protagonist sprite; the cosmetics layer
    overwrites sprites 31-37 with the protagonist character's full animation
    set, so any NPC slot using sprite 31 has access to the same animations
    as the protagonist. We use this on the protagonist's native slot when
    the protagonist is not Mario, so the recruit-only sprite at that slot
    is replaced with the full protagonist sprite.

    Pass `directions` (e.g. VramStore.DIR4_ALL_DIRECTIONS) to also override
    the VRAM-store directions; defaults to copying base's existing value.
    """
    return NPCBase(
        sprite_id=SPR0031_ALT_PROTAGONIST_1,
        shadow_size=base.shadow_size,
        acute_axis=base.acute_axis,
        obtuse_axis=base.obtuse_axis,
        height=base.height,
        y_shift=base.y_shift,
        show_shadow=base.show_shadow,
        directions=directions if directions is not None else base.directions,
        min_vram_size=base.min_vram_size,
        priority_0=base.priority_0,
        priority_1=base.priority_1,
        priority_2=base.priority_2,
        cannot_clone=base.cannot_clone,
        extra_palette_source_offset=base.extra_palette_source_offset,
        extra_palette_row_count=base.extra_palette_row_count,
        byte5_bit6=base.byte5_bit6,
        byte5_bit7=base.byte5_bit7,
        byte6_bit2=base.byte6_bit2,
    )


def _swap_room_npc_coords(
    world: GameWorld,
    room_id: int,
    role_slots: "dict[str, AreaObject]",
    coords: "Mapping[str, tuple[int, int, int, Direction]]",
) -> None:
    """Move each role's NPC slot to that role's native (x, y, z, direction)."""
    room = world.rooms._rooms[room_id]
    if room is None:
        return
    for role, slot in role_slots.items():
        c = coords.get(role)
        if c is None:
            continue
        obj = room.get_npc_by_target_id(slot)
        if obj is None:
            continue
        x, y, z, direction = c
        obj.set_x(x)
        obj.set_y(y)
        obj.set_z(z)
        obj.set_direction(direction)


def _apply_overworld_character_sprite_swap(
    world: GameWorld,
    room_id: int,
    slot_for_prize: "dict[type, AreaObject]",
) -> None:
    """Swap the overworld character's NPC slot to sprite 31.

    Cosmetics writes sprite 31-37 with the **overworld character**'s sprite
    data (driven by `world.overworld_character.ally`, which is StartingCharacter1
    by default). Whichever NPC slot belongs to that character — Toadstool's,
    Mallow's, Geno's, or Bowser's — needs to render via sprite 31 so its
    cosmetic data lands. The cutscene "protagonist" role is unrelated; that
    role can be played by any character.

    No-op for Mario, since Mario's slot already uses sprite 0 and cosmetics
    doesn't remap it.

    Also reduces Mario's NPC slot's VRAM-store directions to DIR0_SWSE_NWNE
    when the overworld character isn't Mario, since Mario's slot won't run
    the full DIR4 animation set.
    """
    ally_index = world.overworld_character.ally.index
    if ally_index == 0:
        return  # Mario — no swap needed
    ally_index_to_prize_class: dict[int, type[CharacterPrize]] = {
        1: ToadstoolRecruitmentPrize,
        2: BowserRecruitmentPrize,
        3: GenoRecruitmentPrize,
        4: MallowRecruitmentPrize,
    }
    overworld_prize_class = ally_index_to_prize_class[ally_index]
    overworld_slot = slot_for_prize[overworld_prize_class]
    mario_slot = slot_for_prize[MarioRecruitmentPrize]

    room = world.rooms._rooms[room_id]
    if room is None:
        return
    overworld_obj = room.get_npc_by_target_id(overworld_slot)
    if overworld_obj is not None:
        overworld_obj._npc = _make_protagonist_sprite_31_variant(
            overworld_obj._npc, directions=VramStore.DIR4_ALL_DIRECTIONS
        )
    mario_obj = room.get_npc_by_target_id(mario_slot)
    if mario_obj is not None:
        mario_obj._npc = _swap_npc_directions(
            mario_obj._npc, VramStore.DIR0_SWSE_NWNE
        )


def _swap_npc_directions(base: NPCBase, directions: VramStore) -> NPCBase:
    """Return a copy of `base` with the given VramStore directions value."""
    return NPCBase(
        sprite_id=base.sprite_id,
        shadow_size=base.shadow_size,
        acute_axis=base.acute_axis,
        obtuse_axis=base.obtuse_axis,
        height=base.height,
        y_shift=base.y_shift,
        show_shadow=base.show_shadow,
        directions=directions,
        min_vram_size=base.min_vram_size,
        priority_0=base.priority_0,
        priority_1=base.priority_1,
        priority_2=base.priority_2,
        cannot_clone=base.cannot_clone,
        extra_palette_source_offset=base.extra_palette_source_offset,
        extra_palette_row_count=base.extra_palette_row_count,
        byte5_bit6=base.byte5_bit6,
        byte5_bit7=base.byte5_bit7,
        byte6_bit2=base.byte6_bit2,
    )


def _apply_ending_cutscene_assignments(
    world: GameWorld,
    *,
    marrymore_prize: CharacterPrize,
    mushroom_way_prize: CharacterPrize,
    forest_maze_prize: CharacterPrize,
    inner_mines_prize: CharacterPrize,
    protagonist_prize: CharacterPrize,
) -> None:
    """Per-seed ending-cutscene plumbing for R496/R088/R375.

    For each of the three rooms:
      1. Rebuild the cutscene event script via its `build_contents` factory,
         passing the role NPC slots so script-internal references resolve to
         the right NPC for whichever character now plays each role.
      2. Move each character's NPC slot to its role's native (x, y, z,
         direction) so the cutscene visuals line up.
      3. When the protagonist isn't Mario, swap that NPC's sprite_id to
         sprite 31 and grow its VRAM directions to DIR4_ALL_DIRECTIONS;
         reduce the Mario NPC's directions to DIR0_SWSE_NWNE so its VRAM
         footprint stays compact.

    Per-character "native NPC slot" is the slot that always renders that
    character's model regardless of cutscene role. The slot is moved to a
    role-specific coord so the same slot can play different roles per seed.
    """
    # =========================================================================
    # TOGGLE: bump R292 forest NPC min_vram_size to 1.
    # Set True to apply, False to skip. R496 forest is bumped unconditionally
    # below; this flag only gates the R292 bump (which we currently leave off
    # because R292's cannot_clone budget is tight and the bump can push
    # NPC_24/Bowser into the spinning-stars buffer).
    # =========================================================================
    R292_FOREST_MIN_VRAM_BUMP = True
    # =========================================================================


    rooms = (
        (
            R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
            R496_NATIVE_SLOT_FOR_PRIZE,
            _R496_COORDS,
            E3885_END_GAME,
            script_3885.build_contents,
            ("marrymore", "mushroom_way", "forest_maze", "inner_mines"),
        ),
        # R292 shares script_3885 with R496 (same E3885_END_GAME). Re-running
        # build_contents is idempotent — the second call overwrites with the
        # same content. The coord-swap and sprite-31 logic must apply to R292
        # too so the post-RunStarPieceSequence half of the cutscene renders
        # correctly after EnterArea(R292).
        (
            R292_UNMAPPED_HOUSE_ROOM,
            R292_NATIVE_SLOT_FOR_PRIZE,
            _R292_COORDS,
            E3885_END_GAME,
            script_3885.build_contents,
            ("marrymore", "mushroom_way", "forest_maze", "inner_mines"),
        ),
        (
            R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
            R88_NATIVE_SLOT_FOR_PRIZE,
            _R88_COORDS,
            E3950_POST_FINAL_BOSS_INIT,
            script_3950.build_contents,
            ("marrymore", "mushroom_way", "inner_mines"),  # forest is removed in 3950
        ),
        (
            R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
            R375_NATIVE_SLOT_FOR_PRIZE,
            _R375_COORDS,
            E3951_STAR_PIECE_CREDITS_INIT,
            script_3951.build_contents,
            ("marrymore", "mushroom_way", "inner_mines"),  # forest is removed in 3951
        ),
    )

    for (
        room_id,
        slot_for_prize,
        coords,
        script_id,
        build_contents,
        coord_roles,
    ) in rooms:
        protagonist_slot = slot_for_prize[type(protagonist_prize)]
        marrymore_slot = slot_for_prize[type(marrymore_prize)]
        mway_slot = slot_for_prize[type(mushroom_way_prize)]
        forest_slot = slot_for_prize[type(forest_maze_prize)]
        mines_slot = slot_for_prize[type(inner_mines_prize)]
        mario_slot = slot_for_prize[MarioRecruitmentPrize]

        # 1. Rebuild script and replace contents in-place.
        new_contents = build_contents(
            protagonist=protagonist_slot,
            marrymore=marrymore_slot,
            mway=mway_slot,
            forest=forest_slot,
            mines=mines_slot,
        )
        world.event_scripts.get_script_by_id(script_id).set_contents(new_contents)

        # 2. Coord swap. Compose role → slot only for roles this room cares
        # about; protagonist always gets coord-swapped too.
        full_role_to_slot: dict[str, AreaObject] = {
            "protagonist":  protagonist_slot,
            "marrymore":    marrymore_slot,
            "mushroom_way": mway_slot,
            "forest_maze":  forest_slot,
            "inner_mines":  mines_slot,
        }
        active_role_slots = {
            r: full_role_to_slot[r]
            for r in ("protagonist",) + coord_roles
        }
        _swap_room_npc_coords(world, room_id, active_role_slots, coords)

        # 3. Sprite 31 swap on the OVERWORLD CHARACTER's NPC slot. Cosmetics
        # has written that character's sprite data to sprite 31, so it must
        # be the slot belonging to the overworld character — not whatever
        # the cutscene's protagonist role happens to be (those can differ).
        _apply_overworld_character_sprite_swap(world, room_id, slot_for_prize)

        # 4. Bump min_vram_size on the slot whose role uses sprite_offset alt
        # sprites. Adds one 16-subtile row so the alt sprite molds fit when
        # the base character's sprite is gridplane-only (e.g. Toadstool's
        # sprite 7) and the slot's tilemap allocation would otherwise be 0
        # subtiles per direction.
        #   R496: forest role (spell frames pre-sequence). Always applied.
        #   R292: forest role (victory_pose post-sequence). Gated by toggle.
        #   R088: mines role (shocked_bwd sprite_offset=1) by default.
        #     Special case: if mines is Bowser, his NPC default is already
        #     min_vram_size=1 — bumping is a no-op. Bump the marrymore slot
        #     instead so its sprite_offset=1 frames have headroom too.
        #     Note: the cannot_clone region in R088 is tight; this bump is
        #     only safe because NPC_2 (Sparkle) is now cannot_clone=False,
        #     freeing space that the bump's growth consumes.
        #   R375: no bump (no sprite_offset alts in that cutscene).
        bump_slot: AreaObject | None = None
        if room_id == R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE:
            bump_slot = forest_slot
        elif room_id == R292_UNMAPPED_HOUSE_ROOM and R292_FOREST_MIN_VRAM_BUMP:
            bump_slot = forest_slot
        elif room_id == R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION:
            if isinstance(inner_mines_prize, BowserRecruitmentPrize):
                bump_slot = marrymore_slot
            else:
                bump_slot = mines_slot

        if bump_slot is not None:
            room = world.rooms._rooms[room_id]
            if room is not None:
                obj = room.get_npc_by_target_id(bump_slot)
                if obj is not None:
                    obj.set_min_vram_size(1)

        # 5. Palette-collision fix (Geno protagonist only, R292 only). The
        # hardcoded Geno doll (NPC_7) carries Geno's palette. When Geno is the
        # overworld protagonist, the doll dedups against the protagonist in
        # R292's OBJ palette-row arrangement, so the star-piece ("glow") palette
        # lands one row off and the spinning stars render with the wrong palette.
        # Swap the doll to a Peach doll: Peach is always present in this
        # cutscene, so this only rearranges existing palette rows (adds no new
        # palette) and restores the row the star piece expects. Only R292 needs
        # it — the spinning stars live in R292's half of the cutscene.
        if room_id == R292_UNMAPPED_HOUSE_ROOM and isinstance(
            world.overworld_character, GenoRecruitmentPrize
        ):
            r292 = world.rooms._rooms[room_id]
            if r292 is not None:
                doll_obj = r292.get_npc_by_target_id(NPC_7)
                if doll_obj is not None:
                    doll_obj._npc = TOADSTOOL_DOLL_NPC


def _doll_for_prize(prize: CharacterPrize) -> NPCBase | None:
    """Return the doll NPC matching `prize` for the render_ending_character_3
    cutscene, or None if no doll variant exists for this character."""
    if isinstance(prize, MallowRecruitmentPrize):
        return MALLOW_DOLL_NPC
    if isinstance(prize, BowserRecruitmentPrize):
        return BOWSER_DOLL_NPC
    if isinstance(prize, ToadstoolRecruitmentPrize):
        return TOADSTOOL_DOLL_NPC
    if isinstance(prize, MarioRecruitmentPrize):
        return MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE_NPC
    return None


def _apply_ending_character_npc_fills(
    world: GameWorld, prize: CharacterPrize, fills: list[AllyNPCSub]
) -> None:
    """Replace each NPC listed in `fills` with the model corresponding to `prize`.

    Mirrors the AllyNPCSub loop in CharacterRecruitmentLocation.render() so
    that ending-cutscene rooms can be populated with the chosen character
    independently of the recruitment location's own _npc_fills.

    For MarioRecruitmentPrize, MARIO_WALKING_DOWN_LEFT_NPC is used instead of
    `prize.character_model.base` (which would resolve to the SPR0409_MARIO_CLONE
    sprite). The clone sprite uses sprite_offset shifts that crash in many
    cutscene contexts; MARIO_WALKING_DOWN_LEFT_NPC uses the protagonist sprite
    (0) and avoids that problem."""
    if isinstance(prize, MarioRecruitmentPrize):
        model = MARIO_WALKING_DOWN_LEFT_NPC
    else:
        model = prize.character_model.base
    for npc_sub in fills:
        room = world.rooms._rooms[npc_sub.room_id]
        if room is None:
            raise ValueError(
                f"Room ID {npc_sub.room_id} not found while applying ending character NPC fills."
            )
        obj = room.get_npc_by_target_id(npc_sub.npc_id)
        if obj is None:
            raise ValueError(
                f"NPC ID {npc_sub.npc_id} not found in room {npc_sub.room_id} while applying ending character NPC fills."
            )
        obj._npc = model


def _apply_ending_character_3_doll_fills(
    world: GameWorld, prize: CharacterPrize, fills: list[AllyNPCSub]
) -> None:
    """Replace each NPC listed in `fills` with the doll variant matching `prize`."""
    doll = _doll_for_prize(prize)
    if doll is None:
        return
    for npc_sub in fills:
        room = world.rooms._rooms[npc_sub.room_id]
        if room is None:
            raise ValueError(
                f"Room ID {npc_sub.room_id} not found while applying ending character 3 doll fills."
            )
        obj = room.get_npc_by_target_id(npc_sub.npc_id)
        if obj is None:
            raise ValueError(
                f"NPC ID {npc_sub.npc_id} not found in room {npc_sub.room_id} while applying ending character 3 doll fills."
            )
        obj._npc = doll


def render_ending_character_1(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    """Apply animation/sprite changes for the protagonist's NPC slot in the
    ending cutscenes (the Mario-NPC slot at the front of R088/R375/R496).

    For Mario protagonist this is a no-op — the script source already hardcodes
    Mario's correct mold (index=23, sprite_offset=2). For non-Mario protagonists
    the cosmetics layer remaps sprite 31 to the protagonist character's full
    sprite, so the LEAN_BACK mold-id refs in script_3885 must come from
    `_sprites_primary` (the protagonist character's full sprite data).
    """
    if isinstance(prize, MarioRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_1_NPC_FILLS)
    ally = prize.ally
    # The protagonist's NPC slot is rendered through sprite 31 = the cosmetics-
    # remapped full protagonist sprite, so always use _sprites_primary here.
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    a0 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_protag_lean_back_1_aq",
        "ending_protag_lean_back_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a0, ally, SpriteAnimationState.LEAN_BACK, use_primary=use_primary
    )
    a1 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_protag_lean_back_2_aq",
        "ending_protag_lean_back_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.LEAN_BACK, use_primary=use_primary
    )
    a2 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_protag_look_at_doll_aq",
        "ending_protag_look_at_doll",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.LOOK_AT_DOLL, use_primary=use_primary
    )


def render_ending_character_2(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    if isinstance(prize, MallowRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_2_NPC_FILLS)
    ally = prize.ally
    # use_primary: Mario always uses sprite 0 (_sprites_primary). Non-Mario
    # protagonists use sprite 31 in their R496 slot, which also has full
    # protagonist data → also _sprites_primary. Recruits with their native
    # sprite use _sprites_secondary.
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    a0 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_1",
        "ending_prince_aq_1_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a0, ally, SpriteAnimationState.PRINCE_NEUTRAL, use_primary=use_primary
    )
    a1 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.PRINCE_DOWN, use_primary=use_primary
    )
    a2 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.PRINCE_NEUTRAL, use_primary=use_primary
    )
    a3 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_3",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a3, ally, SpriteAnimationState.PRINCE_LEFT, use_primary=use_primary
    )
    a4 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_4",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a4, ally, SpriteAnimationState.PRINCE_NEUTRAL, use_primary=use_primary
    )
    a5 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_5",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.PRINCE_JOY, use_primary=use_primary
    )
    a6 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_looks_south_aq",
        "ending_mway_character_looks_south",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a6, ally, SpriteAnimationState.LOOK_TO_DOWN, use_primary=use_primary
    )
    a7 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_looks_down_aq",
        "ending_mway_character_looks_down",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.LOOKING_DOWN, use_primary=use_primary
    )
    a8 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_shocked_fwd_aq",
        "ending_mway_character_shocked_fwd",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a8, ally, SpriteAnimationState.SHOCKED_SHADOW, use_primary=use_primary
    )
    a9 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_look_down_2_aq",
        "ending_mway_character_look_down_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a9, ally, SpriteAnimationState.LOOKING_DOWN, use_primary=use_primary
    )
    a10 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_sees_geno_aq",
        "ending_mway_character_sees_geno",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a10, ally, SpriteAnimationState.SEES_GENO, use_primary=use_primary
    )
    a11 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_geno_joy_aq",
        "ending_mway_character_geno_joy",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a11, ally, SpriteAnimationState.JOY, use_primary=use_primary
    )


def render_ending_character_3(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    if isinstance(prize, GenoRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_3_NPC_FILLS)
    _apply_ending_character_3_doll_fills(world, prize, _ENDING_CHARACTER_3_DOLL_FILLS)
    ally = prize.ally
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "ending_doll_aq_a",
        "ending_doll_",
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "ending_doll_cliff_seq_aq",
        "ending_doll_cliff_seq",
    )
    a0 = world.action_scripts.get_command_by_identifier(
        "ending_forest_char_spin",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a0, ally, SpriteAnimationState.SPIN, use_primary=use_primary
    )
    # a1 = world.event_scripts.get_subscript_command_by_identifier(
    #     "ending_mway_character_geno_joy_aq",
    #     "ending_mway_character_geno_joy",
    #     A_SetSpriteSequence,
    # )
    # update_ally_animation(
    #     a1, ally, SpriteAnimationState.JOY, use_primary=use_primary
    # )
    a2 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frame_3_aq",
        "ending_geno_palette_spell_frame_3",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.SPELL_FRAME_3, use_primary=use_primary
    )
    a3 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frames_aq",
        "ending_geno_palette_spell_frame_3_",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a3, ally, SpriteAnimationState.SPELL_FRAME_3, use_primary=use_primary
    )
    a4 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frames_aq",
        "ending_geno_palette_spell_frame_4",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a4, ally, SpriteAnimationState.SPELL_FRAME_4, use_primary=use_primary
    )
    a5 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frames_aq",
        "ending_geno_palette_spell_frame_5",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.SPELL_FRAME_5, use_primary=use_primary
    )
    a6 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frames_aq",
        "ending_geno_palette_spell_frame_6",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a6, ally, SpriteAnimationState.SPELL_FRAME_6, use_primary=use_primary
    )
    a7 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_looks_down_aq",
        "ending_geno_palette_looks_down",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a8 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_victory_pose_aq",
        "ending_geno_palette_victory_pose",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a8, ally, SpriteAnimationState.VICTORY_POSE, use_primary=use_primary
    )


def render_ending_character_4(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    if isinstance(prize, BowserRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_4_NPC_FILLS)
    ally = prize.ally
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    a0 = world.action_scripts.get_command_by_identifier(
        "mines_character_hammering",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a0, ally, SpriteAnimationState.HAMMER, use_primary=use_primary
    )
    a1 = world.action_scripts.get_command_by_identifier(
        "mines_character_hammering_stop",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.HAMMER_STATIC, use_primary=use_primary
    )
    a2 = world.action_scripts.get_command_by_identifier(
        "mines_character_hammering_look_away",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.DISTRACTED, use_primary=use_primary
    )
    a3 = world.action_scripts.get_command_by_identifier(
        "mines_character_hammering_mad",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a3, ally, SpriteAnimationState.DISPLEASED, use_primary=use_primary
    )
    a4 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_looks_left_aq",
        "ending_mines_character_looks_left",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a4, ally, SpriteAnimationState.LOOK_TO_SIDE_BEHIND, use_primary=use_primary
    )
    a5 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_looks_down_aq",
        "ending_mines_character_looks_down",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a6 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_shocked_bwd_aq",
        "ending_mines_character_shocked_bwd",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a6, ally, SpriteAnimationState.SHOCKED_SHADOW_BACKWARDS, use_primary=use_primary
    )
    a7 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_look_down_2_aq",
        "ending_mines_character_look_down_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a8 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_lean_2_aq",
        "ending_mines_character_lean_2_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a8, ally, SpriteAnimationState.LEAN_BACK, use_primary=use_primary
    )
    a9 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_lean_2_aq",
        "ending_mines_character_lean_2_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a9, ally, SpriteAnimationState.LEAN_BACK_2, use_primary=use_primary
    )
    a10 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_looks_upward_aq",
        "ending_mines_character_looks_upward",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a10, ally, SpriteAnimationState.DISTRACTED, use_primary=use_primary
    )
    a11 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_raised_arms_aq",
        "ending_mines_character_raised_arms",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a11, ally, SpriteAnimationState.JOY_BEHIND, use_primary=use_primary
    )


def render_ending_character_5(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    if isinstance(prize, ToadstoolRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_5_NPC_FILLS)
    ally = prize.ally
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    a23 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_looks_north_aq",
        "ending_mmr_character_looks_north",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a23, ally, SpriteAnimationState.DISTRACTED, use_primary=use_primary
    )
    a24 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_looks_down_aq",
        "ending_mmr_character_looks_down",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a24, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a25 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_shocked_bwd_aq",
        "ending_mmr_character_shocked_bwd",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a25, ally, SpriteAnimationState.SHOCKED_SHADOW_BACKWARDS, use_primary=use_primary
    )
    a26 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_lean_far_aq",
        "ending_mmr_character_lean_far",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a26, ally, SpriteAnimationState.LEAN_BACK_2, use_primary=use_primary
    )
    a27 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_marrymore_char_look_down_2_aq",
        "ending_marrymore_char_look_down_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a27, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a28 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_lean_2_aq",
        "ending_mmr_character_lean_far_2_partial",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a28, ally, SpriteAnimationState.LEAN_BACK, use_primary=use_primary
    )
    a29 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_lean_2_aq",
        "ending_mmr_character_lean_far_2_full",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a29, ally, SpriteAnimationState.LEAN_BACK_2, use_primary=use_primary
    )
    a30 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_marrymore_char_look_left_aq",
        "ending_marrymore_char_look_left",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a30, ally, SpriteAnimationState.LOOK_TO_SIDE_BEHIND, use_primary=use_primary
    )
    a31 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_marrymore_char_joy_jump_aq",
        "ending_marrymore_char_joy_jump_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a31, ally, SpriteAnimationState.JOY_JUMP, use_primary=use_primary
    )
    a32 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_marrymore_char_joy_jump_aq",
        "ending_marrymore_char_joy_jump_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a32, ally, SpriteAnimationState.JOY_BEHIND, use_primary=use_primary
    )

def _ending_palette_for_prize(prize: CharacterPrize) -> int:
    """Return the light ending-credits palette ID for `prize`."""
    if isinstance(prize, MarioRecruitmentPrize):
        return EPAL0084_MARIO_ENDING
    if isinstance(prize, MallowRecruitmentPrize):
        return EPAL0085_MALLOW_ENDING
    if isinstance(prize, GenoRecruitmentPrize):
        return EPAL0086_GENO_ENDING
    if isinstance(prize, ToadstoolRecruitmentPrize):
        return EPAL0141_TOADSTOOL_ENDING
    if isinstance(prize, BowserRecruitmentPrize):
        return EPAL0140_BOWSER_ENDING
    raise ValueError(f"No light ending palette mapping for {type(prize).__name__}")


def _ending_dark_palette_for_prize(prize: CharacterPrize) -> int:
    """Return the dark ending-credits palette ID for `prize`."""
    if isinstance(prize, MarioRecruitmentPrize):
        return EPAL0163_MARIO_ENDING_DARK
    if isinstance(prize, ToadstoolRecruitmentPrize):
        return EPAL0164_TOADSTOOL_ENDING_DARK
    if isinstance(prize, MallowRecruitmentPrize):
        return EPAL0166_MALLOW_ENDING_DARK
    if isinstance(prize, GenoRecruitmentPrize):
        return EPAL0167_GENO_ENDING_DARK
    if isinstance(prize, BowserRecruitmentPrize):
        return EPAL0165_BOWSER_ENDING_DARK
    raise ValueError(f"No dark ending palette mapping for {type(prize).__name__}")


# Identifiers for the light/dark PaletteSetMorphs and PaletteSet commands in
# script_3951. The light commands are PaletteSetMorphs (use set_palette_set);
# the dark commands are PaletteSet (use set_palette_set_starts_at).
_ENDING_PALETTE_IDS_PROTAGONIST = ("ending_mario_palette", "ending_mario_palette_dark")
_ENDING_PALETTE_IDS_2 = ("ending_mallow_palette", "ending_mallow_palette_dark")
_ENDING_PALETTE_IDS_3 = ("ending_geno_palette", "ending_geno_palette_dark")
_ENDING_PALETTE_IDS_4 = ("ending_bowser_palette", "ending_bowser_palette_dark")
_ENDING_PALETTE_IDS_5 = ("ending_toadstool_palette", "ending_toadstool_palette_dark")


def _set_ending_palette_pair(
    world: GameWorld, ids: tuple[str, str], prize: CharacterPrize
) -> None:
    """Update the (light, dark) palette command pair identified by `ids` so
    that they show `prize`'s ending palette."""
    light_id, dark_id = ids
    world.event_scripts.get_command_by_identifier(
        light_id, PaletteSetMorphs
    ).set_palette_set(_ending_palette_for_prize(prize))
    world.event_scripts.get_command_by_identifier(
        dark_id, PaletteSet
    ).set_palette_set_starts_at(_ending_dark_palette_for_prize(prize))


# script_3951 (R375 ending credits) per-NPC palette command info. Each tuple is
# (character class, light morph id, dark set id, light palette id, dark palette id).
# Every NPC slot in R375 has a static sprite, so each command's palette content
# is fixed by character — only the target row varies based on the protagonist
# and forest character's identity (see _apply_r375_protagonist_palette_rows).
_R375_CHARACTER_PALETTE_INFO: list[
    tuple[type[CharacterPrize], str, str, int, int]
] = [
    (MarioRecruitmentPrize,
     "ending_mario_palette",     "ending_mario_palette_dark",
     EPAL0084_MARIO_ENDING,      EPAL0163_MARIO_ENDING_DARK),
    (ToadstoolRecruitmentPrize,
     "ending_toadstool_palette", "ending_toadstool_palette_dark",
     EPAL0141_TOADSTOOL_ENDING,  EPAL0164_TOADSTOOL_ENDING_DARK),
    (MallowRecruitmentPrize,
     "ending_mallow_palette",    "ending_mallow_palette_dark",
     EPAL0085_MALLOW_ENDING,     EPAL0166_MALLOW_ENDING_DARK),
    (GenoRecruitmentPrize,
     "ending_geno_palette",      "ending_geno_palette_dark",
     EPAL0086_GENO_ENDING,       EPAL0167_GENO_ENDING_DARK),
    (BowserRecruitmentPrize,
     "ending_bowser_palette",    "ending_bowser_palette_dark",
     EPAL0140_BOWSER_ENDING,     EPAL0165_BOWSER_ENDING_DARK),
]

_R375_DOLL_LIGHT_ID = "ending_doll_palette"
_R375_DOLL_DARK_ID = "ending_doll_palette_dark"

# NPC slot order in R375 with each slot's "kind" used by the row-allocation
# walk. "DOLL" = NPC_4 (palette tracks forest character; Mario doll has its
# own unique palette). "FILLER" = NPC_5 Geno_redemption (non-ally, consumes a
# row but receives no PaletteSet command).
_R375_SLOT_ORDER: list[tuple[int, "type[CharacterPrize] | str"]] = [
    (0, MarioRecruitmentPrize),
    (1, ToadstoolRecruitmentPrize),
    (2, MallowRecruitmentPrize),
    (3, GenoRecruitmentPrize),
    (4, "DOLL"),
    (5, "FILLER"),
    (6, BowserRecruitmentPrize),
]


def _apply_r375_protagonist_palette_rows(
    world: GameWorld, forest_maze_prize: CharacterPrize
) -> None:
    """Assign rows + palette content to script_3951's per-character palette
    commands based on the overworld protagonist and the forest character.

    Walking NPC slots 0–6 in order with a counter starting at NPC_PALETTE_ROW_1:
    the protagonist's NPC takes MARIO_PALETTE without consuming the counter;
    every other unique palette gets the next NPC_PALETTE_ROW. Repeated palettes
    (e.g. a non-Mario doll matching its character) reuse the existing row. The
    Mario doll has a unique palette ID so it always consumes its own row when
    Mario is the forest character; in every other case the doll's palette is
    provided by its character's command, so `ending_doll_palette[/_dark]` are
    deleted from the script.
    """
    proto = world.overworld_character
    is_mario_forest = isinstance(forest_maze_prize, MarioRecruitmentPrize)
    forest_class = type(forest_maze_prize)

    counter = 1
    palette_to_row: dict[str, PaletteRow] = {}

    def _next_npc_row() -> PaletteRow:
        nonlocal counter
        row = PaletteRow(int(NPC_PALETTE_ROW_1) + (counter - 1))
        counter += 1
        return row

    for _slot, kind in _R375_SLOT_ORDER:
        if isinstance(kind, str) and kind == "DOLL":
            if is_mario_forest:
                pal_key = "MARIO_DOLL"
                is_proto_pal = False
            else:
                pal_key = forest_class.__name__
                is_proto_pal = isinstance(proto, forest_class)
        elif isinstance(kind, str) and kind == "FILLER":
            pal_key = "GENO_REDEMPTION"
            is_proto_pal = False
        else:
            assert isinstance(kind, type)
            pal_key = kind.__name__
            is_proto_pal = isinstance(proto, kind)

        if pal_key in palette_to_row:
            continue
        if is_proto_pal:
            palette_to_row[pal_key] = MARIO_PALETTE
        else:
            palette_to_row[pal_key] = _next_npc_row()

    for cls, light_id, dark_id, light_pal, dark_pal in _R375_CHARACTER_PALETTE_INFO:
        row = palette_to_row[cls.__name__]
        light_cmd = world.event_scripts.get_command_by_identifier(
            light_id, PaletteSetMorphs
        )
        light_cmd.set_row(row)
        light_cmd.set_palette_set(light_pal)
        dark_cmd = world.event_scripts.get_command_by_identifier(dark_id, PaletteSet)
        dark_cmd.set_from_row(row)
        dark_cmd.set_to_row(row)
        dark_cmd.set_palette_set_starts_at(dark_pal)

    if is_mario_forest:
        row = palette_to_row["MARIO_DOLL"]
        light_cmd = world.event_scripts.get_command_by_identifier(
            _R375_DOLL_LIGHT_ID, PaletteSetMorphs
        )
        light_cmd.set_row(row)
        light_cmd.set_palette_set(EPAL0084_MARIO_ENDING)
        dark_cmd = world.event_scripts.get_command_by_identifier(
            _R375_DOLL_DARK_ID, PaletteSet
        )
        dark_cmd.set_from_row(row)
        dark_cmd.set_to_row(row)
        dark_cmd.set_palette_set_starts_at(EPAL0163_MARIO_ENDING_DARK)
    else:
        world.event_scripts.delete_command_by_identifier(_R375_DOLL_LIGHT_ID)
        world.event_scripts.delete_command_by_identifier(_R375_DOLL_DARK_ID)


def apply_ending_characters(
    world: GameWorld,
    *,
    mushroom_way_prize: CharacterPrize | None,
    forest_maze_prize: CharacterPrize | None,
    inner_mines_prize: CharacterPrize | None,
    marrymore_prize: CharacterPrize | None,
    substitute_prizes: list[CharacterPrize],
    mario_override: CharacterPrize | None = None,
    protagonist_override: CharacterPrize | None = None,
) -> None:
    """Resolve the four ending-cutscene character prizes plus the protagonist
    and dispatch to the matching render_ending_character_N function.

    Mapping of named recruitment slot to ending-cutscene function:
        MushroomWayCharacter -> render_ending_character_2
        ForestMazeCharacter  -> render_ending_character_3
        InnerMinesCharacter  -> render_ending_character_4
        MarrymoreCharacter   -> render_ending_character_5

    `substitute_prizes` is the pool of CharacterPrize instances that are not
    placed in any of the named recruitment slots above — i.e. the StartingCharacterX
    prizes plus stand-in prizes for any character excluded from the seed via
    the AvailableCharacters flag. The pool is shuffled and drained without
    replacement: each empty named slot pops one prize, and the single remaining
    prize is used as the protagonist (whose palette goes into the
    "ending_mario_palette" pair).

    `mario_override`, when provided, replaces every MarioRecruitmentPrize among
    the named-slot prizes and the substitute pool — but NOT the protagonist —
    with the given prize. This is used when PlayAsStarter is disabled and Mario
    is not the starter: the player plays as Mario in the overworld, so Mario is
    the cutscene protagonist, but Mario is *also* recruited as a battle
    character in one of the named slots. To avoid showing Mario twice, that
    named slot displays the starter instead (the starter is recruited at the
    start and so has no named slot of its own). The protagonist is the literal
    overworld character and is never routed through this override.

    `protagonist_override`, when provided, locks the cutscene protagonist to
    that prize regardless of pool draw. Required because the cutscene script
    targets the protagonist-role NPC for the player-character animations
    (lean back, hold star, etc.) — that NPC must be the slot that belongs to
    the actual overworld character, not whoever happens to be left in the
    pool after filling empty named slots.

    Side effects:
      - The five ending-cutscene PaletteSetMorphs / PaletteSet command pairs
        in script_3951 are updated to match each character's actual ending
        slot.
      - Each render_ending_character_N function is called with its resolved
        prize."""

    def _apply_mario_override(p: CharacterPrize | None) -> CharacterPrize | None:
        if mario_override is None or p is None:
            return p
        if isinstance(p, MarioRecruitmentPrize):
            return mario_override
        return p

    ending_prizes: list[CharacterPrize | None] = [
        _apply_mario_override(mushroom_way_prize),
        _apply_mario_override(forest_maze_prize),
        _apply_mario_override(inner_mines_prize),
        _apply_mario_override(marrymore_prize),
    ]
    empty_indexes = [i for i, p in enumerate(ending_prizes) if p is None]

    pool: list[CharacterPrize] = []
    for sp in substitute_prizes:
        overridden = _apply_mario_override(sp)
        assert isinstance(overridden, CharacterPrize)
        pool.append(overridden)

    # Lock the protagonist to the override (the overworld character). Remove
    # one matching prize from the pool so it doesn't get popped into a named
    # slot, leaving someone else stranded as protagonist.
    locked_protagonist: CharacterPrize | None = None
    if protagonist_override is not None:
        # The protagonist is the literal overworld character (Mario when
        # PlayAsStarter is disabled) and must NOT be routed through
        # `_apply_mario_override`. That override rewrites Mario's *named-slot*
        # appearance into the starter; applying it here would rewrite the Mario
        # protagonist into the starter too, animating the starter in the
        # protagonist role and stranding Mario in his recruitment slot.
        locked_protagonist = protagonist_override
        assert isinstance(locked_protagonist, CharacterPrize)
        for i, sp in enumerate(pool):
            if type(sp) is type(locked_protagonist):
                pool.pop(i)
                break

    random.shuffle(pool)

    for i in empty_indexes:
        if not pool:
            raise RuntimeError(
                "Cannot resolve ending character slots: not enough substitute "
                "prizes to cover every empty named recruitment slot."
            )
        ending_prizes[i] = pool.pop()

    if locked_protagonist is not None:
        protagonist_prize = locked_protagonist
    else:
        if not pool:
            raise RuntimeError(
                "Cannot resolve protagonist for ending cutscene: substitute pool "
                "is empty after filling named slots."
            )
        # Whoever is left in the pool is the protagonist. If somehow more than
        # one character is left, pick one at random.
        protagonist_prize = pool.pop() if len(pool) == 1 else random.choice(pool)

    # Dedupe character types across the 5 final ending slots.
    # `_apply_mario_override` can replace a real Mario prize with the starter
    # character — and if that starter is already present somewhere else (as a
    # real recruit or another starter slot), we end up with two prizes of the
    # same type. The role-to-NPC slot mapping (R{496,292,88,375}_NATIVE_SLOT_FOR_PRIZE)
    # is keyed by prize TYPE, so duplicates collapse two cutscene roles onto
    # the same NPC slot, leaving the missing character type entirely absent
    # from the cutscene.
    #
    # Fix: walk the 5 final prizes; for each duplicate type beyond the first,
    # swap it with a stand-in for whichever character type is currently absent.
    _all_ending_prize_classes: tuple[type[CharacterPrize], ...] = (
        MarioRecruitmentPrize,
        ToadstoolRecruitmentPrize,
        MallowRecruitmentPrize,
        GenoRecruitmentPrize,
        BowserRecruitmentPrize,
    )
    _five_slots: list[CharacterPrize | None] = list(ending_prizes) + [protagonist_prize]
    _present = {type(p) for p in _five_slots if p is not None}
    _missing = [cls for cls in _all_ending_prize_classes if cls not in _present]
    # Process the protagonist slot (position 4) FIRST so its type is locked in
    # _seen — duplicates in named slots (positions 0-3) get replaced instead.
    # Without this protection, `_apply_mario_override` rewriting a real Mario
    # prize into the starter could create a duplicate that gets resolved by
    # replacing the protagonist (since the loop processes indices in order),
    # which silently breaks the protagonist_override lock.
    _seen: set[type] = set()
    if _five_slots[4] is not None:
        _seen.add(type(_five_slots[4]))
    for i in range(4):
        p = _five_slots[i]
        if p is None:
            continue
        t = type(p)
        if t in _seen and _missing:
            stand_in = _missing.pop(0)()
            _five_slots[i] = stand_in
            _seen.add(type(stand_in))
        else:
            _seen.add(t)
    ending_prizes = _five_slots[:4]
    protagonist_prize = _five_slots[4]
    assert protagonist_prize is not None

    p2, p3, p4, p5 = ending_prizes
    assert (
        isinstance(p2, CharacterPrize)
        and isinstance(p3, CharacterPrize)
        and isinstance(p4, CharacterPrize)
        and isinstance(p5, CharacterPrize)
    )

    # DEBUG OVERRIDE: force vanilla cutscene assignment regardless of recruit
    # shuffle. Set R496_FORCE_VANILLA_CUTSCENE_ASSIGNMENT = False to disable.
    # When enabled, Peach is marrymore (p5), Mallow is mushroom_way (p2),
    # Geno is forest (p3), Bowser is inner_mines (p4), Mario is protagonist —
    # so the only non-trivial retarget in _apply_r496_role_assignments is
    # MARIO → NPC_19 (Mario's native slot). Recruit-room placements are
    # untouched; only the ending cutscene is reassigned. Useful for
    # isolating Mario-NPC-as-protagonist behavior from the role-swap path.
    R496_FORCE_VANILLA_CUTSCENE_ASSIGNMENT = False
    if R496_FORCE_VANILLA_CUTSCENE_ASSIGNMENT:
        all_five: list[CharacterPrize] = [p2, p3, p4, p5, protagonist_prize]
        by_type: dict[type, CharacterPrize] = {type(p): p for p in all_five}
        if len(by_type) == 5:
            p2 = by_type[MallowRecruitmentPrize]
            p3 = by_type[GenoRecruitmentPrize]
            p4 = by_type[BowserRecruitmentPrize]
            p5 = by_type[ToadstoolRecruitmentPrize]
            protagonist_prize = by_type[MarioRecruitmentPrize]
        # If fewer than 5 distinct character types are present (excluded char,
        # duplicate stand-ins), leave the random assignment alone.

    # Rebuild scripts 3885/3950/3951 with role NPCs baked in, swap room NPC
    # coords/directions, and apply sprite-31 + VRAM-store overrides. This MUST
    # run before the palette pair / palette-row logic below so the rebuilt
    # script contents (carrying the same identifiers) are what subsequent
    # `get_command_by_identifier` calls operate on.
    _apply_ending_cutscene_assignments(
        world,
        marrymore_prize=p5,
        mushroom_way_prize=p2,
        forest_maze_prize=p3,
        inner_mines_prize=p4,
        protagonist_prize=protagonist_prize,
    )

    _apply_r375_protagonist_palette_rows(world, p3)

    render_ending_character_1(world, protagonist_prize, protagonist_prize=protagonist_prize)
    render_ending_character_2(world, p2, protagonist_prize=protagonist_prize)
    render_ending_character_3(world, p3, protagonist_prize=protagonist_prize)
    render_ending_character_4(world, p4, protagonist_prize=protagonist_prize)
    render_ending_character_5(world, p5, protagonist_prize=protagonist_prize)


# =============================================================================
# Seaside / Ship
# =============================================================================


    


        
# =============================================================================
# Dojo
# =============================================================================


def mario_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=2, sprite_offset=4, is_sequence=True, looping=False),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(15),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(30)
        ])

def mallow_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_Pause(5),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=6, sprite_offset=4, is_sequence=True, looping=False),
            A_Pause(7),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(15),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(18)
        ])

def geno_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_Pause(19),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=0, sprite_offset=5, is_sequence=True, looping=False),
            A_Pause(20),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(6)
        ])

def bowser_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_Pause(9),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=0, sprite_offset=4, is_sequence=True, looping=False),
            A_Pause(24),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(12)
        ])
        

def peach_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_Pause(9),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=0, sprite_offset=4, is_sequence=True, looping=False),
            A_Pause(8),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(14),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(14)
        ])
    
def update_ally_challenge(world: GameWorld, duration: int, id: str):
    if world.overworld_character.ally.index == 0:
        world.event_scripts.replace_command_by_identifier(id, mario_dojo_challenge(duration))
    elif world.overworld_character.ally.index == 1:
        world.event_scripts.replace_command_by_identifier(id, peach_dojo_challenge(duration))
    elif world.overworld_character.ally.index == 2:
        world.event_scripts.replace_command_by_identifier(id, bowser_dojo_challenge(duration))
    elif world.overworld_character.ally.index == 3:
        world.event_scripts.replace_command_by_identifier(id, geno_dojo_challenge(duration))
    elif world.overworld_character.ally.index == 4:
        world.event_scripts.replace_command_by_identifier(id, mallow_dojo_challenge(duration))


def render_dojo_fight(
    world: GameWorld,
    prize: BossFightPrize,
    initiate_aq_id: str,
    initiate_id: str,
    pause_id: str,
    player_challenge_id: str,
) -> None:
    """Apply animation changes for a generic Dojo fight."""
    m = prize.smallest_npc()

    duration = 45
    if isinstance(
        prize, (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight)
    ):
        cast(
            ActionQueueAsync,
            world.event_scripts.get_command_by_identifier(initiate_aq_id),
        ).set_subscript(get_mimic_rise_dojo())
    else:
        if m.animations.dojo_challenge is not None:
            duration = max(45, m.animations.dojo_challenge.total_duration + 12)
            world.event_scripts.get_subscript_command_by_identifier(
                initiate_aq_id,
                initiate_id,
                A_SetSpriteSequence,
            ).set_index(m.animations.dojo_challenge.sequence_id)
            world.event_scripts.get_subscript_command_by_identifier(
                initiate_aq_id, pause_id, A_Pause
            ).set_length(duration)
        else:
            world.event_scripts.get_subscript_command_by_identifier(
                initiate_aq_id,
                initiate_id,
                A_SetSpriteSequence,
            ).set_index(0)    
    update_ally_challenge(world, duration, player_challenge_id) 

# =============================================================================
# Bean Valley
# =============================================================================


# =============================================================================
# Nimbus Castle / Statue Room
# =============================================================================


# =============================================================================
# Volcano
# =============================================================================


# =============================================================================
# Inner Factory
# =============================================================================


