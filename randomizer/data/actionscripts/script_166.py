from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_166_transfer_to_object_xy_0',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'ACTION_166_visibility_on_1',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_166_jump_to_height_silent_2',
        "command": 'jump_to_height_silent',
        "args": [112]
    },
    {
        "identifier": 'ACTION_166_shadow_off_3',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_166_set_vram_priority_4',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_166_set_priority_5',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_166_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_166_shift_f_direction_steps_7',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_166_visibility_off_8',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_166_ret_9',
        "command": 'ret'
    }
]
