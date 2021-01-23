from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_537_move_script_to_background_thread_1_0',
        "command": 'move_script_to_background_thread_1'
    },
    {
        "identifier": 'EVENT_537_set_7000_to_current_level_1',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_537_jmp_if_7000_equals_short_2',
        "command": 'jmp_if_7000_equals_short',
        "args": [98, 'EVENT_537_action_queue_sync_7']
    },
    {
        "identifier": 'EVENT_537_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_537_action_queue_sync_3_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 252, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_537_jmp_if_object_trigger_disabled_4',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_2, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F, 'EVENT_537_jmp_6']
    },
    {
        "identifier": 'EVENT_537_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_537_action_queue_sync_5_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_537_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_537_fade_out_music_to_volume_10']
    },
    {
        "identifier": 'EVENT_537_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_537_action_queue_sync_7_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 252, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_537_jmp_if_object_trigger_disabled_8',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._098_ROSE_TOWN_TREASURE_HOUSE_2F, 'EVENT_537_fade_out_music_to_volume_10']
    },
    {
        "identifier": 'EVENT_537_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_537_action_queue_sync_9_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_537_fade_out_music_to_volume_10',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96]
    },
    {
        "identifier": 'EVENT_537_remember_last_object_11',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_537_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_537_run_event_as_subroutine_13',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_537_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_537_jmp_if_object_trigger_disabled_15',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_2, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_537_jmp_if_object_trigger_disabled_16',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._098_ROSE_TOWN_TREASURE_HOUSE_2F, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_537_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_537_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_537_ret_19',
        "command": 'ret'
    }
]
