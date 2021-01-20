from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1818_jmp_fork_mario_on_object_0',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1818_play_sound_13', 'EVENT_1818_jmp_if_bit_set_1'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704f, 4, 'EVENT_1818_run_dialog_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_run_dialog_2',
        "command": 'run_dialog',
        "args": [1284, AreaObjects.BOWSER, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_set_bit_3',
        "command": 'set_bit',
        "args": [0x704f, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_1818_run_dialog_duration_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_run_dialog_5',
        "command": 'run_dialog',
        "args": [1285, AreaObjects.BOWSER, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_run_dialog_duration_6',
        "command": 'run_dialog_duration',
        "args": [1272, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_jmp_if_dialog_option_b_7',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1818_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_run_dialog_8',
        "command": 'run_dialog',
        "args": [1274, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1818_action_queue_async_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_run_dialog_10',
        "command": 'run_dialog',
        "args": [1273, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1818_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1818_action_queue_async_11_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1818_action_queue_async_11_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_1818_action_queue_async_11_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1818_action_queue_async_11_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1818_action_queue_async_11_SUBSCRIPT_shift_east_steps_5',
                "command": 'shift_east_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1818_action_queue_async_11_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1818_action_queue_async_11_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1818_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_run_dialog_14',
        "command": 'run_dialog',
        "args": [1275, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1818_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
