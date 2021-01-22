from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3782_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02, RadialDirections.SOUTHWEST, 13, 81, 27, [_0x68Flags.Z_HALF]]
    },
    {
        "identifier": 'EVENT_3782_jmp_to_subroutine_1',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3790_jmp_if_present_in_current_level_9']
    },
    {
        "identifier": 'EVENT_3782_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3782_action_queue_sync_2_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3782_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3782_action_queue_sync_2_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3782_action_queue_sync_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3782_action_queue_sync_2_SUBSCRIPT_dec_z_coord_1_step_4',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3782_action_queue_sync_2_SUBSCRIPT_floating_on_5',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3782_pause_3',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3782_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3782_ret_5',
        "command": 'ret'
    }
]
