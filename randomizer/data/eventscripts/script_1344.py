from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1344_apply_tile_mod_0',
        "command": 'apply_tile_mod',
        "args": [Rooms._194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1344_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1344_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 1, 'EVENT_1344_pause_action_script_6']
    },
    {
        "identifier": 'EVENT_1344_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x709a, 4, 'EVENT_1344_pause_action_script_6']
    },
    {
        "identifier": 'EVENT_1344_play_music_default_volume_4',
        "command": 'play_music_default_volume',
        "args": [Music._32_AND_MY_NAMES_BOOSTER]
    },
    {
        "identifier": 'EVENT_1344_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x709a, 4]
    },
    {
        "identifier": 'EVENT_1344_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1344_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1344_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1344_action_queue_async_8_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1344_action_queue_async_8_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1344_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1344_ret_10',
        "command": 'ret'
    }
]
