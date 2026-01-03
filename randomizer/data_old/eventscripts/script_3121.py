
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
        "identifier": "EVENT_3121_start_battle_102",
        "command": "run_event_as_subroutine",
        "args": [354],
    },
    {
        "identifier": "EVENT_3121_jmp_if_bit_set_1",
        "command": "jmp_if_bit_clear",
        "args": [0x7040, 0, "EVENT_3121_set_bit_103"],
    },
    {
        "identifier": "EVENT_3121_reset_and_choose_game_17",
        "command": "reset_and_choose_game",
    },
    {"identifier": "EVENT_3121_set_bit_103", "command": "set_bit", "args": [0x707C, 5]},
    {
        "identifier": "EVENT_3121_clear_bit_104",
        "command": "clear_bit",
        "args": [0x707C, 6],
    },
    {
        "identifier": "EVENT_3121_clear_bit_105",
        "command": "clear_bit",
        "args": [0x707C, 7],
    },
    {"identifier": "EVENT_3121_pause_109", "command": "pause", "args": [10]},
    {"identifier": "EVENT_3121_set_bit_110", "command": "set_bit", "args": [0x7055, 2]},
    {"identifier": "EVENT_3121_restore_all_hp_111", "command": "restore_all_hp"},
    {"identifier": "EVENT_3121_restore_all_fp_112", "command": "restore_all_fp"},
    {
        "identifier": "EVENT_3121_remove_from_current_level_501",
        "command": "remove_from_current_level",
        "args": [AreaObjects.MARIO],
    },
    {"identifier": "EVENT_3121_set_bit_502", "command": "set_bit", "args": [0x704D, 6]},
    {
        "identifier": "EVENT_3121_clear_bit_503",
        "command": "clear_bit",
        "args": [0x7096, 5],
    },
    {"identifier": "EVENT_3121_pause_504", "command": "pause", "args": [1]},
    {
        "identifier": "EVENT_3121_enter_area_505",
        "command": "enter_area",
        "args": [
            Rooms._301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS,
            RadialDirections.SOUTH,
            12,
            108,
            11,
            [],
        ],
    },
    {
        "identifier": "EVENT_3121_run_event_as_subroutine_506",
        "command": "run_event_as_subroutine",
        "args": [14],
    },
    {
        "identifier": "EVENT_3121_action_queue_async_507",
        "command": "action_queue",
        "args": [AreaObjects.MARIO, False],
        "subscript": [
            {
                "identifier": "EVENT_3121_action_queue_async_507_SUBSCRIPT_jump_to_height_silent_0",
                "command": "jump_to_height_silent",
                "args": [144],
            }
        ],
    },
    {
        "identifier": "EVENT_3121_set_short_107",
        "command": "jmp_to_event",
        "args": [168],
    },
    {"identifier": "EVENT_3121_ret_517", "command": "ret"},
]
