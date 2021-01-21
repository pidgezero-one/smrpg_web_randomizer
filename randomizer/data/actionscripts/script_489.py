from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_489_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_489_db_1',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x03, 0x71, 0x5e]
    },
    {
        "identifier": 'ACTION_489_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_489_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_489_db_1']
    },
    {
        "identifier": 'ACTION_489_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_489_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [7, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_489_pause_6',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_489_sequence_looping_on_7',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_489_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_489_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_405_sequence_looping_on_0']
    }
]
