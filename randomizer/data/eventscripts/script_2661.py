from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2661_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 2, 'EVENT_2661_ret_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_set_bit_5',
        "command": 'set_bit',
        "args": [0x7046, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_add_6',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_run_dialog_7',
        "command": 'run_dialog',
        "args": [3321, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2661_action_queue_async_9_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2661_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2661_action_queue_async_9_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_2661_pause_10',
        "command": 'pause',
        "args": [40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_set_action_script_async_12',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2661_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
