from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_551_pause_0',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 3, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_apply_solidity_mod_2',
        "command": 'apply_solidity_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 664],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_pause_4',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 2, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_apply_solidity_mod_6',
        "command": 'apply_solidity_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 3, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_pause_7',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7060, 1, 'EVENT_551_apply_tile_mod_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_551_pause_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 3, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_apply_solidity_mod_11',
        "command": 'apply_solidity_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_pause_12',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 2, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_apply_solidity_mod_14',
        "command": 'apply_solidity_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 3, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_pause_15',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_551_jmp_to_event_16',
        "command": 'jmp_to_event',
        "args": [551],
        "subscript": []
    },
]
