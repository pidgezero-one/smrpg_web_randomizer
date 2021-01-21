from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_395_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_395_overwrite_solidity_1',
        "command": 'overwrite_solidity',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_395_sequence_playback_on_2',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_395_object_memory_modify_bits_3',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_395_set_vram_priority_4',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_395_floating_on_5',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_395_fixed_f_coord_off_6',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_395_shadow_on_7',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_395_reset_properties_8',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_395_sequence_looping_off_9',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_395_ret_10',
        "command": 'ret'
    }
]
