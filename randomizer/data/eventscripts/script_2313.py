from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2313_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._100_BOOSTER_PASS_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_start_battle_2',
        "command": 'start_battle',
        "args": [0x008b, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2313_remove_from_current_level_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_reset_and_choose_game_4',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_store_01_to_0248_6',
        "command": 'store_01_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_apply_tile_mod_7',
        "command": 'apply_tile_mod',
        "args": [Rooms._100_BOOSTER_PASS_AREA_01, 3, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_store_00_to_0248_8',
        "command": 'store_00_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2313_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
