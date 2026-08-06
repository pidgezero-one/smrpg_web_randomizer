"""Switch-menu cursor-navigation rework (open-mode base).

Reworks the switch-window cursor handler ($C3:623F+) so it reads the
alternate controller-input word ($15 instead of $14) and bounds the
cursor against the actual party size.

The window draws the five party slots in two columns: slots 0/1/2 down the
left, slots 3/4 down the right, the right column starting one box lower.
$C3:6393 resolves the highlighted slot as 2*col + row + 1 (col =
$0929, row = $092A), and $C3:63FE places the cursor at
y = row*0x30 + 0x48.

row is *signed*.  row = $FF is the top-left box: the resolver's +1
cancels the -1 to give slot 0, and the cursor Y wraps to 0x3018 whose
low byte 0x18 is exactly that box.  That is what lets the leader be
switched out, and it must survive any change here.  So the reachable cells are
row in $FF..1 at col 0 and row in 0..1 at col 1.

$60 holds party_count - 1, the highest occupied slot, and each
direction checks the slot it is about to land on:

* up - stop at row == col - 1 (top of either column)
* down - stop at row == 1, else need 2*col + row + 2 <= $60
* left - stop at col == 0
* right - stop at col != 0 or row == $FF (leader box has no right
  neighbour), else need row + 3 <= $60

Vanilla assumed at least four characters, since the switch menu was unreachable
below that, and bounded the cursor with party_count - 4.  The randomizer
unlocks the menu at two characters, where that subtraction underflows to
$FE/$FF and every unsigned bound check passes, opening the whole grid
onto slots that hold nobody.  Checking the destination slot against the highest
occupied one degrades cleanly at any party size.

The handlers also absorb vanilla's final clamp at $C3:62AE; down now
falls through to the redraw stub at $C3:62B8.

Render-disjoint engine code relocated from open_mode.json.
"""


def get_patch() -> dict[int, bytes]:
    return {
        # SBC #$01 -> $60 = party_count - 1 = highest occupied slot.
        0x3623B: bytes([0xE9, 0x01]),
        0x3623F: bytes([
            0xEA, 0xEA, 0xA5, 0x15, 0x89, 0x08, 0xD0, 0x28, 0x89, 0x04, 0xD0,
            0x54, 0x89, 0x02, 0xD0, 0x2E, 0x89, 0x01, 0xD0, 0x34, 0xC2, 0x20,
            0xA5, 0x14,
        ]),
        0x3626F: bytes([
            # $C3:626F  UP: stop at row == col - 1.
            0xAD, 0x2A, 0x09,        # LDA  $092A
            0x1A,                    # INC
            0xCD, 0x29, 0x09,        # CMP  $0929
            0xF0, 0x4F,              # BEQ  $62C7 (cancel)
            0xCE, 0x2A, 0x09,        # DEC  $092A
            0x80, 0x3B,              # BRA  $62B8 (redraw)
            # $C3:627D  LEFT: stop at column 0.
            0xAD, 0x29, 0x09,        # LDA  $0929
            0xF0, 0x45,              # BEQ  $62C7
            0xCE, 0x29, 0x09,        # DEC  $0929
            0x80, 0x31,              # BRA  $62B8
            # $C3:6287  RIGHT: need col 0, a non-leader row, and slot row+3.
            0xAD, 0x29, 0x09,        # LDA  $0929
            0xD0, 0x3B,              # BNE  $62C7
            0xAD, 0x2A, 0x09,        # LDA  $092A
            0x30, 0x36,              # BMI  $62C7   (row $FF: leader box)
            0x18,                    # CLC
            0x69, 0x03,              # ADC  #$03
            0xC5, 0x60,              # CMP  $60
            0xF0, 0x02,              # BEQ  +2
            0xB0, 0x2D,              # BCS  $62C7
            0xEE, 0x29, 0x09,        # INC  $0929
            0x80, 0x19,              # BRA  $62B8
            # $C3:629F  DOWN: stop at row 1, else need slot 2*col+row+2.
            0xAD, 0x2A, 0x09,        # LDA  $092A
            0xC9, 0x01,              # CMP  #$01
            0xF0, 0x21,              # BEQ  $62C7
            0xAD, 0x29, 0x09,        # LDA  $0929
            0x0A,                    # ASL
            0x6D, 0x2A, 0x09,        # ADC  $092A
            0x1A,                    # INC
            0x1A,                    # INC
            0xC5, 0x60,              # CMP  $60
            0xF0, 0x02,              # BEQ  +2
            0xB0, 0x12,              # BCS  $62C7
            0xEE, 0x2A, 0x09,        # INC  $092A
        ]),                          # falls through to $C3:62B8
    }
