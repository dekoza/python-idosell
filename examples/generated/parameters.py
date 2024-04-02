from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from pydantic.dataclasses import dataclass

from .xml import LangValue


class ParametersFileFormat(Enum):
    IOF = "IOF"


class ParametersVersion(Enum):
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
        },
    )


@dataclass
class Icons:
    class Meta:
        name = "icons"

    card: List["Icons.Card"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    list_value: List["Icons.ListType"] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Card:
        lang: Optional[Union[str, LangValue]] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
        url: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ListType:
        lang: Optional[Union[str, LangValue]] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
                "required": True,
            },
        )
        url: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
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
        },
    )


@dataclass
class Parameter:
    class Meta:
        name = "parameter"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    icons: List[Icons] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "name",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Section:
    class Meta:
        name = "section"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    icons: List[Icons] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "name",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    icons: List[Icons] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "name",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Parameters:
    """
    :ivar sections:
    :ivar parameters:
    :ivar values:
    :ivar file_format: Format: IOF
    :ivar version: IOF version: major.minor
    :ivar generated_by:
    :ivar language:
    :ivar generated: Date generated: YYYY-MM-DD 00:00:00
    :ivar expires: Date expire offer: YYYY-MM-DD 00:00:00
    """

    class Meta:
        name = "parameters"

    sections: List["Parameters.Sections"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameters: List["Parameters.ParametersInner"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    values: List["Parameters.Values"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    file_format: Optional[ParametersFileFormat] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[ParametersVersion] = field(
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

    @dataclass
    class Sections:
        section: List[Section] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass
    class ParametersInner:
        parameter: List[Parameter] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass
    class Values:
        value: List[Value] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
