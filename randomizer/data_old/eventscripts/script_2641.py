
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
    {"identifier": "EVENT_2641_set_0", "command": "set_var_to_const", "args": [0x70DF, 1]},
    {
        "identifier": "EVENT_2641_stop_sound_0_",
        "command": "jmp_if_bit_clear",
        "args": [0x708B, 0, "EVENT_2641_action_queue_async_15"],
    },
    {
        "identifier": "EVENT_2641_summon_to_current_level_0",
        "command": "summon_to_current_level",
        "args": [AreaObjects.NPC_8],
    },
    {
        "identifier": "EVENT_2641_action_queue_async_15",
        "command": "action_queue",
        "args": [AreaObjects.NPC_7, False],
        "subscript": [
            {
                "identifier": "EVENT_2641_action_queue_async_15_SUBSCRIPT_shift_southwest_pixels_0",
                "command": "shift_southwest_pixels",
                "args": [8],
            }
        ],
    },
    {
        "identifier": "EVENT_2641_set_action_script_sync_16",
        "command": "set_action_script",
        "args": [AreaObjects.NPC_7, True, 978]
    },
    {
        "identifier": "EVENT_2641_action_queue_async_18",
        "command": "action_queue",
        "args": [AreaObjects.NPC_0, False],
        "subscript": [
            {
                "identifier": "EVENT_2641_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_0",
                "command": "set_sprite_sequence",
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]],
            },
            {
                "identifier": "EVENT_2641_action_queue_async_18_SUBSCRIPT_set_vram_priority_1",
                "command": "set_vram_priority",
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES],
            },
        ],
    },
    {
        "identifier": "EVENT_2641_sequence_setter_2",
        "command": "run_event_as_subroutine",
        "args": [859],
    },
    {
        "identifier": "EVENT_2641_fade_in_from_black_async_19",
        "command": "fade_in_from_black_async",
    },
    {
        "identifier": "EVENT_2641_jmp_if_bit_clear_7",
        "command": "jmp_if_bit_clear",
        "args": [0x7087, 0, "EVENT_2641_ret_4"],
    },
    {
        "identifier": "EVENT_2641_run_event_as_subroutine_25_",
        "command": "run_event_as_subroutine",
        "args": [3588],
    },
    {
        "identifier": "EVENT_2641_jmp_if_bit_clear_7_",
        "command": "jmp_if_bit_clear",
        "args": [0x7099, 7, "EVENT_2641_ret_4"],
    },
    {
        "identifier": "EVENT_2641_run_event_as_subroutine_25__",
        "command": "run_event_as_subroutine",
        "args": [3916],
    },
    {"identifier": "EVENT_2641_ret_4", "command": "ret"},
]
