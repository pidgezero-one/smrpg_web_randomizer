from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_678_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._131_JUMP_ON_ORGAN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_pause_6',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_stop_sound_7',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_678_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_678_action_queue_sync_8_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_678_action_queue_sync_8_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_678_action_queue_sync_8_SUBSCRIPT_jmp_if_mario_in_air_3',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_678_action_queue_sync_8_SUBSCRIPT_pause_2']
            },
        ]
    },
    {
        "identifier": 'EVENT_678_run_dialog_9',
        "command": 'run_dialog',
        "args": [2184, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_678_action_queue_async_10_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_678_action_queue_async_10_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_678_action_queue_async_10_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_678_action_queue_async_10_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_678_action_queue_async_10_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_678_action_queue_async_10_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_678_action_queue_async_10_SUBSCRIPT_pause_4']
            },
        ]
    },
    {
        "identifier": 'EVENT_678_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_678_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
