
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3094_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3094_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3094_disable_trigger_at_70A8_2',
        "command": 'disable_trigger_at_70A8'
    },
    {
        "identifier": 'EVENT_3094_set_action_script_sync_3',
        "command": 'set_action_script',
        'args': [AreaObjects.MEM_70A8, True, 7]
    },
    {
        "identifier": 'EVENT_3094_set_7010_to_object_xyz_4',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3094_set_7000_to_7000_short_mem_5',
        "command": 'copy_var_to_var',
        'args': [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_3094_add_6',
        "command": "add_const_to_var",
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_3094_set_7000_short_mem_to_7000_7',
        "command": 'copy_var_to_var',
        'args': [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_3094_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 3, 'EVENT_3094_clear_bit_10']
    },
    {
        "identifier": 'EVENT_3094_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._081_STAR, 6]
    },
    {
        "identifier": 'EVENT_3094_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x704a, 3]
    },
    {
        "identifier": 'EVENT_3094_create_packet_at_7010_11',
        "command": 'create_packet_at_7010',
        "args": [81, 'EVENT_3094_ret_12']
    },
    {
        "identifier": "EVENT_3094_pause_2",
        "command": "pause",
        "args": [45]
    },
    {
        "identifier": 'EVENT_3094_ret_12',
        "command": 'ret'
    }
]
