from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_175_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_175_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_175_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_175_pause_3',
        "command": 'pause',
        "args": [29]
    },
    {
        "identifier": 'ACTION_175_reset_properties_4',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_175_pause_5',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_175_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_175_set_sprite_sequence_2']
    }
]
