; Author: cleartonic
hirom
!enemy_1_status = $7EFC00
!enemy_2_status = $7EFC80
!enemy_3_status = $7EFD00
!enemy_1_id = $7EFC01
!enemy_2_id = $7EFC81
!enemy_3_id = $7EFD01
!ally_1_accessory = $7EFA9E
!ally_1_free_ram = $7EFA9F
!ally_2_accessory = $7EFB1E
!ally_2_free_ram = $7EFB1F
!ally_3_accessory = $7EFB9E
!ally_3_free_ram = $7EFB9F


!BELOME_ID = #$C9
!BOWSER_CLONE_ID = #$7D
!BELOME_ARROW_POS = #$64
!ENDURING_BROOCH_ID = #$49




!freerom = $CFF7B0   ;start of expanded rom


!subroutine_apply_damage = $C2C55E
!subroutine_zero_brooch = $C2972E
!subroutine_brooch_perfect_block = $C2CA73
!subroutine_brooch_timed_block = $C2C9FE

org !subroutine_apply_damage
jsl apply_damage

org !subroutine_zero_brooch
jsl zero_out_brooch_addresses
nop
nop

org !subroutine_brooch_perfect_block
jsl brooch_perfect_block
rts

org !subroutine_brooch_timed_block
jsl brooch_timed_block
nop



org !freerom
apply_damage:

; =================================
; BELOME 3
; =================================

; check enemy ID in slot 1
lda !enemy_1_id ; load main enemy ID
cmp !BELOME_ID ; compare belome ID 
bne .return_to_apply_damage ; if not belome's ID, resume normal code

; check targeting, this is the offset used to apply the final damage calc
; by using this, you can proxy who the target is, which should always be enemy 1 in the belome fight
lda $ca 
cmp #$00 ; #$7EFC00 = enemy 1
bne .return_to_apply_damage
lda $cb
cmp #$FC

bne .return_to_apply_damage


; then check if bowser clone is present, enemy ID #
.check_clones:
lda !enemy_2_id
cmp !BOWSER_CLONE_ID
beq .check_valid_enemy2
lda !enemy_3_id
cmp !BOWSER_CLONE_ID
beq .check_valid_enemy3
bra .return_to_apply_damage ; if no match on bowser clone, resume normal code

; this checks that the enemy is in a valid state, which is $#00 in the byte to the left of the enemy's ID
; if you were asm genius you would code this better but idgaf, max cycle count lfg
.check_valid_enemy2:
lda !enemy_2_status
cmp #$00
beq .skill_check ; if bowser clone detected, then skill check 
bra .return_to_apply_damage ; otherwise resume normal code

.check_valid_enemy3:
lda !enemy_3_status
cmp #$00
beq .skill_check ; if bowser clone detected, then skill check 
bra .return_to_apply_damage ; otherwise resume normal code
 

; check if skill being used is among the following:
; 0B psych bomb
; 0C terrorize
; 0D poison gas
; 0E crusher
; 0F bowser crush
; 10 geno beam
; 12 geno whirl
; 13 geno blast
; 14 geno flash
; 1A star rain

.skill_check:
lda $CD ; last skill used ID
cmp #$0B
beq .nullify ; branch to nullify if compare condition met
cmp #$0C
beq .nullify
cmp #$0D
beq .nullify
cmp #$0E
beq .nullify
cmp #$0F
beq .nullify
cmp #$10
beq .nullify
cmp #$12
beq .nullify
cmp #$13
beq .nullify
cmp #$14
beq .nullify
cmp #$1A
beq .nullify

bra .return_to_apply_damage ; if no match, resume normal 

; nullify damage 
.nullify
lda #$00
sta $c2
sta $c3
bra .finish ; if this check passed, this is obvioulsy not the enduring brooch situation, so exit function




.return_to_apply_damage
; =================================
; ENDURING BROOCH
; =================================

; check if party is getting targeted
rep #$20
lda $CA
CMP #$FA80
beq .slot_accessory_check
CMP #$FB00
beq .slot_accessory_check
CMP #$FB80
beq .slot_accessory_check
bra .finish

.slot_accessory_check:
tax ; store the offset in x
sep #$20
lda $7E001E, x ; this will load the slot's accessory
cmp !ENDURING_BROOCH_ID
bne .finish

; check if enduring brooch has been activated yet 
lda $7E001F, x ; this will load the unused RAM for this slot, which we're repurposing for this
bmi .finish ; if >=0x80, then finish function, since the brooch has already been activated

; check if damage would defeat slot
rep #$20
clc
lda $7E0011, x
sbc $c2
bmi .activate_brooch ; if calc is negative, then branch
bra .finish

.activate_brooch:
sep #$20
lda #$80
sta $7E001F, x
rep #$20
lda $c2
sta $7F0010 ; temp damage for turn
lda #$0001
sta $7F0020 ; temp flag for brooch activating this turn
lda $7E0011, x
sta $7F0000 ; temp current character hp 
sec
sbc #$0001
sta $c2

; original code
.finish
rep #$20
ldx $ca
rtl


zero_out_brooch_addresses:
sep #$20
lda #$00
sta !ally_1_free_ram
sta !ally_2_free_ram
sta !ally_3_free_ram 
rep #$20
lda $ba
and #$00FF
tay
rtl







brooch_perfect_block:
; first check brooch conditions
rep #$20
lda $CA
CMP #$FA80
beq .slot_accessory_check_perfect
CMP #$FB00
beq .slot_accessory_check_perfect
CMP #$FB80
beq .slot_accessory_check_perfect
bra .finish_perfect

.slot_accessory_check_perfect:
sep #$20
lda $7F0020 ; check if activated THIS turn
beq .finish_perfect
;if not, undo
lda #$00
sta $7E001F, x
; then continue

.finish_perfect:
rep #$20
lda $7E0041, X
bit #$0080
bne brooch_bit_test
lda $7E0011, X 
clc
adc $c2
sta $7E0011, X 
lda #$0000
sta $7E0045, X
rtl

brooch_bit_test: ; tbh i have no idea what this does but i'm preserving the original code's branch here
lda $7e0035,x
sta $7e0011,x
lda #$0000   
sta $7e0045,x
lda $7e0000,x
and #$ff3f   
sta $7e0000,x
lda $7e0030,x
sta $7e0040,x
lda $7e0033,x
sta $7e0043,x
lda #$0002   
trb $0700    
lda #$8000   
trb $0708    
rtl



brooch_timed_block:
; first check brooch conditions
rep #$20
lda $CA
CMP #$FA80
beq .slot_accessory_check_timed
CMP #$FB00
beq .slot_accessory_check_timed
CMP #$FB80
beq .slot_accessory_check_timed
bra .apply_half_damage_normal_case

.slot_accessory_check_timed:
sep #$20
lda $7F0020 ; check if activated THIS turn
beq .apply_half_damage_normal_case

; recalc if new timed defense would have NOT triggered ohko
rep #$20
lda $7F0010
lsr
sta $7F0030
lda $7F0000
sec
sbc $7F0030
bmi .finish_timed ; if negative value, do nothing and finish, brooch activated, no damage adjustments

; if positive, undo activation, recalc hp
sep #$20
lda #$00
sta $7E001F, x
rep #$20
lda $7F0010 
sta $c2 ; reset original damage dealt
sta $7E0045, x ; reset damage display number
lda $7F0000
sec
sbc $c2
sta $7E0011, x

.apply_half_damage_normal_case
rep #$20
lda $c2
lsr 
sta $c2

; reset all temp variables
lda #$0000
sta $7F0000
sta $7F0010
sta $7F0020
sta $7F0030

.finish_timed
rtl