from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3746_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 0, 'EVENT_3746_run_event_as_subroutine_11']
    },
    {
        "identifier": 'EVENT_3746_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_3746_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE, RadialDirections.SOUTHWEST, 28, 17, 0, []]
    },
    {
        "identifier": 'EVENT_3746_fade_in_from_black_sync_3',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3746_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3746_action_queue_async_4_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3746_action_queue_async_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3746_action_queue_async_4_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [132]
            },
            {
                "identifier": 'EVENT_3746_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3746_action_queue_async_4_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3746_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_3746_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3746_set_bit_6',
        "command": 'set_bit',
        "args": [0x7068, 1]
    },
    {
        "identifier": 'EVENT_3746_set_bit_7',
        "command": 'set_bit',
        "args": [0x7070, 0]
    },
    {
        "identifier": 'EVENT_3746_set_8',
        "command": 'set',
        "args": [0x70df, 49]
    },
    {
        "identifier": 'EVENT_3746_pause_script_until_effect_done_9',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3746_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3746_run_event_as_subroutine_11',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_3746_ret_12',
        "command": 'ret'
    }
]
