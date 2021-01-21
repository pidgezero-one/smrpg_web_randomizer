from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2079_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2079_freeze_camera_1',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2079_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2079_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_2_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_2_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_2_SUBSCRIPT_face_south_3',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_2_SUBSCRIPT_floating_off_4',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_2_SUBSCRIPT_sequence_playback_off_5',
                "command": 'sequence_playback_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2079_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2079_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2079_action_queue_async_4_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_object_memory_set_bit_3',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_shadow_on_5',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [165]
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_walk_1_step_south_9',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_jmp_if_mario_in_air_11',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2079_action_queue_async_4_SUBSCRIPT_pause_10']
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_object_memory_clear_bit_12',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_2079_action_queue_async_4_SUBSCRIPT_set_solidity_bits_13',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2079_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2079_unfreeze_camera_6',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2079_enable_controls_until_return_7',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2079_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_2079_ret_9',
        "command": 'ret'
    }
]
