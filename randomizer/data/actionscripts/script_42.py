from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_42_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_42_pause_1',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_42_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_42_set_sprite_sequence_0']
    }
]
