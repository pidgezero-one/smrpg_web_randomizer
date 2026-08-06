"""Expanded dialogue/message text injection (open-mode base).

Repoints dialogue text control codes 0x18 and 0x19 in the Dialogue
Function Pointer table ($C0:6905-6952, dispatched by the message parser at
$C0:5F26) from the vanilla bank-$FA preset-string inserters to a custom
handler at $C0:60EF that pulls text from an expanded message/string table in
bank $E4. Supports randomizer-injected dynamic text. Render-disjoint engine
code relocated from open_mode.json (verified byte-identical via
diff_open_mode).

- $C0:6935: fn 0x18 ptr $6049 -> $60EF; fn 0x19 ptr LSB
  $51 -> $EF (bytes 49 60 51 -> ef 60 ef).
"""


def get_patch() -> dict[int, bytes]:
    return {
        0x06935: bytes([0xEF, 0x60, 0xEF]),
    }
