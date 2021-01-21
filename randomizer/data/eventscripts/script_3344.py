from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3344_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 7, 'EVENT_3344_jmp_to_event_13']
    },
    {
        "identifier": 'EVENT_3344_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3344_action_queue_async_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_1_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_1_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3344_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3344_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_shift_xy_pixels_0',
                "command": 'shift_xy_pixels',
                "args": [4, 4]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_set_vram_priority_7',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_walk_1_step_southwest_10',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_jmp_if_bit_clear_12',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 0, 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_pause_11']
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_floating_off_13',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_shift_z_down_pixels_15',
                "command": 'shift_z_down_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_jump_to_height_16',
                "command": 'jump_to_height',
                "args": [256]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_floating_off_18',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_visibility_off_19',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_3_SUBSCRIPT_db_20',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3344_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_shift_xy_pixels_0',
                "command": 'shift_xy_pixels',
                "args": [252, 254]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_walk_1_step_southwest_8',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x1e]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_floating_off_12',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_set_bit_13',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_shift_z_down_pixels_15',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_jump_to_height_16',
                "command": 'jump_to_height',
                "args": [256]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_floating_off_18',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_visibility_off_19',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_4_SUBSCRIPT_db_20',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3344_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_shift_xy_pixels_0',
                "command": 'shift_xy_pixels',
                "args": [252, 254]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_walk_1_step_southwest_9',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x4f]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_12',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_floating_off_13',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_set_bit_14',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_shift_z_down_pixels_16',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_jump_to_height_17',
                "command": 'jump_to_height',
                "args": [256]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_floating_off_19',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_visibility_off_20',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_5_SUBSCRIPT_db_21',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3344_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_shift_xy_pixels_0',
                "command": 'shift_xy_pixels',
                "args": [252, 254]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_walk_1_step_southwest_9',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x80]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_clear_solidity_bits_12',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_floating_off_13',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_set_bit_14',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_shift_z_down_pixels_16',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_jump_to_height_17',
                "command": 'jump_to_height',
                "args": [256]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_floating_off_19',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_visibility_off_20',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_6_SUBSCRIPT_db_21',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3344_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_shift_xy_pixels_0',
                "command": 'shift_xy_pixels',
                "args": [252, 254]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_walk_1_step_southwest_9',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0xb1]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_set_bit_12',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_clear_solidity_bits_13',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_floating_off_14',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_shift_z_down_pixels_16',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_jump_to_height_17',
                "command": 'jump_to_height',
                "args": [256]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_floating_off_19',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_visibility_off_20',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_7_SUBSCRIPT_db_21',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3344_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_shift_xy_pixels_0',
                "command": 'shift_xy_pixels',
                "args": [252, 254]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_walk_1_step_southwest_9',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0xe2]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_clear_solidity_bits_12',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_floating_off_13',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_set_bit_14',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_shift_z_down_pixels_16',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_jump_to_height_17',
                "command": 'jump_to_height',
                "args": [256]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_floating_off_19',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_visibility_off_20',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3344_action_queue_sync_8_SUBSCRIPT_db_21',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3344_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3344_action_queue_async_9_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_9_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_9_SUBSCRIPT_jmp_if_bit_clear_2',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 0, 'EVENT_3344_action_queue_async_9_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_9_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_9_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_9_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_9_SUBSCRIPT_clear_bit_7',
                "command": 'clear_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_9_SUBSCRIPT_end_loop_8',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3344_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3344_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_10_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3344_action_queue_async_10_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3344_set_bit_11',
        "command": 'set_bit',
        "args": [0x707e, 7]
    },
    {
        "identifier": 'EVENT_3344_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3344_jmp_to_event_13',
        "command": 'jmp_to_event',
        "args": [15]
    }
]
