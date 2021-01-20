from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1711_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [65],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1711_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._076_BANDITS_WAY_AREA_01, RadialDirections.SOUTH, 4, 52, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1711_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1711_action_queue_async_2_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1711_action_queue_async_2_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xc8, 0x00]
            },
            {
                "identifier": 'EVENT_1711_action_queue_async_2_SUBSCRIPT_add_short_2',
                "command": 'add_short',
                "args": [0x701a, 0x0900]
            },
            {
                "identifier": 'EVENT_1711_action_queue_async_2_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_1711_action_queue_async_2_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1711_action_queue_async_2_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1711_action_queue_async_2_SUBSCRIPT_jmp_if_mario_in_air_6',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1711_action_queue_async_2_SUBSCRIPT_pause_5']
            },
            {
                "identifier": 'EVENT_1711_action_queue_async_2_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1711_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
