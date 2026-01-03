
from randomizer.helpers.eventtables import (
    ControllerDirections,
    RadialDirections,
    Rooms,
    Sounds,
    AreaObjects,
    NPCPackets,
    Locations,
    Shops,
    EventSequences,
    MenuTutorials,
    OverworldSequences,
    PlayableCharacters,
    EquipSlots,
    DialogDurations,
    IntroTitles,
    Colours,
    PaletteSetTypes,
    Music,
    MusicDirections,
    MusicPitch,
    Coords,
    CoordUnits,
    Tutorials,
    _0x40Flags,
    _0x60Flags,
    _0x62Flags,
    _0x63Flags,
    _0x68Flags,
    _0x6AFlags,
    _0x6BFlags,
    _0x81Flags,
    _0x84Flags)
from randomizer.helpers.objectsequencetables import (
    SequenceSpeeds,
    VramPriority,
    _0x08Flags,
    _0x0AFlags,
    _0x10Flags)
from randomizer.data import items

script = [
    {"identifier": "EVENT_357_current_lvl", "command": "set_7000_to_current_level"},
    {
        "identifier": "EVENT_357_room_224_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 224, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_225_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 225, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_226_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 226, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_227_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 227, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_228_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 228, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_229_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 229, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_230_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 230, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_231_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 231, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_232_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 232, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_233_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 233, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_234_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 234, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_235_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 235, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_236_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 236, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_242_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 242, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_256_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 256, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_35_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 35, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_36_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 36, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_37_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 37, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_38_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 38, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_39_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 39, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_40_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 40, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_41_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 41, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_42_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 42, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_43_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 43, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_48_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 48, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_192_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 192, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_193_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 193, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_194_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 194, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_195_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 195, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_196_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 196, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_197_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 197, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_198_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 198, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_199_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 199, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_200_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 200, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_201_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 201, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_258_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 258, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_259_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 259, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_24_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 24, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_25_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 25, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_26_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 26, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_27_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 27, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_28_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 28, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_160_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 160, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_161_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 161, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_162_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 162, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_163_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 163, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_164_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 164, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_165_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 165, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_166_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 166, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_167_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 167, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_168_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 168, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_169_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 169, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_170_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 170, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_171_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 171, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_172_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 172, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_173_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 173, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_175_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 175, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_176_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 176, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_177_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 177, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_178_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 178, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_179_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 179, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_180_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 180, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_181_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 181, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_182_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 182, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_183_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 183, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_184_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 184, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_185_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 185, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_186_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 186, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_187_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 187, "EVENT_357_play_star_music"]
    },
    {
        "identifier": "EVENT_357_room_188_jump",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 188, "EVENT_357_play_star_music"]
    },
    {"identifier": "EVENT_357_ret", "command": "ret"},
    {
        "identifier": "EVENT_357_play_star_music",
        "command": "play_music_current_volume",
        "args": [Music._08_INVINCIBLE_STAR],
    },
    {"identifier": "EVENT_357_ret_", "command": "ret"},
]
