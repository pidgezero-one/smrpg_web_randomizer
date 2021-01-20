from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3793_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x704c, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7044, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_3793_pause_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_unsync_action_script_4',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_unsync_action_script_5',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_unsync_action_script_6',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_unsync_action_script_7',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_pause_8',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 991],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 241],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 990],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_pause_13',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_3793_clear_bit_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3793_pause_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_short_20',
        "command": 'set_short',
        "args": [0x7010, 0x0004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_short_21',
        "command": 'set_short',
        "args": [0x7012, 0x0013],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_short_22',
        "command": 'set_short',
        "args": [0x7014, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_db_23',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_create_packet_at_7010_coords_jmp_if_null_24',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._050_WATER_BLAST_SFX, 'EVENT_3793_clear_bit_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_pause_25',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3793_clear_bit_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3793_pause_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_28',
        "command": 'clear_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_31',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_short_32',
        "command": 'set_short',
        "args": [0x7010, 0x0004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_short_33',
        "command": 'set_short',
        "args": [0x7012, 0x0013],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_short_34',
        "command": 'set_short',
        "args": [0x7014, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_db_35',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_create_packet_at_7010_coords_jmp_if_null_36',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._051_DRILL_BIT, 'EVENT_3793_set_bit_40'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_pause_37',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_3793_set_bit_40'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_3793_pause_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_set_bit_40',
        "command": 'set_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_pause_41',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_clear_bit_42',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_pause_43',
        "command": 'pause',
        "args": [29],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3793_jmp_to_event_44',
        "command": 'jmp_to_event',
        "args": [3793],
        "subscript": []
    },
]
