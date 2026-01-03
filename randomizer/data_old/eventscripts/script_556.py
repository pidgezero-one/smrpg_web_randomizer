
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
        "identifier": "EVENT_556_fade_out_music_to_volume_0",
        "command": "fade_out_music_to_volume",
        "args": [1, 127],
    },
    {
        "identifier": "EVENT_556_jmp_if_bit_clear_1",
        "command": "jmp_if_bit_clear",
        "args": [0x704C, 6, "EVENT_556_action_queue_sync_4"],
    },
    {
        "identifier": "EVENT_556_apply_tile_mod_2",
        "command": "apply_tile_mod",
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 4, [_0x6AFlags.USE_ALTERNATE]],
    },
    {
        "identifier": "EVENT_556_apply_solidity_mod_3",
        "command": "apply_solidity_mod",
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 4, [_0x6BFlags.PERMANENT]],
    },
    {
        "identifier": "EVENT_556_action_queue_sync_4",
        "command": "action_queue",
        "args": [AreaObjects.NPC_2, True],
        "subscript": [
            {
                "identifier": "EVENT_556_action_queue_sync_4_SUBSCRIPT_set_priority_0",
                "command": "set_priority",
                "args": [3],
            }
        ],
    },
    {
        "identifier": "EVENT_556_action_queue_sync_5",
        "command": "action_queue",
        "args": [AreaObjects.NPC_3, True],
        "subscript": [
            {
                "identifier": "EVENT_556_action_queue_sync_5_SUBSCRIPT_set_priority_0",
                "command": "set_priority",
                "args": [3],
            }
        ],
    },
    {
        "identifier": "EVENT_556_action_queue_sync_6",
        "command": "action_queue",
        "args": [AreaObjects.NPC_4, True],
        "subscript": [
            {
                "identifier": "EVENT_556_action_queue_sync_6_SUBSCRIPT_set_priority_0",
                "command": "set_priority",
                "args": [3],
            }
        ],
    },
    {
        "identifier": "EVENT_556_action_queue_sync_7",
        "command": "action_queue",
        "args": [AreaObjects.NPC_5, True],
        "subscript": [
            {
                "identifier": "EVENT_556_action_queue_sync_7_SUBSCRIPT_set_priority_0",
                "command": "set_priority",
                "args": [3],
            }
        ],
    },
    {
        "identifier": "EVENT_556_action_queue_sync_8",
        "command": "action_queue",
        "args": [AreaObjects.NPC_0, True],
        "subscript": [
            {
                "identifier": "EVENT_556_action_queue_sync_8_SUBSCRIPT_set_priority_0",
                "command": "set_priority",
                "args": [3],
            }
        ],
    },
    {
        "identifier": "EVENT_556_action_queue_sync_9",
        "command": "action_queue",
        "args": [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": "EVENT_556_action_queue_sync_9_SUBSCRIPT_set_priority_0",
                "command": "set_priority",
                "args": [3],
            }
        ],
    },
    {
        "identifier": "EVENT_556_action_queue_sync_10",
        "command": "action_queue",
        "args": [AreaObjects.NPC_9, True],
        "subscript": [
            {
                "identifier": "EVENT_556_action_queue_sync_10_SUBSCRIPT_set_priority_0",
                "command": "set_priority",
                "args": [3],
            }
        ],
    },
    {
        "identifier": "EVENT_556_remember_last_object_11",
        "command": "remember_last_object",
    },
    {
        "identifier": "EVENT_556_summon_to_level_12",
        "command": "summon_to_level",
        "args": [AreaObjects.NPC_2, Rooms._087_ROSE_TOWN_ITEM_SHOP],
    },
    {
        "identifier": "EVENT_556_summon_to_level_13",
        "command": "summon_to_level",
        "args": [AreaObjects.NPC_3, Rooms._087_ROSE_TOWN_ITEM_SHOP],
    },
    {
        "identifier": "EVENT_556_summon_to_level_14",
        "command": "summon_to_level",
        "args": [AreaObjects.NPC_1, Rooms._091_ROSE_TOWN_COUPLES_HOUSE],
    },
    {
        "identifier": "EVENT_556_run_background_event_23",
        "command": "run_background_event",
        "args": [557, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
    },
    {
        "identifier": "EVENT_556_fade_in_from_black_async_24",
        "command": "fade_in_from_black_async",
    },
    {"identifier": "EVENT_556_set_bit_33", "command": "set_bit", "args": [0x709F, 5]},
    {
        "identifier": "EVENT_556_jmp_if_bit_clear_7",
        "command": "jmp_if_bit_clear",
        "args": [0x7087, 0, "EVENT_556_ret_40"],
    },
    {
        "identifier": "EVENT_556_run_event_as_subroutine_25_",
        "command": "run_event_as_subroutine",
        "args": [3588],
    },
    {
        "identifier": "EVENT_556_jmp_if_bit_clear_7_",
        "command": "jmp_if_bit_clear",
        "args": [0x7099, 7, "EVENT_556_ret_40"],
    },
    {
        "identifier": "EVENT_556_run_event_as_subroutine_25__",
        "command": "run_event_as_subroutine",
        "args": [3895],
    },
    {"identifier": "EVENT_556_ret_40", "command": "ret"},
]
