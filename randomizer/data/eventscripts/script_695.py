from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_695_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 65, 'EVENT_695_jmp_if_bit_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_run_dialog_2',
        "command": 'run_dialog',
        "args": [2120, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_run_dialog_3',
        "command": 'run_dialog',
        "args": [2121, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 7, 'EVENT_687_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_695_run_dialog_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_run_dialog_7',
        "command": 'run_dialog',
        "args": [2172, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_set_bit_8',
        "command": 'set_bit',
        "args": [0x7042, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_695_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_695_action_queue_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_695_action_queue_async_9_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_695_action_queue_async_9_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_695_action_queue_async_9_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_695_action_queue_async_9_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_695_action_queue_async_9_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [10]
            },
        ]
    },
    {
        "identifier": 'EVENT_695_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_run_dialog_12',
        "command": 'run_dialog',
        "args": [2052, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_695_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
