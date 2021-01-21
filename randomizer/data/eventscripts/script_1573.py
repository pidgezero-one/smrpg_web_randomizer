from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1573_set_short_0',
        "command": 'set_short',
        "args": [0x701a, 0x0000]
    },
    {
        "identifier": 'EVENT_1573_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 6, 'EVENT_1573_set_short_mem_4']
    },
    {
        "identifier": 'EVENT_1573_add_short_2',
        "command": 'add_short',
        "args": [0x7016, 0x0001]
    },
    {
        "identifier": 'EVENT_1573_add_short_3',
        "command": 'add_short',
        "args": [0x7018, 0x0002]
    },
    {
        "identifier": 'EVENT_1573_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1573_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_1573_reset_coords_6',
        "command": 'reset_coords',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1573_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 595]
    },
    {
        "identifier": 'EVENT_1573_add_8',
        "command": 'add',
        "args": [0x7000, 8]
    },
    {
        "identifier": 'EVENT_1573_set_short_mem_9',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_1573_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 170]
    },
    {
        "identifier": 'EVENT_1573_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_1573_set_short_mem_12',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_1573_reset_coords_13',
        "command": 'reset_coords',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1573_reset_coords_14',
        "command": 'reset_coords',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1573_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_1573_set_action_script_sync_19']
    },
    {
        "identifier": 'EVENT_1573_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 596]
    },
    {
        "identifier": 'EVENT_1573_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 596]
    },
    {
        "identifier": 'EVENT_1573_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_1573_pause_21']
    },
    {
        "identifier": 'EVENT_1573_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 594]
    },
    {
        "identifier": 'EVENT_1573_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 594]
    },
    {
        "identifier": 'EVENT_1573_pause_21',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1573_set_bit_22',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1573_ret_23',
        "command": 'ret'
    }
]
