from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1549_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1549_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 7, 'EVENT_1549_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_1549_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 172]
    },
    {
        "identifier": 'EVENT_1549_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7094, 3, 'EVENT_1846_jmp_if_bit_set_0']
    },
    {
        "identifier": 'EVENT_1549_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [1840]
    },
    {
        "identifier": 'EVENT_1549_ret_5',
        "command": 'ret'
    }
]
