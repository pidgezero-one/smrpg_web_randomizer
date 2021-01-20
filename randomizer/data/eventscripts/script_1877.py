from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1877_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1877_pause_action_script_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_1877_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70AA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_jmp_if_mario_in_air_5',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1877_pause_action_script_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_set_7000_to_object_coord_6',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_mem_compare_7',
        "command": 'mem_compare',
        "args": [0x7000, 384],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_jmp_if_comparison_result_is_lesser_8',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1877_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_resume_action_script_9',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70AA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1877_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_1877_pause_0'],
        "subscript": []
    },
]
