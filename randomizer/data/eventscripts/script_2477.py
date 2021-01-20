from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2477_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_2477_jmp_if_bit_set_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_2477_jmp_if_bit_set_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_2477_jmp_if_bit_set_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_2477_jmp_if_bit_set_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_2477_jmp_if_bit_set_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_2477_jmp_if_bit_set_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_2477_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_2477_jmp_if_bit_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_bit_9',
        "command": 'set_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 845],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_summon_to_current_level_11',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_2477_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_2477_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_bit_14',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 845],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_summon_to_current_level_16',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_2477_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_2477_jmp_if_bit_set_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_bit_19',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 845],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_summon_to_current_level_21',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_2477_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_2477_jmp_if_bit_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_bit_24',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 845],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_summon_to_current_level_26',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_2477_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_2477_jmp_if_bit_set_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_bit_29',
        "command": 'set_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 845],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_summon_to_current_level_31',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_2477_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_2477_jmp_if_bit_set_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_bit_34',
        "command": 'set_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 845],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_summon_to_current_level_36',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2477_jmp_37',
        "command": 'jmp',
        "args": ['EVENT_2477_pause_0'],
        "subscript": []
    }
]
