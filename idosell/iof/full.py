from decimal import Decimal
from typing import Literal

from pydantic import HttpUrl
from pydantic_xml.model import BaseXmlModel, element, attr, wrapped
import datetime as dt


class Price(BaseXmlModel):
    gross: Decimal | None = attr(default=None)
    net: Decimal = attr()


class Stock(BaseXmlModel):
    id: str = attr()
    quantity: Decimal | None = attr(default=None)
    available_stock_quantity: Decimal | None = attr(default=None)
    stock_quantity: Decimal | None = attr(default=None)


class Size(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str = attr()
    name: str | None = attr(default=None)
    panel_name: str | None = attr(default=None)
    code: str = attr()
    weight: str | None = attr(default=None)
    code_producer: str | None = attr(default=None)

    price: Price
    srp: Price
    strikethrough_retail_price: Price | None = element(default=None)
    strikethrough_wholesale_price: Price | None = element(default=None)
    stock: list[Stock] | None = element(tag="stock", default=None)


class IdName(BaseXmlModel):
    id: str = attr()
    name: str = attr()


class IdPath(BaseXmlModel):
    id: str = attr()
    path: str = attr()


class Warranty(IdName):
    type: str = attr()
    period: str = attr()


class Name(BaseXmlModel, nsmap={"xml": "http://www.w3.org/XML/1998/namespace"}):
    lang: str = attr(name="lang", ns="xml")
    name: str


class Card(BaseXmlModel):
    url: HttpUrl = attr()


class Version(BaseXmlModel):
    main_name: str = attr(name="name")
    names: list[Name] = element(tag="name")


class Description(
    BaseXmlModel,
    search_mode="unordered",
):
    names: list[Name] = element(tag="name")
    versions: list[Version] | None = element(tag="version", default=None)
    long_descs: list[Name] = element(tag="long_desc")
    short_descs: list[Name] = element(tag="short_desc")


class Product(
    BaseXmlModel,
    tag="product",
    search_mode="unordered",
):
    id: str = attr()
    currency: str = attr()
    code_on_card: str = attr()
    producer_code_standard: str = attr()
    type: str = attr()
    vat: Decimal | None = attr(default=None)
    site: str = attr()

    producer: IdName
    category: IdName
    category_idosell: IdPath | None = element(default=None)
    warranty: Warranty | None = element(default=None)
    card: Card
    description: Description

    price: Price = element()
    srp: Price = element()

    sizes: list[Size] = wrapped(
        "sizes",
        element(tag="size"),
    )


class Full(
    BaseXmlModel,
    tag="offer",
    search_mode="unordered",
):
    file_format: str = attr(default="IOF")
    version: str = attr(default="3.0")
    extensions: Literal["yes", "no"] = attr(default="no")
    generated: dt.datetime = attr()
    expires: dt.datetime = attr()
    products: list[Product] = wrapped(
        "products",
        element(tag="product"),
    )
