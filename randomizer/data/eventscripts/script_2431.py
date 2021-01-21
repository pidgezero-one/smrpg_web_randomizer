from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2431_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_2',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_66_4',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2431_jmp_if_random_above_66_7']
    },
    {
        "identifier": 'EVENT_2431_summon_to_current_level_5',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2431_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 405]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_66_7',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2431_jmp_if_random_above_66_10']
    },
    {
        "identifier": 'EVENT_2431_summon_to_current_level_8',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2431_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 405]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_66_10',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2431_jmp_if_random_above_128_13']
    },
    {
        "identifier": 'EVENT_2431_summon_to_current_level_11',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2431_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 405]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_13',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_remove_from_current_level_18']
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_14',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_15',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_jmp_if_random_above_128_24']
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_16',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2431_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_2431_jmp_if_random_above_128_24']
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_18',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_19',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_summon_to_current_level_22']
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_20',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2431_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_2431_jmp_if_random_above_128_24']
    },
    {
        "identifier": 'EVENT_2431_summon_to_current_level_22',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2431_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2431_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_24',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_remove_from_current_level_29']
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_25',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_26',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_jmp_if_random_above_128_35']
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_27',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2431_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_2431_jmp_if_random_above_128_35']
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_29',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_30',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_summon_to_current_level_33']
    },
    {
        "identifier": 'EVENT_2431_remove_from_current_level_31',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2431_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_2431_jmp_if_random_above_128_35']
    },
    {
        "identifier": 'EVENT_2431_summon_to_current_level_33',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2431_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2431_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_35',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_jmp_if_random_above_128_38']
    },
    {
        "identifier": 'EVENT_2431_summon_to_current_level_36',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2431_set_action_script_sync_37',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 410]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_38',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_jmp_if_random_above_128_41']
    },
    {
        "identifier": 'EVENT_2431_summon_to_current_level_39',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2431_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 411]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_41',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_jmp_if_random_above_128_44']
    },
    {
        "identifier": 'EVENT_2431_summon_to_current_level_42',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2431_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 412]
    },
    {
        "identifier": 'EVENT_2431_jmp_if_random_above_128_44',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2431_fade_in_from_black_async_47']
    },
    {
        "identifier": 'EVENT_2431_summon_to_current_level_45',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2431_set_action_script_sync_46',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 412]
    },
    {
        "identifier": 'EVENT_2431_fade_in_from_black_async_47',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2431_ret_48',
        "command": 'ret'
    }
]
