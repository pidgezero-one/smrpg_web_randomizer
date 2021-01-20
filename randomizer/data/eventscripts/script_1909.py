from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1909_freeze_all_npcs_until_return_0',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_jmp_if_random_above_128_1',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_1909_set_short_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_set_short_2',
        "command": 'set_short',
        "args": [0x700e, 0x0088],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_1909_start_battle_700E_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_set_short_4',
        "command": 'set_short',
        "args": [0x700e, 0x0089],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_start_battle_700E_5',
        "command": 'start_battle_700E',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1909_disable_trigger_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1695_reset_and_choose_game_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1909_action_queue_async_8_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1909_set_bit_9',
        "command": 'set_bit',
        "args": [0x704d, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_disable_trigger_10',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_resume_action_script_11',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_unfreeze_all_npcs_12',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_set_short_14',
        "command": 'set_short',
        "args": [0x701c, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1909_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
