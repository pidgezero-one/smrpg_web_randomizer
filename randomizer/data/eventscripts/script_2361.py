from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2361_summon_to_level_0',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_12, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_13, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_14, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_15, Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7091, 0, 'EVENT_2361_set_action_script_sync_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2361_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2361_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_set_action_script_async_12',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 457],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 459],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 461],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 463],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 481],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_fade_in_from_black_async_18',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2361_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
