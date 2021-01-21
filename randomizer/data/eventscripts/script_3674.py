from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3674_set_0',
        "command": 'set',
        "args": [0x70a7, 32]
    },
    {
        "identifier": 'EVENT_3674_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [32]
    },
    {
        "identifier": 'EVENT_3674_disable_trigger_in_level_2',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM]
    },
    {
        "identifier": 'EVENT_3674_disable_trigger_in_level_3',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._498_NIMBUS_CASTLE_AREA_10_____DUMMY]
    },
    {
        "identifier": 'EVENT_3674_ret_4',
        "command": 'ret'
    }
]
