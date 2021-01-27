from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_151_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_151_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_151_pause_2',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_151_pause_3',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_151_pause_4',
        "command": 'pause',
        "args": [55]
    },
    {
        "identifier": 'ACTION_151_reset_properties_5',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_151_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_148_reset_properties_0']
    }
]