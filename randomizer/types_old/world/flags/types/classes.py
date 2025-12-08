"""Settings classes for the randomizer."""

from typing import Any, TypeVar
from markdown import markdown
import bleach
from django.utils.safestring import mark_safe, SafeString

from randomizer.types.world.flags.enums import FlagOptions, FlagTypes


# ************************************** Flag classes


class FlagError(ValueError):
    """Error to throw when flags have a problem"""


class Flag:
    """Class representing a flag with its description, and possible values/choices/options."""

    _name: str = ""
    _description: str = ""
    _inverse_description: str = ""
    _hard: bool = False
    _id: str = ""
    _type: FlagTypes

    @property
    def name(self) -> str:
        """Setting name as it will appear on the side"""
        return self._name

    @property
    def description(self) -> str:
        """An explanation of what the setting does"""
        return self._description

    @property
    def inverse_description(self) -> str:
        """(deprecated)"""
        return self._inverse_description

    @property
    def hard(self) -> bool:
        """(deprecated?)"""
        return self._hard

    @property
    def id(self) -> str:
        """An internal identifier to refer to this setting with"""
        return self._id

    @property
    def type(self) -> FlagTypes:
        """Defines the input type of this setting"""
        return self._type

    @classmethod
    def description_as_markdown(cls) -> SafeString:
        """Return description as markdown"""
        return mark_safe(markdown(bleach.clean(cls().description)))

    @classmethod
    def description_or_name_as_markdown(cls) -> SafeString:
        """Return description or name as markdown"""
        if cls().description:
            return mark_safe(markdown(bleach.clean(cls().description)))
        return mark_safe(markdown(bleach.clean(cls().name)))

    @classmethod
    def inverse_description_as_markdown(cls) -> SafeString:
        """(deprecated)"""
        return mark_safe(markdown(bleach.clean(cls().inverse_description)))

    @classmethod
    def inverse_description_or_name_as_markdown(cls) -> SafeString:
        """(deprecated)"""
        if cls().inverse_description:
            return mark_safe(markdown(bleach.clean(cls().inverse_description)))
        return mark_safe(markdown(bleach.clean(f"({cls().name})")))


class CategorizationFlag(Flag):
    """A setting containing values that have to be sorted into one of two
    categories, enabled or disabled.\n
    Example: choosing which locations can and cannot cntain progression."""

    _type: FlagTypes = FlagTypes.CATEGORIZATION
    _options: list[FlagOptions] = []
    _enabled: list[FlagOptions] = []
    _optionEnum: type[FlagOptions]

    @property
    def options(self) -> list[FlagOptions]:
        """The values to be sorted."""
        return self._options

    @property
    def enabled(self) -> list[FlagOptions]:
        """The values that the user wants to enable."""
        return self._enabled

    def set_enabled(self, options: list[FlagOptions]) -> None:
        """Overwrite the values that the user wants to enable."""
        for opt in options:
            assert opt in self.options
        self._enabled = list(set(options))

    @property
    def disabled(self) -> list[FlagOptions]:
        """The values that the user wants to disable, which is necessarily
        the inverse of `enabled`."""
        return [o for o in self.options if o not in self.enabled]

    @property
    def option_enum(self) -> type[FlagOptions]:
        """The enum from which this setting's options come."""
        return self._optionEnum

    @property
    def options_dict(self) -> list[dict[str, Any]]:
        """All options as a dict."""
        return [{"id": c.name, "text": c.value} for c in self.options]

    @property
    def default_dict(self) -> list[dict[str, Any]]:
        """Enabled options as a dict."""
        return [{"id": c.name, "text": c.value} for c in self.enabled]
        # this really should be coming from its enum


class SelectOneFlag(Flag):
    """A setting with multiple options where only one may be chosen.\n
    Example: choosing which condition needs to be met to unlock an area."""

    _type: FlagTypes = FlagTypes.SELECT_ONE
    _choices: list[FlagOptions] = []
    _value: FlagOptions
    _optionEnum: type[FlagOptions]
    _default: FlagOptions

    @property
    def option_enum(self) -> type[FlagOptions]:
        """The enum from which this setting's options come."""
        return self._optionEnum

    @property
    def choices(self) -> list[FlagOptions]:
        """The values to be chosen from."""
        return self._choices

    @property
    def value(self) -> FlagOptions:
        """The currently chosen value."""
        return self._value

    @property
    def default(self) -> FlagOptions:
        """The default chosen value."""
        return self._default

    def set_value(self, value: FlagOptions) -> None:
        """Set the currently chosen value."""
        assert value in self.choices
        self._value = value

    @property
    def choices_dict(self) -> list[dict[str, Any]]:
        """All options as a dict."""
        return [{"id": c.name, "text": c.value} for c in self.choices]
        # this really should be coming from its enum

    @property
    def default_dict(self) -> dict[str, str]:
        """Selected option as a dict."""
        return {"text": self.default.value, "id": self.default.name}
        # this really should be coming from its enum


class BooleanFlag(Flag):
    """For settings which can only be on or off"""

    _type: FlagTypes = FlagTypes.BOOLEAN
    _default: bool = False
    _value: bool = False

    @property
    def default(self) -> bool:
        """Default value"""
        return self._default

    @property
    def value(self) -> bool:
        """Current value"""
        return self._value

    def set_value(self, value: bool) -> None:
        """Set the current value"""
        self._value = value


class NumberThresholdFlag(Flag):
    """For settings which require a number from a range.\n
    Example: number of super jumps required to get your first prize."""

    _type: FlagTypes = FlagTypes.NUMBER
    _min: int = 0
    _max: int = 0
    _value: int = 0
    _default: int = 0

    @property
    def min(self) -> int:
        """The lowest legal value for the setting."""
        return self._min

    @property
    def max(self) -> int:
        """The highest legal value for the setting."""
        return self._max

    @property
    def value(self) -> int:
        """The current value for the setting."""
        return self._value

    @property
    def default(self) -> int:
        """The default value for the setting."""
        return self._default

    def set_value(self, value: int) -> None:
        """Set the current value for the setting."""
        self._value = value


FlagT = TypeVar("FlagT", bound="Flag")
