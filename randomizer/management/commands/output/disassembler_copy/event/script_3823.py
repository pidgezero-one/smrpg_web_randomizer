
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3823_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 3, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3823_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 4, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3823_set_bit_2',
        "command": 'set_bit',
        "args": [0x7089, 4]
    },
    {
        "identifier": 'EVENT_3823_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_3823_play_sound_5']
    },
    {
        "identifier": 'EVENT_3823_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [456]
    },
    {
        "identifier": 'EVENT_3823_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3823_set_6',
        "command": 'set',
        "args": [0x70a7, 161]
    },
    {
        "identifier": 'EVENT_3823_run_dialog_7',
        "command": 'run_dialog',
        "args": [516, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3823_put_inventory_8',
        "command": 'put_inventory',
        "args": [items.BigBooFlag]
    },
    {
        "identifier": 'EVENT_3823_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3823_run_background_event_10',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_3823_ret_11',
        "command": 'ret'
    }
]
