from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_557_pause_0',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_557_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 3, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_557_apply_solidity_mod_2',
        "command": 'apply_solidity_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_557_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 662]
    },
    {
        "identifier": 'EVENT_557_set_bit_4',
        "command": 'set_bit',
        "args": [0x7060, 1]
    },
    {
        "identifier": 'EVENT_557_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_557_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_557_set_action_script_sync_8']
    },
    {
        "identifier": 'EVENT_557_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_557_pause_5']
    },
    {
        "identifier": 'EVENT_557_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 672]
    },
    {
        "identifier": 'EVENT_557_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 674]
    },
    {
        "identifier": 'EVENT_557_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 675]
    },
    {
        "identifier": 'EVENT_557_pause_11',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_557_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_557_set_action_script_sync_14']
    },
    {
        "identifier": 'EVENT_557_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_557_pause_11']
    },
    {
        "identifier": 'EVENT_557_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 663]
    },
    {
        "identifier": 'EVENT_557_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_557_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_557_apply_tile_mod_18']
    },
    {
        "identifier": 'EVENT_557_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_557_pause_15']
    },
    {
        "identifier": 'EVENT_557_apply_tile_mod_18',
        "command": 'apply_tile_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_557_apply_solidity_mod_19',
        "command": 'apply_solidity_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 3, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_557_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_557_clear_bit_21',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_557_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_557_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7060, 1]
    },
    {
        "identifier": 'EVENT_557_pause_24',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_557_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_557_pause_0']
    }
]
