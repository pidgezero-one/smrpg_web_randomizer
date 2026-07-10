"""Bar ``no_sell`` items from being sold or thrown in the Waste Basket.

Item stat byte 0 bit 6 (``0x40``) is unused by vanilla: no code reads it and
``smrpgpatchbuilder`` never wrote it before ``_no_sell`` existed. This module
teaches three menu code paths to honour it.

Applied unconditionally. Which items carry the bit is decided per seed by
``logic.setup.item_protection`` from the ``ProtectSpecialItems`` flag (plus
Debug Candy, always). With no item flagged, all three hooks behave exactly as
vanilla did, so there is nothing to gate.

Everything here reuses machinery the engine already has:

* ``$C3:77E2`` turns an item id in ``$70`` into ``X = 0x014D + id*18``, the
  offset of that item's stat record inside bank ``$FA``.
* ``$9D`` is the item-name gray flag. ``$C3:7A3C`` folds it into the name's tile
  attribute (``LDA $9D : ASL : ASL : ORA #$20``), so 0 draws white and 1 draws
  the dark-blue "unusable" palette. The X menu sets it per row by calling the
  gray setter ``$C3:2D9E`` immediately before the name drawer ``$C3:7A07``.
* ``$C3:3F3C`` and ``$C3:2BEC`` are the engine's own rejection stubs
  (``JSR $1963`` -- error buzz -- then ``RTS``), already used for empty slots and
  for the Waste Basket item itself.

Three hooks:

A. Sell Items name list (``$C3:3FD9``, entered from ``$C3:3DFE`` on open and
   ``$C3:3F25`` on redraw after a sale) does ``STZ $9D`` once at ``$C3:3FF2``
   and then two bare ``JSR $7A07``, so nothing ever grays. Only the two ``JSR``
   *operands* change, to a helper that sets ``$9D`` then tail-calls ``$7A07``.

B. Sell Items A-button handler ``$C3:3EF0`` hardcodes ``CMP #$FF`` /
   ``CMP #$A0`` as its only refusals. Replaced with a gate that also refuses on
   the ``no_sell`` bit.

C. Waste Basket drop ``$C3:2BCD`` erases the carried item
   (``LDY $095F : LDA #$FF : STA $0000,Y``). Replaced with a gate that performs
   that erase only for sellable items, and otherwise falls to the buzz.

D. The "items maxed out" menu (``SC05_OPEN_ITEMS_MAXED_OUT_MENU``, init at
   ``$C3:509A``, input at ``$C3:512C``, A-press at ``$C3:51B4``). Its cursor sits
   either on the incoming "limbo" item (``$0931 == 0``, id in ``$59``) or on a bag
   slot (``$0931 != 0``). Both land in ``$70`` before ``$C3:51CC``, where vanilla
   refuses the Waste Basket and any ``price == 0`` item with message ``#$18``
   ("That's a Special Item") plus the buzz. We widen that same test to the
   ``no_sell`` bit, so one hook covers both:

   * tossing a protected item **out of the bag** to make room, and
   * tossing the protected item **you just picked up** (which is never written to
     any inventory, so no store-site hook could ever have caught it).

   Refusing here happens *before* the Yes/No confirm at ``$C3:51E2``, so the store
   at ``$C3:5233`` (``LDA $59 : STA $2940,X`` -- an overwrite, not an ``#$FF``
   erase, which is why store-site scans never found it) is unreachable with a
   protected item and needs no hook of its own.

Note ``$7E:2940`` is only a 30-byte scratch list shared by the item and equipment
menus, not the real bag; ``$C3:72E6``/``$72FD`` and ``$C3:7316``/``$732D`` copy it
to and from the canonical inventories in bank ``$7F``.

Note ``price == 0`` is NOT a sell gate -- ``$C3:3EE6`` will happily sell a
price-0 item for 0 coins. Key items are safe only because they live in a
separate inventory at ``$7FF8F0`` (see ``key_item_inventory``), not ``$2940``.

Free space: ``$C3:F000`` (ROM ``0x03F000``), 1024 bytes of ``$FF`` in vanilla,
unclaimed by ``open_mode.json`` (nothing in bank C3 above ``0x0362B8``) or
``static_data.bin`` (carries only ``>= 0x140000``).
"""

# Free-space helper entry points, as SNES bank-C3 addresses.
_SELL_GATE = 0xF000
_CHECK_NOSELL = 0xF020
_NOSELL_DRAW = 0xF040
_DISCARD_GATE = 0xF050
_MAXED_GATE = 0xF090

_NO_SELL_BIT = 0x40

# Vanilla routines we call into.
_ITEM_STAT_OFFSET = 0x77E2  # id in $70 -> X = 0x014D + id*18
_DRAW_ITEM_NAME = 0x7A07  # draw name for id in $70, honouring $9D
_ITEM_PRICE = 0x7A7F  # id in $70 -> 16-bit price in $72

# Vanilla rejection stubs (JSR $1963 : RTS).
_SELL_REFUSE = 0x3F3C
_DISCARD_REFUSE = 0x2BEC
# Where $C3:51CC jumps when the item IS tossable: the Yes/No confirm window.
_MAXED_CONFIRM = 0x51E2

# Hook sites (ROM offsets).
_SELL_HOOK = 0x033EF0  # $C3:3EF0, 10 bytes through $3EF9
_DISCARD_HOOK = 0x032BCD  # $C3:2BCD, 8 bytes through $2BD4
_MAXED_HOOK = 0x0351CC  # $C3:51CC, 11 bytes through $51D6
_DRAW_OPERAND_A = 0x034007  # operand of JSR $7A07 at $C3:4006
_DRAW_OPERAND_B = 0x03401B  # operand of JSR $7A07 at $C3:401A

# Branch displacements are hand-assembled; assert them rather than trust
# arithmetic done by eye. A wrong displacement lands mid-instruction and the
# failure is a lockup in a shop, far from here.
_SELL_BEQ_DISP = _SELL_REFUSE - 0x3EF5
_DISCARD_BEQ_DISP = _DISCARD_REFUSE - 0x2BD2
# This gate branches on the *allowed* path (BNE -> confirm); refusal falls
# through into the vanilla message-#$18 stub at $C3:51D7.
_MAXED_BNE_DISP = _MAXED_CONFIRM - 0x51D1
assert _SELL_BEQ_DISP == 0x47, hex(_SELL_BEQ_DISP)
assert _DISCARD_BEQ_DISP == 0x1A, hex(_DISCARD_BEQ_DISP)
assert _MAXED_BNE_DISP == 0x11, hex(_MAXED_BNE_DISP)


def _lo(addr: int) -> int:
    return addr & 0xFF


def _hi(addr: int) -> int:
    return (addr >> 8) & 0xFF


def _free_space() -> bytes:
    """Assemble the four helpers as one contiguous $C3:F000 block.

    Laid out at fixed offsets so the ``JSR`` targets above stay stable; the gaps
    between routines are padded with $FF.
    """
    blocks: dict[int, list[int]] = {}

    # ---- $F000 sell_gate ------------------------------------------------
    # out: Z=1 -> caller refuses the sale, Z=0 -> proceed.
    # Subsumes the vanilla CMP #$FF / CMP #$A0 pair it replaces.
    blocks[_SELL_GATE] = [
        0xAD, 0x46, 0x09,           # $F000  LDA $0946      ; highlighted item id
        0xC9, 0xFF,                 # $F003  CMP #$FF       ; empty slot
        0xF0, 0x0E,                 # $F005  BEQ $F015
        0xC9, 0xA0,                 # $F007  CMP #$A0       ; Waste Basket
        0xF0, 0x0A,                 # $F009  BEQ $F015
        0x85, 0x70,                 # $F00B  STA $70
        0x20, _lo(_CHECK_NOSELL), _hi(_CHECK_NOSELL),  # $F00D JSR check_nosell
        0xD0, 0x03,                 # $F010  BNE $F015      ; bit set -> refuse
        0xA9, 0x01,                 # $F012  LDA #$01       ; Z=0 -> proceed
        0x60,                       # $F014  RTS
        0xA9, 0x00,                 # $F015  LDA #$00       ; Z=1 -> refuse
        0x60,                       # $F017  RTS
    ]

    # ---- $F020 check_nosell ---------------------------------------------
    # in:  $70 = item id
    # out: A = $00 (sellable) or $40 (no_sell), Z set to match. X, Y preserved.
    blocks[_CHECK_NOSELL] = [
        0xDA,                       # $F020  PHX
        0xA5, 0x70,                 # $F021  LDA $70
        0xC9, 0xFF,                 # $F023  CMP #$FF       ; empty slot
        0xF0, 0x0D,                 # $F025  BEQ $F034
        0x20, _lo(_ITEM_STAT_OFFSET), _hi(_ITEM_STAT_OFFSET),  # $F027 JSR $77E2
        0xBF, 0x00, 0x00, 0xFA,     # $F02A  LDA $FA0000,X  ; stat byte 0
        0x29, _NO_SELL_BIT,         # $F02E  AND #$40
        0xFA,                       # $F030  PLX            ; PLX clobbers Z...
        0x09, 0x00,                 # $F031  ORA #$00       ; ...restore it from A
        0x60,                       # $F033  RTS
        0xFA,                       # $F034  PLX
        0xA9, 0x00,                 # $F035  LDA #$00       ; Z=1 -> sellable
        0x60,                       # $F037  RTS
    ]

    # ---- $F040 nosell_draw ----------------------------------------------
    # Drop-in for ``JSR $7A07`` in the sell list: sets $9D from the bit, then
    # tail-calls the name drawer so its RTS returns to the list loop.
    blocks[_NOSELL_DRAW] = [
        0x20, _lo(_CHECK_NOSELL), _hi(_CHECK_NOSELL),  # $F040 JSR check_nosell
        0xF0, 0x06,                 # $F043  BEQ $F04B
        0xA9, 0x01,                 # $F045  LDA #$01
        0x85, 0x9D,                 # $F047  STA $9D        ; dark blue
        0x80, 0x02,                 # $F049  BRA $F04D
        0x64, 0x9D,                 # $F04B  STZ $9D        ; normal
        0x4C, _lo(_DRAW_ITEM_NAME), _hi(_DRAW_ITEM_NAME),  # $F04D JMP $7A07
    ]

    # ---- $F050 discard_gate ----------------------------------------------
    # out: Z=1 -> caller buzzes; Z=0 -> the carried item was erased.
    # Clobbers $70, which is safe: neither $C3:2630 nor $C3:72FD reads it, and
    # $C3:2BE4 reloads it before the next use.
    blocks[_DISCARD_GATE] = [
        0xAD, 0x46, 0x09,           # $F050  LDA $0946      ; carried item id
        0x85, 0x70,                 # $F053  STA $70
        0x20, _lo(_CHECK_NOSELL), _hi(_CHECK_NOSELL),  # $F055 JSR check_nosell
        0xD0, 0x0B,                 # $F058  BNE $F065      ; bit set -> refuse
        0xAC, 0x5F, 0x09,           # $F05A  LDY $095F      ; carried item's slot
        0xA9, 0xFF,                 # $F05D  LDA #$FF
        0x99, 0x00, 0x00,           # $F05F  STA $0000,Y    ; the discard
        0xA9, 0x01,                 # $F062  LDA #$01       ; Z=0 -> proceed
        0x60,                       # $F064  RTS
        0xA9, 0x00,                 # $F065  LDA #$00       ; Z=1 -> refuse
        0x60,                       # $F067  RTS
    ]

    # ---- $F090 maxed_gate -------------------------------------------------
    # Replaces the vanilla "Waste Basket or price==0" test at $C3:51CC. $70 is
    # already the item under the cursor -- the incoming limbo item when
    # $0931 == 0, otherwise the bag slot -- so this covers both.
    # out: Z=0 -> caller BNEs to the confirm window; Z=1 -> falls through into
    #      the vanilla message-#$18 ("That's a Special Item") + buzz stub.
    # $70 must survive: $C3:51E7 draws the item's name from it.
    blocks[_MAXED_GATE] = [
        0xA5, 0x70,                 # $F090  LDA $70
        0xC9, 0xA0,                 # $F092  CMP #$A0       ; Waste Basket
        0xF0, 0x0F,                 # $F094  BEQ $F0A5
        0x20, _lo(_ITEM_PRICE), _hi(_ITEM_PRICE),  # $F096  JSR $7A7F  ; price -> $72
        0xA6, 0x72,                 # $F099  LDX $72
        0xF0, 0x08,                 # $F09B  BEQ $F0A5      ; price 0 -> key item
        0x20, _lo(_CHECK_NOSELL), _hi(_CHECK_NOSELL),  # $F09D JSR check_nosell
        0xD0, 0x03,                 # $F0A0  BNE $F0A5      ; no_sell -> refuse
        0xA9, 0x01,                 # $F0A2  LDA #$01       ; Z=0 -> confirm
        0x60,                       # $F0A4  RTS
        0xA9, 0x00,                 # $F0A5  LDA #$00       ; Z=1 -> refuse
        0x60,                       # $F0A7  RTS
    ]

    start = min(blocks)
    end = max(addr + len(code) for addr, code in blocks.items())
    out = bytearray([0xFF] * (end - start))
    for addr, code in blocks.items():
        out[addr - start : addr - start + len(code)] = bytes(code)
    return bytes(out)


def get_patch() -> dict[int, bytes]:
    """Return the byte writes that make ``no_sell`` items unsellable."""
    return {
        # Free-space helpers at $C3:F000.
        0x03F000: _free_space(),

        # Hook A: gray the two Sell Items name columns. Operand-only rewrite of
        # ``JSR $7A07`` -> ``JSR nosell_draw`` at $C3:4006 and $C3:401A.
        _DRAW_OPERAND_A: bytes([_lo(_NOSELL_DRAW), _hi(_NOSELL_DRAW)]),
        _DRAW_OPERAND_B: bytes([_lo(_NOSELL_DRAW), _hi(_NOSELL_DRAW)]),

        # Hook B: refuse the sale. Replaces CMP #$FF / BEQ / CMP #$A0 / BEQ /
        # REP #$20 ($C3:3EF0-$3EF9); the REP moves up and the tail is padded so
        # $C3:3EFA (LDA $7FF8AF) keeps its address.
        _SELL_HOOK: bytes([
            0x20, _lo(_SELL_GATE), _hi(_SELL_GATE),  # JSR sell_gate
            0xF0, _SELL_BEQ_DISP,                    # BEQ $3F3C (buzz)
            0xC2, 0x20,                              # REP #$20
            0xEA, 0xEA, 0xEA,                        # NOP x3
        ]),

        # Hook C: refuse the Waste Basket discard. Replaces LDY $095F /
        # LDA #$FF / STA $0000,Y ($C3:2BCD-$2BD4); the gate does that erase
        # itself on the allowed path. The CMP #$A0 at $C3:2BC9 that identifies
        # the drop target stays put.
        _DISCARD_HOOK: bytes([
            0x20, _lo(_DISCARD_GATE), _hi(_DISCARD_GATE),  # JSR discard_gate
            0xF0, _DISCARD_BEQ_DISP,                       # BEQ $2BEC (buzz)
            0xEA, 0xEA, 0xEA,                              # NOP x3
        ]),

        # Hook D: refuse the maxed-out-inventory toss, for BOTH the bag item and
        # the incoming limbo item. Replaces CMP #$A0 / BEQ / JSR $7A7F / LDX $72 /
        # BNE ($C3:51CC-$51D6); the gate subsumes all of it. Refusal falls through
        # to $C3:51D7 (message #$18 + buzz), which keeps its address.
        _MAXED_HOOK: bytes([
            0x20, _lo(_MAXED_GATE), _hi(_MAXED_GATE),  # JSR maxed_gate
            0xD0, _MAXED_BNE_DISP,                     # BNE $51E2 (confirm)
            0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA,        # NOP x6 -> $51D7
        ]),
    }
