from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3209_run_dialog_0',
        "command": 'run_dialog',
        "args": [1656, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3209_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3209_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3209_action_queue_sync_1_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3209_action_queue_sync_1_SUBSCRIPT_walk_1_step_f_direction_2',
                "command": 'walk_1_step_f_direction'
            },
            {
                "identifier": 'EVENT_3209_action_queue_sync_1_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3209_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3209_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3209_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3209_action_queue_async_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [36]
            }
        ]
    },
    {
        "identifier": 'EVENT_3209_set_short_3',
        "command": 'set_short',
        "args": [0x700e, 0x0048]
    },
    {
        "identifier": 'EVENT_3209_jmp_to_event_4',
        "command": 'jmp_to_event',
        "args": [16]
    }
]
