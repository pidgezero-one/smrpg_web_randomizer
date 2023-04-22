"""A0337_VARIOUS_SHIP_OBJECTS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 172, ["ACTION_337_set_palette_row_20"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 177, ["ACTION_337_set_palette_row_20"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 163, ["ACTION_337_set_palette_row_24"]),
        IncPaletteRowBy(1),
        Db(bytearray(b"\xfd\x9c\x05"), identifier="ACTION_337_db_6"),
        Db(bytearray(b" \x04")),
        Db(bytearray(b"%\xc0\x03\x80\xff")),
        Pause(8),
        Db(bytearray(b"%@\x00\x80\xff")),
        Pause(8),
        BPL262728(),
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 172, ["ACTION_337_set_palette_row_22"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 177, ["ACTION_337_set_palette_row_22"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 163, ["ACTION_337_set_palette_row_26"]),
        IncPaletteRowBy(15),
        ObjectMemoryClearBit(
            arg_1=0x30, bits=[4], identifier="ACTION_337_object_memory_clear_bit_18"
        ),
        Return(),
        SetPaletteRow(2, identifier="ACTION_337_set_palette_row_20"),
        Jmp(["ACTION_337_db_6"]),
        SetPaletteRow(1, identifier="ACTION_337_set_palette_row_22"),
        Jmp(["ACTION_337_object_memory_clear_bit_18"]),
        SetPaletteRow(3, identifier="ACTION_337_set_palette_row_24"),
        Jmp(["ACTION_337_db_6"]),
        SetPaletteRow(2, identifier="ACTION_337_set_palette_row_26"),
        Jmp(["ACTION_337_object_memory_clear_bit_18"]),
    ]
)
