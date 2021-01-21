from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2309_pause_0',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_2309_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_2309_jmp_20']
    },
    {
        "identifier": 'EVENT_2309_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_2309_jmp_20']
    },
    {
        "identifier": 'EVENT_2309_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2309_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._100_BOOSTER_PASS_AREA_01, 'EVENT_2309_summon_to_level_16']
    },
    {
        "identifier": 'EVENT_2309_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._100_BOOSTER_PASS_AREA_01, 'EVENT_2309_summon_to_level_12']
    },
    {
        "identifier": 'EVENT_2309_jmp_if_object_not_in_level_6',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._100_BOOSTER_PASS_AREA_01, 'EVENT_2309_summon_to_level_8']
    },
    {
        "identifier": 'EVENT_2309_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_2309_jmp_20']
    },
    {
        "identifier": 'EVENT_2309_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2309_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 555]
    },
    {
        "identifier": 'EVENT_2309_set_temp_action_script_sync_10',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_4, 556]
    },
    {
        "identifier": 'EVENT_2309_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_2309_pause_19']
    },
    {
        "identifier": 'EVENT_2309_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2309_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 555]
    },
    {
        "identifier": 'EVENT_2309_set_temp_action_script_sync_14',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_4, 556]
    },
    {
        "identifier": 'EVENT_2309_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_2309_pause_19']
    },
    {
        "identifier": 'EVENT_2309_summon_to_level_16',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2309_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 555]
    },
    {
        "identifier": 'EVENT_2309_set_temp_action_script_sync_18',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_4, 556]
    },
    {
        "identifier": 'EVENT_2309_pause_19',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2309_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_2309_pause_0']
    }
]
