from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3247_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [33]
    },
    {
        "identifier": 'EVENT_3247_set_7000_to_current_level_1',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3247_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 133, 'EVENT_3247_run_dialog_6']
    },
    {
        "identifier": 'EVENT_3247_run_dialog_3',
        "command": 'run_dialog',
        "args": [1586, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3247_put_inventory_4',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_3247_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3247_run_dialog_6',
        "command": 'run_dialog',
        "args": [1586, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3247_put_inventory_7',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_3247_ret_8',
        "command": 'ret'
    }
]
