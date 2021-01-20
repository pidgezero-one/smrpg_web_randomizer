from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3615_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._378_BEAN_VALLEY_BEANSTALKS_AREA_01, RadialDirections.NORTHWEST, 6, 123, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3615_db_1',
        "command": 'db',
        "args": [0xfd, 0x49],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3615_set_bit_2',
        "command": 'set_bit',
        "args": [0x704b, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3615_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 977],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3615_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3615_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3615_action_queue_sync_4_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [132]
            },
            {
                "identifier": 'EVENT_3615_action_queue_sync_4_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3615_action_queue_sync_4_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3615_action_queue_sync_4_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3615_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3615_pause_6',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3615_jmp_if_mario_in_air_7',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3615_pause_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3615_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
