from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_523_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'ACTION_523_sequence_looping_off_26']
    },
    {
        "identifier": 'ACTION_523_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_523_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_523_pause_3',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_523_sequence_looping_off_4',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_523_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'ACTION_523_sequence_looping_off_26']
    },
    {
        "identifier": 'ACTION_523_pause_6',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_523_sequence_looping_off_7',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_523_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_523_face_southwest_9',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_523_pause_10',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_523_face_southeast_11',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_523_pause_12',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_523_jmp_if_object_not_in_level_13',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'ACTION_523_sequence_looping_off_26']
    },
    {
        "identifier": 'ACTION_523_pause_14',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_523_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_523_sequence_looping_on_16',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_523_pause_17',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_523_sequence_looping_off_18',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_523_jmp_if_object_not_in_level_19',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'ACTION_523_sequence_looping_off_26']
    },
    {
        "identifier": 'ACTION_523_pause_20',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_523_face_southwest_21',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_523_pause_22',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_523_face_southeast_23',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_523_pause_24',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_523_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_523_jmp_if_object_not_in_level_0']
    },
    {
        "identifier": 'ACTION_523_sequence_looping_off_26',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_523_pause_27',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_523_face_southwest_28',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_523_pause_29',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_523_face_southeast_30',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_523_pause_31',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_523_face_southwest_32',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_523_pause_33',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_523_face_southeast_34',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_523_pause_35',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_523_face_southwest_36',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_523_pause_37',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_523_set_animation_speed_38',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_523_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_523_shift_northeast_steps_40',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_523_shift_northwest_steps_41',
        "command": 'shift_northwest_steps',
        "args": [12]
    },
    {
        "identifier": 'ACTION_523_walk_to_xy_coords_42',
        "command": 'walk_to_xy_coords',
        "args": [22, 101]
    },
    {
        "identifier": 'ACTION_523_face_northwest_43',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_523_fixed_f_coord_on_44',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_523_sequence_playback_off_45',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_523_set_animation_speed_46',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_523_shift_southwest_pixels_47',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_523_shift_northeast_pixels_48',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_523_jmp_49',
        "command": 'jmp',
        "args": ['ACTION_523_shift_southwest_pixels_47']
    }
]
