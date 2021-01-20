from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1008_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1008_set_temp_action_script_sync_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_287_reset_and_choose_game_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_remove_object_at_70A8_from_current_level_2',
        "command": 'remove_object_at_70A8_from_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 2, 'EVENT_1010_clear_bit_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_set_temp_action_script_sync_7',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 2, 'EVENT_1010_clear_bit_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1008_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
