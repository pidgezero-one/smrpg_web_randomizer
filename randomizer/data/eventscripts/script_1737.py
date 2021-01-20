from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1737_jmp_fork_mario_on_object_0',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1737_jmp_if_bit_set_4', 'EVENT_1737_ret_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1737_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_1737_ret_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1737_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1737_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_1737_action_queue_async_2_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [153]
            },
            {
                "identifier": 'EVENT_1737_action_queue_async_2_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1737_action_queue_async_2_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1737_action_queue_async_2_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_1737_action_queue_async_2_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [50]
            },
            {
                "identifier": 'EVENT_1737_action_queue_async_2_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1737_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1737_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7094, 3, 'EVENT_1846_jmp_if_bit_set_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1737_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
