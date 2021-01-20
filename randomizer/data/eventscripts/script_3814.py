from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3814_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7042, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 7, 'EVENT_3585_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 0, 'EVENT_3814_remove_from_current_level_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_summon_to_current_level_6',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3814_action_queue_async_8_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [6, 250, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3814_apply_tile_mod_9',
        "command": 'apply_tile_mod',
        "args": [Rooms._022_MUSHROOM_KINGDOM_CASTLE_GUEST_ROOM, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3814_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
