
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_871_fade_out_to_black_async_0',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_871_____enter_area_178',
        "command": 'enter_area',
        "args": [Rooms._000_DEBUG_ROOM, RadialDirections.SOUTHEAST, 7, 24, 5, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_871_ret',
        "command": 'ret'
    }
]
