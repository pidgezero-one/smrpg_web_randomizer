"""Base classes for settings presets."""


class Preset:
    """A pre-created settings string"""

    _name: str = ""
    _description: str = ""
    _flags: str = ""

    @property
    def name(self) -> str:
        """The name of this preset as it appears on the site"""
        return self._name

    @property
    def description(self) -> str:
        """A brief description of who this preset is meant for and what it does"""
        return self._description

    @property
    def flags(self) -> str:
        """The string that corresponds to the desired settings"""
        return self._flags

    @classmethod
    def id(cls):
        """An identifier for this preset to use internally."""
        return cls.__name__
