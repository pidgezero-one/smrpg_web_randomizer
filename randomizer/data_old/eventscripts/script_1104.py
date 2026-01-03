
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1104_deactivate_sound_channels_1',
        "command": 'deactivate_sound_channels',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1104_action_queue_async_1',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_9, False],
        "subscript": [
            {
                "identifier": 'EVENT_1104_action_queue_async_1_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1104_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1104_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7087, 0, 'EVENT_1104_ret_26']
    },
    {
        "identifier": 'EVENT_1104_run_event_as_subroutine_25_',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_1104_jmp_if_bit_clear_7_',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_1104_ret_26']
    },
    {
        "identifier": 'EVENT_1104_run_event_as_subroutine_25__',
        "command": 'run_event_as_subroutine',
        "args": [3893]
    },
    {
        "identifier": 'EVENT_1104_ret_26',
        "command": 'ret'
    }
]
