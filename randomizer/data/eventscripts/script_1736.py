from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1736_add_short_0',
        "command": 'add_short',
        "args": [0x7030, 0x01]
    },
    {
        "identifier": 'EVENT_1736_jmp_if_var_not_equals_short_1',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7030, 4, 'EVENT_1736_pause_action_script_7']
    },
    {
        "identifier": 'EVENT_1736_set_bit_2',
        "command": 'set_bit',
        "args": [0x707c, 3]
    },
    {
        "identifier": 'EVENT_1736_pause_3',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1736_create_packet_at_object_coords_jmp_if_null_4',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._031_LEVELUP_TEXT, AreaObjects.MARIO, 'EVENT_1736_set_bit_2']
    },
    {
        "identifier": 'EVENT_1736_set_short_5',
        "command": 'set_short',
        "args": [0x7020, 0x0040]
    },
    {
        "identifier": 'EVENT_1736_run_background_event_with_pause_return_on_exit_6',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [254, 0x7020, [12, 13]]
    },
    {
        "identifier": 'EVENT_1736_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1736_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_overwrite_solidity_3',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_object_memory_clear_bit_4',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_floating_off_5',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_embedded_animation_routine_8',
                "command": 'embedded_animation_routine',
                "args": [0x26]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_embedded_animation_routine_9',
                "command": 'embedded_animation_routine',
                "args": [0x27]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0xfd, 0x24, 0x00, 0x07]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_jmp_if_random_above_128_11',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_1736_action_queue_sync_8_SUBSCRIPT_db_16']
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_jmp_if_random_above_128_12',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_1736_action_queue_sync_8_SUBSCRIPT_add_15']
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_add_13',
                "command": 'add',
                "args": [0x700c, 24]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_jmp_14',
                "command": 'jmp',
                "args": ['EVENT_1736_action_queue_sync_8_SUBSCRIPT_db_16']
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_add_15',
                "command": 'add',
                "args": [0x700c, 232]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_db_16',
                "command": 'db',
                "args": [0xfd, 0x25]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_db_17',
                "command": 'db',
                "args": [0x25, 0xa0, 0x08, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_jmp_if_bit_clear_18',
                "command": 'jmp_if_bit_clear',
                "args": [0x7076, 1, 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_pause_20']
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [88]
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_bpl_26_27_28_21',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_1736_action_queue_sync_8_SUBSCRIPT_visibility_off_22',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1736_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1736_ret_10',
        "command": 'ret'
    }
]
