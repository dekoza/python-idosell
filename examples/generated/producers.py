from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from pydantic.dataclasses import dataclass


@dataclass
class Producer:
    class Meta:
        name = "producer"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class ProducersFileFormat(Enum):
    IOF = "IOF"


class ProducersVersion(Enum):
    VALUE_3_0 = Decimal("3.0")


@dataclass
class Producers:
    """
    :ivar producer:
    :ivar file_format: Format: IOF
    :ivar version: IOF version: major.minor
    :ivar generated_by:
    :ivar language:
    :ivar generated: Date generated: YYYY-MM-DD 00:00:00
    :ivar expires: Date expire offer: YYYY-MM-DD 00:00:00
    """

    class Meta:
        name = "producers"

    producer: List[Producer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    file_format: Optional[ProducersFileFormat] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[ProducersVersion] = field(
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
