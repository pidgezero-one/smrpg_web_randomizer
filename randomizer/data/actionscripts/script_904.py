from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_904_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_904_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_904_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_904_shift_z_up_steps_3',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_904_visibility_off_4',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_904_ret_5',
        "command": 'ret'
    }
]
