from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_746_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 7, 'EVENT_746_enter_area_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7082, 0, 'EVENT_746_enter_area_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_stop_sound_2',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_stop_sound_3',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_stop_sound_4',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_stop_sound_5',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_enter_area_6',
        "command": 'enter_area',
        "args": [Rooms._049_MUSHROOM_KINGDOM_BEFORE_CROCO_INN_1F, RadialDirections.SOUTHWEST, 4, 84, 0, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_enter_area_8',
        "command": 'enter_area',
        "args": [Rooms._485_MUSHROOM_KINGDOM_DURING_MACK_INN_1F, RadialDirections.SOUTHWEST, 4, 84, 0, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_enter_area_10',
        "command": 'enter_area',
        "args": [Rooms._493_MUSHROOM_KINGDOM_INN_1F, RadialDirections.SOUTHWEST, 4, 84, 0, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_746_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
