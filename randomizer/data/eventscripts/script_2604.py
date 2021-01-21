from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2604_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708f, 5, 'EVENT_2604_ret_16']
    },
    {
        "identifier": 'EVENT_2604_set_bit_1',
        "command": 'set_bit',
        "args": [0x708f, 5]
    },
    {
        "identifier": 'EVENT_2604_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2604_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_2_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_2_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2604_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 7]
    },
    {
        "identifier": 'EVENT_2604_pause_4',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_2604_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2604_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_5_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_5_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_5_SUBSCRIPT_shirt_to_xy_coords_3',
                "command": 'shirt_to_xy_coords',
                "args": [21, 50]
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_5_SUBSCRIPT_shift_west_pixels_4',
                "command": 'shift_west_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_5_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_5_SUBSCRIPT_shirt_to_xy_coords_6',
                "command": 'shirt_to_xy_coords',
                "args": [0, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2604_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2604_action_queue_sync_6_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_6_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2604_action_queue_sync_6_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_2604_action_queue_sync_6_SUBSCRIPT_ret_2',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_2604_stop_embedded_action_script_7',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2604_pause_8',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2604_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 385]
    },
    {
        "identifier": 'EVENT_2604_pause_10',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2604_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2604_run_dialog_12',
        "command": 'run_dialog',
        "args": [3161, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_2604_put_inventory_13',
        "command": 'put_inventory',
        "args": [items.UltraHammer]
    },
    {
        "identifier": 'EVENT_2604_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2604_jmp_if_objects_action_script_running_15',
        "command": 'jmp_if_objects_action_script_running',
        "args": [AreaObjects.MARIO, 'EVENT_2604_pause_14']
    },
    {
        "identifier": 'EVENT_2604_ret_16',
        "command": 'ret'
    }
]
