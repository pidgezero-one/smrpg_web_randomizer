from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2391_freeze_camera_0',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2391_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_overwrite_solidity_3',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [26, 17, 5, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_shift_west_pixels_8',
                "command": 'shift_west_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x20, 0x01]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x24, 0x20, 0x00, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_shift_z_up_steps_13',
                "command": 'shift_z_up_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_1_SUBSCRIPT_bpl_26_27_28_14',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2391_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2391_action_queue_sync_2_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2391_action_queue_sync_2_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [5]
            },
        ]
    },
    {
        "identifier": 'EVENT_2391_pause_3',
        "command": 'pause',
        "args": [112],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2391_fade_out_to_black_async_duration_4',
        "command": 'fade_out_to_black_async_duration',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2391_set_bit_5',
        "command": 'set_bit',
        "args": [0x708e, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2391_enter_area_6',
        "command": 'enter_area',
        "args": [Rooms._417_GARDENERS_HOUSE_OUTSIDE, RadialDirections.SOUTH, 8, 87, 3, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2391_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
