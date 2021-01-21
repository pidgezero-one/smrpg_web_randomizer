from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1831_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1831_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1831_set_bit_3']
    },
    {
        "identifier": 'EVENT_1831_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_1831_pause_0']
    },
    {
        "identifier": 'EVENT_1831_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1831_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1831_priority_set_5',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [_0x81Flags.LAYER_3], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.HALF_INTENSITY]]
    },
    {
        "identifier": 'EVENT_1831_pause_6',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_1831_priority_set_7',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.HALF_INTENSITY]]
    },
    {
        "identifier": 'EVENT_1831_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1831_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1831_pause_0']
    }
]
