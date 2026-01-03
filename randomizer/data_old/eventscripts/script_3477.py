
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
        "identifier": "EVENT_3477_set_7000_to_70A0_short_mem_2",
        "command": "copy_var_to_var",
        "args": [0x70A7, 0x7000]
    },
    {
        "identifier": "EVENT_3477_room_9_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 240, "EVENT_3477_j"]
    },
    {
        "identifier": "EVENT_3477_disable_trigger_in_level_70",
        "command": "disable_trigger_in_level",
        "args": [AreaObjects.NPC_2, Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL],
    },
    {
        "identifier": "EVENT_3477_disable_trigger_in_level_71",
        "command": "disable_trigger_in_level",
        "args": [
            AreaObjects.NPC_6,
            Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
        ],
    },
    {
        "identifier": "EVENT_3477_j",
        "command": "jmp_if_bit_set",
        "args": [0x7042, 0, "EVENT_3477_item_grant"],
    },
    {"identifier": "EVENT_3477_s", "command": "set_bit", "args": [0x7042, 0]},
    {"identifier": "EVENT_3477_freeze_camera_137", "command": "freeze_camera"},
    {
        "identifier": "EVENT_3477_action_queue_sync_138",
        "command": "action_queue",
        "args": [AreaObjects.SCREEN_FOCUS, True],
        "subscript": [
            {
                "identifier": "EVENT_3477_action_queue_sync_138_SUBSCRIPT_set_animation_speed_0",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_3477_action_queue_sync_138_SUBSCRIPT_shift_z_up_steps_1",
                "command": "shift_z_up_steps",
                "args": [2],
            },
            {
                "identifier": "EVENT_3477_action_queue_sync_138_SUBSCRIPT_set_animation_speed_2",
                "command": "set_animation_speed",
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]],
            },
            {
                "identifier": "EVENT_3477_action_queue_sync_138_SUBSCRIPT_shift_z_down_steps_3",
                "command": "shift_z_down_steps",
                "args": [2],
            },
            {
                "identifier": "EVENT_3477_s2",
                "command": "clear_bit",
                "args": [0x7042, 0],
            },
        ],
    },
    {"identifier": "EVENT_3477_unfreeze_camera_137", "command": "unfreeze_camera"},
    {"identifier": "EVENT_3477_item_grant", "command": "jmp_to_event", "args": [172]},
]
