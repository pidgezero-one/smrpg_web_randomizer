from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1552_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7047, 0, 'EVENT_1552_fade_in_from_black_sync_10']
    },
    {
        "identifier": 'EVENT_1552_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1552_action_queue_async_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1552_freeze_all_npcs_until_return_2',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1552_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1552_freeze_camera_4',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1552_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 482]
    },
    {
        "identifier": 'EVENT_1552_set_action_script_async_6',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1552_unfreeze_camera_7',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_1552_unfreeze_all_npcs_8',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_1552_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1552_set_11']
    },
    {
        "identifier": 'EVENT_1552_fade_in_from_black_sync_10',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1552_set_11',
        "command": 'set',
        "args": [0x70a9, 20]
    },
    {
        "identifier": 'EVENT_1552_start_loop_n_times_12',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'EVENT_1552_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1552_action_queue_sync_13_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1552_inc_14',
        "command": 'inc',
        "args": [0x70a9]
    },
    {
        "identifier": 'EVENT_1552_end_loop_15',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1552_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1552_action_queue_async_16_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1552_set_17',
        "command": 'set',
        "args": [0x70ab, 28]
    },
    {
        "identifier": 'EVENT_1552_run_background_event_18',
        "command": 'run_background_event',
        "args": [1553, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1552_ret_19',
        "command": 'ret'
    }
]
