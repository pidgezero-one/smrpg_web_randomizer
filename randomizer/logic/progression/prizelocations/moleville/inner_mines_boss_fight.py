from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_mines, can_damage_enemies_with_spells, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_SetSpriteSequence, A_Pause)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def set_mines_punch_command(world: GameWorld, boss: BossNPC):
    contact_frame = 1  # Default to 1 (minimum valid pause duration)
    if boss.animations is None or boss.animations.mines_punch is None:
        world.event_scripts.delete_command_by_identifier("inner_mines_boss_shove_animation")
    else:
        collection = boss.animations.mines_punch
        contact_frame = collection.contact_frame or 12  # Ensure at least 1
        boss_pause_length = collection.total_duration
        boss_animation = ActionQueueSync(target=NPC_0, subscript=[
            A_SetSpriteSequence(index=collection.sequence_id, is_sequence=True, looping=False),
            A_Pause(boss_pause_length),
        ])
        world.event_scripts.replace_command_by_identifier("inner_mines_boss_shove_animation", boss_animation)
    world.event_scripts.replace_subscript_command_by_identifier(
        "inner_mines_mario_shoved_backward",
        "inner_mines_mario_shoved_backward_duration",
        A_Pause(contact_frame)
    )
    world.event_scripts.get_command_by_identifier("inner_mines_mario_shoved_backward_pause", Pause).set_length(contact_frame)


class InnerMinesBossFight(BossFightLocation):
    _bias = True
    _originally_held = PunchinelloBossFight
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT
    _world_area = WorldAreaEnum.MOLEVILLE
    _pack_id = PACK140_MINES_BOSS_2
    _post_unlocks_event_id = E1200_INNER_MINES_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            NPC_0,
            sequence_setter_event_id=E0788_MINES_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            ],
            [NPC_4, NPC_5, NPC_6],
            PACK152_MINES_BOSS_ROOM_HENCHMAN,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationHenchmanNPC(
            [
                R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER,
            ],
            [NPC_1],
        ),
    ]
    _tiny_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            ],
            [NPC_1, NPC_2, NPC_3],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MINES):
            content.extend(
                [
                    ApplySolidityModToLevel(
                        permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0
                    ),
                    ApplyTileModToLevel(
                        use_alternate=True,
                        room_id=R202_BOOSTER_TOWER_ENTRANCE,
                        mod_id=32,
                    ),
                    SetBit(TOWER_OPENED),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        # Check if any tiny henchman slots were assigned
        if self._tiny_henchman_slots is not None:
            assigned_slots = {slot for slot, _ in henchmen_assignments}
            for slot in self._tiny_henchman_slots:
                if slot in assigned_slots:
                    world.action_scripts.delete_command_by_identifier("microbomb_spark")
                    break

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        assert self._npc_slots is not None
        # Read the NPC model placement chose (cached on the location).
        npc_model = self.resolve_npc_model_for_slot(world, self._npc_slots[0])
        set_mines_punch_command(world, npc_model())
        # A1021_PUNCHINELLO_IN_MINES is a Punchinello-specific animation. If any
        # other boss was shuffled in here, point event script 596's explosion-loop
        # triggers at A0000_DO_NOTHING instead.
        if not isinstance(
            self.prize, (PunchinelloBossFight, Punchinello2BossFight)
        ):
            for identifier in (
                "EVENT_596_set_action_script_4",
                "EVENT_596_set_action_script_11",
                "EVENT_596_set_action_script_18",
            ):
                world.event_scripts.get_command_by_identifier(
                    identifier, SetSyncActionScript
                ).set_action_script_id(A0000_DO_NOTHING)
        return op


__all__ = ["InnerMinesBossFight"]
