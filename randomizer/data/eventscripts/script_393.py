from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_393_jmp_if_object_in_level_0',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_3, Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 'EVENT_393_set_bit_16']
    },
    {
        "identifier": 'EVENT_393_jmp_if_object_in_level_1',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 'EVENT_393_set_bit_16']
    },
    {
        "identifier": 'EVENT_393_jmp_if_object_not_in_level_2',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, 'EVENT_393_summon_to_current_level_4']
    },
    {
        "identifier": 'EVENT_393_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 6, 'EVENT_393_jmp_if_object_not_in_level_27']
    },
    {
        "identifier": 'EVENT_393_summon_to_current_level_4',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_393_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_393_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 22, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_393_action_queue_async_5_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_393_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_393_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 119]
    },
    {
        "identifier": 'EVENT_393_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_393_action_queue_sync_8_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 16, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_393_action_queue_sync_8_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_393_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_393_action_queue_sync_9_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 18, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_393_action_queue_sync_9_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_393_remember_last_object_10',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_393_pause_action_script_11',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_393_pause_action_script_12',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_393_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 119]
    },
    {
        "identifier": 'EVENT_393_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 128]
    },
    {
        "identifier": 'EVENT_393_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_261_fade_out_music_to_volume_2']
    },
    {
        "identifier": 'EVENT_393_set_bit_16',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_393_pause_action_script_17',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_393_pause_action_script_18',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_393_pause_action_script_19',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_393_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_393_action_queue_sync_20_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_393_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_393_action_queue_sync_21_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_393_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_393_action_queue_sync_22_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_393_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 113]
    },
    {
        "identifier": 'EVENT_393_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 113]
    },
    {
        "identifier": 'EVENT_393_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 113]
    },
    {
        "identifier": 'EVENT_393_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_261_fade_out_music_to_volume_2']
    },
    {
        "identifier": 'EVENT_393_jmp_if_object_not_in_level_27',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, 'EVENT_393_summon_to_current_level_4']
    },
    {
        "identifier": 'EVENT_393_remove_from_current_level_28',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_393_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_393_action_queue_sync_8']
    }
]
