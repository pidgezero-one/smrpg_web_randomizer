from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2387_run_dialog_0',
        "command": 'run_dialog',
        "args": [3074, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_jmp_if_dialog_option_b_1',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2387_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._254_BEAN_VALLEY_SMILAX_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 385],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_run_dialog_5',
        "command": 'run_dialog',
        "args": [3152, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_put_inventory_7',
        "command": 'put_inventory',
        "args": [items.Seed],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_pause_8',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_jmp_if_objects_action_script_running_9',
        "command": 'jmp_if_objects_action_script_running',
        "args": [AreaObjects.MARIO, 'EVENT_2387_pause_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2387_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
