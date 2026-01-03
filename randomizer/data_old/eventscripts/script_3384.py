
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3384_create_packet_at_7010_with_event_10',
        "command": 'create_packet_at_7010_with_event',
        "args": [NPCPackets._036_MUSHROOM_JUMPS, 3288, 'EVENT_3223_pause_9']
    },
    {
        "identifier": 'EVENT_3384_ret',
        "command": "jmp",
        "args": ['EVENT_3223_ret_11']
    }
]
