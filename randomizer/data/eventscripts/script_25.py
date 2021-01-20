from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_25_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_25_set_temp_action_script_sync_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_25_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_24_reset_and_choose_game_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_25_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_24_jmp_if_bit_clear_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_25_set_temp_action_script_sync_3',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 284],
        "subscript": []
    },
    {
        "identifier": 'EVENT_25_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 5, 'EVENT_24_clear_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_25_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_25_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_24_load_600f_15'],
        "subscript": []
    },
]
