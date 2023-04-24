"""Base classes supporting NPC action script assembly."""

from .classes import (
    ActionScriptCommand,
    ActionScriptCommandWithJmps,
    ActionScriptCommandNoArgs,
    ActionScriptCommandAnySizeMem,
    ActionScriptCommandShortMem,
    ActionScriptCommandShortAddrAndValueOnly,
    ActionScriptCommandBasicShortOperation,
    ActionScriptCommandByteSteps,
    ActionScriptCommandBytePixels,
    ActionScriptCommandXYBytes,
    UsableActionScriptCommand,
)
