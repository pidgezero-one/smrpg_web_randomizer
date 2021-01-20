from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2644_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2644_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2644_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2644_set_7010_to_object_xyz_3',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2644_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2644_add_5',
        "command": 'add',
        "args": [0x7000, 512],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2644_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2644_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2644_create_packet_at_7010_coords_jmp_if_null_8',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._005_ITEM_BAG, 'EVENT_2644_ret_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2644_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
