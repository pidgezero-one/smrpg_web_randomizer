from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3142_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x000c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_set_short_1',
        "command": 'set_short',
        "args": [0x7018, 0x006c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7055, 2, 'EVENT_3142_set_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._302_KERO_SEWERS_AREA_08_BELOMES_ROOM, RadialDirections.NORTHEAST, 6, 40, 9, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3280_action_queue_sync_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_stop_sound_6',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_stop_sound_7',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_stop_sound_8',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_stop_sound_9',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3142_action_queue_sync_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3142_action_queue_sync_10_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3142_action_queue_sync_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3142_pause_11',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_jmp_if_mario_in_air_12',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3142_pause_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_set_bit_14',
        "command": 'set_bit',
        "args": [0x704d, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7096, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_enter_area_16',
        "command": 'enter_area',
        "args": [Rooms._069_MIDAS_RIVER_WATERFALL, RadialDirections.SOUTH, 9, 108, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3142_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
