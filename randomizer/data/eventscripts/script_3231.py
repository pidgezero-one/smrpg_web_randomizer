from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3231_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3231_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3231_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_set_palette_row_0',
                "command": 'set_palette_row',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x05]
            },
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x25, 0xc0, 0x03, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x40, 0x00, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_set_palette_row_8',
                "command": 'set_palette_row',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3231_action_queue_sync_2_SUBSCRIPT_ret_9',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3231_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 319],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3231_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
