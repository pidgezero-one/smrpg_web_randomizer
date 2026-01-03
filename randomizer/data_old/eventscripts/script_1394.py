
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1394_jmp_if_var_equals_const_0',
        "command": 'jmp_if_var_equals_const',
        "args": [0x71f0, 200, 'EVENT_1394_set_7000_to_7000_short_mem_6']
    },
    {
        "identifier": 'EVENT_1394_store_coin_amount_7000_1',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_1394_dec_coins_2',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_1394_set_7000_short_mem_to_7000_3',
        "command": 'copy_var_to_var',
        'args': [0x7000, 0x700a]
    },
    {
        "identifier": 'EVENT_1394_set_short_4',
        "command": "set_var_to_const",
        "args": [0x71f0, 0x00c8]
    },
    {
        "identifier": 'EVENT_1394_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1394_set_7000_to_7000_short_mem_6',
        "command": 'copy_var_to_var',
        'args': [0x700a, 0x7000]
    },
    {
        "identifier": 'EVENT_1394_add_coins_7',
        "command": 'add_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_1394_ret_8',
        "command": 'ret'
    }
]
