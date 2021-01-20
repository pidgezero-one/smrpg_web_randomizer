from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1546_summon_to_current_level_0',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [33],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_run_dialog_3',
        "command": 'run_dialog',
        "args": [1177, AreaObjects.MARIO, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_put_inventory_4',
        "command": 'put_inventory',
        "args": [0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_1546_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_stop_sound_6',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1546_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1546_action_queue_sync_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1546_add_8',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_set_short_9',
        "command": 'set_short',
        "args": [0x701c, 0x0028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_run_background_event_with_pause_return_on_exit_10',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1543, 0x701c, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1546_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
