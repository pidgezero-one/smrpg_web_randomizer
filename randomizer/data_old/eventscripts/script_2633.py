
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
        "identifier": "EVENT_2633_check_bit",
        "command": "jmp_if_bit_clear",
        "args": [0x7088, 5, "EVENT_2633_set_bit_0"],
    },
    {
        "identifier": "EVENT_2633_open_Warp",
        "command": "run_event_as_subroutine",
        "args": [2645],
    },
    {"identifier": "EVENT_2633_set_bit_0", "command": "set_bit", "args": [0x7046, 1]},
    {
        "identifier": "EVENT_2633_action_queue_sync_1",
        "command": "action_queue",
        "args": [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": "EVENT_2633_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_2633_action_queue_sync_1_SUBSCRIPT_shift_west_pixels_1",
                "command": "shift_west_pixels",
                "args": [5],
            },
        ],
    },
    {
        "identifier": "EVENT_2633_action_queue_sync_2",
        "command": "action_queue",
        "args": [AreaObjects.NPC_2, True],
        "subscript": [
            {
                "identifier": "EVENT_2633_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_2633_action_queue_sync_2_SUBSCRIPT_shift_north_pixels_1",
                "command": "shift_north_pixels",
                "args": [8],
            },
            {
                "identifier": "EVENT_2633_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_2",
                "command": "set_sprite_sequence",
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]],
            },
        ],
    },
    {
        "identifier": "EVENT_2633_action_queue_sync_3",
        "command": "action_queue",
        "args": [AreaObjects.NPC_3, True],
        "subscript": [
            {
                "identifier": "EVENT_2633_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_2633_action_queue_sync_3_SUBSCRIPT_shift_west_pixels_1",
                "command": "shift_west_pixels",
                "args": [16],
            },
            {
                "identifier": "EVENT_2633_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_2",
                "command": "set_sprite_sequence",
                "args": [
                    10,
                    0,
                    [
                        _0x08Flags.READ_AS_MOLD,
                        _0x08Flags.READ_AS_SEQUENCE,
                        _0x08Flags.MIRROR_SPRITE,
                    ],
                ],
            },
        ],
    },
    {
        "identifier": "EVENT_2633_action_queue_sync_4",
        "command": "action_queue",
        "args": [AreaObjects.NPC_8, True],
        "subscript": [
            {
                "identifier": "EVENT_2633_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_2633_action_queue_sync_4_SUBSCRIPT_shift_southwest_pixels_1",
                "command": "shift_southwest_pixels",
                "args": [3],
            },
        ],
    },
    {
        "identifier": "EVENT_2633_action_queue_async_5",
        "command": "action_queue",
        "args": [AreaObjects.NPC_9, False],
        "subscript": [
            {
                "identifier": "EVENT_2633_action_queue_async_5_SUBSCRIPT_set_animation_speed_0",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_2633_action_queue_async_5_SUBSCRIPT_shift_northwest_pixels_1",
                "command": "shift_northwest_pixels",
                "args": [8],
            },
            {
                "identifier": "EVENT_2633_action_queue_async_5_SUBSCRIPT_shift_southwest_pixels_2",
                "command": "shift_southwest_pixels",
                "args": [3],
            },
        ],
    },
    {
        "identifier": "EVENT_2633_action_queue_async_5_",
        "command": "action_queue",
        "args": [AreaObjects.NPC_4, False],
        "subscript": [
            {
                "identifier": "EVENT_2633_action_queue_async_5_SUBSCRIPT_set_animation_speed_0",
                "command": "visibility_on",
            }
        ],
    },
    {
        "identifier": "EVENT_2633_action_queue_async_5__",
        "command": "action_queue",
        "args": [AreaObjects.NPC_5, False],
        "subscript": [
            {
                "identifier": "EVENT_2633_action_queue_async_5_SUBSCRIPT_set_animation_speed_0",
                "command": "visibility_off",
            }
        ],
    },
    {
        "identifier": "EVENT_2633_action_queue_async_5___",
        "command": "action_queue",
        "args": [AreaObjects.NPC_6, False],
        "subscript": [
            {
                "identifier": "EVENT_2633_action_queue_async_5_SUBSCRIPT_set_animation_speed_0",
                "command": "visibility_off",
            }
        ],
    },
    {
        "identifier": "EVENT_2633_action_queue_async_5____",
        "command": "action_queue",
        "args": [AreaObjects.NPC_7, False],
        "subscript": [
            {
                "identifier": "EVENT_2633_action_queue_async_5_SUBSCRIPT_set_animation_speed_0",
                "command": "visibility_off",
            }
        ],
    },
    {
        "identifier": "EVENT_2633_fade_in_from_black_async_6",
        "command": "fade_in_from_black_async",
    },
    {
        "identifier": "EVENT_2633_jmp_if_bit_set_22",
        "command": "jmp_if_bit_clear",
        "args": [0x7077, 5, "EVENT_2633_ret_7"],
    },
    {"identifier": "EVENT_2633_set_factory_", "command": "set_var_to_const", "args": [0x7000, 523]},
    {
        "identifier": "EVENT_2633_star_grant",
        "command": "jmp_to_event",
        "args": [167],
    },
    {"identifier": "EVENT_2633_ret_7", "command": "ret"},
]
