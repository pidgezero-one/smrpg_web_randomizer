from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1807_set_short_0',
        "command": 'set_short',
        "args": [0x700e, 0x0057]
    },
    {
        "identifier": 'EVENT_1807_start_battle_700E_1',
        "command": 'start_battle_700E'
    },
    {
        "identifier": 'EVENT_1807_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_1807_set_bit_3',
        "command": 'set_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_1807_set_bit_4',
        "command": 'set_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_1807_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_1807_jmp_if_object_in_level_6',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_5, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, 'EVENT_1807_ret_8']
    },
    {
        "identifier": 'EVENT_1807_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [1767]
    },
    {
        "identifier": 'EVENT_1807_ret_8',
        "command": 'ret'
    }
]
