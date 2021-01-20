from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3748_set_0',
        "command": 'set',
        "args": [0x70a7, 82],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3748_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [33],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3748_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3748_pause_3',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3748_jmp_if_mario_in_air_4',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3748_pause_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3748_set_bit_5',
        "command": 'set_bit',
        "args": [0x704b, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3748_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 510],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3748_run_dialog_7',
        "command": 'run_dialog',
        "args": [522, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3748_put_inventory_8',
        "command": 'put_inventory',
        "args": [0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3748_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
