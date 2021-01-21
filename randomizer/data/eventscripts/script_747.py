from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_747_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_747_remove_from_current_level_11']
    },
    {
        "identifier": 'EVENT_747_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 7, 'EVENT_747_remove_from_current_level_8']
    },
    {
        "identifier": 'EVENT_747_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_747_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 5, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_747_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 6, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_747_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 7, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_747_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_747_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_747_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_747_summon_to_current_level_9',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_747_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_747_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_747_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_747_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_747_jmp_if_bit_set_3']
    }
]
