from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1312_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1312_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1312_action_queue_sync_1_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_1312_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1312_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1312_action_queue_sync_2_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1312_action_queue_sync_2_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1312_action_queue_sync_2_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1312_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1312_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1312_action_queue_async_3_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1312_action_queue_async_3_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1312_action_queue_async_3_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1312_action_queue_async_3_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1312_action_queue_async_3_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1312_action_queue_async_3_SUBSCRIPT_shadow_off_6',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1312_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'EVENT_1312_pause_action_script_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 'EVENT_1312_pause_action_script_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_pause_action_script_9',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_remove_from_level_11',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_remove_from_current_level_13',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1312_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
