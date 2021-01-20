from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3736_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, 'EVENT_3736_fade_in_from_black_async_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3736_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3736_action_queue_async_1_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3736_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3736_run_background_event_2',
        "command": 'run_background_event',
        "args": [3735, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3736_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3736_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3736_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3736_set_short_6',
        "command": 'set_short',
        "args": [0x7022, 0x0046],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3736_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x707c, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3736_create_packet_at_object_coords_jmp_if_null_8',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._022_SPARKLES_MOVE_N, AreaObjects.MARIO, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3736_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
