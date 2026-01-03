
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
        "identifier": "EVENT_375_play_music_default_volume_0",
        "command": "play_music_default_volume",
        "args": [Music._02_MUSHROOM_KINGDOM],
    },
    {
        "identifier": "EVENT_375_enter_area_42",
        "command": "enter_area",
        "args": [
            Rooms._018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
            RadialDirections.NORTHEAST,
            16,
            30,
            2,
            [],
        ],
    },
    {
        "identifier": "EVENT_375_action_queue_async_43",
        "command": "action_queue",
        "args": [AreaObjects.SCREEN_FOCUS, False],
        "subscript": [
            {
                "identifier": "EVENT_375_action_queue_async_43_SUBSCRIPT_set_animation_speed_0",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_375_action_queue_async_43_SUBSCRIPT_shift_east_pixels_1",
                "command": "shift_east_pixels",
                "args": [16],
            },
        ],
    },
    {
        "identifier": "EVENT_375_fade_in_from_black_sync_duration_44",
        "command": "fade_in_from_black_sync_duration",
        "args": [200],
    },
    {
        "identifier": "EVENT_375_action_queue_async_45",
        "command": "action_queue",
        "args": [AreaObjects.NPC_0, False],
        "subscript": [
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_set_animation_speed_0",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_set_animation_speed_1",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]],
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_shift_northwest_pixels_2",
                "command": "shift_northwest_pixels",
                "args": [8],
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_face_southwest_3",
                "command": "face_southwest",
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_pause_4",
                "command": "pause",
                "args": [20],
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_walk_1_step_southeast_5",
                "command": "walk_1_step_southeast",
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_face_southwest_6",
                "command": "face_southwest",
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_pause_7",
                "command": "pause",
                "args": [20],
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_walk_1_step_northwest_8",
                "command": "walk_1_step_northwest",
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_face_southwest_9",
                "command": "face_southwest",
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_pause_10",
                "command": "pause",
                "args": [20],
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_shift_southeast_pixels_11",
                "command": "shift_southeast_pixels",
                "args": [8],
            },
            {
                "identifier": "EVENT_375_action_queue_async_45_SUBSCRIPT_face_southwest_12",
                "command": "face_southwest",
            },
        ],
    },
    {
        "identifier": "EVENT_375_pause_script_until_effect_done_46",
        "command": "pause_script_until_effect_done",
    },
    {"identifier": "EVENT_375_set_bit_115", "command": "set_bit", "args": [0x7065, 5]},
    {"identifier": "EVENT_375_set_bit_116", "command": "set_bit", "args": [0x7065, 6]},
    {"identifier": "EVENT_375_set_bit_117", "command": "set_bit", "args": [0x7065, 7]},
    {"identifier": "EVENT_375_set_bit_118", "command": "set_bit", "args": [0x706D, 5]},
    {"identifier": "EVENT_375_set_bit_119", "command": "set_bit", "args": [0x7042, 0]},
    {"identifier": "EVENT_375_set_bit_121", "command": "set_bit", "args": [0x7082, 0]},
    {
        "identifier": "EVENT_375_star_grant",
        "command": "jmp_to_event",
        "args": [168],
    },
    {"identifier": "EVENT_375_ret_124", "command": "ret"},
]
