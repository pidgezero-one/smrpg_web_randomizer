from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_943_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_943_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 395, 'ACTION_943_set_sprite_sequence_23']
    },
    {
        "identifier": 'ACTION_943_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 13, 'ACTION_943_set_sprite_sequence_4']
    },
    {
        "identifier": 'ACTION_943_set_vram_priority_3',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_943_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_943_jmp_if_random_above_128_5',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_943_shift_xy_pixels_9']
    },
    {
        "identifier": 'ACTION_943_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_943_jmp_if_random_above_128_11']
    },
    {
        "identifier": 'ACTION_943_shift_xy_pixels_7',
        "command": 'shift_xy_pixels',
        "args": [252, 2]
    },
    {
        "identifier": 'ACTION_943_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_943_pause_15']
    },
    {
        "identifier": 'ACTION_943_shift_xy_pixels_9',
        "command": 'shift_xy_pixels',
        "args": [4, 2]
    },
    {
        "identifier": 'ACTION_943_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_943_pause_15']
    },
    {
        "identifier": 'ACTION_943_jmp_if_random_above_128_11',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_943_shift_xy_pixels_14']
    },
    {
        "identifier": 'ACTION_943_shift_xy_pixels_12',
        "command": 'shift_xy_pixels',
        "args": [4, 254]
    },
    {
        "identifier": 'ACTION_943_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_943_pause_15']
    },
    {
        "identifier": 'ACTION_943_shift_xy_pixels_14',
        "command": 'shift_xy_pixels',
        "args": [252, 254]
    },
    {
        "identifier": 'ACTION_943_pause_15',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_943_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'ACTION_943_visibility_off_21']
    },
    {
        "identifier": 'ACTION_943_create_packet_at_object_coords_jmp_if_null_17',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.MARIO, 'ACTION_943_pause_18']
    },
    {
        "identifier": 'ACTION_943_pause_18',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_943_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'ACTION_943_visibility_off_21']
    },
    {
        "identifier": 'ACTION_943_create_packet_at_object_coords_jmp_if_null_20',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.MARIO, 'ACTION_943_visibility_off_21']
    },
    {
        "identifier": 'ACTION_943_visibility_off_21',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_943_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_943_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_943_add_24',
        "command": 'add',
        "args": [0x70ae, 0x01]
    },
    {
        "identifier": 'ACTION_943_jmp_if_var_equals_byte_25',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 1, 'ACTION_943_pause_28']
    },
    {
        "identifier": 'ACTION_943_jmp_if_var_equals_byte_26',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 2, 'ACTION_943_pause_36']
    },
    {
        "identifier": 'ACTION_943_jmp_if_var_equals_byte_27',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 3, 'ACTION_943_set_44']
    },
    {
        "identifier": 'ACTION_943_pause_28',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_943_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_943_visibility_off_21']
    },
    {
        "identifier": 'ACTION_943_create_packet_at_object_coords_jmp_if_null_30',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_2, 'ACTION_943_pause_31']
    },
    {
        "identifier": 'ACTION_943_pause_31',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_943_jmp_if_bit_set_32',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_943_visibility_off_21']
    },
    {
        "identifier": 'ACTION_943_create_packet_at_object_coords_jmp_if_null_33',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_2, 'ACTION_943_visibility_off_34']
    },
    {
        "identifier": 'ACTION_943_visibility_off_34',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_943_ret_35',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_943_pause_36',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_943_jmp_if_bit_set_37',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_943_visibility_off_21']
    },
    {
        "identifier": 'ACTION_943_create_packet_at_object_coords_jmp_if_null_38',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_3, 'ACTION_943_pause_39']
    },
    {
        "identifier": 'ACTION_943_pause_39',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_943_jmp_if_bit_set_40',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_943_visibility_off_21']
    },
    {
        "identifier": 'ACTION_943_create_packet_at_object_coords_jmp_if_null_41',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_3, 'ACTION_943_visibility_off_42']
    },
    {
        "identifier": 'ACTION_943_visibility_off_42',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_943_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_943_set_44',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'ACTION_943_pause_45',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_943_jmp_if_bit_set_46',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_943_visibility_off_21']
    },
    {
        "identifier": 'ACTION_943_create_packet_at_object_coords_jmp_if_null_47',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_4, 'ACTION_943_pause_48']
    },
    {
        "identifier": 'ACTION_943_pause_48',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_943_jmp_if_bit_set_49',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_943_visibility_off_21']
    },
    {
        "identifier": 'ACTION_943_create_packet_at_object_coords_jmp_if_null_50',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_4, 'ACTION_943_visibility_off_51']
    },
    {
        "identifier": 'ACTION_943_visibility_off_51',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_943_ret_52',
        "command": 'ret'
    }
]
