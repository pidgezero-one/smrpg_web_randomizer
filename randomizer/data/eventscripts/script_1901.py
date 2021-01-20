from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1901_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1901_ret_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1901_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1901_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [1840],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1901_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1901_action_queue_sync_3_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1901_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1901_action_queue_sync_4_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_4_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_4_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_4_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_4_SUBSCRIPT_walk_1_step_southeast_5',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_4_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1901_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1901_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_5_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_5_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_5_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_5_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_5_SUBSCRIPT_walk_1_step_northwest_5',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_5_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_5_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1901_action_queue_sync_5_SUBSCRIPT_clear_bit_8',
                "command": 'clear_bit',
                "args": [0x7043, 0]
            },
        ]
    },
    {
        "identifier": 'EVENT_1901_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
