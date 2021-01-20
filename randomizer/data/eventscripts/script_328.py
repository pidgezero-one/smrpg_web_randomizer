from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_328_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_set_bit_7_offset_1',
        "command": 'set_bit_7_offset',
        "args": [0x0158],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 3, 'EVENT_262_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 6, 'EVENT_328_jmp_if_bit_set_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_328_summon_to_current_level_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [262],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_summon_to_current_level_10',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_328_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 96, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_328_action_queue_sync_11_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_328_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_328_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 1, 'EVENT_328_set_action_script_sync_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_328_action_queue_sync_13_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 110, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_328_action_queue_sync_13_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_328_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_328_action_queue_sync_14_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 110, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_328_action_queue_sync_14_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_328_action_queue_sync_14_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_328_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 128],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_palette_set_17',
        "command": 'palette_set',
        "args": [17, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_jmp_to_event_18',
        "command": 'jmp_to_event',
        "args": [262],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 2, 'EVENT_262_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_pause_action_script_20',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_jmp_if_bit_clear_22',
        "command": 'jmp_if_bit_clear',
        "args": [0x709c, 1, 'EVENT_262_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_remove_from_current_level_23',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_328_jmp_to_event_24',
        "command": 'jmp_to_event',
        "args": [262],
        "subscript": []
    },
]
