from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_431_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_431_set_short_1',
        "command": 'set_short',
        "args": [0x7016, 0x000d]
    },
    {
        "identifier": 'EVENT_431_set_short_2',
        "command": 'set_short',
        "args": [0x7018, 0x0026]
    },
    {
        "identifier": 'EVENT_431_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [66]
    },
    {
        "identifier": 'EVENT_431_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._143_PIPE_VAULT_GOOMBATHUMPING_ROOM, RadialDirections.NORTHEAST, 2, 123, 1, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_431_enable_controls_until_return_5',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_431_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_431_action_queue_async_6_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x00]
            },
            {
                "identifier": 'EVENT_431_action_queue_async_6_SUBSCRIPT_add_short_1',
                "command": 'add_short',
                "args": [0x701a, 0x0900]
            },
            {
                "identifier": 'EVENT_431_action_queue_async_6_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_431_action_queue_async_6_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [16, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_431_action_queue_async_6_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_431_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_431_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_431_jmp_if_mario_in_air_9',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_431_pause_8']
    },
    {
        "identifier": 'EVENT_431_ret_10',
        "command": 'ret'
    }
]
