from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_526_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_526_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_526_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_526_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_526_set_vram_priority_4',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_526_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_526_visibility_off_6',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_526_shift_southeast_steps_7',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_526_pause_8',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'ACTION_526_shift_northwest_pixels_9',
        "command": 'shift_northwest_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_526_visibility_on_10',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_526_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_526_set_vram_priority_12',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_526_shift_northeast_steps_13',
        "command": 'shift_northeast_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_526_visibility_off_14',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_526_ret_15',
        "command": 'ret'
    }
]
