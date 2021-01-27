from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_26_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_26_pause_1',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_26_reset_properties_2',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_26_pause_3',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_26_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_26_set_sprite_sequence_0']
    }
]