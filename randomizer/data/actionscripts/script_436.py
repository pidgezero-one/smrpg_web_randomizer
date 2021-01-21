from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_436_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_436_db_1',
        "command": 'db',
        "args": [0xc8, 0x17]
    },
    {
        "identifier": 'ACTION_436_run_away_transfer_2',
        "command": 'run_away_transfer'
    },
    {
        "identifier": 'ACTION_436_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_436_set_vram_priority_0']
    }
]
