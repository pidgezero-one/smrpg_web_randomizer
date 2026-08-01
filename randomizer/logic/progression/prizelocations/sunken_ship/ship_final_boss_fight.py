from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_FaceNorthwest, A_FaceSouthwest, A_SetSpriteSequence)
from randomizer.logic.progression.prizelocations.access import (can_clear_ship, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, RemoveIfNotFilled, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_8)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_ship_final_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Ship Final boss fight."""
    m = prize.smallest_npc()
    # boss room on revisit
    if m.animations.ship_chair is not None:
        c = world.action_scripts.get_command_by_identifier(
            "ship_boss_idle_sequence", A_SetSpriteSequence
        )
        c.set_index(m.animations.ship_chair.sequence_id)
    else:
        world.action_scripts.replace_command_by_identifier(
            "ship_boss_idle_sequence", A_FaceSouthwest()
        )
        world.action_scripts.delete_command_by_identifier(
            "ship_boss_idle_sequence_loop"
        )

    # ending credits
    if m.animations.tpose_mold_id is not None:
        mirror_sprite = m.base.directions == VramStore.DIR2_SWSE
        world.event_scripts.replace_subscript_command_by_identifier(
            "ending_credits_sunset_npc_0_sequence_setup",
            "ending_credits_sunset_npc_0_sequence",
            A_SetSpriteSequence(index=m.animations.tpose_mold_id, is_mold=True, mirror_sprite=mirror_sprite),
        )
    else:
        world.event_scripts.replace_subscript_command_by_identifier(
            "ending_credits_sunset_npc_0_sequence_setup",
            "ending_credits_sunset_npc_0_sequence",
            A_FaceNorthwest(),
        )

    # Delete event script commands for unfilled character henchman slots
    assigned_count = (
        len(prize.character_henchmen) if prize.character_henchmen is not None else 0
    )
    if assigned_count > 0 and assigned_count < 2:
        # Slot 0 unfilled
        if assigned_count < 1:
            for d in [
                "ship_henchman_1_beach_1",
                "ship_henchman_1_beach_2",
                "ship_henchman_1_beach_3",
            ]:
                world.event_scripts.delete_command_by_identifier(d)
        # Slot 1 unfilled
        if assigned_count < 2:
            world.event_scripts.delete_command_by_identifier("ship_henchman_2_beach_1")


class ShipFinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = JohnnyBossFight
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _pack_id = PACK166_SHIP_SECOND_BOSS
    _post_unlocks_event_id = E1208_SHIP_END_BOSS_UNLOCKS
    _henchman_can_run_away = False
    _npc_slots = [
        BossFightLocationNPC(
            R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            NPC_8,
            sequence_setter_event_id=E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R432_ENDING_CREDITS_JOHNNY_LOOKING_OUT_AT_SUNSET_ON_BEACH_SHORE,
            NPC_0,
            sequence_setter_event_id=E1191_ENDING_CREDITS_CLIFF_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_1, NPC_4],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_2, NPC_5],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
            [NPC_3],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
            [NPC_4],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
            ],
            [NPC_0, NPC_1, NPC_2, NPC_3],
            PACK068_SHIP_HENCHMAN_1,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationHenchmanNPC(
            [
                R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
                R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
            ],
            [NPC_0, NPC_1],
            PACK069_SHIP_HENCHMAN_2,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING,
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER,
        DI1781_SHIP_BOSS_JUMP_ON_HEAD,
        DI1782_SHIP_BOSS_DRINK,
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2,
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1,
        DI1786_LETTER_FROM_SHIP_BOSS,
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3,
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4,
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED,
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED,
    ]

    @property
    def eligible_mook_henchmen(self) -> list[BossFightHenchman] | None:
        pool = super().eligible_mook_henchmen
        if pool is None or not isinstance(self.prize, Belome2BossFight):
            return pool
        # Belome 2's Bowser clone sprite doesn't fit the ship henchman rooms.
        return [
            h
            for h in pool
            if h.model not in (BowsercloneHenchman, BowsercloneHenchman_2)
        ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(YaridovichGate, YaridovichGating.SHIP):
            content.extend([SetBit(SEASIDE_BOSS_AVAILABLE)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, (JohnnyBossFight, Johnny2Fight)):
            render_ship_final_boss(world, self.prize)

        return op


__all__ = ["ShipFinalBossFight"]
