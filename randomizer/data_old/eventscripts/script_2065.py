
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
    {"identifier": "EVENT_2065_pause_0", "command": "pause", "args": [1]},
    {"identifier": "EVENT_2065_pause_1", "command": "pause", "args": [1]},
    {
        "identifier": "EVENT_2065_action_queue_async_2",
        "command": "action_queue",
        "args": [AreaObjects.NPC_1, False],
        "subscript": [
            {
                "identifier": "EVENT_2065_action_queue_async_2_SUBSCRIPT_face_southwest_0",
                "command": "face_southwest",
            },
            {
                "identifier": "EVENT_2065_action_queue_async_2_SUBSCRIPT_pause_1",
                "command": "pause",
                "args": [30],
            },
            {
                "identifier": "EVENT_2065_action_queue_async_2_SUBSCRIPT_set_animation_speed_2",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]],
            },
            {
                "identifier": "EVENT_2065_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_3",
                "command": "set_sprite_sequence",
                "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]],
            },
            {
                "identifier": "EVENT_2065_action_queue_async_2_SUBSCRIPT_pause_4",
                "command": "pause",
                "args": [15],
            },
            {
                "identifier": "EVENT_2065_action_queue_async_2_SUBSCRIPT_reset_properties_5",
                "command": "reset_properties",
            },
        ],
    },
    {
        "identifier": "EVENT_2065_action_queue_async_11",
        "command": "action_queue",
        "args": [AreaObjects.NPC_1, False],
        "subscript": [
            {
                "identifier": "EVENT_2065_action_queue_async_11_SUBSCRIPT_set_animation_speed_0",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]],
            },
            {
                "identifier": "EVENT_2065_action_queue_async_11_SUBSCRIPT_set_animation_speed_1",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_2065_action_queue_async_11_SUBSCRIPT_shift_southwest_steps_2",
                "command": "shift_southwest_steps",
                "args": [2],
            },
            {
                "identifier": "EVENT_2065_action_queue_async_11_SUBSCRIPT_reset_properties_3",
                "command": "reset_properties",
            },
            {
                "identifier": "EVENT_2065_action_queue_async_11_SUBSCRIPT_fixed_f_coord_off_4",
                "command": "fixed_f_coord_off",
            },
        ],
    },
    {"identifier": "EVENT_2065_jmp_12", "command": "set_bit", "args": [0x708A, 1]},
    {"identifier": "EVENT_2065_ret_24", "command": "ret"},
]
