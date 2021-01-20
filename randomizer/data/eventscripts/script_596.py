from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_596_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_596_pause_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_if_present_in_current_level_2',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_3, 'EVENT_596_stop_sound_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_596_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_4',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_5',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_6',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_7',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_pause_8',
        "command": 'pause',
        "args": [34],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 299],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_pause_10',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_596_pause_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_if_present_in_current_level_12',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_4, 'EVENT_596_stop_sound_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_596_pause_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_14',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_15',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_16',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_17',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_pause_18',
        "command": 'pause',
        "args": [34],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 299],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_pause_20',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_596_pause_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_if_present_in_current_level_22',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_2, 'EVENT_596_stop_sound_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_596_pause_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_24',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_25',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_26',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_stop_sound_27',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_pause_28',
        "command": 'pause',
        "args": [34],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 299],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_596_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_pause_31',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_create_packet_at_object_coords_jmp_if_null_32',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._033_BOMB_EXPLOSION, AreaObjects.NPC_3, 'EVENT_596_pause_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_33',
        "command": 'jmp',
        "args": ['EVENT_596_pause_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_pause_34',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_create_packet_at_object_coords_jmp_if_null_35',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._033_BOMB_EXPLOSION, AreaObjects.NPC_4, 'EVENT_596_pause_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_596_pause_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_pause_37',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_create_packet_at_object_coords_jmp_if_null_38',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._033_BOMB_EXPLOSION, AreaObjects.NPC_2, 'EVENT_596_pause_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_596_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_596_pause_0'],
        "subscript": []
    }
]
