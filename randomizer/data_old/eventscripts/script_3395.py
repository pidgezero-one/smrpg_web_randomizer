
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": "EVENT_3395_unlock_beetlemania",
        "command": "set_bit",
        "args": [0x7062, 3]
    },
    {
        "identifier": 'EVENT_3395_run_dialog_104',
        "command": 'run_dialog',
        "args": [3074, AreaObjects.BOWSER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3395_ret',
        "command": 'ret'
    }
]
