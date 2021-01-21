from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1679_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_1679_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._265_LANDS_END_UNDERGROUND_AREA_03, RadialDirections.SOUTH, 22, 93, 4, []]
    },
    {
        "identifier": 'EVENT_1679_fade_in_from_black_sync_2',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1679_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1679_action_queue_async_3_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1679_action_queue_async_3_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [144]
            },
            {
                "identifier": 'EVENT_1679_action_queue_async_3_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_1679_action_queue_async_3_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1679_action_queue_async_3_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1679_action_queue_async_3_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1679_action_queue_async_3_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_1679_action_queue_async_3_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1679_ret_4',
        "command": 'ret'
    }
]
