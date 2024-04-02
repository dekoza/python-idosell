from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from pydantic.dataclasses import dataclass

from .xml import LangValue


@dataclass
class Terms:
    class Meta:
        name = "terms"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    period_number: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    period_unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class WarrantiesFileFormat(Enum):
    IOF = "IOF"


class WarrantiesVersion(Enum):
    VALUE_3_0 = Decimal("3.0")


@dataclass
class Description:
    class Meta:
        name = "description"

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
class Warranty:
    class Meta:
        name = "warranty"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    terms: List[Terms] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    description: List[Description] = field(
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
class Warranties:
    """
    :ivar warranty:
    :ivar file_format: Format: IOF
    :ivar version: IOF version: major.minor
    :ivar generated_by:
    :ivar language:
    :ivar generated: Date generated: YYYY-MM-DD 00:00:00
    :ivar expires: Date expire offer: YYYY-MM-DD 00:00:00
    """

    class Meta:
        name = "warranties"

    warranty: List[Warranty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    file_format: Optional[WarrantiesFileFormat] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[WarrantiesVersion] = field(
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
