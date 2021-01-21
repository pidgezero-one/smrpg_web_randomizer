from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2336_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2336_summon_to_level_9']
    },
    {
        "identifier": 'EVENT_2336_jmp_if_object_not_in_level_1',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2336_summon_to_level_14']
    },
    {
        "identifier": 'EVENT_2336_jmp_if_object_not_in_level_2',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2336_summon_to_level_19']
    },
    {
        "identifier": 'EVENT_2336_jmp_if_object_not_in_level_3',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_3, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2336_summon_to_level_24']
    },
    {
        "identifier": 'EVENT_2336_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2336_summon_to_level_29']
    },
    {
        "identifier": 'EVENT_2336_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_5, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2336_summon_to_level_34']
    },
    {
        "identifier": 'EVENT_2336_jmp_if_object_not_in_level_6',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_5, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, 'EVENT_2336_summon_to_level_34']
    },
    {
        "identifier": 'EVENT_2336_pause_7',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2336_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_2336_jmp_if_object_not_in_level_0']
    },
    {
        "identifier": 'EVENT_2336_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2336_reset_coords_10',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2336_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 696]
    },
    {
        "identifier": 'EVENT_2336_pause_12',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'EVENT_2336_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_2336_jmp_if_object_not_in_level_0']
    },
    {
        "identifier": 'EVENT_2336_summon_to_level_14',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2336_reset_coords_15',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2336_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 696]
    },
    {
        "identifier": 'EVENT_2336_pause_17',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'EVENT_2336_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_2336_jmp_if_object_not_in_level_0']
    },
    {
        "identifier": 'EVENT_2336_summon_to_level_19',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2336_reset_coords_20',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2336_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 696]
    },
    {
        "identifier": 'EVENT_2336_pause_22',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'EVENT_2336_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_2336_jmp_if_object_not_in_level_0']
    },
    {
        "identifier": 'EVENT_2336_summon_to_level_24',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2336_reset_coords_25',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2336_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 696]
    },
    {
        "identifier": 'EVENT_2336_pause_27',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'EVENT_2336_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_2336_jmp_if_object_not_in_level_0']
    },
    {
        "identifier": 'EVENT_2336_summon_to_level_29',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2336_reset_coords_30',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2336_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 696]
    },
    {
        "identifier": 'EVENT_2336_pause_32',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'EVENT_2336_jmp_33',
        "command": 'jmp',
        "args": ['EVENT_2336_jmp_if_object_not_in_level_0']
    },
    {
        "identifier": 'EVENT_2336_summon_to_level_34',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2336_reset_coords_35',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2336_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 696]
    },
    {
        "identifier": 'EVENT_2336_pause_37',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'EVENT_2336_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_2336_jmp_if_object_not_in_level_0']
    }
]
