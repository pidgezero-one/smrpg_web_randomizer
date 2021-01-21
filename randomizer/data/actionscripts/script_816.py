from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_816_shadow_on_0',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_816_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_816_shift_z_up_steps_2',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_816_shift_z_down_steps_3',
        "command": 'shift_z_down_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_816_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_816_shift_z_up_steps_2']
    }
]
