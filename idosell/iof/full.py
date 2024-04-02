from decimal import Decimal
from typing import Literal
from enum import StrEnum, auto
from pydantic import HttpUrl, conlist
from pydantic_xml.model import BaseXmlModel, element, attr, wrapped
import datetime as dt

from .shared import YesNo


class PriceBase(BaseXmlModel):
    gross: Decimal | None = attr(default=None)
    vat: Decimal | None = attr(default=None)
    net: Decimal = attr()


class Price(PriceBase):
    normal_retail_price: PriceBase | None = element(default=None)
    normal_wholesale_price: PriceBase | None = element(default=None)


class Stock(BaseXmlModel):
    id: str = attr()
    quantity: Decimal | None = attr(default=None)
    available_stock_quantity: Decimal | None = attr(default=None)
    stock_quantity: Decimal | None = attr(default=None)


class Size(
    BaseXmlModel,
    search_mode="unordered",
):
    id: str | None = attr(default=None)
    name: str | None = attr(default=None)
    panel_name: str | None = attr(default=None)
    code: str | None = attr(default=None)
    weight: str | None = attr(default=None)
    code_producer: str | None = attr(default=None)
    # code_external
    # weight_net
    # min_weight
    # max_weight
    # priority
    # iai_shop_com_developers_iof_extensions_phtml_code
    # iai_shop_com_developers_iof_extensions_phtml_code_producer

    prices: list[PriceBase] | None = element(default=None, tag="price")
    srps: list[PriceBase] | None = element(default=None, tag="srp")
    strikethrough_retail_prices: list[PriceBase] | None = element(
        default=None, tag="strikethrough_retail_price"
    )
    strikethrough_wholesale_prices: PriceBase | None = element(
        default=None, tag="strikethrough_wholesale_price"
    )

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
    type: str | None = attr(default=None)
    name: str


class Card(BaseXmlModel):
    url: HttpUrl = attr()
    url_mobile: HttpUrl | None = attr(default=None)


class Version(BaseXmlModel, nsmap={"xml": "http://www.w3.org/XML/1998/namespace"}):
    lang: str | None = attr(name="lang", ns="xml", default=None)
    name_attribute: str = attr(name="name")
    names: conlist(Name, min_length=1) = element(tag="name")


class Description(
    BaseXmlModel,
    search_mode="unordered",
):
    names: list[Name] = element(tag="name")
    versions: list[Version] | None = element(tag="version", default=None)
    long_descs: list[Name] = element(tag="long_desc")
    short_descs: list[Name] = element(tag="short_desc")
    # auction_names: list[Name] = element(tag="auction_name", ns=...)
    # ...


class Image(BaseXmlModel, search_mode="unordered"):
    url: HttpUrl = attr()
    hash: str | None = attr(default=None)
    changed: dt.datetime | None = attr(default=None)
    width: int | None = attr(default=None)
    height: int | None = attr(default=None)
    # priority


class Icons(BaseXmlModel):
    icons: list[Image] = element(tag="icon")
    auction_icons: list[Image] | None = element(default=None, tag="auction_icon")
    group_icons: list[Image] | None = element(default=None, tag="group_icon")


class Images(BaseXmlModel):
    large: list[Image] = wrapped("large", element(tag="image"))
    icons: list[Icons] = element(tag="icons")


class Limitation(BaseXmlModel):
    downloads: int | None = attr(default=None)
    days: int | None = attr(default=None)


class File(BaseXmlModel):
    version: str | None = attr(default=None)
    url: HttpUrl = attr()
    priority: int = attr()
    attachment_file_type: str | None = attr(default=None)
    attachment_file_extension: str | None = attr(default=None)
    enable: str | None = attr(default=None)
    download_log: str | None = attr(default=None)
    names: list[Name] | None = element(tag="name", default=None)
    limitations: list[Limitation] | None = element(tag="limitation", default=None)


class IdName2(BaseXmlModel):
    id: str = attr()
    names: list[Name] = element(tag="name")


class GroupByParam(IdName2):
    product_values: list[IdName2] = element(tag="product_value")


class Group(BaseXmlModel):
    id: str = attr()
    group_by_parameter: GroupByParam = element(tag="group_by_parameter")


class IdNamePrio(IdName):
    priority: int = attr()


class Parameter(IdName, nsmap={"xml": "http://www.w3.org/XML/1998/namespace"}):
    value: IdNamePrio | None = element(default=None)
    lang: str | None = attr(name="lang", ns="xml", default=None)
    type: str | None = attr(default=None)
    priority: str | None = attr(default=None)
    distinction: YesNo | None = attr(default=None)
    group_distinction: YesNo | None = attr(default=None)
    hide: YesNo | None = attr(default=None)
    auction_template_hide: YesNo | None = attr(default=None)
    context_id: str | None = attr(default=None)


class BundleProduct(BaseXmlModel):
    id: str = attr()
    type: str = attr()
    quantity: Decimal = attr()
    sizes: list[Size] | None = wrapped(
        "sizes", element(tag="size", default=None), default=None
    )


class Bundle(BaseXmlModel):
    type: str = attr()
    products: list[BundleProduct] = element(tag="product")


class ProdCodeStandard(StrEnum):
    AUTO = auto()
    GTIN14 = auto()
    GTIN13 = auto()
    GTIN12 = auto()
    GTIN8 = auto()
    ISBN13 = auto()
    ISBN10 = auto()
    UPCE = auto()
    MPN = auto()
    OTHER = auto()

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member == value:
                return member
        return None


class ShownInTheZone(BaseXmlModel):
    promotion: YesNo | None = attr(default=None)
    discount: YesNo | None = attr(default=None)
    distinguished: YesNo | None = attr(default=None)
    special: YesNo | None = attr(default=None)
    bestseller: YesNo | None = attr(default=None)
    newproduct: YesNo | None = attr(default=None)


class Promotion(BaseXmlModel):
    price: Price
    shown_in_the_zone: ShownInTheZone
    name: str = attr()
    start_date: str | None = attr(default=None)
    ending_date: str | None = attr(default=None)


class Product(
    BaseXmlModel,
    tag="product",
    search_mode="unordered",
):
    id: str = attr()
    currency: str | None = attr(default=None)
    code_on_card: str = attr()
    producer_code_standard: ProdCodeStandard = attr()
    type: str = attr()
    vat: Decimal | None = attr(default=None)
    site: int | None = attr(default=None)
    removed: YesNo | None = attr(default=None)

    producers: list[IdName] | None = element(default=None, tag="producer")
    categories: list[IdName] | None = element(default=None, tag="category")
    categories_idosell: list[IdPath] | None = element(
        default=None, tag="category_idosell"
    )
    units: list[IdName] | None = element(default=None, tag="unit")
    series: list[IdName] | None = element(default=None, tag="series")
    warranty: Warranty | None = element(default=None)
    cards: list[Card] | None = element(default=None, tag="card")
    descriptions: list[Description] | None = element(default=None, tag="description")

    prices: list[PriceBase] | None = element(default=None, tag="price")
    srps: list[PriceBase] | None = element(default=None, tag="srp")
    strikethrough_retail_prices: list[PriceBase] | None = element(
        default=None, tag="strikethrough_retail_price"
    )
    strikethrough_wholesale_prices: PriceBase | None = element(
        default=None, tag="strikethrough_wholesale_price"
    )

    promotions: list[Promotion] | None = element(default=None, tag="promotion")

    sizes: list[Size] = wrapped(
        "sizes",
        element(tag="size"),
    )

    images: Images
    attachments: list[File] | None = wrapped(
        "attachments", element(tag="file", default=None), default=None
    )
    group: Group | None = element(default=None)
    parameters: list[Parameter] = wrapped("parameters", element(tag="parameter"))
    bundled: Bundle | None = element(default=None)


class Products(BaseXmlModel):
    language: str = attr()
    currency: str | None = attr(default=None)
    iof_translation_generated: YesNo | None = attr(default=None)
    products: list[Product] | None = element(default=None)


class Full(
    BaseXmlModel,
    tag="offer",
    search_mode="unordered",
    nsmap={
        "iof": "http://www.iai-shop.com/developers/iof.phtml",
        "xml": "http://www.w3.org/XML/1998/namespace",
        "iaiext": "http://www.iai-shop.com/developers/iof/extensions.phtml",
    },
):
    file_format: Literal["IOF"] | None = attr(default="IOF")
    version: Decimal = attr(default="3.0")
    extensions: YesNo = attr(default="no")
    generated: dt.datetime | None = attr(default=None)
    generated_by: str | None = attr(default=None)
    expires: dt.datetime | None = attr(default=None)
    products: Products
