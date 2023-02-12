# ************************************** Default lists for the site.

# List of categories for the site.
from randomizer.types.world.flags.categories.categories import (
    AccessCategory,
    BossCategory,
    CosmeticCategory,
    ItemsCategory,
    PartyCategory,
)
from randomizer.types.world.flags.categories.presets import (
    ExplorerPreset,
    Spring2021AsyncTourneyPreset,
)


CATEGORIES = (
    PartyCategory,
    ItemsCategory,
    AccessCategory,
    BossCategory,
    CosmeticCategory,
)

# List of presets.
PRESETS = (ExplorerPreset, Spring2021AsyncTourneyPreset)
