from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3626_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3626_jmp_if_object_trigger_disabled_1',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._344_NIMBUS_LAND_ITEM_SHOP, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3626_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3626_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3626_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3626_action_queue_async_3_SUBSCRIPT_walk_1_step_north_1',
                "command": 'walk_1_step_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3626_action_queue_async_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3626_action_queue_async_3_SUBSCRIPT_walk_1_step_north_3',
                "command": 'walk_1_step_north',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3626_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
