from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3623_jmp_if_present_in_current_level_0',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_9, 'EVENT_3625_play_sound_21']
    },
    {
        "identifier": 'EVENT_3623_jmp_to_subroutine_1',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3625_freeze_camera_137']
    },
    {
        "identifier": 'EVENT_3623_set_2',
        "command": 'set',
        "args": [0x70a7, 48]
    },
    {
        "identifier": 'EVENT_3623_add_3',
        "command": 'add',
        "args": [0x70c8, 0x01]
    },
    {
        "identifier": 'EVENT_3623_add_4',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_3623_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [32]
    },
    {
        "identifier": 'EVENT_3623_disable_trigger_in_level_6',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_9, Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    },
    {
        "identifier": 'EVENT_3623_remember_last_object_7',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3623_unfreeze_camera_8',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3623_ret_9',
        "command": 'ret'
    }
]
