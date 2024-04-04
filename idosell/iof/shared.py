from decimal import Decimal
from enum import StrEnum
from typing import Literal
import datetime as dt

from pydantic_xml import BaseXmlModel, attr


class SharedBaseModel(
    BaseXmlModel,
    search_mode="unordered",
    nsmap={
        "iof": "http://www.iai-shop.com/developers/iof.phtml",
        "xml": "http://www.w3.org/XML/1998/namespace",
        "iaiext": "http://www.iai-shop.com/developers/iof/extensions.phtml",
    },
):
    file_format: Literal["IOF"] | None = attr(default="IOF")
    version: Decimal = attr(default="3.0")
    generated: dt.datetime | None = attr(default=None)
    generated_by: str | None = attr(default=None)
    expires: dt.datetime | None = attr(default=None)


class YesNo(StrEnum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ProductType(StrEnum):
    REGULAR = "regular"
    PACKAGING = "packaging"
    VIRTUAL = "virtual"
    BUNDLE = "bundle"
    COLLECTION = "collection"
    SERVICE = "service"
