from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_548_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_548_jmp_if_random_above_128_35']
    },
    {
        "identifier": 'EVENT_548_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_548_jmp_if_random_above_128_39']
    },
    {
        "identifier": 'EVENT_548_set_7000_to_object_coord_2',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F, []]
    },
    {
        "identifier": 'EVENT_548_jmp_if_7000_equals_short_3',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_548_jmp_if_random_above_66_19']
    },
    {
        "identifier": 'EVENT_548_jmp_if_7000_equals_short_4',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_548_jmp_if_random_above_128_13']
    },
    {
        "identifier": 'EVENT_548_jmp_if_7000_equals_short_5',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_548_jmp_if_random_above_66_23']
    },
    {
        "identifier": 'EVENT_548_jmp_if_7000_equals_short_6',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_548_jmp_if_random_above_128_17']
    },
    {
        "identifier": 'EVENT_548_jmp_if_7000_equals_short_7',
        "command": 'jmp_if_7000_equals_short',
        "args": [4, 'EVENT_548_jmp_if_random_above_66_27']
    },
    {
        "identifier": 'EVENT_548_jmp_if_7000_equals_short_8',
        "command": 'jmp_if_7000_equals_short',
        "args": [5, 'EVENT_548_jmp_if_random_above_128_15']
    },
    {
        "identifier": 'EVENT_548_jmp_if_7000_equals_short_9',
        "command": 'jmp_if_7000_equals_short',
        "args": [6, 'EVENT_548_jmp_if_random_above_66_31']
    },
    {
        "identifier": 'EVENT_548_jmp_if_7000_equals_short_10',
        "command": 'jmp_if_7000_equals_short',
        "args": [7, 'EVENT_548_jmp_if_random_above_128_11']
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_128_11',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_548_jmp_if_random_above_66_19']
    },
    {
        "identifier": 'EVENT_548_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_548_jmp_if_random_above_66_31']
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_128_13',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_548_jmp_if_random_above_66_19']
    },
    {
        "identifier": 'EVENT_548_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_548_jmp_if_random_above_66_23']
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_128_15',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_548_jmp_if_random_above_66_27']
    },
    {
        "identifier": 'EVENT_548_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_548_jmp_if_random_above_66_31']
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_128_17',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_548_jmp_if_random_above_66_27']
    },
    {
        "identifier": 'EVENT_548_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_548_jmp_if_random_above_66_23']
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_66_19',
        "command": 'jmp_if_random_above_66',
        "args": [0x5f56, 0x5f6e]
    },
    {
        "identifier": 'EVENT_548_set_bit_20',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_548_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 635]
    },
    {
        "identifier": 'EVENT_548_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_66_23',
        "command": 'jmp_if_random_above_66',
        "args": [0x5f62, 0x5f4a]
    },
    {
        "identifier": 'EVENT_548_set_bit_24',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_548_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 635]
    },
    {
        "identifier": 'EVENT_548_ret_26',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_66_27',
        "command": 'jmp_if_random_above_66',
        "args": [0x5f56, 0x5f6e]
    },
    {
        "identifier": 'EVENT_548_set_bit_28',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_548_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 635]
    },
    {
        "identifier": 'EVENT_548_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_66_31',
        "command": 'jmp_if_random_above_66',
        "args": [0x5f62, 0x5f4a]
    },
    {
        "identifier": 'EVENT_548_set_bit_32',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_548_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 635]
    },
    {
        "identifier": 'EVENT_548_ret_34',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_128_35',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_548_pause_43']
    },
    {
        "identifier": 'EVENT_548_set_bit_36',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_548_set_action_script_sync_37',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 635]
    },
    {
        "identifier": 'EVENT_548_ret_38',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_548_jmp_if_random_above_128_39',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_548_pause_43']
    },
    {
        "identifier": 'EVENT_548_set_bit_40',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_548_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 635]
    },
    {
        "identifier": 'EVENT_548_ret_42',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_548_pause_43',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_548_set_bit_44',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_548_ret_45',
        "command": 'ret'
    }
]
