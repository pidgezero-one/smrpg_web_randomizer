from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3076_move_script_to_main_thread_0',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_3076_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._102_TIME_RUNNING_OUT, 6]
    },
    {
        "identifier": 'EVENT_3076_stop_music_FDA1_2',
        "command": 'stop_music_FDA1'
    },
    {
        "identifier": 'EVENT_3076_set_bit_3',
        "command": 'set_bit',
        "args": [0x707c, 2]
    },
    {
        "identifier": 'EVENT_3076_set_bit_4',
        "command": 'set_bit',
        "args": [0x707c, 3]
    },
    {
        "identifier": 'EVENT_3076_set_short_5',
        "command": 'set_short',
        "args": [0x7022, 0x0032]
    },
    {
        "identifier": 'EVENT_3076_run_background_event_with_pause_6',
        "command": 'run_background_event_with_pause',
        "args": [3079, 0x7022, [12]]
    },
    {
        "identifier": 'EVENT_3076_ret_7',
        "command": 'ret'
    }
]
