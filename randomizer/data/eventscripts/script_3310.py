from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3310_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_3310_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3310_stop_all_background_events_1',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3310_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3310_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3310_action_queue_sync_2_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3310_action_queue_sync_2_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3310_action_queue_sync_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3310_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3310_action_queue_sync_3_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3310_action_queue_sync_3_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3310_action_queue_sync_3_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3310_summon_object_at_70A8_to_current_level_4',
        "command": 'summon_object_at_70A8_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3310_disable_event_trigger_for_object_at_70A8_5',
        "command": 'disable_event_trigger_for_object_at_70A8',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3310_add_6',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3310_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [33],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3310_run_dialog_8',
        "command": 'run_dialog',
        "args": [1586, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3310_put_inventory_9',
        "command": 'put_inventory',
        "args": [0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3310_run_background_event_10',
        "command": 'run_background_event',
        "args": [3228, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3310_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
