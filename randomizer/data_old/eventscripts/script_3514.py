
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3514_jmp_if_bit_set__0',
        "command": 'jmp_if_bit_set',
        "args": [0x705F, 4, 'EVENT_3514_enter_area_1']
    },
    {
        "identifier": 'EVENT_3514_enter_area__1',
        "command": 'enter_area',
        "args": [Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, RadialDirections.SOUTHWEST, 26, 109, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3514_ret__2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3514_enter_area_1',
        "command": 'enter_area',
        "args": [499, RadialDirections.SOUTHWEST, 26, 109, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3514_ret_4',
        "command": 'ret'
    }
]
