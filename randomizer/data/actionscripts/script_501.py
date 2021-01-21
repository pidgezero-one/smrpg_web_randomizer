from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_501_bpl_26_27_28_0',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_501_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_501_db_2',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_501_db_3',
        "command": 'db',
        "args": [0x24, 0x40, 0x01, 0x60, 0xff]
    },
    {
        "identifier": 'ACTION_501_pause_4',
        "command": 'pause',
        "args": [14]
    },
    {
        "identifier": 'ACTION_501_set_bit_5',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_501_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_500_db_0']
    }
]
