# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .api_meta import ApiMeta
from .embed_by_type_response_embeddings import EmbedByTypeResponseEmbeddings

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EmbedByTypeResponse(pydantic.BaseModel):
    id: str
    embeddings: EmbedByTypeResponseEmbeddings = pydantic.Field(
        description="An object with different embedding types. The length of each embedding type array will be the same as the length of the original `texts` array."
    )
    texts: typing.List[str] = pydantic.Field(description="The text entries for which embeddings were returned.")
    meta: typing.Optional[ApiMeta] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
