from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_511_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_511_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_511_action_queue_sync_7']
    },
    {
        "identifier": 'EVENT_511_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_511_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_511_action_queue_sync_2_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_511_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [32]
    },
    {
        "identifier": 'EVENT_511_disable_trigger_in_level_4',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_8, Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    },
    {
        "identifier": 'EVENT_511_remember_last_object_5',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_511_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_511_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_511_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_511_action_queue_sync_7_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_511_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [32]
    },
    {
        "identifier": 'EVENT_511_disable_trigger_in_level_9',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    },
    {
        "identifier": 'EVENT_511_remember_last_object_10',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_511_ret_11',
        "command": 'ret'
    }
]
