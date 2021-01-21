from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_127_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_127_floating_off_1',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_127_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_127_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_127_visibility_off_4',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_127_sequence_looping_on_5',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_127_pause_6',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_127_visibility_on_7',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_127_pause_8',
        "command": 'pause',
        "args": [26]
    },
    {
        "identifier": 'ACTION_127_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_127_pause_10',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_127_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_127_ret_12',
        "command": 'ret'
    }
]
