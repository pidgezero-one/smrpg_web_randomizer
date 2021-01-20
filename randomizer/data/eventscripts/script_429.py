from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_429_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_429_set_action_script_async_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_429_pause_1',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_429_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_429_jmp_if_bit_set_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_429_set_action_script_async_3',
        "command": 'set_action_script_async',
        "args": [AreaObjects.SCREEN_FOCUS, 658],
        "subscript": []
    },
    {
        "identifier": 'EVENT_429_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_429_jmp_if_bit_set_0'],
        "subscript": []
    }
]
