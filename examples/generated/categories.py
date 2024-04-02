from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from pydantic.dataclasses import dataclass

from .xml import LangValue


class CategoriesFileFormat(Enum):
    IOF = "IOF"


class CategoriesVersion(Enum):
    VALUE_3_0 = Decimal("3.0")


@dataclass
class Name:
    class Meta:
        name = "name"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "type": str,
                    "default": "",
                },
            ),
        },
    )


@dataclass
class Category:
    class Meta:
        name = "category"

    category: List["Category"] = field(
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


@dataclass
class Categories:
    """
    :ivar category:
    :ivar file_format: Format: IOF
    :ivar version: IOF version: major.minor
    :ivar generated_by:
    :ivar language:
    :ivar generated: Date generated: YYYY-MM-DD 00:00:00
    :ivar expires: Date expire offer: YYYY-MM-DD 00:00:00
    """

    class Meta:
        name = "categories"

    category: List[Category] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    file_format: Optional[CategoriesFileFormat] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[CategoriesVersion] = field(
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
