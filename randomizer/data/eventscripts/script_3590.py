from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3590_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x0017]
    },
    {
        "identifier": 'EVENT_3590_set_short_1',
        "command": 'set_short',
        "args": [0x7018, 0x002f]
    },
    {
        "identifier": 'EVENT_3590_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [66]
    },
    {
        "identifier": 'EVENT_3590_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._087_ROSE_TOWN_ITEM_SHOP, RadialDirections.SOUTH, 7, 69, 3, []]
    },
    {
        "identifier": 'EVENT_3590_fade_out_music_to_volume_4',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96]
    },
    {
        "identifier": 'EVENT_3590_jmp_if_object_trigger_disabled_5',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_5, Rooms._087_ROSE_TOWN_ITEM_SHOP, 'EVENT_3590_set_bit_7']
    },
    {
        "identifier": 'EVENT_3590_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3590_action_queue_sync_6_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3590_set_bit_7',
        "command": 'set_bit',
        "args": [0x709c, 3]
    },
    {
        "identifier": 'EVENT_3590_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_3590_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [282]
    },
    {
        "identifier": 'EVENT_3590_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3590_pause_11',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3590_jmp_if_mario_in_air_12',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3590_pause_11']
    },
    {
        "identifier": 'EVENT_3590_stop_sound_13',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3590_play_sound_14',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 6]
    },
    {
        "identifier": 'EVENT_3590_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_3590_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_3591_run_event_as_subroutine_4']
    }
]
