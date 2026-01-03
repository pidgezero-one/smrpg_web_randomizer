
from randomizer.helpers.eventtables import (
    ControllerDirections,
    RadialDirections,
    Rooms,
    Sounds,
    AreaObjects,
    NPCPackets,
    Locations,
    Shops,
    EventSequences,
    MenuTutorials,
    OverworldSequences,
    PlayableCharacters,
    EquipSlots,
    DialogDurations,
    IntroTitles,
    Colours,
    PaletteSetTypes,
    Music,
    MusicDirections,
    MusicPitch,
    Coords,
    CoordUnits,
    Tutorials,
    _0x40Flags,
    _0x60Flags,
    _0x62Flags,
    _0x63Flags,
    _0x68Flags,
    _0x6AFlags,
    _0x6BFlags,
    _0x81Flags,
    _0x84Flags)
from randomizer.helpers.objectsequencetables import (
    SequenceSpeeds,
    VramPriority,
    _0x08Flags,
    _0x0AFlags,
    _0x10Flags)
from randomizer.data import items

script = [
    {
        "identifier": "EVENT_3402_disable_trigger_0",
        "command": "disable_trigger",
        "args": [AreaObjects.MEM_70A8],
    },
    {
        "identifier": "EVENT_3402_jmp_if_var_equals_const_1",
        "command": "jmp_if_var_equals_const",
        "args": [0x70A7, 240, "EVENT_3402_play_sound_3"],
    },
    {
        "identifier": "EVENT_3402_disable_trigger_at_70A8_2",
        "command": "disable_trigger_at_70A8",
    },
    {
        "identifier": "EVENT_3402_play_sound_3",
        "command": "play_sound",
        "args": [Sounds._005_BLOCK_SWITCH, 6],
    },
    {
        "identifier": "EVENT_3402_set_7000_to_70A0_short_mem_4",
        "command": "copy_var_to_var",
        "args": [0x70A8, 0x7000]
    },
    {
        "identifier": "EVENT_3402_set_70A0_short_mem_to_7000_5",
        "command": "copy_var_to_var",
        "args": [0x7000, 0x70AA]
    },
    {
        "identifier": "EVENT_3402_set_7000_to_70A0_short_mem_4_",
        "command": "set_var_to_const",
        "args": [0x7000, 290],
    },
    {
        "identifier": "EVENT_3402_jmp_if_mem_704x_at_7000_bit_set_9",
        "command": "jmp_if_mem_704x_at_7000_bit_set",
        "args": ["EVENT_3402_jmp_if_var_not_equals_const_26"],
    },
    {
        "identifier": "EVENT_3402_set_mem_704x_at_7000_bit_10",
        "command": "set_mem_704x_at_7000_bit",
    },
    {
        "identifier": "EVENT_3402_set_7000_to_70A0_short_mem_11",
        "command": "copy_var_to_var",
        "args": [0x70A7, 0x7000]
    },
    {
        "identifier": "EVENT_3402_mem_7000_and_const_12",
        "command": "mem_7000_and_const",
        "args": [0x000F],
    },
    {
        "identifier": "EVENT_3402_check_multiplier",
        "command": "jmp_if_var_equals_const",
        "args": [0x70BC, 0, "EVENT_3402_set_70A0_short_mem_to_7000_16"],
    },
    {"identifier": "EVENT_3402_add_counter", "command": "add_const_to_var", "args": [0x7000, 15]},
    {
        "identifier": "EVENT_3402_get_multiplier",
        "command": "dec",
        "args": [0x70BC],
    },
    {
        "identifier": "EVENT_3402_loop",
        "command": "jmp",
        "args": ["EVENT_3402_check_multiplier"],
    },
    {
        "identifier": "EVENT_3402_set_70A0_short_mem_to_7000_16",
        "command": "copy_var_to_var",
        "args": [0x7000, 0x70DC]
    },
    {
        "identifier": "EVENT_3402_jmp_if_var_not_equals_const_26",
        "command": "jmp_if_var_not_equals_const",
        "args": [0x70DC, 1, "EVENT_3402_set_temp_action_script_sync_35"],
    },
    {
        "identifier": "EVENT_3402_set_action_script_sync_33",
        "command": "set_action_script",
        "args": [AreaObjects.MEM_70AA, True, 7],
    },
    {
        "identifier": "EVENT_3402_set_7000_to_70A0_short_mem_4_2",
        "command": "set_var_to_const",
        "args": [0x7000, 290],
    },
    {
        "identifier": "EVENT_3402_clear_mem_704x_at_7000_bit_10",
        "command": "clear_mem_704x_at_7000_bit",
    },
    {
        "identifier": "EVENT_3402_jmp_34",
        "command": "jmp",
        "args": ["EVENT_3402_set_7010_to_object_xyz_36"],
    },
    {
        "identifier": "EVENT_3402_set_temp_action_script_sync_35",
        "command": "set_temp_action_script",
        "args": [AreaObjects.MEM_70AA, True, 8]
    },
    {
        "identifier": "EVENT_3402_set_7010_to_object_xyz_36",
        "command": "set_7010_to_object_xyz",
        "args": [AreaObjects.MEM_70AA],
    },
    {
        "identifier": "EVENT_3402_set_7000_to_7000_short_mem_37",
        "command": "copy_var_to_var",
        "args": [0x7014, 0x7000]
    },
    {"identifier": "EVENT_3402_add_38", "command": "add_const_to_var", "args": [0x7000, 608]},
    {
        "identifier": "EVENT_3402_set_7000_short_mem_to_7000_39",
        "command": "copy_var_to_var",
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": "EVENT_3402_set_7000_to_70A0_short_mem_40",
        "command": "copy_var_to_var",
        "args": [0x70A7, 0x7000]
    },
    {
        "identifier": "EVENT_3402_mem_7000_and_const_41",
        "command": "mem_7000_and_const",
        "args": [0x00F0],
    },
    {
        "identifier": "EVENT_3402_jmp_if_7000_equals_short_42",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 240, "EVENT_3402_add_coins_79"]
    },
    {
        "identifier": "EVENT_3402_jmp_if_7000_equals_short_43",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 160, "EVENT_3402_dec_53"]
    },
    {
        "identifier": "EVENT_3402_jmp_if_7000_equals_short_44",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 128, "EVENT_3402_dec_68"]
    },
    {
        "identifier": "EVENT_3402_jmp_45",
        "command": "jmp",
        "args": ["EVENT_3402_ret_80"],
    },
    {"identifier": "EVENT_3402_dec_53", "command": "dec", "args": [0x70DC]},
    {"identifier": "EVENT_3402_add_coins_49", "command": "add_coins", "args": [10]},
    {
        "identifier": "EVENT_3402_play_sound_46",
        "command": "play_sound",
        "args": [Sounds._013_COIN, 6],
    },
    {
        "identifier": "EVENT_3402_create_packet_at_7010_47",
        "command": "create_packet_at_7010",
        "args": [NPCPackets._016_BIG_COIN, "EVENT_3402_ret_80"],
    },
    {
        "identifier": "EVENT_3402_set_action_script_sync_48",
        "command": "set_action_script",
        "args": [AreaObjects.MEM_70A9, True, 906],
    },
    {
        "identifier": "EVENT_3402_jmp_54",
        "command": "jmp",
        "args": ["EVENT_3402_ret_80"],
    },
    {"identifier": "EVENT_3402_dec_68", "command": "dec", "args": [0x70DC]},
    {"identifier": "EVENT_3402_add_coins_64", "command": "add_coins", "args": [1]},
    {
        "identifier": "EVENT_3402_play_sound_61",
        "command": "play_sound",
        "args": [Sounds._013_COIN, 6],
    },
    {
        "identifier": "EVENT_3402_create_packet_at_7010_62",
        "command": "create_packet_at_7010",
        "args": [NPCPackets._018_SMALL_COIN, "EVENT_3402_ret_80"],
    },
    {
        "identifier": "EVENT_3402_set_action_script_sync_63",
        "command": "set_action_script",
        "args": [AreaObjects.MEM_70A9, True, 906],
    },
    {
        "identifier": "EVENT_3402_jmp_69",
        "command": "jmp",
        "args": ["EVENT_3402_ret_80"],
    },
    {"identifier": "EVENT_3402_add_coins_79", "command": "add_coins", "args": [1]},
    {
        "identifier": "EVENT_3402_play_sound_76",
        "command": "play_sound",
        "args": [Sounds._013_COIN, 6],
    },
    {
        "identifier": "EVENT_3402_create_packet_at_7010_77",
        "command": "create_packet_at_7010",
        "args": [NPCPackets._018_SMALL_COIN, "EVENT_3402_ret_80"],
    },
    {
        "identifier": "EVENT_3402_set_action_script_sync_78",
        "command": "set_action_script",
        "args": [AreaObjects.MEM_70A9, True, 906],
    },
    {
        "identifier": "EVENT_3402_enable_trigger_0",
        "command": "enable_trigger",
        "args": [AreaObjects.MEM_70AA],
    },
    {"identifier": "EVENT_3402_ret_80", "command": "ret"},
]
