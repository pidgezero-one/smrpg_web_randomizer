from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2132_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2132_set_1',
        "command": 'set',
        "args": [0x70a7, 91]
    },
    {
        "identifier": 'EVENT_2132_set_2',
        "command": 'set',
        "args": [0x7000, 3351]
    },
    {
        "identifier": 'EVENT_2132_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [3829]
    },
    {
        "identifier": 'EVENT_2132_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT]
    },
    {
        "identifier": 'EVENT_2132_set_bit_5',
        "command": 'set_bit',
        "args": [0x7093, 1]
    },
    {
        "identifier": 'EVENT_2132_ret_6',
        "command": 'ret'
    }
]
