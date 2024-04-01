from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from pydantic.dataclasses import dataclass

from generated.xml import LangValue


class SeriesFileFormat(Enum):
    IOF = "IOF"


class SeriesVersion(Enum):
    VALUE_3_0 = Decimal("3.0")


@dataclass
class Name:
    class Meta:
        name = "name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class Series:
    """
    :ivar series:
    :ivar name:
    :ivar file_format: Format: IOF
    :ivar version: IOF version: major.minor
    :ivar generated_by:
    :ivar language:
    :ivar generated: Date generated: YYYY-MM-DD 00:00:00
    :ivar expires: Date expire offer: YYYY-MM-DD 00:00:00
    :ivar id:
    :ivar name_attribute:
    """

    class Meta:
        name = "series"

    series: List["Series"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    file_format: Optional[SeriesFileFormat] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[SeriesVersion] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    generated_by: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-z]{3,3}",
        },
    )
    generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}",
        },
    )
    expires: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "name",
            "type": "Attribute",
        },
    )
