from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3779_jmp_if_mario_in_air_0',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3779_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._379_BEAN_VALLEY_BEANSTALKS_AREA_02, RadialDirections.NORTHWEST, 7, 59, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3779_db_2',
        "command": 'db',
        "args": [0xfd, 0x49],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3779_jmp_if_object_not_in_level_3',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._379_BEAN_VALLEY_BEANSTALKS_AREA_02, 'EVENT_3779_action_queue_sync_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3779_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3779_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3779_action_queue_sync_5_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3779_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3779_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3779_action_queue_sync_6_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [132]
            },
            {
                "identifier": 'EVENT_3779_action_queue_sync_6_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3779_action_queue_sync_6_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3779_action_queue_sync_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3779_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3779_pause_8',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3779_jmp_if_mario_in_air_9',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3779_pause_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3779_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
