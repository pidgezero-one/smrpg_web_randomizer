"""Dialog table for the randomizer."""

from randomizer.types.dialogs import (
    DialogCollection,
)
from randomizer.entities.dialogs.overworld_dialogs.data.dialog_pointers import (
    pointers as dialog_pointers,
)
from randomizer.entities.dialogs.overworld_dialogs.data.dialog_table_0x22 import (
    dialog_data as dialog_table_0x22,
)
from randomizer.entities.dialogs.overworld_dialogs.data.dialog_table_0x23 import (
    dialog_data as dialog_table_0x23,
)
from randomizer.entities.dialogs.overworld_dialogs.data.dialog_table_0x24 import (
    dialog_data as dialog_table_0x24,
)

dialog_table = DialogCollection(
    dialogs=dialog_pointers,
    raw_data=[dialog_table_0x22, dialog_table_0x23, dialog_table_0x24],
)
