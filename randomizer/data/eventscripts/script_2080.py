from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2080_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2080_action_queue_sync_0_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2080_action_queue_sync_0_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2080_action_queue_sync_0_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2080_action_queue_sync_0_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_2080_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
        ]
    },
    {
        "identifier": 'EVENT_2080_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2080_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
