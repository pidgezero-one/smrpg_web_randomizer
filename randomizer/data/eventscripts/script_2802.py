from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2802_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2802_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_2802_pause_0']
    },
    {
        "identifier": 'EVENT_2802_set_7000_to_tapped_button_2',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_2802_jmp_if_7000_equals_short_3',
        "command": 'jmp_if_7000_equals_short',
        "args": [128, 'EVENT_2802_set_short_mem_5']
    },
    {
        "identifier": 'EVENT_2802_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_2802_pause_0']
    },
    {
        "identifier": 'EVENT_2802_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ae]
    },
    {
        "identifier": 'EVENT_2802_mem_compare_val_6',
        "command": 'mem_compare_val',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2802_jmp_if_comparison_result_is_greater_or_equal_7',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2802_jmp_if_bit_clear_14']
    },
    {
        "identifier": 'EVENT_2802_inc_8',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'EVENT_2802_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 6, 'EVENT_2802_pause_11']
    },
    {
        "identifier": 'EVENT_2802_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2802_pause_11',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2802_jmp_if_mario_in_air_12',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_2802_pause_11']
    },
    {
        "identifier": 'EVENT_2802_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_2802_pause_0']
    },
    {
        "identifier": 'EVENT_2802_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 6, 'EVENT_2802_summon_to_level_16']
    },
    {
        "identifier": 'EVENT_2802_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2802_summon_to_level_16',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO]
    },
    {
        "identifier": 'EVENT_2802_summon_to_current_level_17',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2802_apply_tile_mod_18',
        "command": 'apply_tile_mod',
        "args": [Rooms._347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2802_apply_solidity_mod_19',
        "command": 'apply_solidity_mod',
        "args": [Rooms._347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2802_ret_20',
        "command": 'ret'
    }
]
