from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3221_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3221_action_queue_sync_0_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._009_GREEN_SWITCH, 4]
            },
            {
                "identifier": 'EVENT_3221_action_queue_sync_0_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3221_action_queue_sync_0_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3221_action_queue_sync_0_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3221_action_queue_sync_0_SUBSCRIPT_object_memory_set_bit_4',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3221_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3221_action_queue_sync_1_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3221_action_queue_sync_1_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3221_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 338],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3221_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 2, 'EVENT_3221_ret_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3221_set_short_4',
        "command": 'set_short',
        "args": [0x7010, 0x001a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3221_set_short_5',
        "command": 'set_short',
        "args": [0x7012, 0x006e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3221_set_short_6',
        "command": 'set_short',
        "args": [0x7014, 0x0015],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3221_db_7',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3221_pause_8',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3221_create_packet_event_at_coords_jmp_if_null_9',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._037_ITEM_BAG_JUMPS, 0x0cda, 'EVENT_3221_pause_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3221_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
