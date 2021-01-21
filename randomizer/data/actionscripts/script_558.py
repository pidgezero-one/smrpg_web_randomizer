from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_558_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_558_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_558_set_random_2',
        "command": 'set_random',
        "args": [0x700c, 112]
    },
    {
        "identifier": 'ACTION_558_add_3',
        "command": 'add',
        "args": [0x700c, 32]
    },
    {
        "identifier": 'ACTION_558_load_mem_4',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_558_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_558_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_558_set_700C_to_pressed_button_7',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_558_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 36, 'ACTION_558_visibility_on_10']
    },
    {
        "identifier": 'ACTION_558_set_priority_9',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_558_visibility_on_10',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [16, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_shadow_off_12',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_558_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._084_SMOKED, 4]
    },
    {
        "identifier": 'ACTION_558_pause_14',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_db_16',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_558_db_17',
        "command": 'db',
        "args": [0x25, 0x00, 0x0c, 0x70, 0xff]
    },
    {
        "identifier": 'ACTION_558_pause_18',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'ACTION_558_bpl_26_27_28_19',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_20',
        "command": 'set_sprite_sequence',
        "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_pause_21',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_22',
        "command": 'set_sprite_sequence',
        "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_pause_23',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_24',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_pause_25',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_26',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_pause_27',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_558_start_loop_n_times_28',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_29',
        "command": 'set_sprite_sequence',
        "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_pause_30',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_31',
        "command": 'set_sprite_sequence',
        "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_pause_32',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_33',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_pause_34',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_35',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_pause_36',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_558_end_loop_37',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_38',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_set_random_39',
        "command": 'set_random',
        "args": [0x700c, 18]
    },
    {
        "identifier": 'ACTION_558_add_40',
        "command": 'add',
        "args": [0x700c, 8]
    },
    {
        "identifier": 'ACTION_558_load_mem_41',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_558_pause_42',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_558_end_loop_43',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_558_db_44',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_558_db_45',
        "command": 'db',
        "args": [0x25, 0x00, 0x00, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_558_pause_46',
        "command": 'pause',
        "args": [21]
    },
    {
        "identifier": 'ACTION_558_set_sprite_sequence_47',
        "command": 'set_sprite_sequence',
        "args": [16, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_558_pause_48',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_558_jmp_49',
        "command": 'jmp',
        "args": ['ACTION_558_visibility_off_0']
    }
]
