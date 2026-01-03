
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3781_jmp_if_mario_in_air_0',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3781_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE, RadialDirections.NORTHEAST, 24, 25, 0, []]
    },
    {
        "identifier": 'EVENT_3781_db_2',
        "command": 'db',
        "args": [0xfd, 0x49]
    },
    {
        "identifier": 'EVENT_3781_action_queue_sync_3',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
        "subscript": [
            {
                "identifier": 'EVENT_3781_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3781_action_queue_sync_3_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [132]
            },
            {
                "identifier": 'EVENT_3781_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3781_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3781_action_queue_sync_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3781_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3781_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3781_jmp_if_mario_in_air_8',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3781_pause_7']
    },
    {
        "identifier": 'EVENT_3781_set_11',
        "command": "set_var_to_const",
        "args": [0x70df, 49]
    },
    {
        "identifier": 'EVENT_3781_run_event_as_subroutine_25_',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_3781_jmp_if_bit_clear_7_',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3781_ret_12']
    },
    {
        "identifier": 'EVENT_3781_run_event_as_subroutine_25__',
        "command": 'run_event_as_subroutine',
        "args": [3912]
    },
    {
        "identifier": 'EVENT_3781_ret_12',
        "command": 'ret'
    }
]
