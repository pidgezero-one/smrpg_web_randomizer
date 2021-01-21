from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_479_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_479_db_1',
        "command": 'db',
        "args": [0xfd, 0x45]
    },
    {
        "identifier": 'EVENT_479_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_479_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_479_action_queue_sync_3_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_479_action_queue_sync_3_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_479_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_479_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_479_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_479_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_479_action_queue_async_4_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_479_action_queue_async_4_SUBSCRIPT_bounce_to_xy_with_height_4',
                "command": 'bounce_to_xy_with_height',
                "args": [23, 54, 0]
            },
            {
                "identifier": 'EVENT_479_action_queue_async_4_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_479_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_479_start_embedded_action_script_async_6',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_479_start_embedded_action_script_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_479_start_embedded_action_script_async_6_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[]]
            },
            {
                "identifier": 'EVENT_479_start_embedded_action_script_async_6_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_479_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_479_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_479_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_479_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_479_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_479_set_short_12',
        "command": 'set_short',
        "args": [0x703e, 0x0007]
    },
    {
        "identifier": 'EVENT_479_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 289]
    },
    {
        "identifier": 'EVENT_479_set_action_script_async_14',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 288]
    },
    {
        "identifier": 'EVENT_479_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_479_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_479_action_queue_async_16_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_479_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_479_enable_controls_18',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_479_ret_19',
        "command": 'ret'
    }
]
