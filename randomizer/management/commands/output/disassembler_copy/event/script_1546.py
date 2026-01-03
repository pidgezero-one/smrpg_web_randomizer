
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1546_summon_to_current_level_0',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1546_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [33]
    },
    {
        "identifier": 'EVENT_1546_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1546_run_dialog_3',
        "command": 'run_dialog',
        "args": [1177, AreaObjects.MARIO, [_0x60Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_1546_put_inventory_4',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_1546_freeze_camera_5',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1546_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1546_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1546_action_queue_sync_6_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1546_action_queue_sync_6_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1546_inc_7',
        "command": 'inc',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_1546_set_short_8',
        "command": 'set_short',
        "args": [0x701c, 0x0028]
    },
    {
        "identifier": 'EVENT_1546_run_background_event_with_pause_return_on_exit_9',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1543, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_1546_ret_10',
        "command": 'ret'
    }
]
