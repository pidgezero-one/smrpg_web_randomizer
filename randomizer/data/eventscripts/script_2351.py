from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2351_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_2351_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_if_present_in_current_level_3',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_8, 'EVENT_2351_ret_40'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_if_present_in_current_level_4',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_0, 'EVENT_2351_reset_coords_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2351_jmp_if_present_in_current_level_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_reset_coords_6',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 389],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_pause_8',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_summon_to_current_level_9',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_pause_10',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_2351_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_if_present_in_current_level_13',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_2351_reset_coords_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_2351_jmp_if_present_in_current_level_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_reset_coords_15',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 389],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_pause_17',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_summon_to_current_level_18',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_pause_19',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_remove_from_current_level_20',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_2351_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_if_present_in_current_level_22',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_2, 'EVENT_2351_reset_coords_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_2351_jmp_if_present_in_current_level_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_reset_coords_24',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 389],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_pause_26',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_summon_to_current_level_27',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_pause_28',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_remove_from_current_level_29',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_2351_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_if_present_in_current_level_31',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_3, 'EVENT_2351_reset_coords_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_2351_jmp_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_reset_coords_33',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 389],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_pause_35',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_summon_to_current_level_36',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_pause_37',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_remove_from_current_level_38',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_2351_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2351_ret_40',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
