
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3594_jmp_to_subroutine_0',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3593_pause_16']
    },
    {
        "identifier": 'EVENT_3594_freeze_all_npcs_until_return_1',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_3594_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 3, 'EVENT_3594_jmp_to_subroutine_11']
    },
    {
        "identifier": 'EVENT_3594_set_3',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3594_run_dialog_4',
        "command": 'run_dialog',
        "args": [2497, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3594_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_3594_run_dialog_6',
        "command": 'run_dialog',
        "args": [2095, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3594_unfreeze_all_npcs_7',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_3594_inc_8',
        "command": 'inc',
        "args": [0x70af]
    },
    {
        "identifier": 'EVENT_3594_set_bit_9',
        "command": 'set_bit',
        "args": [0x704c, 3]
    },
    {
        "identifier": 'EVENT_3594_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3594_jmp_to_subroutine_11',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3593_pause_16']
    },
    {
        "identifier": 'EVENT_3594_freeze_all_npcs_until_return_12',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_3594_set_13',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3594_run_dialog_14',
        "command": 'run_dialog',
        "args": [2496, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3594_ret_15',
        "command": 'ret'
    }
]
