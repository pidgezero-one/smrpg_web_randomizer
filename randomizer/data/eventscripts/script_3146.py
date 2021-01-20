from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3146_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3146_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3146_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3146_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3146_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3146_action_queue_sync_2_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3146_action_queue_sync_2_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3146_action_queue_sync_2_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3146_add_coins_3',
        "command": 'add_coins',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3146_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
