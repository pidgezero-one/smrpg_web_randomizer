from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.types.ally import (SpriteAnimationState)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_SetSpriteSequence)
from typing import (cast)
from randomizer.logic.renders import (update_ally_animation)
from randomizer.logic.progression.prizelocations.access import (can_clear_chapel, is_all_starting_chars_set)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (AllyNPCSub, CharacterRecruitmentLocation, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10, NPC_8)
from randomizer.data.rooms.npcs import MARIO_ENDING_2
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_marrymore_character_empty(world: GameWorld) -> None:
    """Remove character sprite animations when Toad substitute remains in chapel."""
    deletions: list[tuple[str, list[str]]] = [
        (
            "chapel_character_queue_1",
            ["chapel_character_animation_1", "chapel_character_animation_2"],
        ),
        ("chapel_character_queue_2", ["chapel_character_animation_3"]),
        ("chapel_character_queue_3", []),
        (
            "chapel_character_queue_4",
            ["chapel_character_animation_4", "chapel_character_animation_5"],
        ),
        ("chapel_character_queue_5", ["chapel_character_animation_6"]),
        ("chapel_character_queue_6", ["chapel_character_animation_7"]),
        (
            "chapel_character_queue_7",
            ["chapel_character_animation_8", "chapel_character_animation_9"],
        ),
        (
            "chapel_character_queue_8",
            ["chapel_character_animation_10", "chapel_character_animation_11"],
        ),
        ("chapel_character_queue_9", ["chapel_character_animation_12"]),
        (
            "EVENT_3499_action_queue_42",
            ["chapel_character_animation_13", "chapel_character_animation_14"],
        ),
        (
            "EVENT_3499_action_queue_45",
            ["chapel_character_animation_15", "chapel_character_animation_16"],
        ),
        ("chapel_character_queue_10", ["chapel_character_animation_17"]),
        (
            "chapel_character_queue_11",
            ["chapel_character_animation_18", "chapel_character_animation_19"],
        ),
        (
            "chapel_character_queue_12",
            ["chapel_character_animation_20", "chapel_character_animation_21"],
        ),
        (
            "chapel_reload_crying_aq",
            ["chapel_reload_crying"],
        ),
    ]
    for queue, actions in deletions:
        if len(actions) == 0:
            world.event_scripts.delete_command_by_identifier(queue)
        else:
            e = cast(
                ActionQueueAsync,
                world.event_scripts.get_command_by_identifier(queue),
            )
            ss = e.subscript
            for action in actions:
                idx = ss.get_index_of_identifier(action)
                ss.delete_at_index(idx)
            e.set_subscript(ss.contents)


def render_marrymore_character(world: GameWorld, prize: CharacterPrize) -> None:
    ally = prize.ally
    # Mario uses protagonist sprite (0) at this location, so needs _sprites_primary
    # which has sprite_offsets relative to sprite 0. Other allies use _sprites_secondary
    # with offsets relative to their non-protagonist sprite IDs.
    use_primary = isinstance(prize, MarioRecruitmentPrize)

    a1 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_1", "chapel_character_animation_1", A_SetSpriteSequence
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a2 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_1", "chapel_character_animation_2", A_SetSpriteSequence
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.FLOORED, use_primary=use_primary
    )
    a3 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_2", "chapel_character_animation_3", A_SetSpriteSequence
    )
    update_ally_animation(a3, ally, SpriteAnimationState.HURT, use_primary=use_primary)
    a4 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_3", "chapel_character_queue_3_", A_SetSpriteSequence
    )
    update_ally_animation(
        a4, ally, SpriteAnimationState.LOOKING_DOWN_STATIC, use_primary=use_primary
    )
    a5 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_4", "chapel_character_animation_4", A_SetSpriteSequence
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.SHAKING_HEAD, use_primary=use_primary
    )
    a6 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_4", "chapel_character_animation_5", A_SetSpriteSequence
    )
    update_ally_animation(
        a6, ally, SpriteAnimationState.LOOKING_DOWN_STATIC, use_primary=use_primary
    )
    a7 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_5", "chapel_character_animation_6", A_SetSpriteSequence
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.CRYING, use_primary=use_primary
    )
    a8 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_6", "chapel_character_animation_7", A_SetSpriteSequence
    )
    update_ally_animation(
        a8, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a9 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_7", "chapel_character_animation_9", A_SetSpriteSequence
    )
    update_ally_animation(
        a9, ally, SpriteAnimationState.LOOKING_DOWN_STATIC, use_primary=use_primary
    )
    a10 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_7", "chapel_character_animation_8", A_SetSpriteSequence
    )
    update_ally_animation(
        a10, ally, SpriteAnimationState.CRYING, use_primary=use_primary
    )
    a11 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_8", "chapel_character_animation_10", A_SetSpriteSequence
    )
    update_ally_animation(
        a11, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a12 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_8", "chapel_character_animation_11", A_SetSpriteSequence
    )
    update_ally_animation(
        a12, ally, SpriteAnimationState.CRYING_BACKWARDS, use_primary=use_primary
    )
    a13 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_9", "chapel_character_animation_12", A_SetSpriteSequence
    )
    update_ally_animation(
        a13, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a14 = world.event_scripts.get_subscript_command_by_identifier(
        "EVENT_3499_action_queue_42",
        "chapel_character_animation_13",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a14, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a15 = world.event_scripts.get_subscript_command_by_identifier(
        "EVENT_3499_action_queue_42",
        "chapel_character_animation_14",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a15, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a16 = world.event_scripts.get_subscript_command_by_identifier(
        "EVENT_3499_action_queue_45",
        "chapel_character_animation_15",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a16, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a17 = world.event_scripts.get_subscript_command_by_identifier(
        "EVENT_3499_action_queue_45",
        "chapel_character_animation_16",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a17, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a18 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_10",
        "chapel_character_animation_17",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a18, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a19 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_11",
        "chapel_character_animation_18",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a19, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a20 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_11",
        "chapel_character_animation_19",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a20, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a21 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_12",
        "chapel_character_animation_20",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a21, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a22 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_12",
        "chapel_character_animation_21",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a22, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a23 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_reload_crying_aq", "chapel_reload_crying", A_SetSpriteSequence
    )
    update_ally_animation(
        a23, ally, SpriteAnimationState.CRYING_BACKWARDS, use_primary=use_primary
    )


class MarrymoreCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = ToadstoolRecruitmentPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_CHARACTER
    _world_area = WorldAreaEnum.MARRYMORE
    _container_event = E1228_MARRYMORE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_10,
        ),
        AllyNPCSub(
            R054_BOOSTER_HILL_DUMMY,
            NPC_8,
        ),
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 201),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(CHAPEL_ITEMS_ANYWHERE_ENABLED, ["marrymore_hint_text"]),
        StoreItemAmountTo7000(RingItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(CrownItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(ShoesItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(BroochItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(9)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.prize is None:
            render_marrymore_character_empty(world)
        else:
            assert isinstance(
                self.prize, CharacterPrize
            ), f"MarrymoreCharacter prize must be CharacterPrize, got {type(self.prize)}"
            self._apply_marrymore_npc_overrides(world)
            render_marrymore_character(world, self.prize)
        return op

    def _apply_marrymore_npc_overrides(self, world: GameWorld) -> None:
        """Apply per-character NPC overrides for Marrymore chapel/Booster Hill.

        Mario: every fill (chapel NPC_10 and Booster Hill NPC_8) gets the
        MARIO_ENDING_2 (sprite 0) NPC. Chapel animations are driven by
        update_ally_animation with use_primary=True, so the sprite_offsets
        are relative to sprite 0; leaving any fill at the default sprite 409
        Mario clone makes those offsets resolve to wrong sprites and corrupts
        the chapel animation.

        Bowser is cannot_clone=True with vram_size=1 (dedicated VRAM).
        All others are cloneable (cannot_clone=False, vram_size=0).
        """

        assert isinstance(self.prize, CharacterPrize)

        if isinstance(self.prize, MarioRecruitmentPrize):

            for npc_sub in self._npc_fills:
                room = world.rooms._rooms[npc_sub.room_id]
                if room is None:
                    continue
                obj = room.get_npc_by_target_id(npc_sub.npc_id)
                if obj is not None:
                    obj._npc = MARIO_ENDING_2

        room_54 = world.rooms._rooms[R054_BOOSTER_HILL_DUMMY]
        if room_54 is None:
            return

        # Apply NPC 8 vram/clone tuning in room 54 (Booster Hill).
        obj = room_54.get_npc_by_target_id(NPC_8)
        if obj is None:
            return
        if isinstance(self.prize, BowserRecruitmentPrize):
            obj._min_vram_size = 1
        else:
            # Mario, Mallow, Geno, Peach — cloneable, use buffer system
            obj._min_vram_size = 0
        obj._cannot_clone = True


__all__ = ["MarrymoreCharacter"]
