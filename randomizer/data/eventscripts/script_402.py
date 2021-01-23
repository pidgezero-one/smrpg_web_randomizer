from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_402_set_bit_0',
        "command": 'set_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_402_set_bit_1',
        "command": 'set_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_402_set_bit_2',
        "command": 'set_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_402_start_battle_3',
        "command": 'start_battle',
        "args": [0x000a, 28]
    },
    {
        "identifier": 'EVENT_402_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_402_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_402_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_402_action_queue_sync_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [17, 113, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_402_action_queue_sync_6_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_402_start_embedded_action_script_async_F1_7',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_402_start_embedded_action_script_async_F1_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [17, 114, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_402_start_embedded_action_script_async_F1_7_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_402_start_embedded_action_script_async_F1_7_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_402_set_bit_8',
        "command": 'set_bit',
        "args": [0x7049, 6]
    },
    {
        "identifier": 'EVENT_402_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_402_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_402_pause_11',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_402_run_dialog_12',
        "command": 'run_dialog',
        "args": [691, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_402_set_13',
        "command": 'set',
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_402_add_coins_14',
        "command": 'add_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_402_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_402_run_dialog_16',
        "command": 'run_dialog',
        "args": [515, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_402_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 98]
    },
    {
        "identifier": 'EVENT_402_ret_18',
        "command": 'ret'
    }
]
