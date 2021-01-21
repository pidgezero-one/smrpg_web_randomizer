from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_195_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_195_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_195_pause_2',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_195_visibility_off_3',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_195_ret_4',
        "command": 'ret'
    }
]
