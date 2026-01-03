
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3822_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 3, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3822_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 6, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3822_set_bit_2',
        "command": 'set_bit',
        "args": [0x7089, 6]
    },
    {
        "identifier": 'EVENT_3822_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3822_set_4',
        "command": 'set',
        "args": [0x70a7, 163]
    },
    {
        "identifier": 'EVENT_3822_run_dialog_5',
        "command": 'run_dialog',
        "args": [516, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3822_put_inventory_6',
        "command": 'put_inventory',
        "args": [items.GreaperFlag]
    },
    {
        "identifier": 'EVENT_3822_ret_7',
        "command": 'ret'
    }
]
