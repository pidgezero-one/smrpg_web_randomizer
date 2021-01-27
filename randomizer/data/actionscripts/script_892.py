from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_892_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_892_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_892_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, 0, []]
    },
    {
        "identifier": 'ACTION_892_pause_3',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_892_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [1, 0, []]
    },
    {
        "identifier": 'ACTION_892_pause_5',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_892_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_892_set_sprite_sequence_2']
    }
]
