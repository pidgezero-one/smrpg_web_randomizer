from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_483_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_483_run_event_as_subroutine_7']
    },
    {
        "identifier": 'EVENT_483_store_item_amount_7000_1',
        "command": 'store_item_amount_7000',
        "args": [items.BrightCard]
    },
    {
        "identifier": 'EVENT_483_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_483_run_dialog_5']
    },
    {
        "identifier": 'EVENT_483_run_dialog_3',
        "command": 'run_dialog',
        "args": [2376, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_483_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_483_run_dialog_5',
        "command": 'run_dialog',
        "args": [2377, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_483_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_483_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [456]
    },
    {
        "identifier": 'EVENT_483_run_dialog_8',
        "command": 'run_dialog',
        "args": [2379, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_483_run_background_event_9',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_483_ret_10',
        "command": 'ret'
    }
]
