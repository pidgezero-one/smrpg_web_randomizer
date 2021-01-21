from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1844_set_random_0',
        "command": 'set_random',
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_1844_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1844_pause_3']
    },
    {
        "identifier": 'EVENT_1844_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1844_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1844_jmp_if_mario_in_air_4',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1844_pause_3']
    },
    {
        "identifier": 'EVENT_1844_set_7010_to_object_xyz_5',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1844_add_short_6',
        "command": 'add_short',
        "args": [0x7014, 0x0400]
    },
    {
        "identifier": 'EVENT_1844_set_short_7',
        "command": 'set_short',
        "args": [0x7034, 0xcccc]
    },
    {
        "identifier": 'EVENT_1844_create_packet_event_at_coords_jmp_if_null_8',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 0x0735, 'EVENT_1844_pause_3']
    },
    {
        "identifier": 'EVENT_1844_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._044_GHOST_FLOAT, 6]
    },
    {
        "identifier": 'EVENT_1844_ret_10',
        "command": 'ret'
    }
]
