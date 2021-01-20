from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3293_jmp_fork_mario_on_object_0',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_3293_pause_action_script_5', 'EVENT_3293_pause_action_script_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3293_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3293_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3293_run_background_event_3',
        "command": 'run_background_event',
        "args": [3294, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3293_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3293_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3293_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3293_action_queue_sync_6_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_6_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._066_KICK_BALL_SHELL, 4]
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_6_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_6_SUBSCRIPT_floating_on_3',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_6_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_6_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_6_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3293_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3293_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3293_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3293_action_queue_sync_9_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_9_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._066_KICK_BALL_SHELL, 4]
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_9_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_9_SUBSCRIPT_floating_on_3',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_9_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_9_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3293_action_queue_sync_9_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3293_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
