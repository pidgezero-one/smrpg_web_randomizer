from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1847_jmp_if_316D_is_3_0',
        "command": 'jmp_if_316D_is_3',
        "args": ['EVENT_1847_enable_controls_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_freeze_all_npcs_until_return_1',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_enable_controls_2',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1847_action_queue_async_4_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._089_LIT_FUSE, 4]
            },
            {
                "identifier": 'EVENT_1847_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1847_action_queue_async_4_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_1847_pause_5',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_create_packet_at_object_coords_jmp_if_null_6',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, AreaObjects.NPC_1, 'EVENT_1847_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._060_DYNAMITE_BOMB_EXPLOSION, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1847_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1847_action_queue_async_9_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1847_action_queue_async_9_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [144]
            },
            {
                "identifier": 'EVENT_1847_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1847_action_queue_async_9_SUBSCRIPT_walk_1_step_f_direction_4',
                "command": 'walk_1_step_f_direction',
                "args": []
            },
            {
                "identifier": 'EVENT_1847_action_queue_async_9_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1847_action_queue_async_9_SUBSCRIPT_jmp_if_mario_in_air_6',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1847_action_queue_async_9_SUBSCRIPT_pause_5']
            }
        ]
    },
    {
        "identifier": 'EVENT_1847_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_1830_store_coin_amount_7000_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_enable_controls_11',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_run_background_event_12',
        "command": 'run_background_event',
        "args": [1849, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1847_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
