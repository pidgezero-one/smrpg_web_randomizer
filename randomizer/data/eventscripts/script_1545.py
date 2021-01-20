from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1545_set_7016_to_object_xyz_0',
        "command": 'set_7016_to_object_xyz',
        "args": [0x90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1545_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1545_action_queue_async_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_1_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_1_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_1_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_1_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x98]
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_1_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_1_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_1_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1545_pixelate_layers_2',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 9, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1545_fade_in_from_black_sync_duration_3',
        "command": 'fade_in_from_black_sync_duration',
        "args": [40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1545_pixelate_layers_4',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 0, 70],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1545_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1545_action_queue_async_5_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_5_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_5_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_5_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_5_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_5_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1545_action_queue_async_5_SUBSCRIPT_walk_1_step_f_direction_6',
                "command": 'walk_1_step_f_direction',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1545_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1545_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
