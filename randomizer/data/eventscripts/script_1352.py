from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1352_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1352_set_1',
        "command": 'set',
        "args": [0x70a7, 140]
    },
    {
        "identifier": 'EVENT_1352_set_2',
        "command": 'set',
        "args": [0x7000, 2802]
    },
    {
        "identifier": 'EVENT_1352_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1352_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS]
    },
    {
        "identifier": 'EVENT_1352_set_bit_5',
        "command": 'set_bit',
        "args": [0x7054, 2]
    },
    {
        "identifier": 'EVENT_1352_ret_6',
        "command": 'ret'
    }
]
