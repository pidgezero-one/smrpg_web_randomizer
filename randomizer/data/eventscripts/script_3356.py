from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3356_fade_out_music_0',
        "command": 'fade_out_music'
    },
    {
        "identifier": 'EVENT_3356_play_music_default_volume_1',
        "command": 'play_music_default_volume',
        "args": [Music._53_SILENCE]
    },
    {
        "identifier": 'EVENT_3356_set_bit_2',
        "command": 'set_bit',
        "args": [0x707f, 0]
    },
    {
        "identifier": 'EVENT_3356_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, RadialDirections.NORTHEAST, 5, 36, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3356_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3356_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x707f, 0]
    },
    {
        "identifier": 'EVENT_3356_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3356_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3356_action_queue_async_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3356_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3356_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3356_set_7000_to_pressed_button_9',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_3356_jmp_if_7000_all_bits_clear_10',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[5, 7], 'EVENT_3356_pause_8']
    },
    {
        "identifier": 'EVENT_3356_fade_in_music_11',
        "command": 'fade_in_music',
        "args": [Music._66_BOWSERS_CASTLE_2ND_TIME]
    },
    {
        "identifier": 'EVENT_3356_set_12',
        "command": 'set',
        "args": [0x70ae, 20]
    },
    {
        "identifier": 'EVENT_3356_set_action_script_async_13',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3356_ret_14',
        "command": 'ret'
    }
]
