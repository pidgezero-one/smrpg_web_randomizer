from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3195_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_3195_ret_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3195_run_background_event_1',
        "command": 'run_background_event',
        "args": [3196, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3195_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3195_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
