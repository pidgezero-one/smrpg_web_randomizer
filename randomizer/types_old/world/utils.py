"""Helper functions for settings."""

from typing import Any
from re import compile as regex_compile


from .constants import B64_TABLE
from .exceptions import RandomizerSettingsException
from .flags import FlagOptions
from .flags.categories import FlagCategoryT
from .flags.categories.types import FlagCategory
from .flags.types import (
    BooleanFlag,
    CategorizationFlag,
    Flag,
    NumberThresholdFlag,
    SelectOneFlag)


def get_flag_string_from_flag_collection(categories: list[type[FlagCategoryT]]) -> str:
    """Converts a series of settings into a copy-pastable string."""
    flag_strings: list[str] = []
    for category in categories:
        for subcategory in category().subcategories:
            flagstring_parts = []
            for flag in subcategory.flags:
                if isinstance(flag, BooleanFlag):
                    if flag.value:
                        flagstring_parts.append(flag.id)
                elif isinstance(flag, SelectOneFlag):
                    flagstring_parts.append(f"{flag.id}:{flag.value.name}")
                elif isinstance(flag, NumberThresholdFlag):
                    flagstring_parts.append(f"{flag.id}:{flag.value}")
                elif isinstance(flag, CategorizationFlag):
                    ctr = 0
                    choice_rep = 0
                    choice_rep_string = ""
                    for f in flag.options:
                        if f in flag.enabled:
                            choice_rep += 1 << ctr
                        ctr += 1
                        if ctr == 6:
                            choice_rep_string += B64_TABLE[choice_rep]
                            ctr = 0
                            choice_rep = 0
                    if ctr > 0:
                        choice_rep_string += B64_TABLE[choice_rep]
                    flagstring_parts.append("{flag.id}:{choice_rep_string}")
            if len(flagstring_parts) != 0:
                flag_strings.append(f"{subcategory.id}.{flagstring_parts}")

    flag_string = "     ".join(flag_strings)

    return flag_string.strip()


def separate_flag_string(
    flag_string: str, cosmetics_string: str
) -> dict[str, dict[str, Any]]:
    """Break up a flag string into individual settings"""
    flag_dict: dict[str, dict[str, Any]] = {}
    flag_words_raw: list[str] = regex_compile(r"\s+").split(
        flag_string
    ) + regex_compile(r"\s+").split(cosmetics_string)
    flag_words: list[str] = [f for f in flag_words_raw if f.strip() != ""]

    # index the supplied flag values to be referenced by category loop
    for word in flag_words:
        subcat = word[0]
        flag_dict[subcat] = {}
        params = word[1:]
        flags_with_settings = params.split("|")
        for setting in flags_with_settings:
            setting_data = setting.split(":")
            if len(setting_data) == 1:
                flag_dict[subcat][setting_data[0]] = True
            else:
                flag_dict[subcat][setting_data[0]] = setting_data[1]
    return flag_dict


# set the flag classes and values according to parsed strings
def set_flag_from_settings_string(
    flag_dict: dict[str, dict[str, Any]], flag: Flag, parent_subcategory: FlagCategory
) -> None:
    """Apply a setting based on settings string"""
    if (
        parent_subcategory.id in flag_dict
        and flag.id in flag_dict[parent_subcategory.id]
    ):
        if isinstance(flag, CategorizationFlag):
            option_booleans = []
            b64_string = flag_dict[parent_subcategory.id][flag.id]
            for char in b64_string:
                b64val = B64_TABLE.index(char)
                for boss_location in range(0, 6):
                    option_booleans.append((b64val & (1 << boss_location)) != 0)
            checked_tuples = zip(option_booleans, flag.options)
            enabled = [v[1] for v in checked_tuples if v[0]]
            flag.set_enabled(enabled)
        elif isinstance(flag, NumberThresholdFlag):
            value_from_dict = int(flag_dict[parent_subcategory.id][flag.id])
            flag.set_value(value_from_dict)
        elif isinstance(flag, SelectOneFlag):
            val: FlagOptions | None = next(
                (
                    x
                    for x in flag.choices
                    if x.name == flag_dict[parent_subcategory.id][flag.id]
                ),
                None)
            if val is None:
                prop = flag_dict[parent_subcategory.id][flag.id]
                raise RandomizerSettingsException(
                    f"invalid property for {parent_subcategory.id}.{flag.id} flag: {prop}"
                )
            flag.set_value(val)
        elif isinstance(flag, BooleanFlag):
            flag.set_value(flag_dict[parent_subcategory.id][flag.id])
        else:
            raise RandomizerSettingsException("unknown flag type")
    else:
        if isinstance(flag, CategorizationFlag):
            # safety
            flag.set_enabled(flag.enabled)
        elif isinstance(flag, NumberThresholdFlag):
            flag.set_value(flag.default)
        elif isinstance(flag, SelectOneFlag):
            flag.set_value(flag.default)
        elif isinstance(flag, BooleanFlag):
            flag.set_value(flag.default)
        else:
            raise RandomizerSettingsException("unknown flag type")
