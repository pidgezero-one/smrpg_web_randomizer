from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1800_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704f, 4, 'EVENT_1800_run_dialog_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1800_run_dialog_1',
        "command": 'run_dialog',
        "args": [1284, AreaObjects.MARIO, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1800_set_bit_2',
        "command": 'set_bit',
        "args": [0x704f, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1800_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_1800_run_dialog_duration_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1800_run_dialog_4',
        "command": 'run_dialog',
        "args": [1285, AreaObjects.MARIO, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1800_run_dialog_duration_5',
        "command": 'run_dialog_duration',
        "args": [1233, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1800_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_10',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_sequence_playback_off_12',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._028_PIPE_ENTRANCE, 4]
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_dec_z_coord_1_step_14',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_visibility_off_15',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1800_action_queue_async_6_SUBSCRIPT_db_16',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1800_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
