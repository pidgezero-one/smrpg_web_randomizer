from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_1023_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_1023_db_1',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_1023_visibility_off_2',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_1023_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_1023_end_all_4',
        "command": 'end_all'
    },
    {
        "identifier": 'ACTION_1023_set_palette_row_5',
        "command": 'set_palette_row',
        "args": [253]
    },
    {
        "identifier": 'ACTION_1023_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.DUMMY_0X06, Rooms._001_____BLUE_BG_NOTHING_THERE]
    },
    {
        "identifier": 'ACTION_1023_summon_object_at_70A8_to_current_level_7',
        "command": 'summon_object_at_70A8_to_current_level'
    },
    {
        "identifier": 'ACTION_1023_end_all_8',
        "command": 'end_all'
    },
    {
        "identifier": 'ACTION_1023_pause_9',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'ACTION_1023_bpl_26_27_28_10',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_1023_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_1023_end_all_12',
        "command": 'end_all'
    },
    {
        "identifier": 'ACTION_1023_object_memory_set_bit_13',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_1023_db_14',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_1023_visibility_off_15',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_1023_clear_solidity_bits_16',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    }
]
