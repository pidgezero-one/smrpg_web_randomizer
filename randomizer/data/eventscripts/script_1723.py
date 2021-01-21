from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1723_enable_controls_0',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1723_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._260_GAME_INTRO_FOREST_MAZE_JUMPING_ON_WIGGLER, RadialDirections.SOUTHEAST, 6, 32, 3, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1723_ret_2',
        "command": 'ret'
    }
]
