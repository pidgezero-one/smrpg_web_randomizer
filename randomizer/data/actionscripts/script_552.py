from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_552_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_552_db_1',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_552_embedded_animation_routine_2',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_552_pause_3',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_552_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_552_pause_5',
        "command": 'pause',
        "args": [22]
    },
    {
        "identifier": 'ACTION_552_bpl_26_27_28_6',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_552_visibility_off_7',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_552_ret_8',
        "command": 'ret'
    }
]
