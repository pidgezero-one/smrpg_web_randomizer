from django.core.management.base import BaseCommand
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.room_names import *
from randomizer.types.constants.coords import *
from randomizer.types.variables.variables import *
from randomizer.types.variables.classes import Flag, ShortVar, ByteVar
from randomizer.data.eventscripts.events import scripts as e_scripts
from randomizer.data.actionscripts.actions import scripts as a_scripts

from randomizer.types.actionscripts.commands import *

from randomizer.management.disassembler_common import (
    writeline,
)

import sys, re

DIRECTIONS = [
    "EAST",
    "SOUTHEAST",
    "SOUTH",
    "SOUTHWEST",
    "WEST",
    "NORTHWEST",
    "NORTH",
    "NORTHEAST",
]

AREA_OBJECTS = [
    "MARIO",
    "TOADSTOOL",
    "BOWSER",
    "GENO",
    "MALLOW",
    "DUMMY_0X05",
    "DUMMY_0X06",
    "DUMMY_0X07",
    "CHARACTER_IN_SLOT_1",
    "CHARACTER_IN_SLOT_2",
    "CHARACTER_IN_SLOT_3",
    "DUMMY_0X0B",
    "SCREEN_FOCUS",
    "LAYER_1",
    "LAYER_2",
    "LAYER_3",
    "MEM_70A8",
    "MEM_70A9",
    "MEM_70AA",
    "MEM_70AB",
    "NPC_0",
    "NPC_1",
    "NPC_2",
    "NPC_3",
    "NPC_4",
    "NPC_5",
    "NPC_6",
    "NPC_7",
    "NPC_8",
    "NPC_9",
    "NPC_10",
    "NPC_11",
    "NPC_12",
    "NPC_13",
    "NPC_14",
    "NPC_15",
    "NPC_16",
    "NPC_17",
    "NPC_18",
    "NPC_19",
    "NPC_20",
    "NPC_21",
    "NPC_22",
    "NPC_23",
    "NPC_24",
    "NPC_25",
    "NPC_26",
    "NPC_27",
]

sys.stdout.reconfigure(encoding="utf-8")

searchable_vars = globals()


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] == obj]


def nameflag(byte, bit, namespace):
    return [
        name
        for name in namespace
        if isinstance(namespace[name], Flag)
        and namespace[name].byte == byte
        and namespace[name].bit == bit
    ]


def namevar(byte, namespace):
    return [
        name
        for name in namespace
        if (
            isinstance(namespace[name], ShortVar)
            or isinstance(namespace[name], ByteVar)
        )
        and int(namespace[name]) == int(byte)
    ]


def get_var_name_string(id, prefix):
    candidates = namestr(id, searchable_vars)
    r = re.compile("^%s.*" % prefix)
    newlist = list(filter(r.match, candidates))
    if len(newlist) != 1:
        print("%s %r" % (prefix, id))
        raise Exception(newlist)
    return newlist[0]


def get_flag(addr, bit):
    candidates = nameflag(addr, bit, searchable_vars)
    if len(candidates) != 1:
        print(f"0x{addr:04X}.{bit}")
        raise Exception(candidates)
    return candidates[0]


def get_var(addr):
    candidates = namevar(addr, searchable_vars)
    if len(candidates) != 1:
        print(f"0x{addr:04X}.{bit}")
        raise Exception(candidates)
    return candidates[0]


def get_event_name(id):
    return get_var_name_string(id, "E")


def get_action_name(id):
    return get_var_name_string(id, "A")


def get_packet_name(id):
    return get_var_name_string(id, "P")


def get_sound_name(id):
    return get_var_name_string(id, "S")


def get_room_name(id):
    return get_var_name_string(id, "R")


actions_jumped_to = []
events_jumped_to = []


def convert_action_script_command(cmd, valid_identifiers):
    use_identifier: bool = cmd["identifier"] in valid_identifiers
    args = {}
    cls = None
    cmdargs = []
    include_argnames = True

    if "args" in cmd:
        cmdargs = cmd["args"]

    if cmd["command"] == "visibility_on":
        cls = "VisibilityOn"
    elif cmd["command"] == "visibility_off":
        cls = "VisibilityOff"
    elif cmd["command"] == "sequence_playback_on":
        cls = "SequencePlaybackOn"
    elif cmd["command"] == "sequence_playback_off":
        cls = "SequencePlaybackOff"
    elif cmd["command"] == "sequence_looping_on":
        cls = "SequenceLoopingOn"
    elif cmd["command"] == "sequence_looping_off":
        cls = "SequenceLoopingOff"
    elif cmd["command"] == "fixed_f_coord_on":
        cls = "FixedFCoordOn"
    elif cmd["command"] == "fixed_f_coord_off":
        cls = "FixedFCoordOff"
    elif cmd["command"] == "set_sprite_sequence":
        cls = "SetSpriteSequence"
        args["index"] = str(cmdargs[0])
        if cmdargs[1] > 0:
            args["sprite_offset"] = str(cmdargs[1])
        flags = cmdargs[2]
        if 3 in flags:
            args["is_mold"] = "True"
        if 4 in flags:
            args["looping_off"] = "True"
        if 6 in flags:
            args["is_sequence"] = "True"
        if 15 in flags:
            args["mirror_sprite"] = "True"
    elif cmd["command"] == "reset_properties":
        cls = "ResetProperties"
    elif cmd["command"] in [
        "overwrite_solidity",
        "set_solidity_bits",
        "clear_solidity_bits",
        "set_movement_bits",
    ]:
        if cmd["command"] == "overwrite_solidity":
            cls = "OverwriteSolidity"
        elif cmd["command"] == "set_solidity_bits":
            cls = "SetSolidityBits"
        elif cmd["command"] == "clear_solidity_bits":
            cls = "ClearSolidityBits"
        elif cmd["command"] == "set_movement_bits":
            cls = "SetMovementsBits"
        flags = cmdargs[0]
        if 0 in flags:
            args["bit_0"] = "True"
        if 1 in flags:
            args["cant_walk_under"] = "True"
        if 2 in flags:
            args["cant_pass_walls"] = "True"
        if 3 in flags:
            args["cant_jump_through"] = "True"
        if 4 in flags:
            args["bit_4"] = "True"
        if 5 in flags:
            args["cant_pass_npcs"] = "True"
        if 6 in flags:
            args["cant_walk_through"] = "True"
        if 7 in flags:
            args["bit_7"] = "True"
    elif cmd["command"] == "set_palette_row":
        cls = "SetPaletteRow"
        include_argnames = False
        args["row"] = str(cmdargs[0])
    elif cmd["command"] == "inc_palette_row_by":
        cls = "IncPaletteRowBy"
        include_argnames = False
        args["rows"] = str(cmdargs[0] & 0x0F)
    elif cmd["command"] == "set_animation_speed":
        speed = cmdargs[0]
        if speed == 0:
            args["speed"] = "NORMAL"
        elif speed == 1:
            args["speed"] = "FAST"
        elif speed == 2:
            args["speed"] = "FASTER"
        elif speed == 3:
            args["speed"] = "VERY_FAST"
        elif speed == 4:
            args["speed"] = "FASTEST"
        elif speed == 5:
            args["speed"] = "SLOW"
        elif speed == 6:
            args["speed"] = "VERY_SLOW"
        else:
            raise Exception("illegal speed")
        flags = cmdargs[1]
        if 0 in flags and 1 not in flags:
            cls = "SetWalkingSpeed"
        elif 1 in flags and 0 not in flags:
            cls = "SetSequenceSpeed"
        elif 0 in flags and 1 in flags:
            cls = "SetAllSpeeds"
        else:
            raise Exception("%s %r speed has no type" % (cmd["identifier"], flags))
    elif cmd["command"] == "set_object_memory_bits":
        cls = "SetObjectMemoryBits"
        args["arg_1"] = f"0x{cmdargs[0]:02X}"
        bits = cmdargs[1]
        if len(bits) > 0:
            args["bits"] = "%r" % bits
    elif cmd["command"] == "set_vram_priority":
        cls = "SetVRAMPriority"
        priority = cmdargs[0]
        include_argnames = False
        if priority == 0:
            args["priority"] = "MARIO_OVERLAPS_ON_ALL_SIDES"
        elif priority == 1:
            args["priority"] = "NORMAL"
        elif priority == 2:
            args["priority"] = "OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES"
        elif priority == 3:
            args["priority"] = "PRIORITY_3"
    elif cmd["command"] == "bpl_26_27_28":
        cls = "BPL262728"
    elif cmd["command"] == "bmi_26_27_28":
        cls = "BMI262728"
    elif cmd["command"] == "embedded_animation_routine":
        cls = "EmbeddedAnimationRoutine"
        include_argnames = False
        args["args"] = "%r" % bytearray(cmdargs)
    elif cmd["command"] == "bpl_26_27":
        cls = "BPL2627"
    elif (
        cmd["command"] == "jmp_if_object_within_range"
        or cmd["command"] == "jmp_if_object_within_range_same_z"
    ):
        if cmd["command"] == "jmp_if_object_within_range":
            cls = "JmpIfObjectWithinRange"
        elif cmd["command"] == "jmp_if_object_within_range_same_z":
            cls = "JmpIfObjectWithinRangeSameZ"
        args["object"] = AREA_OBJECTS[cmdargs[0]]
        args["usually"] = str(cmdargs[1])
        args["tiles"] = str(cmdargs[2])
        args["destinations"] = '["%s"]' % cmdargs[3]
    elif cmd["command"] == "unknown_jmp_3C":
        cls = "UnknownJmp3C"
        include_argnames = False
        args["arg1"] = f"0x{cmdargs[0]:02X}"
        args["arg2"] = f"0x{cmdargs[1]:02X}"
        args["destinations"] = '["%s"]' % cmdargs[2]
    elif cmd["command"] == "jmp_if_mario_in_air":
        cls = "JmpIfMarioInAir"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "create_packet_at_npc_coords":
        cls = "CreatePacketAtNPCCoords"
        args["packet_id"] = get_packet_name(cmdargs[0])
        args["object"] = AREA_OBJECTS[cmdargs[1]]
        args["destinations"] = '["%s"]' % cmdargs[2]
    elif cmd["command"] == "create_packet_at_7010":
        cls = "CreatePacketAtNPCCoords"
        args["packet_id"] = get_packet_name(cmdargs[0])
        args["destinations"] = '["%s"]' % cmdargs[1]
    elif cmd["command"] == "walk_1_step_east":
        cls = "Walk1StepEast"
    elif cmd["command"] == "walk_1_step_southeast":
        cls = "Walk1StepSoutheast"
    elif cmd["command"] == "walk_1_step_south":
        cls = "Walk1StepSouth"
    elif cmd["command"] == "walk_1_step_southwest":
        cls = "Walk1StepSouthwest"
    elif cmd["command"] == "walk_1_step_west":
        cls = "Walk1StepWest"
    elif cmd["command"] == "walk_1_step_northwest":
        cls = "Walk1StepNorthwest"
    elif cmd["command"] == "walk_1_step_north":
        cls = "Walk1StepNorth"
    elif cmd["command"] == "walk_1_step_northeast":
        cls = "Walk1StepNortheast"
    elif cmd["command"] == "walk_1_step_f_direction":
        cls = "Walk1StepFDirection"
    elif cmd["command"] == "add_z_coord_1_step":
        cls = "AddZCoord1Step"
    elif cmd["command"] == "dec_z_coord_1_step":
        cls = "DecZCoord1Step"
    elif cmd["command"] == "shift_east_steps":
        cls = "ShiftEastSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_southeast_steps":
        cls = "ShiftSoutheastSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_south_steps":
        cls = "ShiftSouthSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_southwest_steps":
        cls = "ShiftSouthwestSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_west_steps":
        cls = "ShiftWestSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_northwest_steps":
        cls = "ShiftNorthwestSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_north_steps":
        cls = "ShiftNorthSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_northeast_steps":
        cls = "ShiftNortheastSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_f_direction_steps":
        cls = "ShiftFDirectionSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_z_20_steps":
        cls = "ShiftZ20Steps"
    elif cmd["command"] == "shift_z_up_steps":
        cls = "ShiftZUpSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_z_down_steps":
        cls = "ShiftZDownSteps"
        include_argnames = False
        args["steps"] = str(cmdargs[0])
    elif cmd["command"] == "shift_z_up_20_steps":
        cls = "ShiftZUp20Steps"
    elif cmd["command"] == "shift_z_down_20_steps":
        cls = "ShiftZDown20Steps"
    elif cmd["command"] == "shift_east_pixels":
        cls = "ShiftEastPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "shift_southeast_pixels":
        cls = "ShiftSoutheastPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "shift_south_pixels":
        cls = "ShiftSouthPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "shift_southwest_pixels":
        cls = "ShiftSouthwestPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "shift_west_pixels":
        cls = "ShiftWestPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "shift_northwest_pixels":
        cls = "ShiftNorthwestPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "shift_north_pixels":
        cls = "ShiftNorthPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "shift_northeast_pixels":
        cls = "ShiftNortheastPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "shift_f_direction_pixels":
        cls = "ShiftFDirectionPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "walk_f_direction_16_pixels":
        cls = "WalkFDirection16Pixels"
    elif cmd["command"] == "shift_z_up_pixels":
        cls = "ShiftZUpPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "shift_z_down_pixels":
        cls = "ShiftZDownPixels"
        include_argnames = False
        args["pixels"] = str(cmdargs[0])
    elif cmd["command"] == "face_east":
        cls = "FaceEast"
    elif cmd["command"] == "face_east_7C":
        cls = "FaceEast7C"
    elif cmd["command"] == "face_southeast":
        cls = "FaceSoutheast"
    elif cmd["command"] == "face_south":
        cls = "FaceSouth"
    elif cmd["command"] == "face_southwest":
        cls = "FaceSouthwest"
    elif cmd["command"] == "face_southwest_7D":
        cls = "FaceSouthwest7D"
    elif cmd["command"] == "face_west":
        cls = "FaceWest"
    elif cmd["command"] == "face_northwest":
        cls = "FaceNorthwest"
    elif cmd["command"] == "face_north":
        cls = "FaceNorth"
    elif cmd["command"] == "face_northeast":
        cls = "FaceNortheast"
    elif cmd["command"] == "face_mario":
        cls = "FaceMario"
    elif cmd["command"] == "turn_clockwise_45_degrees":
        cls = "TurnClockwise45Degrees"
    elif cmd["command"] == "turn_random_direction":
        cls = "TurnRandomDirection"
    elif cmd["command"] == "turn_clockwise_45_degrees_n_times":
        cls = "TurnClockwise45DegreesNTimes"
        include_argnames = False
        args["count"] = str(cmdargs[0])
    elif (
        cmd["command"] == "jump_to_height_silent" or cmd["command"] == "jump_to_height"
    ):
        cls = "JumpToHeight"
        args["height"] = str(cmdargs[0])
        if cmd["command"] == "jump_to_height_silent":
            args["silent"] = "True"
        else:
            include_argnames = False
    elif cmd["command"] in [
        "walk_to_xy_coords",
        "walk_xy_steps",
        "shift_to_xy_coords",
        "shift_xy_steps",
        "shift_xy_pixels",
    ]:
        if cmd["command"] == "walk_to_xy_coords":
            cls = "WalkToXYCoords"
        elif cmd["command"] == "walk_xy_steps":
            cls = "WalkXYSteps"
        elif cmd["command"] == "shift_to_xy_coords":
            cls = "ShiftToXYCoords"
        elif cmd["command"] == "shift_xy_steps":
            cls = "ShiftXYSteps"
        elif cmd["command"] == "shift_xy_pixels":
            cls = "ShiftXYPixels"
        args["x"] = str(cmdargs[0])
        args["y"] = str(cmdargs[1])
    elif cmd["command"] == "maximize_sequence_speed":
        cls = "MaximizeSequenceSpeed"
    elif cmd["command"] == "maximize_sequence_speed_86":
        cls = "MaximizeSequenceSpeed86"
    elif cmd["command"] == "transfer_to_object_xy":
        cls = "TransferToObjectXY"
        include_argnames = False
        args["object"] = AREA_OBJECTS[cmdargs[0]]
    elif cmd["command"] == "run_away_shift":
        cls = "RunAwayShift"
    elif cmd["command"] == "transfer_to_7016_7018":
        cls = "TransferTo70167018"
    elif cmd["command"] == "walk_to_7016_7018":
        cls = "WalkTo70167018"
    elif (
        cmd["command"] == "bounce_to_xy_with_height"
        or cmd["command"] == "bounce_xy_steps_with_height"
    ):
        if cmd["command"] == "bounce_to_xy_with_height":
            cls = "BounceToXYWithHeight"
        elif cmd["command"] == "bounce_xy_steps_with_height":
            cls = "BounceXYStepsWithHeight"
        args["x"] = str(cmdargs[0])
        args["y"] = str(cmdargs[1])
        args["height"] = str(cmdargs[2])
    elif cmd["command"] in [
        "transfer_to_xyzf",
        "transfer_xyzf_steps",
        "transfer_xyzf_pixels",
    ]:
        if cmd["command"] == "transfer_to_xyzf":
            cls = "TransferToXYZF"
        elif cmd["command"] == "transfer_xyzf_steps":
            cls = "TransferXYZFSteps"
        elif cmd["command"] == "transfer_xyzf_pixels":
            cls = "TransferXYZFPixels"
        args["x"] = str(cmdargs[0])
        args["y"] = str(cmdargs[1])
        args["z"] = str(cmdargs[2])
        args["direction"] = DIRECTIONS[cmdargs[3]]
    elif cmd["command"] == "transfer_to_object_xyz":
        cls = "TransferToObjectXYZ"
        include_argnames = False
        args["object"] = AREA_OBJECTS[cmdargs[0]]
    elif cmd["command"] == "walk_to_7016_7018_701A":
        cls = "WalkTo70167018701A"
    elif cmd["command"] == "transfer_to_7016_7018_701A":
        cls = "TransferTo70167018701A"
    elif cmd["command"] == "stop_sound":
        cls = "StopSound"
    elif cmd["command"] == "play_sound":
        cls = "PlaySound"
        args["sound"] = get_sound_name(cmdargs[0])
        args["channel"] = str(cmdargs[1])
    elif cmd["command"] == "play_sound_balance":
        cls = "PlaySoundBalance"
        args["sound"] = get_sound_name(cmdargs[0])
        args["balance"] = str(cmdargs[1])
    elif cmd["command"] == "fade_out_sound_to_volume":
        cls = "FadeOutSoundToVolume"
        args["duration"] = str(cmdargs[0])
        args["volume"] = str(cmdargs[1])
    elif cmd["command"] == "set_bit":
        cls = "SetBit"
        include_argnames = False
        args["flag"] = get_flag(cmdargs[0], cmdargs[1])
    elif cmd["command"] == "set_mem_704x_at_700C_bit":
        cls = "SetMem704XAt700CBit"
    elif cmd["command"] == "clear_bit":
        cls = "ClearBit"
        include_argnames = False
        args["flag"] = get_flag(cmdargs[0], cmdargs[1])
    elif cmd["command"] == "clear_mem_704x_at_700C_bit":
        cls = "ClearMem704XAt700CBit"
    elif cmd["command"] == "set_var_to_const":
        cls = "SetVarToConst"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
        args["value"] = str(cmdargs[1])
    elif cmd["command"] == "add_const_to_var":
        cls = "AddConstToVar"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
        args["value"] = str(cmdargs[1])
    elif cmd["command"] == "inc" or cmd["command"] == "inc_short":
        cls = "Inc"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
    elif cmd["command"] == "dec":
        cls = "Dec"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
    elif cmd["command"] == "copy_var_to_var":
        cls = "CopyVarToVar"
        args["from_var"] = get_var(cmdargs[0])
        args["to_var"] = get_var(cmdargs[1])
    elif cmd["command"] == "set_var_to_random":
        cls = "SetVarToRandom"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
        args["value"] = str(cmdargs[1])
    elif cmd["command"] == "add_var_to_700C":
        cls = "AddVarTo700C"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
    elif (
        cmd["command"] == "dec_var_from_700C"
        or cmd["command"] == "dec_short_mem_from_700C"
    ):
        cls = "DecVarFrom700C"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
    elif cmd["command"] == "swap_vars":
        cls = "SwapVars"
        include_argnames = False
        args["from_var"] = get_var(cmdargs[0])
        args["to_var"] = get_var(cmdargs[1])
    elif cmd["command"] == "move_7010_7015_to_7016_701B":
        cls = "Move70107015To7016701B"
    elif cmd["command"] == "move_7016_701B_to_7010_7015":
        cls = "Move7016701BTo70107015"
    elif cmd["command"] == "compare_var_to_const":
        cls = "CompareVarToConst"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
        args["value"] = str(cmdargs[1])
    elif cmd["command"] == "compare_700C_to_var":
        cls = "DecVarFrom700C"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
    elif cmd["command"] == "set_700C_to_current_level":
        cls = "Set700CToCurrentLevel"
    elif cmd["command"] == "set_700C_to_object_coord":
        cls = "Set700CToObjectCoord"
        args["object"] = AREA_OBJECTS[cmdargs[0]]
        coord = cmdargs[1]
        if coord == 0:
            args["coord"] = "X"
        elif coord == 1:
            args["coord"] = "Y"
        elif coord == 2:
            args["coord"] = "Z"
        elif coord == 5:
            args["coord"] = "F"
        if len(cmdargs) > 3 and cmdargs[3] > 0:
            args["isometric"] = True
        else:
            args["pixel"] = True
        if len(cmdargs[2]) > 0:
            args["bit_7"] = "True"
    elif cmd["command"] == "set_700C_to_pressed_button":
        cls = "Set700CToPressedButton"
    elif cmd["command"] == "set_700C_to_tapped_button":
        cls = "Set700CToTappedButton"
    elif cmd["command"] == "jmp_to_script":
        cls = "JmpToScript"
        include_argnames = False
        args["destination"] = get_action_name(cmdargs[0])
    elif cmd["command"] == "jmp":
        cls = "Jmp"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "jmp_to_subroutine":
        cls = "JmpToSubroutine"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "start_loop_n_times":
        cls = "StartLoopNTimes"
        include_argnames = False
        args["count"] = str(cmdargs[0])
    elif cmd["command"] == "start_loop_n_frames":
        cls = "StartLoopNFrames"
        include_argnames = False
        args["length"] = str(cmdargs[0])
    elif cmd["command"] == "load_mem":
        cls = "LoadMemory"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
    elif cmd["command"] == "end_loop":
        cls = "EndLoop"
    elif cmd["command"] == "jmp_if_bit_clear":
        cls = "JmpIfBitClear"
        include_argnames = False
        args["bit"] = get_flag(cmdargs[0], cmdargs[1])
        args["destinations"] = '["%s"]' % cmdargs[2]
    elif cmd["command"] == "jmp_if_bit_set":
        cls = "JmpIfBitSet"
        include_argnames = False
        args["bit"] = get_flag(cmdargs[0], cmdargs[1])
        args["destinations"] = '["%s"]' % cmdargs[2]
    elif cmd["command"] == "jmp_if_mem_704x_at_700C_bit_set":
        cls = "JmpIfMem704XAt700CBitSet"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "jmp_if_mem_704x_at_700C_bit_clear":
        cls = "JmpIfMem704XAt700CBitClear"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "jmp_if_var_equals_const":
        cls = "JmpIfVarEqualsConst"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
        args["value"] = str(cmdargs[1])
        args["destinations"] = '["%s"]' % cmdargs[2]
    elif cmd["command"] == "jmp_if_var_not_equals_const":
        cls = "JmpIfVarNotEqualsConst"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
        args["value"] = str(cmdargs[1])
        args["destinations"] = '["%s"]' % cmdargs[2]
    elif cmd["command"] in ["jmp_if_700C_all_bits_clear", "jmp_if_700C_any_bits_set"]:
        if cmd["command"] == "jmp_if_700C_all_bits_clear":
            cls = "JmpIf700CAllBitsClear"
        elif cmd["command"] == "jmp_if_700C_any_bits_set":
            cls = "JmpIf700CAnyBitsSet"
        bits = cmdargs[0]
        if len(bits) > 0:
            args["bits"] = "%r" % bits
        args["destinations"] = '["%s"]' % cmdargs[1]
    elif cmd["command"] == "jmp_if_random_above_128":
        cls = "JmpIfRandom1of2"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "jmp_if_random_above_66":
        cls = "JmpIfRandom2of3"
        include_argnames = False
        args["destinations"] = "%r" % cmdargs
    elif cmd["command"] == "jmp_if_loaded_memory_is_0":
        cls = "JmpIfLoadedMemoryIs0"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "jmp_if_loaded_memory_is_not_0":
        cls = "JmpIfLoadedMemoryIsNot0"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "jmp_if_comparison_result_is_greater_or_equal":
        cls = "JmpIfComparisonResultIsGreaterOrEqual"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "jmp_if_comparison_result_is_lesser":
        cls = "JmpIfComparisonResultIsLesser"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "jmp_if_loaded_memory_is_below_0":
        cls = "JmpIfLoadedMemoryIsBelow0"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "jmp_if_loaded_memory_is_above_or_equal_0":
        cls = "JmpIfLoadedMemoryIsAboveOrEqual0"
        include_argnames = False
        args["destinations"] = '["%s"]' % cmdargs[0]
    elif cmd["command"] == "pause":
        cls = "Pause"
        include_argnames = False
        args["length"] = str(cmdargs[0])
    elif cmd["command"] in [
        "summon_to_level",
        "remove_from_level",
        "enable_trigger_in_level",
        "disable_trigger_in_level",
    ]:
        if cmd["command"] == "summon_to_level":
            cls = "SummonToLevel"
        elif cmd["command"] == "remove_from_level":
            cls = "RemoveFromLevel"
        elif cmd["command"] == "enable_trigger_in_level":
            cls = "EnableTriggerInLevel"
        elif cmd["command"] == "disable_trigger_in_level":
            cls = "DisableTriggerInLevel"
        include_argnames = False
        args["object"] = AREA_OBJECTS[cmdargs[0]]
        args["level_id"] = get_room_name(cmdargs[1])
    elif cmd["command"] == "summon_object_at_70A8_to_current_level":
        cls = "SummonObjectAt70A8ToCurrentLevel"
    elif cmd["command"] == "remove_object_at_70A8_from_current_level":
        cls = "RemoveObjectAt70A8FromCurrentLevel"
    elif cmd["command"] == "enable_trigger_at_70A8":
        cls = "EnableTriggerAt70A8"
    elif cmd["command"] == "disable_trigger_at_70A8":
        cls = "DisableTriggerInLevel"
    elif cmd["command"] in ["jmp_if_object_in_level", "jmp_if_object_not_in_level"]:
        if cmd["command"] == "jmp_if_object_in_level":
            cls = "JmpIfObjectInSpecificLevel"
        elif cmd["command"] == "jmp_if_object_not_in_level":
            cls = "JmpIfObjectNotInSpecificLevel"
        cls = "JmpIfObjectInSpecificLevel"
        include_argnames = False
        args["object"] = AREA_OBJECTS[cmdargs[0]]
        args["level_id"] = get_room_name(cmdargs[1])
        args["destinations"] = '["%s"]' % cmdargs[2]
    elif cmd["command"] == "jmp_to_start_of_this_script":
        cls = "JmpToStartOfThisScript"
    elif cmd["command"] == "jmp_to_start_of_this_script_FA":
        cls = "JmpToStartOfThisScriptFA"
    elif cmd["command"] == "ret":
        cls = "Return"
    elif cmd["command"] == "end_all":
        cls = "EndAll"
    elif cmd["command"] == "shadow_on":
        cls = "ShadowOn"
    elif cmd["command"] == "shadow_off":
        cls = "ShadowOff"
    elif cmd["command"] == "floating_on":
        cls = "FloatingOn"
    elif cmd["command"] == "floating_off":
        cls = "FloatingOff"
    elif cmd["command"] in ["object_memory_set_bit", "object_memory_clear_bit"]:
        if cmd["command"] == "object_memory_set_bit":
            cls = "ObjectMemorySetBit"
        elif cmd["command"] == "object_memory_clear_bit":
            cls = "ObjectMemoryClearBit"
        args["arg_1"] = f"0x{cmdargs[0]:02X}"
        bits = cmdargs[1]
        if len(bits) > 0:
            args["bits"] = "%r" % bits
    elif cmd["command"] == "object_memory_modify_bits":
        cls = "ObjectMemoryModifyBits"
        args["arg_1"] = f"0x{cmdargs[0]:02X}"
        set_flags = cmdargs[1]
        if len(set_flags) > 0:
            args["set_flags"] = "%r" % set_flags
        clear_bits = cmdargs[2]
        if len(clear_bits) > 0:
            args["clear_bits"] = "%r" % clear_bits
    elif cmd["command"] == "set_priority":
        cls = "SetPriority"
        include_argnames = False
        args["priority"] = str(cmdargs[0])
    elif cmd["command"] == "jmp_if_object_in_air":
        cls = "JmpIfObjectInAir"
        include_argnames = False
        args["object"] = AREA_OBJECTS[cmdargs[0]]
        args["destinations"] = '["%s"]' % cmdargs[1]
    elif cmd["command"] == "create_packet_at_7010_with_event":
        cls = "CreatePacketAt7010WithEvent"
        args["packet_id"] = get_packet_name(cmdargs[0])
        args["event_id"] = get_event_name(cmdargs[1])
        args["destinations"] = '["%s"]' % cmdargs[2]
    elif cmd["command"] in [
        "mem_700C_xor_const",
        "mem_700C_or_const",
        "mem_700C_and_const",
    ]:
        if cmd["command"] == "mem_700C_and_const":
            cls = "Mem700CAndConst"
        elif cmd["command"] == "mem_700C_or_const":
            cls = "Mem700COrConst"
        elif cmd["command"] == "mem_700C_xor_const":
            cls = "Mem700CXorConst"
        include_argnames = False
        args["value"] = f"0x{cmdargs[0]:04X}"
    elif cmd["command"] in ["mem_700C_or_var", "mem_700C_and_var"]:
        if cmd["command"] == "mem_700C_and_var":
            cls = "Mem700CAndVar"
        elif cmd["command"] == "mem_700C_or_var":
            cls = "Mem700COrVar"
        elif cmd["command"] == "mem_700C_xor_var":
            cls = "Mem700CXorVar"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
    elif cmd["command"] == "mem_700C_shift_left":
        cls = "VarShiftLeft"
        include_argnames = False
        args["address"] = get_var(cmdargs[0])
        args["shift"] = str(cmdargs[1])
    elif cmd["command"] == "db":
        cls = "Db"
        include_argnames = False
        args["args"] = "%r" % bytearray(cmdargs)
    else:
        raise Exception("%s not found" % cmd["command"])

    return cls, args, use_identifier, include_argnames


def convert_action_script(script, valid_identifiers):
    new_script = []

    for cmd in script:
        # print(cmd["identifier"])
        identifier = ""
        cls, args, use_identifier, include_argnames = convert_action_script_command(
            cmd, valid_identifiers
        )

        if cls is not None:
            arg_strings = []
            for key in args:
                if include_argnames:
                    arg_strings.append("%s=%s" % (key, args[key]))
                else:
                    arg_strings.append(args[key])
            arg_string = ", ".join(arg_strings)

            if use_identifier:
                if len(arg_string) > 0:
                    arg_string += ", "
                identifier = 'identifier="%s"' % cmd["identifier"]

            output = "%s(%s%s)" % (cls, arg_string, identifier)
            new_script.append(output)

    return new_script


def produce_action_script(script, valid_identifiers):
    output = ""
    output += "#classes"
    output += "\nfrom randomizer.types.actionscripts.commands import *"
    output += "\nfrom randomizer.types.actionscripts.classes import ActionScript"
    output += "\n#ids"
    output += "\nfrom randomizer.types.eventscripts.constants.script_ids import *"
    output += "\nfrom randomizer.types.actionscripts.constants.script_ids import *"
    output += "\nfrom randomizer.types.packets.constants.packet_ids import *"
    output += "\nfrom randomizer.types.constants.sound_names import *"
    output += "\nfrom randomizer.types.constants.directions import *"
    output += "\n#types"
    output += "\nfrom randomizer.types.constants.area_objects import *"
    output += "\nfrom randomizer.types.constants.coords import *"
    output += "\nfrom randomizer.types.actionscripts.constants.sequence_speeds import *"
    output += "\nfrom randomizer.types.actionscripts.constants.vram_priority import *"
    output += "\nfrom randomizer.types.variables.variables import *"
    output += "\n\nscript = ActionScript([\n\t"

    contents = convert_action_script(script, valid_identifiers)
    output += ",\n\t".join(contents)

    output += "\n])"

    return output


class Command(BaseCommand):
    def handle(self, *args, **options):

        ajt = []
        ejt = []

        for i, script_dict in enumerate(a_scripts):
            # print(get_action_name(i))
            for cmd in script_dict:
                if "args" in cmd:
                    ajt.extend([a for a in cmd["args"] if isinstance(a, str)])
            actions_jumped_to.extend(list(set(ajt)))

        for i, script_dict in enumerate(e_scripts):
            # print(get_event_name(i))
            for cmd in script_dict:
                if "args" in cmd:
                    ejt.extend([a for a in cmd["args"] if isinstance(a, str)])
                if "subscript" in cmd:
                    for ccmd in cmd["subscript"]:
                        if "args" in ccmd:
                            ejt.extend([a for a in ccmd["args"] if isinstance(a, str)])
            events_jumped_to.extend(list(set(ejt)))

        for i, script in enumerate(a_scripts):
            output = produce_action_script(script, actions_jumped_to)
            file = open("randomizer/data/actionscripts_new/script_%i.py" % (i), "w")
            writeline(file, output)
            file.close()
