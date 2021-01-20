from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3732_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7090, 3, 'EVENT_3732_action_queue_async_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3732_summon_to_current_level_1',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3732_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3732_action_queue_async_2_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
        ]
    },
    {
        "identifier": 'EVENT_3732_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3732_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3732_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3732_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x707c, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3732_create_packet_at_object_coords_jmp_if_null_7',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._022_SPARKLES_MOVE_N, AreaObjects.MARIO, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3732_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
