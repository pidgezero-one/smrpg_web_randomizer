from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3854_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 26, 'EVENT_3854_enter_area_3']
    },
    {
        "identifier": 'EVENT_3854_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._100_BOOSTER_PASS_AREA_01, RadialDirections.NORTHEAST, 3, 41, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3854_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3854_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._101_BOOSTER_PASS_AREA_02, RadialDirections.SOUTHWEST, 13, 95, 6, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3854_ret_4',
        "command": 'ret'
    }
]
