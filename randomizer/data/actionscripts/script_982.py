from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_982_pause_0',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_982_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_982_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_982_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_982_face_northeast_4',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_982_pause_5',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_982_shift_northwest_steps_6',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_982_face_northeast_7',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_982_pause_8',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_982_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_982_shift_southeast_steps_3']
    }
]
