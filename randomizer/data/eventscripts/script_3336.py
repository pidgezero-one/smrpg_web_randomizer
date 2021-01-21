from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3336_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 1023]
    },
    {
        "identifier": 'EVENT_3336_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 1023]
    },
    {
        "identifier": 'EVENT_3336_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 1023]
    },
    {
        "identifier": 'EVENT_3336_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 1023]
    },
    {
        "identifier": 'EVENT_3336_set_7000_to_current_level_4',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3336_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 363, 'EVENT_3336_jmp_if_object_not_in_level_7']
    },
    {
        "identifier": 'EVENT_3336_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 362, 'EVENT_3336_jmp_if_object_not_in_level_9']
    },
    {
        "identifier": 'EVENT_3336_jmp_if_object_not_in_level_7',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._363_VOLCANO_AREA_15_STOMPING_CORKPEDITE, 'EVENT_3336_run_event_as_subroutine_12']
    },
    {
        "identifier": 'EVENT_3336_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3336_action_queue_async_10']
    },
    {
        "identifier": 'EVENT_3336_jmp_if_object_not_in_level_9',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._362_VOLCANO_AREA_07_STOMPING_CORKPEDITE, 'EVENT_3336_run_event_as_subroutine_12']
    },
    {
        "identifier": 'EVENT_3336_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3336_action_queue_async_10_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3336_action_queue_async_10_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            },
            {
                "identifier": 'EVENT_3336_action_queue_async_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3336_action_queue_async_10_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3336_action_queue_async_10_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3336_run_background_event_11',
        "command": 'run_background_event',
        "args": [3337, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3336_run_event_as_subroutine_12',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3336_ret_13',
        "command": 'ret'
    }
]
