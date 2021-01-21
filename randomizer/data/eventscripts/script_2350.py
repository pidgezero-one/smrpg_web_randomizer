from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2350_freeze_camera_0',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2350_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_overwrite_solidity_3',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [8, 87, 9, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0x20, 0x01]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x24, 0x20, 0x00, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_shift_z_up_steps_12',
                "command": 'shift_z_up_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_1_SUBSCRIPT_bpl_26_27_28_13',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2350_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2350_action_queue_sync_2_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2350_action_queue_sync_2_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2350_pause_3',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'EVENT_2350_fade_out_to_black_async_duration_4',
        "command": 'fade_out_to_black_async_duration',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2350_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._419_LAZY_SHELL_CLOUD, RadialDirections.SOUTH, 4, 109, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2350_ret_6',
        "command": 'ret'
    }
]
