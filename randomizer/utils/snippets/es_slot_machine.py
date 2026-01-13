from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld
    from randomizer.types.prizelocation import TreasureChestLocation
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from ...data.variables.action_script_names import *
from ...data.variables.battlefield_names import *
from ...data.variables.dialog_names import *
from ...data.variables.event_script_names import *
from ...data.variables.music_names import *
from ...data.variables.overworld_area_names import *
from ...data.variables.overworld_sfx_names import *
from ...data.variables.pack_names import *
from ...data.variables.room_names import *
from ...data.variables.shop_names import *
from ...data.variables.variable_names import *
from ...data.items import *
from ...data.packets import *

from smrpgpatchbuilder.datatypes.levels.classes import Room

    

def create_slot_machine_script(location: TreasureChestLocation, world: GameWorld) -> list[UsableEventScriptCommand]:
    output: list[UsableEventScriptCommand] = [Return()]

    for room_id in location._rooms:
        room = world.rooms._rooms[room_id]
        if room is None:
            raise ValueError(f"Room ID {room_id} not found in world while creating slot machine script.")

        slot_machine_script_commands = create_slot_machine_script_for_one_room(room)
        identifier = slot_machine_script_commands[0]._generate_identifier()
        output.insert(0, JmpIfVarEqualsConst(PRIMARY_TEMP_7000, room_id, [identifier]))
        output.extend(slot_machine_script_commands)
    output.insert(0, Set7000ToCurrentLevel())

    return output

def create_slot_machine_script_for_one_room(room: Room) -> list[UsableEventScriptCommand]:
    npc_count = len(room.objects)
    npcs = [
        AreaObject(0x14 + npc_count + x) for x in range(5)
    ]

    return [
        JmpIfBitSet(TEMP_7044_2, ["EVENT_2491_jmp_if_bit_set_22"]),
        SetBit(TEMP_7044_2),
        PauseActionScript(MEM_70A8),
        Set7016701BToObjectXYZ(target=MEM_70A8),
        AddConstToVar(Z_COORD_2, 304),
        ActionQueueSync(target=MEM_70A8, subscript=[
            A_SequenceLoopingOn(),
            A_SetSpriteSequence(index=1, looping=False),
            A_Pause(6),
            A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
        ]),
        ActionQueueSync(target=npcs[0], subscript=[
            A_UnknownCommand(bytearray(b'\x99'))
        ]),
        ActionQueueSync(target=npcs[1], subscript=[
            A_UnknownCommand(bytearray(b'\x99'))
        ]),
        ActionQueueSync(target=npcs[2], subscript=[
            A_UnknownCommand(bytearray(b'\x99'))
        ]),
        ActionQueueSync(target=npcs[3], subscript=[
            A_UnknownCommand(bytearray(b'\x99'))
        ]),
        ActionQueueAsync(target=npcs[4], subscript=[
            A_UnknownCommand(bytearray(b'\x99'))
        ]),
        Pause(6),
        SummonObjectToCurrentLevel(npcs[0]),
        SummonObjectToCurrentLevel(npcs[1]),
        SummonObjectToCurrentLevel(npcs[2]),
        Pause(1),
        ActionQueueSync(target=npcs[1], subscript=[
            A_SetWalkingSpeed(FASTEST),
            A_WalkEastPixels(17)
        ]),
        ActionQueueAsync(target=npcs[2], subscript=[
            A_SetWalkingSpeed(FASTEST),
            A_WalkWestPixels(17)
        ]),
        SetSyncActionScript(npcs[0], A0185_CHEST_SLOT_MACHINE_ROLLER),
        SetSyncActionScript(npcs[1], A0186_CHEST_SLOT_MACHINE_ROLLER),
        SetSyncActionScript(npcs[2], A0184_CHEST_SLOT_MACHINE_ROLLER),
        Return(),
        JmpIfBitSet(TEMP_7044_3, ["EVENT_2491_jmp_if_bit_set_26"], identifier="EVENT_2491_jmp_if_bit_set_22"),
        SetBit(TEMP_7044_3),
        PauseActionScript(npcs[2]),
        Return(),
        JmpIfBitSet(TEMP_7044_4, ["EVENT_2491_disable_trigger_30"], identifier="EVENT_2491_jmp_if_bit_set_26"),
        SetBit(TEMP_7044_4),
        PauseActionScript(npcs[0]),
        Return(),
        DisableObjectTrigger(MEM_70A8, identifier="EVENT_2491_disable_trigger_30"),
        PauseActionScript(npcs[1]),
        Pause(16),
        ActionQueueSync(target=npcs[2], subscript=[
            A_SetWalkingSpeed(VERY_FAST),
            A_WalkEastPixels(8)
        ]),
        ActionQueueSync(target=npcs[1], subscript=[
            A_SetWalkingSpeed(VERY_FAST),
            A_WalkWestPixels(8)
        ]),
        StopEmbeddedActionScript(npcs[1]),
        StopEmbeddedActionScript(npcs[2]),
        RemoveObjectFromCurrentLevel(npcs[0]),
        RemoveObjectFromCurrentLevel(npcs[1]),
        RemoveObjectFromCurrentLevel(npcs[2]),
        SummonObjectToCurrentLevel(npcs[4]),
        ActionQueueAsync(target=npcs[4], subscript=[
            A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
            A_SetSpriteSequence(index=1, looping=False),
            A_Pause(16),
            A_VisibilityOff()
        ]),
        JmpIfVarEqualsConst(FACTORY_FALL_1, 0, ["EVENT_2491_jmp_if_var_equals_const_45"]),
        JmpIfVarEqualsConst(FACTORY_FALL_1, 1, ["EVENT_2491_jmp_if_var_equals_const_48"]),
        JmpIfVarEqualsConst(FACTORY_FALL_1, 2, ["EVENT_2491_jmp_if_var_equals_const_51"]),
        JmpIfVarEqualsConst(FACTORY_FALL_2, 0, ["EVENT_2491_jmp_if_var_equals_const_54"], identifier="EVENT_2491_jmp_if_var_equals_const_45"),
        JmpIfVarEqualsConst(FACTORY_FALL_2, 1, ["EVENT_2491_jmp_if_var_equals_const_56"]),
        Jmp(["EVENT_2491_jmp_if_var_equals_const_59"]),
        JmpIfVarEqualsConst(FACTORY_FALL_2, 0, ["EVENT_2491_jmp_if_var_equals_const_62"], identifier="EVENT_2491_jmp_if_var_equals_const_48"),
        JmpIfVarEqualsConst(FACTORY_FALL_2, 1, ["EVENT_2491_jmp_if_var_equals_const_65"]),
        Jmp(["EVENT_2491_jmp_if_var_equals_const_67"]),
        JmpIfVarEqualsConst(FACTORY_FALL_2, 0, ["EVENT_2491_jmp_if_var_equals_const_70"], identifier="EVENT_2491_jmp_if_var_equals_const_51"),
        JmpIfVarEqualsConst(FACTORY_FALL_2, 1, ["EVENT_2491_jmp_if_var_equals_const_73"]),
        Jmp(["EVENT_2491_jmp_if_var_equals_const_76"]),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2491_summon_to_current_level_78"], identifier="EVENT_2491_jmp_if_var_equals_const_54"),
        Jmp(["EVENT_2491_play_sound_83"]),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2491_play_sound_83"], identifier="EVENT_2491_jmp_if_var_equals_const_56"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_play_sound_88"]),
        Jmp(["EVENT_2491_action_queue_99"]),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2491_play_sound_83"], identifier="EVENT_2491_jmp_if_var_equals_const_59"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_action_queue_99"]),
        Jmp(["EVENT_2491_play_sound_95"]),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2491_play_sound_83"], identifier="EVENT_2491_jmp_if_var_equals_const_62"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_play_sound_88"]),
        Jmp(["EVENT_2491_action_queue_99"]),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_summon_to_current_level_78"], identifier="EVENT_2491_jmp_if_var_equals_const_65"),
        Jmp(["EVENT_2491_play_sound_88"]),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2491_action_queue_99"], identifier="EVENT_2491_jmp_if_var_equals_const_67"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_play_sound_88"]),
        Jmp(["EVENT_2491_play_sound_95"]),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2491_play_sound_83"], identifier="EVENT_2491_jmp_if_var_equals_const_70"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_action_queue_99"]),
        Jmp(["EVENT_2491_play_sound_95"]),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 0, ["EVENT_2491_action_queue_99"], identifier="EVENT_2491_jmp_if_var_equals_const_73"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_play_sound_88"]),
        Jmp(["EVENT_2491_play_sound_95"]),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 2, ["EVENT_2491_summon_to_current_level_78"], identifier="EVENT_2491_jmp_if_var_equals_const_76"),
        Jmp(["EVENT_2491_play_sound_95"]),
        SummonObjectToCurrentLevel(npcs[3], identifier="EVENT_2491_summon_to_current_level_78"),
        PlaySound(sound=SO094_FROG_COIN, channel=6),
        ActionQueueSync(target=npcs[3], subscript=[
            A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
            A_SetPriority(3),
            A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
            A_Pause(32),
            A_VisibilityOff()
        ]),
        AddFrogCoins(1),
        Jmp(["EVENT_2491_action_queue_109"]),
        PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_2491_play_sound_83"),
        ActionQueueSync(target=npcs[0], subscript=[
            A_VisibilityOn(),
            A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
            A_Pause(32),
            A_VisibilityOff()
        ]),
        SetVarToConst(PRIMARY_TEMP_7000, 1),
        Add7000ToMaxFP(),
        Jmp(["EVENT_2491_action_queue_109"]),
        PlaySound(sound=SO071_MUSHROOM_CURE, channel=6, identifier="EVENT_2491_play_sound_88"),
        ActionQueueSync(target=npcs[0], subscript=[
            A_VisibilityOn(),
            A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
            A_Pause(32),
            A_VisibilityOff()
        ]),
        RestoreAllHP(),
        RestoreAllFP(),
        TintLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND], red=64, green=160, blue=64, speed=3, bit_15=True),
        TintLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND], red=0, green=0, blue=0, speed=3, bit_15=True),
        Jmp(["EVENT_2491_action_queue_109"]),
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_2491_play_sound_95"),
        ActionQueueSync(target=npcs[0], subscript=[
            A_VisibilityOn(),
            A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
            A_Pause(32),
            A_VisibilityOff()
        ]),
        AddToInventory(RockCandyItem),
        Jmp(["EVENT_2491_action_queue_109"]),
        ActionQueueAsync(target=npcs[0], subscript=[
            A_VisibilityOn(),
            A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
        ], identifier="EVENT_2491_action_queue_99"),
        Pause(32),
        JmpIfBitSet(ALTERNATE_STAR_PIECE_WIN_CONDITION, ["EVENT_2491_set_var_to_const_104"]),
        RunEventAsSubroutine(E1931_TREASURE_CHEST_FAILURE_MIMIC_FIGHT),
        Jmp(["EVENT_2491_remove_from_current_level_107"]),
        SetVarToConst(PRIMARY_TEMP_7000, 514, identifier="EVENT_2491_set_var_to_const_104"),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        RemoveObjectFromCurrentLevel(npcs[0], identifier="EVENT_2491_remove_from_current_level_107"),
        FadeInFromBlack(sync=False),
        ActionQueueSync(target=MEM_70A8, subscript=[
            A_Pause(32),
            A_SetSequenceSpeed(FAST),
            A_SetSpriteSequence(index=3, looping=False),
            A_Pause(10),
            A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
        ], identifier="EVENT_2491_action_queue_109"),
        DisableObjectTrigger(MEM_70A8),
        ClearBit(TEMP_7044_2),
        ClearBit(TEMP_7044_3),
        ClearBit(TEMP_7044_4),
        Return()
    ]
