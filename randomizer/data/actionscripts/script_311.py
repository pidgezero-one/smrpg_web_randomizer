from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_311_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_311_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_311_set_2',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'ACTION_311_face_mario_3',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_311_walk_1_step_f_direction_4',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_311_shadow_on_5',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_6',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_7',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 15, 'ACTION_311_set_700C_to_object_coord_12']
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_8',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_9',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 111, 'ACTION_311_set_700C_to_object_coord_12']
    },
    {
        "identifier": 'ACTION_311_set_10',
        "command": 'set',
        "args": [0x70ae, 1]
    },
    {
        "identifier": 'ACTION_311_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_311_face_mario_30']
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_12',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_13',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 15, 'ACTION_311_set_700C_to_object_coord_18']
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_14',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_15',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 113, 'ACTION_311_set_700C_to_object_coord_18']
    },
    {
        "identifier": 'ACTION_311_set_16',
        "command": 'set',
        "args": [0x70ae, 2]
    },
    {
        "identifier": 'ACTION_311_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_311_face_mario_30']
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_18',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_19',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 16, 'ACTION_311_set_700C_to_object_coord_24']
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_20',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_21',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 111, 'ACTION_311_set_700C_to_object_coord_24']
    },
    {
        "identifier": 'ACTION_311_set_22',
        "command": 'set',
        "args": [0x70ae, 3]
    },
    {
        "identifier": 'ACTION_311_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_311_face_mario_30']
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_24',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_25',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 16, 'ACTION_311_set_priority_0']
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_26',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_27',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 113, 'ACTION_311_set_priority_0']
    },
    {
        "identifier": 'ACTION_311_set_28',
        "command": 'set',
        "args": [0x70ae, 4]
    },
    {
        "identifier": 'ACTION_311_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_311_face_mario_30']
    },
    {
        "identifier": 'ACTION_311_face_mario_30',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_311_walk_1_step_f_direction_31',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_32',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_33',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 16, 'ACTION_311_set_priority_0']
    },
    {
        "identifier": 'ACTION_311_set_700C_to_object_coord_34',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_311_jmp_if_var_not_equals_short_35',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 112, 'ACTION_311_set_priority_0']
    },
    {
        "identifier": 'ACTION_311_jmp_36',
        "command": 'jmp',
        "args": ['ACTION_311_set_priority_0']
    }
]
