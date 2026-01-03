
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_193_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_193_pause_1',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_193_db_2',
        "command": 'jmp_if_object_within_range_same_z',
        "args": [AreaObjects.MARIO, 0, 5, 'ACTION_193_set_sprite_sequence_4']
    },
    {
        "identifier": 'ACTION_193_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_193_pause_1']
    },
    {
        "identifier": 'ACTION_193_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_193_pause_5',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_193_db_6',
        "command": 'jmp_if_object_within_range_same_z',
        "args": [AreaObjects.MARIO, 0, 5, 'ACTION_193_pause_5']
    },
    {
        "identifier": 'ACTION_193_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_193_set_sprite_sequence_0']
    }
]
