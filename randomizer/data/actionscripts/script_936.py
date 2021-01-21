from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_936_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_936_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_936_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_936_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_936_db_4',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_936_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_936_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_936_set_700C_to_pressed_button_7',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_936_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_936_walk_to_xy_coords_12']
    },
    {
        "identifier": 'ACTION_936_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 23, 'ACTION_936_walk_to_xy_coords_18']
    },
    {
        "identifier": 'ACTION_936_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 24, 'ACTION_936_walk_to_xy_coords_23']
    },
    {
        "identifier": 'ACTION_936_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 25, 'ACTION_936_walk_to_xy_coords_26']
    },
    {
        "identifier": 'ACTION_936_walk_to_xy_coords_12',
        "command": 'walk_to_xy_coords',
        "args": [5, 27]
    },
    {
        "identifier": 'ACTION_936_shift_z_down_pixels_13',
        "command": 'shift_z_down_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_936_shift_south_pixels_14',
        "command": 'shift_south_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_936_set_vram_priority_15',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_936_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_936_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_936_pause_16']
    },
    {
        "identifier": 'ACTION_936_walk_to_xy_coords_18',
        "command": 'walk_to_xy_coords',
        "args": [6, 26]
    },
    {
        "identifier": 'ACTION_936_shift_z_down_pixels_19',
        "command": 'shift_z_down_pixels',
        "args": [16]
    },
    {
        "identifier": 'ACTION_936_shift_east_pixels_20',
        "command": 'shift_east_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_936_set_vram_priority_21',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_936_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_936_pause_16']
    },
    {
        "identifier": 'ACTION_936_walk_to_xy_coords_23',
        "command": 'walk_to_xy_coords',
        "args": [5, 25]
    },
    {
        "identifier": 'ACTION_936_shift_z_down_pixels_24',
        "command": 'shift_z_down_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_936_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_936_pause_16']
    },
    {
        "identifier": 'ACTION_936_walk_to_xy_coords_26',
        "command": 'walk_to_xy_coords',
        "args": [5, 26]
    },
    {
        "identifier": 'ACTION_936_shift_z_down_pixels_27',
        "command": 'shift_z_down_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_936_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_936_pause_16']
    }
]
