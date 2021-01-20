from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1627_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 4, 'EVENT_1627_jmp_if_bit_clear_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_summon_to_current_level_2',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 160],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 1, 'EVENT_1627_summon_to_current_level_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_summon_to_current_level_5',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 160],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_summon_to_current_level_7',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 160],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x7056, 1, 'EVENT_1627_jmp_if_bit_clear_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_summon_to_current_level_12',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 160],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7056, 3, 'EVENT_1627_fade_in_from_black_async_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_summon_to_current_level_15',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 160],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1627_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
