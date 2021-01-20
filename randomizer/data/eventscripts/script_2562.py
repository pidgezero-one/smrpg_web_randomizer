from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2562_enable_controls_0',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2562_freeze_camera_1',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2562_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2562_action_queue_async_2_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_2_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_2_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2562_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2562_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_floating_on_1',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2562_action_queue_async_4_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_walk_1_step_south_6',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_jmp_if_mario_in_air_8',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2562_action_queue_async_4_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_2562_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2562_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2562_unfreeze_camera_6',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2562_enable_controls_7',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2562_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2562_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
