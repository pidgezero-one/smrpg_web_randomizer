from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2492_remove_from_level_0',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2492_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2492_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_2305_jmp_if_bit_set_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2492_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
