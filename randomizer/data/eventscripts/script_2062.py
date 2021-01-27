from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2062_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 4, 'EVENT_2062_set_7000_to_70A0_short_mem_3']
    },
    {
        "identifier": 'EVENT_2062_run_dialog_1',
        "command": 'run_dialog',
        "args": [2634, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2062_set_bit_2',
        "command": 'set_bit',
        "args": [0x7092, 4]
    },
    {
        "identifier": 'EVENT_2062_set_7000_to_70A0_short_mem_3',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_2062_set_7000_short_mem_to_7000_4',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_2062_set_5',
        "command": 'set',
        "args": [0x7000, 39]
    },
    {
        "identifier": 'EVENT_2062_dec_short_mem_6',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_2062_jmp_if_7000_equals_short_7',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_2062_run_dialog_10']
    },
    {
        "identifier": 'EVENT_2062_run_dialog_8',
        "command": 'run_dialog',
        "args": [2635, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2062_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2062_run_dialog_10',
        "command": 'run_dialog',
        "args": [2636, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2062_ret_11',
        "command": 'ret'
    }
]
