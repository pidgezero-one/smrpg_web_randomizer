from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.event_palette_names import (EPAL0024_KEEP_BOSS_1_EVIL, EPAL0025_KEEP_BOSS_1_REFORMED)
from randomizer.logic.progression.prizelocations.access import (can_damage_enemies_with_spells, can_pass_obstacle_courses, not_earlygame, is_early_midgame, is_late_midgame, is_lategame, expect_good_movement, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_exit_keep, can_clear_keep)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from randomizer.utils.event_script_snippets.es_mimic_rise import (get_mimic_rise_kamek)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_FaceSoutheast, A_Pause, A_SetSpriteSequence)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_6)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (Pause)
from typing import (cast)
from randomizer.data.rooms.npcs import MAGIKOOPA_NPC_2
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepAfterObstaclesBossFight(BossFightLocation):
    _bias = True
    _originally_held = KamekBossFight
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _pack_id = PACK209_KEEP_FIRST_BOSS
    _post_unlocks_event_id = E1236_KEEP_1_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0847_KEEP_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY,
            NPC_0,
            sequence_setter_event_id=E0848_KEEP_BATTLE_DOOR_2B_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY,
            NPC_0,
            sequence_setter_event_id=E0849_KEEP_BATTLE_DOOR_2C_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            NPC_0,
            sequence_setter_event_id=E0850_KEEP_BATTLE_DOOR_1A_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
            NPC_0,
            sequence_setter_event_id=E0851_KEEP_BATTLE_DOOR_1B_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            NPC_0,
            sequence_setter_event_id=E0846_KEEP_BATTLE_DOOR_1C_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
            NPC_0,
            sequence_setter_event_id=E0852_KEEP_BATTLE_DOOR_2A_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR,
            NPC_6,
            sequence_setter_event_id=E1192_ENDING_CREDITS_KEEP_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_keep(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if isinstance(self.prize, KamekBossFight):
            # Vanilla Kamek: super().render skips npc_slots swapping, so apply
            # the R435 ending-credits base override manually here.

            credits_room = world.rooms._rooms[
                R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR
            ]
            assert credits_room is not None
            credits_obj = credits_room.get_npc_by_target_id(NPC_6)
            assert credits_obj is not None
            credits_obj._npc = MAGIKOOPA_NPC_2
        if not isinstance(self.prize, KamekBossFight):
            world.event_scripts.get_command_by_identifier(
                "kamek_palette", PaletteSetMorphs
            ).set_palette_set(EPAL0025_KEEP_BOSS_1_REFORMED)
            world.event_scripts.get_command_by_identifier(
                "kamek_palette_2", PaletteSet
            ).set_palette_set_starts_at(EPAL0025_KEEP_BOSS_1_REFORMED)
            m = self.prize.smallest_npc()
            if isinstance(
                self.prize,
                (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight),
            ):
                cast(
                    ActionQueueAsync,
                    world.event_scripts.get_command_by_identifier(
                        "keep_boss_1_animation_aq"
                    ),
                ).set_subscript(get_mimic_rise_kamek())
                world.event_scripts.delete_command_by_identifier(
                    "keep_boss_1_animation_pause"
                )


            elif m.animations.keep_challenge is not None:
                world.event_scripts.get_subscript_command_by_identifier(
                    "keep_boss_1_animation_aq",
                    "keep_boss_1_animation",
                    A_SetSpriteSequence,
                ).set_index(m.animations.keep_challenge.sequence_id)
                cast(
                    Pause,
                    world.event_scripts.get_command_by_identifier(
                        "keep_boss_1_animation_pause",
                    ),
                ).set_length(max(80, m.animations.keep_challenge.total_duration + 10))
            else:
                world.event_scripts.delete_command_by_identifier(
                    "keep_boss_1_animation_aq"
                )

            # rise script not used for box summon or battle halls, so have a separate if block
            if m.animations.keep_summon is not None:
                cast_length = m.animations.keep_summon.contact_frame or m.animations.keep_summon.total_duration
                world.action_scripts.get_command_by_identifier(
                    "keep_battle_room_summon", A_SetSpriteSequence
                ).set_index(m.animations.keep_summon.sequence_id)
                world.event_scripts.get_subscript_command_by_identifier(
                    "keep_boss_1_heal_aq",
                    "keep_boss_1_heal", 
                    A_SetSpriteSequence
                ).set_index(m.animations.keep_summon.sequence_id)
                world.event_scripts.get_command_by_identifier(
                    "EVENT_941_pause_0", Pause
                ).set_length(
                    (
                        cast_length
                    )
                    + 12
                )
                world.event_scripts.get_script_by_id(
                    E0942_KEEP_FIRST_BOSS_SUMMON_CHEST
                ).set_contents(
                    [
                        ActionQueueAsync(
                            NPC_1,
                            [
                                A_FaceSoutheast(),
                                A_Pause(60),
                                A_SetSpriteSequence(
                                    index=m.animations.keep_summon.sequence_id,
                                    is_sequence=True,
                                    looping=False,
                                    mirror_sprite=True,
                                ),
                                A_Pause(
                                    m.animations.keep_summon.contact_frame
                                    or m.animations.keep_summon.total_duration
                                ),
                            ],
                        ),
                        Return(),
                    ]
                )
            else:
                world.event_scripts.get_script_by_id(
                    E0942_KEEP_FIRST_BOSS_SUMMON_CHEST
                ).set_contents(
                    [
                        ActionQueueAsync(NPC_1, [A_FaceSoutheast(), A_Pause(60)]),
                        Return(),
                    ]
                )
                world.action_scripts.delete_command_by_identifier(
                    "keep_battle_room_summon"
                )
                world.event_scripts.delete_subscript_command_by_identifier(
                    "keep_boss_1_heal_aq",
                    "keep_boss_1_heal",
                )

            contact_frame = 25
            cast_duration = 25
            if m.animations.keep_summon is not None:
                cast_duration = m.animations.keep_summon.total_duration
                if m.animations.keep_summon.contact_frame is not None:
                    contact_frame = m.animations.keep_summon.contact_frame
                else:
                    contact_frame = m.animations.keep_summon.total_duration
            arms_go_up = max(0, contact_frame - 5)
            pause_ends = contact_frame
            reset_properties_after = (contact_frame + 10) if contact_frame == cast_duration else cast_duration
            arms_go_down = reset_properties_after + 5
            if arms_go_up == 0:
                world.event_scripts.delete_subscript_command_by_identifier(
                    "keep_heal_arms_raised_aq",
                    "keep_heal_arms_go_up",
                )
            else:
                world.event_scripts.get_subscript_command_by_identifier(
                    "keep_heal_arms_raised_aq",
                    "keep_heal_arms_go_up", A_Pause
                ).set_length(arms_go_up)
            world.event_scripts.get_subscript_command_by_identifier(
                "keep_heal_arms_raised_aq",
                "keep_heal_arms_go_down", A_Pause
            ).set_length(arms_go_down)
            world.event_scripts.get_subscript_command_by_identifier(
                "keep_boss_1_heal_aq",
                "keep_boss_1_heal_length", A_Pause
            ).set_length(reset_properties_after)
            world.event_scripts.get_command_by_identifier(
                "keep_heal_animation_starts", Pause
            ).set_length(pause_ends)
            world.event_scripts.get_command_by_identifier(
                "keep_heal_animation_ends", Pause
            ).set_length(reset_properties_after - pause_ends)
            
        else:
            world.event_scripts.delete_command_by_identifier("kamek_palette_3")

        # Substitute event palettes 24 (evil) and 25 (reformed) with the
        # chosen boss's sprite palette so the pre/post-reformation scene
        # shows the correct colors for the shuffled boss.
        selected_npc = self.prize.smallest_npc()
        selected_sprite = world.get_sprite(selected_npc.base.sprite_id)
        default_palette_index = (
            selected_sprite.palette_id + selected_sprite.palette_offset
        )
        default_colors = list(
            world.sprite_palettes.get_palette(default_palette_index).colors
        )
        world.event_palettes.get_palette(EPAL0025_KEEP_BOSS_1_REFORMED).set_colors(
            default_colors
        )

        evil_palette_colors = selected_npc.evil_palette
        if evil_palette_colors is None:
            evil_colors = default_colors
        else:
            evil_colors = list(evil_palette_colors)
        world.event_palettes.get_palette(EPAL0024_KEEP_BOSS_1_EVIL).set_colors(
            evil_colors
        )

        return op


__all__ = ["KeepAfterObstaclesBossFight"]
