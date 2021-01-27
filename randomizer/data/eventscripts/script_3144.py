from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3144_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3144_action_queue_sync_0_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3144_set_7000_to_70A0_short_mem_1',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70a8]
    },
    {
        "identifier": 'EVENT_3144_set_70A0_short_mem_to_7000_2',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70aa]
    },
    {
        "identifier": 'EVENT_3144_set_3',
        "command": 'set',
        "args": [0x70a9, 20]
    },
    {
        "identifier": 'EVENT_3144_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'EVENT_3144_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A9]
    },
    {
        "identifier": 'EVENT_3144_inc_6',
        "command": 'inc',
        "args": [0x70a9]
    },
    {
        "identifier": 'EVENT_3144_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3144_resume_action_script_8',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_3144_run_background_event_9',
        "command": 'run_background_event',
        "args": [3143, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3144_ret_10',
        "command": 'ret'
    }
]
