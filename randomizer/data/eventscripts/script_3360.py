from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3360_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_dec_short_2',
        "command": 'dec_short',
        "args": [0x703c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_jmp_if_loaded_memory_is_not_0_3',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3360_set_temp_action_script_sync_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3360_set_7010_to_object_xyz_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_set_temp_action_script_sync_6',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_2, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_set_7010_to_object_xyz_7',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_add_9',
        "command": 'add',
        "args": [0x7000, 608],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_set_short_mem_10',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_create_packet_at_7010_coords_jmp_if_null_12',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._016_BIG_COIN, 'EVENT_3360_ret_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 906],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3360_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
