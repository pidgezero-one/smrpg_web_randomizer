from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_478_set_priority_0',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_478_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_478_transfer_to_object_xy_2',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.MEM_70A9]
    },
    {
        "identifier": 'ACTION_478_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_478_db_4',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_478_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80]
    },
    {
        "identifier": 'ACTION_478_embedded_animation_routine_6',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0x00, 0x20, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80]
    },
    {
        "identifier": 'ACTION_478_set_700C_to_7000_short_mem_7',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7024]
    },
    {
        "identifier": 'ACTION_478_db_8',
        "command": 'db',
        "args": [0xfd, 0x25]
    },
    {
        "identifier": 'ACTION_478_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_478_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_478_pause_9']
    }
]
