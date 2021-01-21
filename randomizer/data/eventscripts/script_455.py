from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_455_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x707c, 0]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._123_PIPE_VAULT_AREA_01]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._123_PIPE_VAULT_AREA_01]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._123_PIPE_VAULT_AREA_01]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._123_PIPE_VAULT_AREA_01]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._127_PIPE_VAULT_AREA_02]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_6',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._127_PIPE_VAULT_AREA_02]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_7',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._127_PIPE_VAULT_AREA_02]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._124_PIPE_VAULT_AREA_03_LINE_OF_PIPES]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._124_PIPE_VAULT_AREA_03_LINE_OF_PIPES]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_10',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._124_PIPE_VAULT_AREA_03_LINE_OF_PIPES]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_11',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._124_PIPE_VAULT_AREA_03_LINE_OF_PIPES]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._129_PIPE_VAULT_AREA_05]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._129_PIPE_VAULT_AREA_05]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_14',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._129_PIPE_VAULT_AREA_05]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_15',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._129_PIPE_VAULT_AREA_05]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_16',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_17',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_18',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_12, Rooms._128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    },
    {
        "identifier": 'EVENT_455_summon_to_level_19',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_13, Rooms._128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    },
    {
        "identifier": 'EVENT_455_set_7000_to_current_level_20',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_455_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 33, 'EVENT_455_set_27']
    },
    {
        "identifier": 'EVENT_455_set_22',
        "command": 'set',
        "args": [0x70df, 20]
    },
    {
        "identifier": 'EVENT_455_fade_in_from_black_async_23',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_455_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_455_run_event_as_subroutine_25',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_455_ret_26',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_455_set_27',
        "command": 'set',
        "args": [0x70df, 52]
    },
    {
        "identifier": 'EVENT_455_jmp_if_object_trigger_disabled_28',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT, 'EVENT_455_jmp_if_bit_set_30']
    },
    {
        "identifier": 'EVENT_455_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_455_action_queue_async_29_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_455_jmp_if_bit_set_30',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_455_run_event_as_subroutine_25']
    },
    {
        "identifier": 'EVENT_455_run_event_as_subroutine_31',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_455_jmp_if_bit_clear_32',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_455_fade_in_from_black_async_23']
    },
    {
        "identifier": 'EVENT_455_jmp_if_object_trigger_disabled_33',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT, 'EVENT_455_fade_in_from_black_async_23']
    },
    {
        "identifier": 'EVENT_455_fade_in_from_black_async_34',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_455_play_sound_35',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_455_clear_bit_36',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_455_ret_37',
        "command": 'ret'
    }
]
