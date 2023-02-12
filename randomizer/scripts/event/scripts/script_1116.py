# E1116_JUICE_BAR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(ITEM_ID, SopranoCard),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1116_open_shop_12"]),
	SetVarToConst(ITEM_ID, TenorCard),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1116_open_shop_15"]),
	SetVarToConst(ITEM_ID, AltoCard),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1116_open_shop_18"]),
	JmpToEvent(E1179_JUICE_BAR_NO_CARD),
	JmpToEvent(E1182_JUICE_BAR_SOPRANO_CARD, identifier="EVENT_1116_open_shop_12"),
	JmpToEvent(E1181_JUICE_BAR_TENOR_CARD, identifier="EVENT_1116_open_shop_15"),
	JmpToEvent(E1180_JUICE_BAR_ALTO_CARD, identifier="EVENT_1116_open_shop_18")
])
