from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_748_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, RadialDirections.NORTHEAST, 8, 18, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_748_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_748_action_queue_async_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_748_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_748_run_dialog_3',
        "command": 'run_dialog',
        "args": [2554, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_748_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._486_ENDING_CREDITS_STAR_PIECES_ROSE_TOWN_LAST_STAR_PIECE_TO_THANK_YOU, RadialDirections.NORTHEAST, 8, 18, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_748_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_748_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_748_fade_in_from_black_sync_duration_6',
        "command": 'fade_in_from_black_sync_duration',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_748_db_7',
        "command": 'db',
        "args": [0xfd, 0x8f, 0x00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_748_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
