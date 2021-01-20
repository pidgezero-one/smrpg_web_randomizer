from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_66_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x707c, 0, 'EVENT_66_end_all_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_set_7000_to_tapped_button_1',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 4, 'EVENT_66_end_all_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_set_7000_to_pressed_button_3',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_jmp_if_var_not_equals_short_4',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 4, 'EVENT_66_end_all_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_mem_compare_5',
        "command": 'mem_compare',
        "args": [0x7016, 256],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_jmp_if_comparison_result_is_lesser_6',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_66_set_action_script_async_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7018],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_mem_7000_shift_left_8',
        "command": 'mem_7000_shift_left',
        "args": [0x7016, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_66_end_all_11',
        "command": 'end_all',
        "args": [],
        "subscript": []
    },
]
