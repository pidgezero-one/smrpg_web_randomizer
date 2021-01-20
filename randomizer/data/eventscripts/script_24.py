from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_24_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_24_set_temp_action_script_sync_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_24_reset_and_choose_game_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x707c, 6, 'EVENT_24_jmp_if_bit_clear_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_remove_object_at_70A8_from_current_level_3',
        "command": 'remove_object_at_70A8_from_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x707c, 7, 'EVENT_24_jmp_if_var_not_equals_byte_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_disable_trigger_6',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_pause_8',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_jmp_if_var_not_equals_byte_9',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70bb, 255, 'EVENT_24_add_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_set_10',
        "command": 'set',
        "args": [0x70bb, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_add_11',
        "command": 'add',
        "args": [0x70bb, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 5, 'EVENT_24_clear_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x707c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_load_600f_15',
        "command": 'load_600f',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_reset_and_choose_game_17',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_set_temp_action_script_sync_18',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 5, 'EVENT_24_clear_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_fade_in_from_black_async_20',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_24_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_24_load_600f_15'],
        "subscript": []
    },
]
