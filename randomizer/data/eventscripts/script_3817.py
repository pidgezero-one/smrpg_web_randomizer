from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3817_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._021_MUSHROOM_KINGDOM_CASTLE_BRANCH_ROOM_TO_VAULTGUEST_ROOM, RadialDirections.NORTHEAST, 13, 69, 1, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]]
    },
    {
        "identifier": 'EVENT_3817_ret_1',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3817_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7098, 7, 'EVENT_3817_pause_3']
    },
    {
        "identifier": 'EVENT_3817_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3817_jmp_if_mario_in_air_4',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3817_pause_3']
    },
    {
        "identifier": 'EVENT_3817_run_dialog_5',
        "command": 'run_dialog',
        "args": [3749, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3817_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3817_action_queue_sync_6_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3817_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3817_action_queue_async_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3817_action_queue_async_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3817_action_queue_async_7_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [4, 93]
            },
            {
                "identifier": 'EVENT_3817_action_queue_async_7_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3817_pause_8',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3817_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 99]
    },
    {
        "identifier": 'EVENT_3817_run_dialog_10',
        "command": 'run_dialog',
        "args": [3752, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3817_set_bit_11',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3817_pause_12',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3817_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 978]
    },
    {
        "identifier": 'EVENT_3817_ret_14',
        "command": 'ret'
    }
]
