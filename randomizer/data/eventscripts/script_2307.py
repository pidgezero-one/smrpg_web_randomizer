from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2307_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 5, 'EVENT_2307_ret_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_set_bit_2',
        "command": 'set_bit',
        "args": [0x7047, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_set_3',
        "command": 'set',
        "args": [0x70e2, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2307_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2307_action_queue_async_5_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2307_action_queue_async_5_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2307_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._100_BOOSTER_PASS_AREA_01, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_apply_tile_mod_7',
        "command": 'apply_tile_mod',
        "args": [Rooms._100_BOOSTER_PASS_AREA_01, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_apply_solidity_mod_8',
        "command": 'apply_solidity_mod',
        "args": [Rooms._100_BOOSTER_PASS_AREA_01, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.SCREEN_FOCUS, 391],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_run_dialog_11',
        "command": 'run_dialog',
        "args": [3154, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2307_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
