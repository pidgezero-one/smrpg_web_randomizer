# E3588_SIGNAL_RING_ACTIVATOR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(SIGNAL_RING_DIRECTIONAL_BIT),
	ClearBit(SIGNAL_RING_BIT),
	StoreCharacterEquipmentTo7000(MARIO, Accessory),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 93, ["EVENT_3588_set_bit_8"]),
	StoreCharacterEquipmentTo7000(TOADSTOOL, Accessory),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 93, ["EVENT_3588_set_bit_8"]),
	StoreCharacterEquipmentTo7000(BOWSER, Accessory),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 93, ["EVENT_3588_set_bit_8"]),
	StoreCharacterEquipmentTo7000(MALLOW, Accessory),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 93, ["EVENT_3588_set_bit_8"]),
	StoreCharacterEquipmentTo7000(GENO, Accessory),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 93, ["EVENT_3588_set_bit_8"]),
	Return(),
	SetBit(SIGNAL_RING_BIT, identifier="EVENT_3588_set_bit_8"),
	Return()
])
