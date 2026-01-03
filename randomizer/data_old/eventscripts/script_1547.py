
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1547_j',
        "command": 'jmp_if_bit_set',
        "args": [0x709C, 1, 'EVENT_1547_ret_11']
    },
    {
        "identifier": 'EVENT_1547_s',
        "command": 'set_bit',
        "args": [0x709C, 1]
    },
    {
        "identifier": 'EVENT_1547_stop_sound_6',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1547_action_queue_sync_7',
        "command": 'action_queue',
        'args': [AreaObjects.SCREEN_FOCUS, True],
        "subscript": [
            {
                "identifier": 'EVENT_1547_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1547_action_queue_sync_6_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1547_action_queue_sync_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1547_set_short_9',
        "command": "set_var_to_const",
        "args": [0x701c, 0x0028]
    },
    {
        "identifier": 'EVENT_1547_run_background_event_with_pause_return_on_exit_10',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1543, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_1547_ret_11',
        "command": 'jmp_to_event',
        "args": [173]
    }
]