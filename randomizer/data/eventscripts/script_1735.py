from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1735_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_disable_event_trigger_for_object_at_70A8_1',
        "command": 'disable_event_trigger_for_object_at_70A8',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_mem_7000_and_const_2',
        "command": 'mem_7000_and_const',
        "args": [0x00f0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x70b4, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_set_7010_to_object_xyz_5',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_add_7',
        "command": 'add',
        "args": [0x7000, 608],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_create_packet_at_7010_coords_jmp_if_null_9',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._003_SUPER_STAR, 'EVENT_1735_ret_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_set_bit_10',
        "command": 'set_bit',
        "args": [0x7076, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_mem_7000_and_const_12',
        "command": 'mem_7000_and_const',
        "args": [0x000f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_set_experience_packet_7000_13',
        "command": 'set_experience_packet_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_mario_glows_14',
        "command": 'mario_glows',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x707c, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7064, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x707c, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_create_packet_at_object_coords_jmp_if_null_18',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._022_SPARKLES_MOVE_N, AreaObjects.MARIO, 'EVENT_1735_ret_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1735_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
