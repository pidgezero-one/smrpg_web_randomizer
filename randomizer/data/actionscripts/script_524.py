from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_524_sequence_looping_off_0',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_524_jmp_if_object_not_in_level_1',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'ACTION_524_sequence_looping_off_28']
    },
    {
        "identifier": 'ACTION_524_pause_2',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_524_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_524_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_524_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'ACTION_524_sequence_looping_off_28']
    },
    {
        "identifier": 'ACTION_524_pause_6',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_524_sequence_looping_off_7',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_524_jmp_if_object_not_in_level_8',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'ACTION_524_sequence_looping_off_28']
    },
    {
        "identifier": 'ACTION_524_pause_9',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_524_sequence_looping_on_10',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_524_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_524_pause_12',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_524_sequence_looping_off_13',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_524_pause_14',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_524_jmp_if_object_not_in_level_15',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'ACTION_524_sequence_looping_off_28']
    },
    {
        "identifier": 'ACTION_524_jump_to_height_16',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_524_pause_17',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_524_sequence_looping_on_18',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_524_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_524_pause_20',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'ACTION_524_sequence_looping_off_21',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_524_pause_22',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_524_face_southwest_23',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_524_pause_24',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_524_face_northwest_25',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_524_pause_26',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_524_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_524_sequence_looping_off_0']
    },
    {
        "identifier": 'ACTION_524_sequence_looping_off_28',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_524_pause_29',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_524_face_southwest_30',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_524_pause_31',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_524_face_northwest_32',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_524_pause_33',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_524_face_southwest_34',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_524_pause_35',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_524_face_northwest_36',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_524_pause_37',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_524_face_southwest_38',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_524_pause_39',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_524_set_animation_speed_40',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_524_set_animation_speed_41',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_524_shift_northeast_steps_42',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_524_shift_northwest_steps_43',
        "command": 'shift_northwest_steps',
        "args": [12]
    },
    {
        "identifier": 'ACTION_524_walk_to_xy_coords_44',
        "command": 'walk_to_xy_coords',
        "args": [22, 101]
    },
    {
        "identifier": 'ACTION_524_face_northwest_45',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_524_fixed_f_coord_on_46',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_524_sequence_playback_off_47',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_524_set_animation_speed_48',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_524_shift_southwest_pixels_49',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_524_shift_northeast_pixels_50',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_524_jmp_51',
        "command": 'jmp',
        "args": ['ACTION_524_shift_southwest_pixels_49']
    }
]
