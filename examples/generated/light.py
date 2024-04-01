from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from pydantic.dataclasses import dataclass


class OfferExtensions(Enum):
    YES = "yes"
    NO = "no"


class OfferFileFormat(Enum):
    IOF = "IOF"


class OfferVersion(Enum):
    VALUE_3_0 = Decimal("3.0")


@dataclass
class Price:
    class Meta:
        name = "price"

    gross: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    net: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vat: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Srp:
    class Meta:
        name = "srp"

    gross: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    net: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    vat: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Stock:
    class Meta:
        name = "stock"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    quantity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(-1(.[0]+)?)|(\d+([\.,]\d+)?)",
        },
    )


@dataclass
class StrikethroughRetailPrice:
    class Meta:
        name = "strikethrough_retail_price"

    gross: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    net: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    vat: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StrikethroughWholesalePrice:
    class Meta:
        name = "strikethrough_wholesale_price"

    gross: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    net: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    vat: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Size:
    class Meta:
        name = "size"

    price: List[Price] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    srp: List[Srp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    strikethrough_retail_price: List[StrikethroughRetailPrice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    strikethrough_wholesale_price: List[StrikethroughWholesalePrice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    stock: List[Stock] = field(
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    panel_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    code_producer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_code_external: Optional[str] = field(
        default=None,
        metadata={
            "name": "code_external",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    code_external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    weight: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    weight_net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    min_weight: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    max_weight: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )


@dataclass
class Sizes:
    class Meta:
        name = "sizes"

    size: List[Size] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Product:
    class Meta:
        name = "product"

    price: List[Price] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    srp: List[Srp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    strikethrough_retail_price: List[StrikethroughRetailPrice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    strikethrough_wholesale_price: List[StrikethroughWholesalePrice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sizes: List[Sizes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    vat: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Products:
    class Meta:
        name = "products"

    product: List[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-z]{3,3}",
        },
    )


@dataclass
class Offer:
    class Meta:
        name = "offer"

    products: Optional[Products] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    file_format: Optional[OfferFileFormat] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[OfferVersion] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )
    expires: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )
    generated_by: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    extensions: Optional[OfferExtensions] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
