from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3329_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3329_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3329_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_3329_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3329_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7076, 0, 'EVENT_3329_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3329_enable_controls_4',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3329_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7044, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3329_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_jmp_0',
                "command": 'jmp',
                "args": ['EVENT_3329_non_embedded_action_queue_9']
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_set_bit_2',
                "command": 'set_bit',
                "args": [0x7044, 4]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3329_action_queue_async_6_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_set_700C_to_object_coord_9',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.NPC_0, Coords.F]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_face_east_10',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x3a]
            },
        ]
    },
    {
        "identifier": 'EVENT_3329_enable_controls_7',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3329_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3329_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3329_non_embedded_action_queue_9',
        "command": 'non_embedded_action_queue',
        "args": [bytearray(b'}\x14')],
        "subscript": []
    },
]
