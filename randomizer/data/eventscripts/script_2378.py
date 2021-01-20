from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2378_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708c, 1, 'EVENT_2378_ret_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2378_set_bit_1',
        "command": 'set_bit',
        "args": [0x708c, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2378_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2378_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2378_add_frog_coins_4',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2378_run_dialog_5',
        "command": 'run_dialog',
        "args": [3163, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2378_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
