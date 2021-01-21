from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2643_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 5, 'EVENT_2643_open_shop_6']
    },
    {
        "identifier": 'EVENT_2643_set_bit_1',
        "command": 'set_bit',
        "args": [0x7059, 5]
    },
    {
        "identifier": 'EVENT_2643_set_2',
        "command": 'set',
        "args": [0x70a7, 131]
    },
    {
        "identifier": 'EVENT_2643_set_3',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_2643_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_2643_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2643_open_shop_6',
        "command": 'open_shop',
        "args": [Shops._24_TOADS_SHOP]
    },
    {
        "identifier": 'EVENT_2643_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2643_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2643_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2643_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2643_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2643_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2643_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2643_ret_14',
        "command": 'ret'
    }
]
