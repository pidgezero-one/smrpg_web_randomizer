from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_844_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_844_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_844_shadow_off_2',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_844_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_844_shift_southeast_steps_4',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_844_shift_southeast_pixels_5',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_844_shadow_on_6',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_in_level_7',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_9, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_object_not_in_level_50']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_in_level_8',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_6, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_in_level_9',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_7, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_in_level_10',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_8, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_in_level_11',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_10, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_in_level_12',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_11, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_walk_to_xy_coords_13',
        "command": 'walk_to_xy_coords',
        "args": [7, 28]
    },
    {
        "identifier": 'ACTION_844_shift_southwest_steps_14',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_844_shift_southwest_pixels_15',
        "command": 'shift_southwest_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_844_shadow_off_16',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_844_shift_southwest_steps_17',
        "command": 'shift_southwest_steps',
        "args": [14]
    },
    {
        "identifier": 'ACTION_844_visibility_off_18',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_844_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_844_jmp_if_random_above_128_20',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_844_jmp_if_random_above_66_40']
    },
    {
        "identifier": 'ACTION_844_jmp_if_random_above_128_21',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_844_jmp_if_object_not_in_level_31']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_not_in_level_22',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_10, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_walk_to_xy_coords_23',
        "command": 'walk_to_xy_coords',
        "args": [8, 25]
    },
    {
        "identifier": 'ACTION_844_pause_24',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_set_sprite_sequence_25',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_844_pause_26',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'ACTION_844_set_bit_27',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_844_pause_28',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_reset_properties_29',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_844_jmp_30',
        "command": 'jmp',
        "args": ['ACTION_844_jmp_if_object_in_level_8']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_not_in_level_31',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_11, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_walk_to_xy_coords_32',
        "command": 'walk_to_xy_coords',
        "args": [6, 29]
    },
    {
        "identifier": 'ACTION_844_pause_33',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_set_sprite_sequence_34',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_844_pause_35',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'ACTION_844_set_bit_36',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_844_pause_37',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_reset_properties_38',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_844_jmp_39',
        "command": 'jmp',
        "args": ['ACTION_844_jmp_if_object_in_level_8']
    },
    {
        "identifier": 'ACTION_844_jmp_if_random_above_66_40',
        "command": 'jmp_if_random_above_66',
        "args": [0xa425, 'ACTION_844_jmp_if_object_not_in_level_60']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_not_in_level_41',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_6, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_walk_to_xy_coords_42',
        "command": 'walk_to_xy_coords',
        "args": [8, 34]
    },
    {
        "identifier": 'ACTION_844_pause_43',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_set_sprite_sequence_44',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_844_pause_45',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'ACTION_844_set_bit_46',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_844_pause_47',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_reset_properties_48',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_844_jmp_49',
        "command": 'jmp',
        "args": ['ACTION_844_jmp_if_object_in_level_8']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_not_in_level_50',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_9, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_walk_to_xy_coords_51',
        "command": 'walk_to_xy_coords',
        "args": [9, 29]
    },
    {
        "identifier": 'ACTION_844_shift_east_pixels_52',
        "command": 'shift_east_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_844_pause_53',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_set_sprite_sequence_54',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_844_pause_55',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'ACTION_844_set_bit_56',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_844_pause_57',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_reset_properties_58',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_844_jmp_59',
        "command": 'jmp',
        "args": ['ACTION_844_jmp_if_object_in_level_8']
    },
    {
        "identifier": 'ACTION_844_jmp_if_object_not_in_level_60',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_7, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'ACTION_844_jmp_if_random_above_128_20']
    },
    {
        "identifier": 'ACTION_844_walk_to_xy_coords_61',
        "command": 'walk_to_xy_coords',
        "args": [10, 35]
    },
    {
        "identifier": 'ACTION_844_pause_62',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_set_sprite_sequence_63',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_844_pause_64',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'ACTION_844_set_bit_65',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_844_pause_66',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_844_reset_properties_67',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_844_jmp_68',
        "command": 'jmp',
        "args": ['ACTION_844_jmp_if_object_in_level_8']
    }
]
