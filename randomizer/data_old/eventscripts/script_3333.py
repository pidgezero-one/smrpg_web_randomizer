
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
    {"identifier": "EVENT_3333_set_0", "command": "set_var_to_const", "args": [0x70DF, 50]},
    {
        "identifier": "EVENT_3333_run_event_as_subroutine_1",
        "command": "run_event_as_subroutine",
        "args": [15],
    },
    {
        "identifier": "EVENT_3333_set_7000_to_current_level_2",
        "command": "set_7000_to_current_level",
    },
    {
        "identifier": "EVENT_3333_jmp_if_7000_equals_short_3_",
        "command": "jmp_if_var_not_equals_const",
        "args": [0x7000, 361, "EVENT_3333_jmp_if_7000_equals_short_3_2"]
    },
    {
        "identifier": "EVENT_3333_set_item_priority",
        "command": "action_queue",
        "args": [AreaObjects.NPC_1, False],
        "subscript": [
            {
                "identifier": "ACTION_925_set_priority_0",
                "command": "set_priority",
                "args": [2],
            },
            {
                "identifier": "ACTION_925_set_priority_4",
                "command": "set_priority",
                "args": [3],
            },
        ],
    },
    {
        "identifier": "EVENT_3333_jmp_if_7000_equals_short_3_2",
        "command": "jmp_if_var_not_equals_const",
        "args": [0x7000, 358, "EVENT_3333_jmp_if_7000_equals_short_3"]
    },
    {
        "identifier": "EVENT_3333_set_item_priority2",
        "command": "action_queue",
        "args": [AreaObjects.NPC_2, False],
        "subscript": [
            {
                "identifier": "ACTION_925_set_priority_0",
                "command": "set_priority",
                "args": [2],
            },
            {
                "identifier": "ACTION_925_set_priority_4",
                "command": "set_priority",
                "args": [3],
            },
        ],
    },
    {
        "identifier": "EVENT_3333_jmp_if_7000_equals_short_3",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 354, "EVENT_3333_run_background_event_5_"]
    },
    {
        "identifier": "EVENT_3333_action_queue_async_4",
        "command": "action_queue",
        "args": [AreaObjects.NPC_0, False],
        "subscript": [
            {
                "identifier": "EVENT_3333_action_queue_async_4_SUBSCRIPT_transfer_to_object_xy_0",
                "command": "transfer_to_object_xy",
                "args": [AreaObjects.MARIO],
            },
            {
                "identifier": "EVENT_3333_action_queue_async_4_SUBSCRIPT_set_700C_to_object_coord_1",
                "command": "set_700C_to_object_coord",
                "args": [AreaObjects.MARIO, Coords.F, []],
            },
            {
                "identifier": "EVENT_3333_action_queue_async_4_SUBSCRIPT_face_east_7C_2",
                "command": "face_east_7C",
            },
            {
                "identifier": "EVENT_3333_action_queue_async_4_SUBSCRIPT_pause_3",
                "command": "pause",
                "args": [1],
            },
        ],
    },
    {
        "identifier": "EVENT_3333_run_background_event_5",
        "command": "run_background_event",
        "args": [3329, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
    },
    {"identifier": "EVENT_3333_ret_6", "command": "ret"},
    {
        "identifier": "EVENT_3333_run_background_event_5_",
        "command": "run_background_event",
        "args": [3329, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
    },
    {
        "identifier": "EVENT_3333_jmp_if_bit_clear_7",
        "command": "jmp_if_bit_clear",
        "args": [0x7087, 0, "EVENT_3333_ret_6_"],
    },
    {
        "identifier": "EVENT_3333_run_event_as_subroutine_25_",
        "command": "run_event_as_subroutine",
        "args": [3588],
    },
    {
        "identifier": "EVENT_3333_jmp_if_bit_clear_7_",
        "command": "jmp_if_bit_clear",
        "args": [0x7099, 7, "EVENT_3333_ret_6_"],
    },
    {
        "identifier": "EVENT_3333_run_event_as_subroutine_25__",
        "command": "run_event_as_subroutine",
        "args": [3913],
    },
    {"identifier": "EVENT_3333_ret_6_", "command": "ret"},
]
