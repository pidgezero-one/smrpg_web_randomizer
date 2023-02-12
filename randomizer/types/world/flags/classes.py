from django.utils.safestring import mark_safe, SafeString
from markdown import markdown
from typing import Type, Any
import bleach

from randomizer.types.world.flags.enums import FlagOptions, FlagTypes


# ************************************** Flag classes


class FlagError(ValueError):
    pass


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
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def inverse_description(self) -> str:
        return self._inverse_description

    @property
    def hard(self) -> bool:
        return self._hard

    @property
    def id(self) -> str:
        return self._id

    @property
    def type(self) -> FlagTypes:
        return self._type

    # @classmethod
    # def id(cls):
    #     return cls.__name__
    # return cls.description_or_name_as_markdown

    @classmethod
    def description_as_markdown(cls) -> SafeString:
        return mark_safe(markdown(bleach.clean(cls().description)))

    @classmethod
    def description_or_name_as_markdown(cls) -> SafeString:
        if cls.description:
            return mark_safe(markdown(bleach.clean(cls().description)))
        else:
            return mark_safe(markdown(bleach.clean(cls().name)))

    @classmethod
    def inverse_description_as_markdown(cls) -> SafeString:
        return mark_safe(markdown(bleach.clean(cls().inverse_description)))

    @classmethod
    def inverse_description_or_name_as_markdown(cls) -> SafeString:
        if cls.inverse_description:
            return mark_safe(markdown(bleach.clean(cls().inverse_description)))
        else:
            return mark_safe(markdown(bleach.clean(f"({cls().name})")))


class CategorizationFlag(Flag):
    """For things like selecting which locations can and cannot contain progression"""

    _type: FlagTypes = FlagTypes.Categorization
    _options: List[FlagOptions] = []
    _enabled: List[FlagOptions] = []
    _optionEnum: Type[FlagOptions]

    @property
    def options(self) -> List[FlagOptions]:
        return self._options

    @property
    def enabled(self) -> List[FlagOptions]:
        return self._enabled

    def set_enabled(self, options: List[FlagOptions]) -> None:
        for opt in options:
            assert opt in self.options
        self._enabled = list(set([o for o in options]))

    @property
    def disabled(self) -> List[FlagOptions]:
        return [o for o in self.options if o not in self.enabled]

    @property
    def optionEnum(self) -> Type[FlagOptions]:
        return self._optionEnum

    @property
    def options_dict(self) -> List[dict[str, Any]]:
        return [{"id": c.name, "text": c.value} for c in self.options]

    @property
    def default_dict(self) -> List[dict[str, Any]]:
        return [{"id": c.name, "text": c.value} for c in self.enabled]
        # this really should be coming from its enum


class SelectOneFlag(Flag):
    """For things like choosing an area gating option can and cannot contain progression"""

    _type: FlagTypes = FlagTypes.SelectOne
    _choices: List[FlagOptions] = []
    _value: FlagOptions
    _optionEnum: Type[FlagOptions]
    _default: FlagOptions

    @property
    def optionEnum(self) -> Type[FlagOptions]:
        return self._optionEnum

    @property
    def choices(self) -> List[FlagOptions]:
        return self._choices

    @property
    def value(self) -> FlagOptions:
        return self._value

    @property
    def default(self) -> FlagOptions:
        return self._default

    def set_value(self, value: FlagOptions) -> None:
        assert value in self.choices
        self._value = value

    @property
    def choices_dict(self) -> List[dict[str, Any]]:
        return [{"id": c.name, "text": c.value} for c in self.choices]
        # this really should be coming from its enum

    @property
    def default_dict(self) -> Dict[str, str]:
        return {"text": self.default.value, "id": self.default.name}
        # this really should be coming from its enum


class BooleanFlag(Flag):
    """For settings which can only be on or off"""

    _type: FlagTypes = FlagTypes.Boolean
    _default: bool = False
    _value: bool = False

    @property
    def default(self) -> bool:
        return self._default

    @property
    def value(self) -> bool:
        return self._value

    def set_value(self, value: bool) -> None:
        self._value = value


class NumberThresholdFlag(Flag):
    """For settings which require a number from a range"""

    _type: FlagTypes = FlagTypes.Number
    _min: int = 0
    _max: int = 0
    _value: int = 0
    _default: int = 0

    @property
    def min(self) -> int:
        return self._min

    @property
    def max(self) -> int:
        return self._max

    @property
    def value(self) -> int:
        return self._value

    @property
    def default(self) -> int:
        return self._default

    def set_value(self, value: int) -> None:
        self._value = value
