from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_403_start_battle_0',
        "command": 'start_battle',
        "args": [0x000b, 28]
    },
    {
        "identifier": 'EVENT_403_set_bit_1',
        "command": 'set_bit',
        "args": [0x704a, 2]
    },
    {
        "identifier": 'EVENT_403_set_2',
        "command": 'set',
        "args": [0x70a9, 26]
    },
    {
        "identifier": 'EVENT_403_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [1010]
    },
    {
        "identifier": 'EVENT_403_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_403_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_403_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_403_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_403_action_queue_sync_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 119, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_403_action_queue_sync_6_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_403_start_embedded_action_script_async_7',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_403_start_embedded_action_script_async_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 120, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_403_start_embedded_action_script_async_7_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_403_start_embedded_action_script_async_7_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_403_start_embedded_action_script_async_7_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_403_remember_last_object_8',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_403_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_403_pause_10',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_403_run_dialog_11',
        "command": 'run_dialog',
        "args": [668, AreaObjects.NPC_7, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_403_unsync_dialog_12',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_403_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": [0x1725]
    },
    {
        "identifier": 'EVENT_403_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_403_action_queue_async_14_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            }
        ]
    },
    {
        "identifier": 'EVENT_403_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 128]
    },
    {
        "identifier": 'EVENT_403_ret_16',
        "command": 'ret'
    }
]
