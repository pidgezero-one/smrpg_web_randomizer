
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3616_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_3616_stop_sound_1']
    },
    {
        "identifier": 'EVENT_3616_fade_in_from_black_async_1',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3616_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3616_stop_sound_1',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3616_fade_out_music_to_volume_2',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96]
    },
    {
        "identifier": 'EVENT_3616_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_3616_run_event_as_subroutine_25_',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_3616_jmp_if_bit_clear_7_',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3616_ret_26']
    },
    {
        "identifier": 'EVENT_3616_run_event_as_subroutine_25__',
        "command": 'run_event_as_subroutine',
        "args": [3912]
    },
    {
        "identifier": 'EVENT_3616_ret_26',
        "command": 'ret'
    }
]
