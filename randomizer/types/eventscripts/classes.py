from constants.classes import EventScriptCommandName
import uuid


class EventScriptCommand:
    command_name: EventScriptCommandName
    identifier: str

    def _generate_identifier(self) -> str:
        return self.command_name + "_" + str(uuid.uuid4())

    def __init__(self, identifier: str = None) -> None:
        if identifier is None or len(identifier) == 0:
            identifier = self._generate_identifier()
        self.identifier = identifier


class EventScriptCommandNoArgs(EventScriptCommand):

    def __init__(self, identifier: str = None) -> None:
        super().__init__(identifier)
