from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.utils.npcs import (is_swse_only)
from randomizer.utils.event_script_snippets.es_non_smithy_final_boss import (es_non_smithy_3792, es_non_smithy_3794)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_FixedFCoordOn)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_Pause, A_SetSpriteSequence)
from typing import (cast)
from randomizer.logic.progression.prizelocations.access import (can_access_inner_factory_final_boss, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_10, NPC_11, NPC_15, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_final_boss_fight(
    world: GameWorld,
    prize: BossFightPrize,
) -> None:
    """Apply animation changes for Final Boss fight."""

    e3792 = world.event_scripts.get_script_by_id(E3792_FACTORY_FINAL_BOSS_ROOM_LOADER)
    e3794 = world.event_scripts.get_script_by_id(E3794_FACTORY_FINAL_BOSS_FIGHT)
    e3792.set_contents(es_non_smithy_3792.contents)
    e3794.set_contents(es_non_smithy_3794.contents)

    anim = prize.largest_npc().animations.endgame_challenge
    if anim is not None:
        if anim.total_duration > 55:
            cast(
                Pause, world.event_scripts.get_command_by_identifier("final_boss_pause")
            ).set_length(anim.total_duration)
            cast(
                ActionQueueSync,
                world.event_scripts.get_command_by_identifier("final_boss_mario_rise"),
            ).subscript.insert_before_nth_command(0, A_Pause(anim.total_duration - 55))
        world.event_scripts.get_script_by_id(
            E0944_FINAL_BOSS_ANIMATION_SUBROUTINE_1
        ).insert_before_nth_command(
            0,
            ActionQueueSync(
                NPC_0,
                [
                    A_SetSpriteSequence(
                        index=anim.sequence_id,
                        is_sequence=True,
                    )
                ],
            ),
        )

        
    room = world.rooms._rooms[R509_FACTORY_GROUNDS_SMITHYS_PAD]
    assert (
        room is not None
    ), f"Room {R509_FACTORY_GROUNDS_SMITHYS_PAD} not found"
    for npc_id in [NPC_4, NPC_5, NPC_6, NPC_7, NPC_9]:
        obj = room.get_npc_by_target_id(npc_id)
        assert (
            obj is not None
        ), f"NPC {npc_id} not found in room {R509_FACTORY_GROUNDS_SMITHYS_PAD}"
        obj.set_visible(False)
    obj = room.get_npc_by_target_id(NPC_8)
    obj.set_z(0)
    obj.set_action_script(A0015_DO_NOTHING)


def render_final_boss_conveyor_lackeys(
    world: GameWorld,
    model: type[HenchmanNPC],
) -> None:
    """Strip the northeast turns from the Gun Yolk room conveyor lackey scripts
    when the henchman model that landed there has no north-facing sequence.

    Sprites limited to SW/SE would draw their south molds while walking away
    from the camera, so the turns are dropped and facing is pinned instead.
    """
    m = model()
    spr = world.sprites.sprites[m.base.sprite_id]
    assert spr is not None
    if not (is_swse_only(spr) or m.base.directions == VramStore.DIR2_SWSE):
        return

    world.action_scripts.delete_command_by_identifier(
        "as_955_factory_lackey_faces_north"
    )
    world.action_scripts.delete_command_by_identifier(
        "as_955_factory_lackey_faces_north_2"
    )
    for script_id in [
        A0955_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES,
        A0956_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES,
        A0954_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES,
    ]:
        world.get_action_script(script_id).insert_before_nth_command(
            0, A_FixedFCoordOn()
        )


class FinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = SmithyBossFight
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_FINAL
    _world_area = WorldAreaEnum.INNER_FACTORY
    _rooms = [R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, R509_FACTORY_GROUNDS_SMITHYS_PAD]
    _pack_id = PACK185_FINAL_BOSS
    _force_battlefield = BF44_FACTORY_GROUNDS_SMITHYS_PAD
    _post_unlocks_event_id = E1245_INNER_FACTORY_5_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R509_FACTORY_GROUNDS_SMITHYS_PAD,
            NPC_8,
            sequence_setter_event_id=E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
            ],
            [
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_7,
                NPC_8,
                NPC_9,
                NPC_10,
                NPC_11,
                NPC_15,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
                NPC_7,
                NPC_8,
                NPC_9,
                NPC_10,
                NPC_11,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
            ],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_factory_final_boss(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, SmithyBossFight):
            render_final_boss_fight(world, self.prize)
        mook = self.get_chosen_henchman_model_for_slot(
            R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, NPC_7
        )
        if mook is not None:
            render_final_boss_conveyor_lackeys(world, mook)
        return op


__all__ = ["FinalBossFight"]
