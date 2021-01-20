from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2118_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_start_battle_1',
        "command": 'start_battle',
        "args": [0x00d0, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2118_remove_from_level_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_reset_and_choose_game_3',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7092, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_set_short_8',
        "command": 'set_short',
        "args": [0x700a, 0x00db],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2118_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
