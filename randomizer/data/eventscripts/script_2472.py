from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2472_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x0007]
    },
    {
        "identifier": 'EVENT_2472_set_short_1',
        "command": 'set_short',
        "args": [0x7018, 0x004b]
    },
    {
        "identifier": 'EVENT_2472_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [66]
    },
    {
        "identifier": 'EVENT_2472_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._252_BEAN_VALLEY_MAIN_AREA, RadialDirections.SOUTH, 13, 66, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2472_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 10]
    },
    {
        "identifier": 'EVENT_2472_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_2472_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2472_ret_11']
    },
    {
        "identifier": 'EVENT_2472_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 5, 'EVENT_2472_ret_11']
    },
    {
        "identifier": 'EVENT_2472_pause_8',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2472_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2472_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2472_ret_11',
        "command": 'ret'
    }
]
