from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2126_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_sequence_looping_on_6',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [19]
            },
            {
                "identifier": 'EVENT_2126_action_queue_async_0_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2126_ret_1',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
