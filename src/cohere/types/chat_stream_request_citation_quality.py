# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChatStreamRequestCitationQuality(str, enum.Enum):
    """
    Defaults to `"accurate"`.

    Dictates the approach taken to generating citations as part of the RAG flow by allowing the user to specify whether they want `"accurate"` results or `"fast"` results.
    """

    FAST = "fast"
    ACCURATE = "accurate"

    def visit(self, fast: typing.Callable[[], T_Result], accurate: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatStreamRequestCitationQuality.FAST:
            return fast()
        if self is ChatStreamRequestCitationQuality.ACCURATE:
            return accurate()