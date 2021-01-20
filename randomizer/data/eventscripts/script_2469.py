from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2469_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x0009],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_set_short_1',
        "command": 'set_short',
        "args": [0x7018, 0x006d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._252_BEAN_VALLEY_MAIN_AREA, RadialDirections.SOUTH, 16, 72, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2469_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 5, 'EVENT_2469_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_pause_8',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2469_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]