from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2348_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_2348_jmp_if_present_in_current_level_1',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_4, 'EVENT_2348_jmp_if_present_in_current_level_3']
    },
    {
        "identifier": 'EVENT_2348_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2348_action_queue_sync_2_SUBSCRIPT_shift_north_pixels_0',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2348_action_queue_sync_2_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2348_jmp_if_present_in_current_level_3',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_5, 'EVENT_2348_jmp_if_present_in_current_level_5']
    },
    {
        "identifier": 'EVENT_2348_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2348_action_queue_sync_4_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [18]
            },
            {
                "identifier": 'EVENT_2348_action_queue_sync_4_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2348_jmp_if_present_in_current_level_5',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_6, 'EVENT_2348_jmp_if_present_in_current_level_7']
    },
    {
        "identifier": 'EVENT_2348_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2348_action_queue_sync_6_SUBSCRIPT_shift_north_pixels_0',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2348_action_queue_sync_6_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2348_jmp_if_present_in_current_level_7',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_8, 'EVENT_2348_action_queue_async_9']
    },
    {
        "identifier": 'EVENT_2348_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2348_action_queue_sync_8_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2348_action_queue_sync_8_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2348_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2348_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2348_action_queue_async_9_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2348_action_queue_async_9_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2348_action_queue_async_9_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2348_action_queue_async_9_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2348_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2348_ret_11',
        "command": 'ret'
    }
]
