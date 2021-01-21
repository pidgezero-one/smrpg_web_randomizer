from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3787_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, RadialDirections.NORTHEAST, 26, 120, 29, []]
    },
    {
        "identifier": 'EVENT_3787_jmp_to_subroutine_1',
        "command": 'jmp_to_subroutine',
        "args": [0xc24d]
    },
    {
        "identifier": 'EVENT_3787_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3787_action_queue_sync_2_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3787_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3787_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3787_action_queue_sync_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3787_action_queue_sync_2_SUBSCRIPT_dec_z_coord_1_step_4',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3787_action_queue_sync_2_SUBSCRIPT_floating_on_5',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3787_pause_3',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3787_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3787_set_5',
        "command": 'set',
        "args": [0x70df, 39]
    },
    {
        "identifier": 'EVENT_3787_ret_6',
        "command": 'ret'
    }
]
