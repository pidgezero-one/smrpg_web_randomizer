from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3330_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3330_action_queue_async_0_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            }
        ]
    },
    {
        "identifier": 'EVENT_3330_set_7010_to_object_xyz_1',
        "command": 'set_7010_to_object_xyz',
        "args": [0x94]
    },
    {
        "identifier": 'EVENT_3330_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7010, 0x7024]
    },
    {
        "identifier": 'EVENT_3330_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7026]
    },
    {
        "identifier": 'EVENT_3330_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7028]
    },
    {
        "identifier": 'EVENT_3330_set_7000_to_object_coord_5',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F, []]
    },
    {
        "identifier": 'EVENT_3330_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x702a, 0x7000]
    },
    {
        "identifier": 'EVENT_3330_run_background_event_7',
        "command": 'run_background_event',
        "args": [3329, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3330_apply_tile_mod_8',
        "command": 'apply_tile_mod',
        "args": [Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3330_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3330_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 0, 'EVENT_3330_ret_15']
    },
    {
        "identifier": 'EVENT_3330_run_background_event_11',
        "command": 'run_background_event',
        "args": [3346, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_3330_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3330_action_queue_sync_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3330_action_queue_sync_12_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3330_action_queue_sync_12_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3330_action_queue_sync_12_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3330_action_queue_sync_12_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3330_action_queue_sync_12_SUBSCRIPT_walk_1_step_northeast_5',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3330_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3330_action_queue_sync_13_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3330_run_event_at_return_14',
        "command": 'run_event_at_return',
        "args": [3331]
    },
    {
        "identifier": 'EVENT_3330_ret_15',
        "command": 'ret'
    }
]
