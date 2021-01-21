from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3331_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 0, 'EVENT_3331_play_music_default_volume_23']
    },
    {
        "identifier": 'EVENT_3331_pause_short_1',
        "command": 'pause_short',
        "args": [700]
    },
    {
        "identifier": 'EVENT_3331_start_battle_2',
        "command": 'start_battle',
        "args": [0x00ac, 8]
    },
    {
        "identifier": 'EVENT_3331_set_bit_3',
        "command": 'set_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_3331_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_3331_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3331_set_bit_6',
        "command": 'set_bit',
        "args": [0x707e, 0]
    },
    {
        "identifier": 'EVENT_3331_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 1023]
    },
    {
        "identifier": 'EVENT_3331_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 1023]
    },
    {
        "identifier": 'EVENT_3331_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 1023]
    },
    {
        "identifier": 'EVENT_3331_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 1023]
    },
    {
        "identifier": 'EVENT_3331_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 1023]
    },
    {
        "identifier": 'EVENT_3331_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 1023]
    },
    {
        "identifier": 'EVENT_3331_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 1023]
    },
    {
        "identifier": 'EVENT_3331_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 1023]
    },
    {
        "identifier": 'EVENT_3331_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 1023]
    },
    {
        "identifier": 'EVENT_3331_apply_tile_mod_16',
        "command": 'apply_tile_mod',
        "args": [Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3331_apply_tile_mod_17',
        "command": 'apply_tile_mod',
        "args": [Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3331_db_18',
        "command": 'db',
        "args": [0xfd, 0x44]
    },
    {
        "identifier": 'EVENT_3331_reset_priority_set_19',
        "command": 'reset_priority_set'
    },
    {
        "identifier": 'EVENT_3331_fade_in_from_black_async_20',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3331_set_short_21',
        "command": 'set_short',
        "args": [0x700a, 0x00de]
    },
    {
        "identifier": 'EVENT_3331_jmp_to_event_22',
        "command": 'jmp_to_event',
        "args": [720]
    },
    {
        "identifier": 'EVENT_3331_play_music_default_volume_23',
        "command": 'play_music_default_volume',
        "args": [Music._15_HERES_SOME_WEAPONS]
    },
    {
        "identifier": 'EVENT_3331_ret_24',
        "command": 'ret'
    }
]
