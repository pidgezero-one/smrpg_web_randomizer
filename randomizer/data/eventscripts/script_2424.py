from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2424_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 246, 'EVENT_2424_disable_trigger_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_disable_trigger_2',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_2424_unfreeze_all_npcs_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_disable_trigger_4',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_unfreeze_all_npcs_5',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2424_action_queue_async_6_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2424_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2424_pause_7',
        "command": 'pause',
        "args": [112],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_set_7000_to_current_level_10',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 246, 'EVENT_2424_enable_trigger_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_enable_trigger_12',
        "command": 'enable_trigger',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_enable_trigger_14',
        "command": 'enable_trigger',
        "args": [AreaObjects.NPC_13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2424_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
