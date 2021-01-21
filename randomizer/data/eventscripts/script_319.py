from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_319_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_319_summon_to_current_level_4']
    },
    {
        "identifier": 'EVENT_319_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_319_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_319_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 5, 'EVENT_319_jmp_if_bit_set_7']
    },
    {
        "identifier": 'EVENT_319_summon_to_current_level_4',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_319_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_319_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_319_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 6, 'EVENT_319_summon_to_current_level_4']
    },
    {
        "identifier": 'EVENT_319_jmp_to_event_8',
        "command": 'jmp_to_event',
        "args": [257]
    }
]
