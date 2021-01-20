from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3294_enable_controls_0',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3294_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3294_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_700C_to_object_coord_2',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MEM_70AA, Coords.F]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_mem_700C_and_const_3',
                "command": 'mem_700C_and_const',
                "args": [0x000f]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 1, 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_6']
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 3, 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_10']
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_jmp_if_mario_in_air_8',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_bit_14']
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_jmp_9',
                "command": 'jmp',
                "args": ['EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_6']
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_shift_southwest_pixels_11',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_jmp_if_mario_in_air_12',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_bit_14']
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_jmp_13',
                "command": 'jmp',
                "args": ['EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_10']
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_bit_14',
                "command": 'set_bit',
                "args": [0x7044, 7]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_reset_properties_15',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_shift_z_down_pixels_17',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_solidity_bits_18',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3294_action_queue_sync_2_SUBSCRIPT_ret_19',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3294_pause_3',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3294_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_3294_pause_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3294_enable_controls_5',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3294_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
