
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2210_run_dialog_0',
        "command": 'run_dialog',
        "args": [3416, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2210_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2210_action_queue_sync_1_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2210_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2210_action_queue_async_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2210_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2210_action_queue_async_2_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [25, 100]
            },
            {
                "identifier": 'EVENT_2210_action_queue_async_2_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2210_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2210_pause_4',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2210_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2210_action_queue_sync_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2210_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2210_action_queue_sync_5_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2210_action_queue_sync_5_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2210_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2210_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2210_action_queue_sync_6_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2210_action_queue_sync_6_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [55]
            },
            {
                "identifier": 'EVENT_2210_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [15, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2210_action_queue_sync_6_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2210_action_queue_sync_6_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2210_pause_7',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2210_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._071_MUSHROOM_CURE, 6]
    },
    {
        "identifier": 'EVENT_2210_tint_layers_9',
        "command": 'tint_layers',
        "args": [0x40, 0xa0, 0x40, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.LAYER_4, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND], [7]]
    },
    {
        "identifier": 'EVENT_2210_tint_layers_10',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.LAYER_4, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND], [7]]
    },
    {
        "identifier": 'EVENT_2210_reset_priority_set_11',
        "command": 'reset_priority_set'
    },
    {
        "identifier": 'EVENT_2210_restore_all_hp_12',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2210_restore_all_fp_13',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2210_pause_14',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2210_enable_controls_until_return_15',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2210_ret_16',
        "command": 'ret'
    }
]
