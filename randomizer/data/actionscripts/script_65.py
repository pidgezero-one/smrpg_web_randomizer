from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_65_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_65_db_1',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_65_shift_northeast_steps_2',
        "command": 'shift_northeast_steps',
        "args": [13]
    },
    {
        "identifier": 'ACTION_65_shift_northeast_pixels_3',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_65_set_bit_4',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_65_pause_5',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_65_shift_northeast_steps_6',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_65_shift_northeast_pixels_7',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_65_visibility_off_8',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_65_ret_9',
        "command": 'ret'
    }
]
