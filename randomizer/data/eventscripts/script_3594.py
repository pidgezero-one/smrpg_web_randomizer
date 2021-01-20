from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3594_jmp_to_subroutine_0',
        "command": 'jmp_to_subroutine',
        "args": [0x76a4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_freeze_all_npcs_until_return_1',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 3, 'EVENT_3594_jmp_to_subroutine_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_set_3',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_run_dialog_5',
        "command": 'run_dialog',
        "args": [2095, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_unfreeze_all_npcs_6',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_add_7',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_set_bit_8',
        "command": 'set_bit',
        "args": [0x704c, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_jmp_to_subroutine_10',
        "command": 'jmp_to_subroutine',
        "args": [0x76a4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_freeze_all_npcs_until_return_11',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_set_12',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_stop_sound_13',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_stop_sound_14',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_stop_sound_15',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_stop_sound_16',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_stop_sound_17',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_stop_sound_18',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_stop_sound_19',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_stop_sound_20',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3594_ret_21',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
