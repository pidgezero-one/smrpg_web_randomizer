from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3337_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3337_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3337_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 4, 'EVENT_3337_set_bit_7']
    },
    {
        "identifier": 'EVENT_3337_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 5, 'EVENT_3337_set_bit_7']
    },
    {
        "identifier": 'EVENT_3337_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 6, 'EVENT_3337_set_bit_7']
    },
    {
        "identifier": 'EVENT_3337_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 7, 'EVENT_3337_set_bit_7']
    },
    {
        "identifier": 'EVENT_3337_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_3337_clear_bit_0']
    },
    {
        "identifier": 'EVENT_3337_set_bit_7',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3337_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3337_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3337_pause_8']
    },
    {
        "identifier": 'EVENT_3337_pause_10',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3337_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3337_action_queue_sync_11_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x15]
            },
            {
                "identifier": 'EVENT_3337_action_queue_sync_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3337_action_queue_sync_11_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3337_action_queue_sync_11_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3337_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3337_action_queue_sync_11_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3337_action_queue_sync_11_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3337_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_3337_jmp_if_bit_set_15']
    },
    {
        "identifier": 'EVENT_3337_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 935]
    },
    {
        "identifier": 'EVENT_3337_set_bit_14',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_3337_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_3337_jmp_if_bit_set_18']
    },
    {
        "identifier": 'EVENT_3337_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 935]
    },
    {
        "identifier": 'EVENT_3337_set_bit_17',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_3337_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_3337_jmp_if_bit_set_21']
    },
    {
        "identifier": 'EVENT_3337_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 935]
    },
    {
        "identifier": 'EVENT_3337_set_bit_20',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_3337_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3337_pause_24']
    },
    {
        "identifier": 'EVENT_3337_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 935]
    },
    {
        "identifier": 'EVENT_3337_set_bit_23',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3337_pause_24',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3337_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_3337_clear_bit_0']
    }
]
