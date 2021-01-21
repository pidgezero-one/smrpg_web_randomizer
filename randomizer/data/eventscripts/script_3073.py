from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3073_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3073_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3073_disable_event_trigger_for_object_at_70A8_2',
        "command": 'disable_event_trigger_for_object_at_70A8'
    },
    {
        "identifier": 'EVENT_3073_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 7]
    },
    {
        "identifier": 'EVENT_3073_set_7010_to_object_xyz_4',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3073_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_3073_add_6',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_3073_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_3073_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 3, 'EVENT_3073_clear_bit_10']
    },
    {
        "identifier": 'EVENT_3073_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3073_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x704a, 3]
    },
    {
        "identifier": 'EVENT_3073_create_packet_at_7010_coords_jmp_if_null_11',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._005_ITEM_BAG, 'EVENT_3073_ret_12']
    },
    {
        "identifier": 'EVENT_3073_ret_12',
        "command": 'ret'
    }
]
