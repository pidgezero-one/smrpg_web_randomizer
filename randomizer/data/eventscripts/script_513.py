from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_513_pause_0',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_513_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._099_ROSE_TOWN_GENO_AWAKENS_IN_INN_1F, RadialDirections.SOUTH, 4, 17, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_513_stop_music_2',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_513_summon_to_current_level_3',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_513_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_513_action_queue_sync_4_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_513_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_513_action_queue_sync_5_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_513_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_513_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [8, 18, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_513_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_513_action_queue_sync_6_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_513_action_queue_sync_6_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [8, 9, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_513_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_513_action_queue_sync_6_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_513_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_513_action_queue_async_7_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_513_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_513_action_queue_async_8_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_513_action_queue_async_8_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 17, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_513_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [3776],
        "subscript": []
    },
]
