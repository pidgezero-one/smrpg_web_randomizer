from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2337_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2337_summon_to_level_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_if_object_not_in_level_1',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2337_summon_to_level_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_if_object_not_in_level_2',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2337_summon_to_level_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_if_object_not_in_level_3',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_3, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2337_summon_to_level_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2337_summon_to_level_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_5, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2337_summon_to_level_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_if_object_not_in_level_6',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_5, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2337_summon_to_level_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_pause_7',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_2337_jmp_if_object_not_in_level_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 695],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_pause_11',
        "command": 'pause',
        "args": [112],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_2337_jmp_if_object_not_in_level_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 695],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_pause_15',
        "command": 'pause',
        "args": [112],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_2337_jmp_if_object_not_in_level_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_summon_to_level_17',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 695],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_pause_19',
        "command": 'pause',
        "args": [112],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_2337_jmp_if_object_not_in_level_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_summon_to_level_21',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 695],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_pause_23',
        "command": 'pause',
        "args": [112],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_2337_jmp_if_object_not_in_level_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_summon_to_level_25',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 695],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_pause_27',
        "command": 'pause',
        "args": [112],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_2337_jmp_if_object_not_in_level_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_summon_to_level_29',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 695],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_pause_31',
        "command": 'pause',
        "args": [112],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2337_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_2337_jmp_if_object_not_in_level_0'],
        "subscript": []
    }
]
