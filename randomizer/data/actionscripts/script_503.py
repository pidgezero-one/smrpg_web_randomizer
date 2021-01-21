from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_503_bpl_26_27_28_0',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_503_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_503_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_503_shift_northeast_steps_3',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_503_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_503_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_503_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_500_db_0']
    }
]
