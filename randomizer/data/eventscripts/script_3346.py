from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3346_tint_layers_0',
        "command": 'tint_layers',
        "args": [0x80, 0x20, 0x20, 4, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3346_pause_1',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3346_tint_layers_2',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 4, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3346_pause_3',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3346_reset_priority_set_4',
        "command": 'reset_priority_set',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3346_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3346_tint_layers_0'],
        "subscript": []
    },
]
