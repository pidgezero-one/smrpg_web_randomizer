from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_479_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_479_transfer_to_object_xy_1',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.MEM_70A9]
    },
    {
        "identifier": 'ACTION_479_visibility_on_2',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_479_db_3',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_479_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2c, 0x00, 0x01, 0x00, 0x00, 0x80, 0x00, 0x80]
    },
    {
        "identifier": 'ACTION_479_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0x00, 0x20, 0x00, 0x01, 0x00, 0x00, 0x80, 0x00, 0x80]
    },
    {
        "identifier": 'ACTION_479_set_700C_to_7000_short_mem_6',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x702a]
    },
    {
        "identifier": 'ACTION_479_db_7',
        "command": 'db',
        "args": [0xfd, 0x25]
    },
    {
        "identifier": 'ACTION_479_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_479_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_479_pause_8']
    }
]
