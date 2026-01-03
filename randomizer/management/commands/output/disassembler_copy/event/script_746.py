
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_746_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_746_enter_area_7']
    },
    {
        "identifier": 'EVENT_746_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_746_enter_area_3']
    },
    {
        "identifier": 'EVENT_746_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 7, 'EVENT_746_enter_area_5']
    },
    {
        "identifier": 'EVENT_746_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._049_MUSHROOM_KINGDOM_BEFORE_CROCO_INN_1F, RadialDirections.SOUTHWEST, 4, 84, 0, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]]
    },
    {
        "identifier": 'EVENT_746_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_746_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._485_MUSHROOM_KINGDOM_DURING_MACK_INN_1F, RadialDirections.SOUTHWEST, 4, 84, 0, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]]
    },
    {
        "identifier": 'EVENT_746_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_746_enter_area_7',
        "command": 'enter_area',
        "args": [Rooms._493_MUSHROOM_KINGDOM_INN_1F, RadialDirections.SOUTHWEST, 4, 84, 0, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]]
    },
    {
        "identifier": 'EVENT_746_ret_8',
        "command": 'ret'
    }
]
