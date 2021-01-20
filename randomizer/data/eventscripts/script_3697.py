from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3697_pause_0',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3697_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3697_action_queue_async_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3697_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3697_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3697_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 809],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3697_pause_4',
        "command": 'pause',
        "args": [240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3697_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3697_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3697_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3697_action_queue_async_6_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3697_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 814],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3697_jmp_to_event_8',
        "command": 'jmp_to_event',
        "args": [3697],
        "subscript": []
    },
]
