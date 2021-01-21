from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_429_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_429_jmp_if_random_above_128_1',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_429_transfer_xyzf_pixels_3']
    },
    {
        "identifier": 'ACTION_429_pause_2',
        "command": 'pause',
        "args": [28]
    },
    {
        "identifier": 'ACTION_429_transfer_xyzf_pixels_3',
        "command": 'transfer_xyzf_pixels',
        "args": [2, 255, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_429_pause_4',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_429_transfer_xyzf_pixels_5',
        "command": 'transfer_xyzf_pixels',
        "args": [254, 1, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_429_pause_6',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_429_transfer_xyzf_pixels_7',
        "command": 'transfer_xyzf_pixels',
        "args": [254, 255, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_429_pause_8',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_429_transfer_xyzf_pixels_9',
        "command": 'transfer_xyzf_pixels',
        "args": [2, 1, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_429_pause_10',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_429_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_429_transfer_xyzf_pixels_3']
    }
]
