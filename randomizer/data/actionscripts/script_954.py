from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_954_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_954_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_954_walk_to_xy_coords_2',
        "command": 'walk_to_xy_coords',
        "args": [16, 94]
    },
    {
        "identifier": 'ACTION_954_shirt_to_xy_coords_3',
        "command": 'shirt_to_xy_coords',
        "args": [8, 35]
    },
    {
        "identifier": 'ACTION_954_set_vram_priority_4',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_954_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_954_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_953_set_animation_speed_0']
    }
]
