from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_294_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_294_db_1',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_294_embedded_animation_routine_2',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_294_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_294_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_294_shift_z_up_steps_5',
        "command": 'shift_z_up_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_294_pause_6',
        "command": 'pause',
        "args": [240]
    },
    {
        "identifier": 'ACTION_294_set_7',
        "command": 'set',
        "args": [0x700c, 255]
    },
    {
        "identifier": 'ACTION_294_db_8',
        "command": 'db',
        "args": [0x35, 0x00, 0x04]
    },
    {
        "identifier": 'ACTION_294_db_9',
        "command": 'db',
        "args": [0x35, 0x01, 0x04]
    },
    {
        "identifier": 'ACTION_294_pause_10',
        "command": 'pause',
        "args": [420]
    },
    {
        "identifier": 'ACTION_294_bpl_26_27_28_11',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_294_ret_12',
        "command": 'ret'
    }
]
