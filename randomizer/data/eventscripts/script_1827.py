from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1827_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x704d, 1]
    },
    {
        "identifier": 'EVENT_1827_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_1827_set_short_3']
    },
    {
        "identifier": 'EVENT_1827_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7095, 4]
    },
    {
        "identifier": 'EVENT_1827_set_short_3',
        "command": 'set_short',
        "args": [0x7038, 0x0e80]
    },
    {
        "identifier": 'EVENT_1827_set_short_4',
        "command": 'set_short',
        "args": [0x703a, 0x3a80]
    },
    {
        "identifier": 'EVENT_1827_set_short_5',
        "command": 'set_short',
        "args": [0x703c, 0x0200]
    },
    {
        "identifier": 'EVENT_1827_set_6',
        "command": 'set',
        "args": [0x70a9, 21]
    },
    {
        "identifier": 'EVENT_1827_start_loop_n_times_7',
        "command": 'start_loop_n_times',
        "args": [8]
    },
    {
        "identifier": 'EVENT_1827_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1827_action_queue_sync_8_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1827_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1827_inc_9',
        "command": 'inc',
        "args": [0x70a9]
    },
    {
        "identifier": 'EVENT_1827_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1827_start_loop_n_times_11',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1827_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1827_action_queue_sync_12_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1827_inc_13',
        "command": 'inc',
        "args": [0x70a9]
    },
    {
        "identifier": 'EVENT_1827_end_loop_14',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1827_set_15',
        "command": 'set',
        "args": [0x70a9, 21]
    },
    {
        "identifier": 'EVENT_1827_start_loop_n_times_16',
        "command": 'start_loop_n_times',
        "args": [8]
    },
    {
        "identifier": 'EVENT_1827_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 829]
    },
    {
        "identifier": 'EVENT_1827_inc_18',
        "command": 'inc',
        "args": [0x70a9]
    },
    {
        "identifier": 'EVENT_1827_end_loop_19',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1827_remove_from_current_level_20',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_1827_run_background_event_21',
        "command": 'run_background_event',
        "args": [1828, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1827_run_background_event_22',
        "command": 'run_background_event',
        "args": [1833, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_1827_jmp_to_event_23',
        "command": 'jmp_to_event',
        "args": [1829]
    }
]
