from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2553_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708c, 5, 'EVENT_2495_ret_9']
    },
    {
        "identifier": 'EVENT_2553_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [2644]
    },
    {
        "identifier": 'EVENT_2553_set_bit_2',
        "command": 'set_bit',
        "args": [0x708c, 5]
    },
    {
        "identifier": 'EVENT_2553_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    },
    {
        "identifier": 'EVENT_2553_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    },
    {
        "identifier": 'EVENT_2553_run_dialog_5',
        "command": 'run_dialog',
        "args": [3164, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2553_put_inventory_6',
        "command": 'put_inventory',
        "args": [items.RedEssence]
    },
    {
        "identifier": 'EVENT_2553_add_7',
        "command": 'add',
        "args": [0x70c8, 0x01]
    },
    {
        "identifier": 'EVENT_2553_ret_8',
        "command": 'ret'
    }
]
