
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_204_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_204_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_204_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_917_pause_2']
    }
]
