from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3733_move_script_to_background_thread_2_0',
        "command": 'move_script_to_background_thread_2',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7090, 3, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_enable_controls_until_return_4',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_set_7000_to_tapped_button_5',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_jmp_if_7000_any_bits_set_7',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_3733_jmp_if_present_in_current_level_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_jmp_if_7000_any_bits_set_8',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 1, 2, 3], 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_pause_9',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_3733_set_7000_to_tapped_button_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_jmp_if_present_in_current_level_11',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_6, 'EVENT_3733_play_sound_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_3733_summon_to_current_level_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_set_bit_14',
        "command": 'set_bit',
        "args": [0x7090, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_summon_to_current_level_15',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3733_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
