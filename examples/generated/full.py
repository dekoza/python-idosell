from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from pydantic.dataclasses import dataclass

from .extensions import (
    Advance,
    AssociatedProducts,
    AttachmentFileTypeValue,
    AuctionLongDesc,
    AuctionName,
    AuctionPrice,
    Availability,
    AvailabilityManagement,
    AvailabilityProfile,
    CardTranslation,
    CategoryTranslation,
    ContextIdValue,
    Deliverer,
    DeliveryTime,
    DownloadLogValue,
    EnableInPos,
    EnableValue,
    Hotspots,
    IaiCategory,
    IaiCategoryTranslation,
    Inwrapper,
    LoyaltyProgram,
    MetaDescription,
    MetaKeywords,
    MetaTitle,
    Navigation,
    Note,
    PosPricesConfig,
    PricecomparatorName,
    PricecomparatorPrice,
    PriceMinimal,
    PricePos,
    PriceRetail,
    PricesConfig,
    PricesConfigurationForShops,
    PriceWholesale,
    Priority,
    ProductFreeValue,
    SaveSerialNumbersValue,
    SellBy,
    SeriesTranslation,
    SizeChart,
    SumInBasket,
    Taxcode,
    UnitTranslation,
    Visibility,
    WarrantyTranslation,
)
from generated.extensions import (
    Srp as ExtensionsSrp,
)
from generated.extensions import (
    StrikethroughWholesalePrice as ExtensionsStrikethroughWholesalePrice,
)
from generated.xml import LangValue


@dataclass
class AuctionIcon:
    class Meta:
        name = "auction_icon"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    changed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class BundledType(Enum):
    SPECIFIED = "specified"
    UNSPECIFIED = "unspecified"


@dataclass
class Card:
    class Meta:
        name = "card"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    url_mobile: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_url_mobile: Optional[str] = field(
        default=None,
        metadata={
            "name": "url_mobile",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )


class FileAttachmentFileType(Enum):
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    DOCUMENT = "document"
    OTHER = "other"


class FileDownloadLog(Enum):
    Y = "y"
    N = "n"


class FileEnable(Enum):
    ALL = "all"
    ONLY_LOGGED = "only_logged"
    ORDERED = "ordered"
    WHOLESALER = "wholesaler"
    WHOLESALER_OR_ORDERER = "wholesaler_or_orderer"
    WHOLESALER_AND_ORDERED = "wholesaler_and_ordered"


class FileVersion(Enum):
    FULL = "full"
    SAMPLE = "sample"
    DEMO = "demo"


@dataclass
class GroupIcon:
    class Meta:
        name = "group_icon"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    changed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Icon:
    class Meta:
        name = "icon"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    changed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Limitation:
    class Meta:
        name = "limitation"

    downloads: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    days: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class NormalRetailPrice:
    class Meta:
        name = "normal_retail_price"

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
class NormalWholesalePrice:
    class Meta:
        name = "normal_wholesale_price"

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


class OfferExtensions(Enum):
    YES = "yes"
    NO = "no"


class OfferFileFormat(Enum):
    IOF = "IOF"


class OfferVersion(Enum):
    VALUE_3_0 = Decimal("3.0")


class ParameterAuctionTemplateHide(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ParameterContextId(Enum):
    CONTEXT_STD_UNIT_LENGTH_CM = "CONTEXT_STD_UNIT_LENGTH_CM"
    CONTEXT_STD_UNIT_LENGTH = "CONTEXT_STD_UNIT_LENGTH"
    CONTEXT_MOVIE_RELEASE_DATE = "CONTEXT_MOVIE_RELEASE_DATE"
    CONTEXT_MOVIE_ORIGINAL_TITLE = "CONTEXT_MOVIE_ORIGINAL_TITLE"
    CONTEXT_AGE_GROUP = "CONTEXT_AGE_GROUP"
    CONTEXT_ENERGY_EFFICIENCY_CLASS = "CONTEXT_ENERGY_EFFICIENCY_CLASS"
    CONTEXT_COLOR = "CONTEXT_COLOR"
    CONTEXT_BOOK_AUTHOR = "CONTEXT_BOOK_AUTHOR"
    CONTEXT_BOOK_PUBLICATION_DATE = "CONTEXT_BOOK_PUBLICATION_DATE"
    CONTEXT_BOOK_PAGES_NUMBER = "CONTEXT_BOOK_PAGES_NUMBER"
    CONTEXT_BOOK_PUBLICATION_LANGUAGE = "CONTEXT_BOOK_PUBLICATION_LANGUAGE"
    CONTEXT_PRESCRIPTION_MEDICINE = "CONTEXT_PRESCRIPTION_MEDICINE"
    CONTEXT_STD_UNIT_QUANTITY_PACKAGE = "CONTEXT_STD_UNIT_QUANTITY_PACKAGE"
    CONTEXT_MAX_SIZE_QUANTITY_PER_RETAIL_ORDER = (
        "CONTEXT_MAX_SIZE_QUANTITY_PER_RETAIL_ORDER"
    )
    CONTEXT_MAX_SIZE_QUANTITY_PER_WHOLESALE_ORDER = (
        "CONTEXT_MAX_SIZE_QUANTITY_PER_WHOLESALE_ORDER"
    )
    CONTEXT_MAX_QUANTITY_PER_RETAIL_ORDER = "CONTEXT_MAX_QUANTITY_PER_RETAIL_ORDER"
    CONTEXT_MAX_QUANTITY_PER_WHOLESALE_ORDER = (
        "CONTEXT_MAX_QUANTITY_PER_WHOLESALE_ORDER"
    )
    CONTEXT_MIN_SIZE_QUANTITY_PER_RETAIL_ORDER = (
        "CONTEXT_MIN_SIZE_QUANTITY_PER_RETAIL_ORDER"
    )
    CONTEXT_MIN_SIZE_QUANTITY_PER_WHOLESALE_ORDER = (
        "CONTEXT_MIN_SIZE_QUANTITY_PER_WHOLESALE_ORDER"
    )
    CONTEXT_MIN_QUANTITY_PER_RETAIL_ORDER = "CONTEXT_MIN_QUANTITY_PER_RETAIL_ORDER"
    CONTEXT_MIN_QUANTITY_PER_WHOLESALE_ORDER = (
        "CONTEXT_MIN_QUANTITY_PER_WHOLESALE_ORDER"
    )
    CONTEXT_MODEL = "CONTEXT_MODEL"
    CONTEXT_STD_UNIT_VOLUME_SI = "CONTEXT_STD_UNIT_VOLUME_SI"
    CONTEXT_STD_UNIT_VOLUME_M3 = "CONTEXT_STD_UNIT_VOLUME_M3"
    CONTEXT_STD_UNIT_VOLUME = "CONTEXT_STD_UNIT_VOLUME"
    CONTEXT_DOCUMENTS_JPK_VAT = "CONTEXT_DOCUMENTS_JPK_VAT"
    CONTEXT_SEX = "CONTEXT_SEX"
    CONTEXT_STD_UNIT_AREA_M2 = "CONTEXT_STD_UNIT_AREA_M2"
    CONTEXT_SEASON = "CONTEXT_SEASON"
    CONTEXT_STATE = "CONTEXT_STATE"
    CONTEXT_STD_UNIT_WIDTH_CM = "CONTEXT_STD_UNIT_WIDTH_CM"
    CONTEXT_ONLY_ADULTS = "CONTEXT_ONLY_ADULTS"
    CONTEXT_STD_OVERHEAD_WEIGHT = "CONTEXT_STD_OVERHEAD_WEIGHT"
    CONTEXT_WEIGHT_NET = "CONTEXT_WEIGHT_NET"
    CONTEXT_WEIGHT_PACKAGING = "CONTEXT_WEIGHT_PACKAGING"
    CONTEXT_STD_UNIT_WEIGHT = "CONTEXT_STD_UNIT_WEIGHT"
    CONTEXT_STD_UNIT_WEIGHT_SI = "CONTEXT_STD_UNIT_WEIGHT_SI"
    CONTEXT_STD_UNIT_HEIGHT_CM = "CONTEXT_STD_UNIT_HEIGHT_CM"
    CONTEXT_HEEL_HEIGHT = "CONTEXT_HEEL_HEIGHT"
    HEEL_HEIGHT = "HEEL_HEIGHT"


class ParameterDistinction(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ParameterGroupDistinction(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ParameterHide(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ParameterType(Enum):
    SECTION = "section"
    PARAMETER = "parameter"
    VALUE = "value"


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
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class ProductProducerCodeStandard(Enum):
    AUTO = "AUTO"
    GTIN14 = "GTIN14"
    GTIN13 = "GTIN13"
    GTIN12 = "GTIN12"
    GTIN8 = "GTIN8"
    ISBN13 = "ISBN13"
    ISBN10 = "ISBN10"
    UPCE = "UPCE"
    MPN = "MPN"
    OTHER = "OTHER"
    AUTO_1 = "auto"
    GTIN14_1 = "gtin14"
    GTIN13_1 = "gtin13"
    GTIN12_1 = "gtin12"
    GTIN8_1 = "gtin8"
    ISBN13_1 = "isbn13"
    ISBN10_1 = "isbn10"
    UPCE_1 = "upce"
    MPN_1 = "mpn"
    OTHER_1 = "other"


class ProductRemoved(Enum):
    YES = "yes"


class ProductType(Enum):
    REGULAR = "regular"
    PACKAGING = "packaging"
    VIRTUAL = "virtual"
    BUNDLE = "bundle"
    COLLECTION = "collection"
    SERVICE = "service"


class ShownInTheZoneBestseller(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ShownInTheZoneDiscount(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ShownInTheZoneDistinguished(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ShownInTheZoneNewproduct(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ShownInTheZonePromotion(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class ShownInTheZoneSpecial(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


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

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    location_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    location_text_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_location_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "location_id",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_location_text_id: Optional[str] = (
        field(
            default=None,
            metadata={
                "name": "location_text_id",
                "type": "Attribute",
                "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
            },
        )
    )
    quantity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(-1(.[0]+)?)|(\d+([\.,]\d+)?)",
        },
    )
    available_stock_quantity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stock_quantity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


class ValueContextId(Enum):
    CONTEXT_AGE_GROUP_ADULT = "CONTEXT_AGE_GROUP_ADULT"
    CONTEXT_AGE_GROUP_MINOR = "CONTEXT_AGE_GROUP_MINOR"
    CONTEXT_PRESCRIPTION_MEDICINE_YES = "CONTEXT_PRESCRIPTION_MEDICINE_YES"
    CONTEXT_PRESCRIPTION_MEDICINE_NO = "CONTEXT_PRESCRIPTION_MEDICINE_NO"
    CONTEXT_SEX_MAN = "CONTEXT_SEX_MAN"
    CONTEXT_SEX_WOMAN = "CONTEXT_SEX_WOMAN"
    CONTEXT_SEX_UNISEX = "CONTEXT_SEX_UNISEX"
    CONTEXT_STD_UNIT_DEFAULT = "CONTEXT_STD_UNIT_DEFAULT"
    CONTEXT_STD_UNIT_WHOLE = "CONTEXT_STD_UNIT_WHOLE"
    CONTEXT_STD_UNIT_TENS = "CONTEXT_STD_UNIT_TENS"
    CONTEXT_STD_UNIT_HUNDREDS = "CONTEXT_STD_UNIT_HUNDREDS"
    CONTEXT_STD_UNIT_ONES = "CONTEXT_STD_UNIT_ONES"
    CONTEXT_SEASON_SPRING = "CONTEXT_SEASON_SPRING"
    CONTEXT_SEASON_SUMMER = "CONTEXT_SEASON_SUMMER"
    CONTEXT_SEASON_FALL = "CONTEXT_SEASON_FALL"
    CONTEXT_SEASON_WINTER = "CONTEXT_SEASON_WINTER"
    CONTEXT_SEASON_SPRING_SUMMER = "CONTEXT_SEASON_SPRING_SUMMER"
    CONTEXT_SEASON_FALL_WINTER = "CONTEXT_SEASON_FALL_WINTER"
    CONTEXT_STATE_NEW = "CONTEXT_STATE_NEW"
    CONTEXT_STATE_NEW_OTHERS = "CONTEXT_STATE_NEW_OTHERS"
    CONTEXT_STATE_NEW_WITH_DEFECTS = "CONTEXT_STATE_NEW_WITH_DEFECTS"
    CONTEXT_STATE_USED = "CONTEXT_STATE_USED"
    CONTEXT_STATE_REFURBISHED_BY_PRODUCER = "CONTEXT_STATE_REFURBISHED_BY_PRODUCER"
    CONTEXT_STATE_REFURBISHED_BY_SELLER = "CONTEXT_STATE_REFURBISHED_BY_SELLER"
    CONTEXT_STATE_FOR_PARTS_OR_BROKEN = "CONTEXT_STATE_FOR_PARTS_OR_BROKEN"
    CONTEXT_ONLY_ADULTS_YES = "CONTEXT_ONLY_ADULTS_YES"
    CONTEXT_ONLY_ADULTS_NO = "CONTEXT_ONLY_ADULTS_NO"


class WarrantyType(Enum):
    SELLER = "seller"
    PRODUCER = "producer"
    NONE = "none"


@dataclass
class Category:
    class Meta:
        name = "category"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CategoryIdosell:
    class Meta:
        name = "category_idosell"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    path: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Icons:
    class Meta:
        name = "icons"

    icon: List[Icon] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    auction_icon: List[AuctionIcon] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    group_icon: List[GroupIcon] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Image:
    class Meta:
        name = "image"

    priority: Optional[Priority] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    changed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LongDesc:
    class Meta:
        name = "long_desc"

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
    type_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
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
class Price:
    class Meta:
        name = "price"

    normal_retail_price: Optional[NormalRetailPrice] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    normal_wholesale_price: Optional[NormalWholesalePrice] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
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
class Section:
    class Meta:
        name = "section"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Series:
    class Meta:
        name = "series"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ShortDesc:
    class Meta:
        name = "short_desc"

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
class ShownInTheZone:
    class Meta:
        name = "shown_in_the_zone"

    promotion: Optional[ShownInTheZonePromotion] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    discount: Optional[ShownInTheZoneDiscount] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    distinguished: Optional[ShownInTheZoneDistinguished] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    special: Optional[ShownInTheZoneSpecial] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    bestseller: Optional[ShownInTheZoneBestseller] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    newproduct: Optional[ShownInTheZoneNewproduct] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Unit:
    class Meta:
        name = "unit"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    context_id: Optional[ValueContextId] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_context_id: Optional[
        ContextIdValue
    ] = field(
        default=None,
        metadata={
            "name": "context_id",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )


@dataclass
class Warranty:
    class Meta:
        name = "warranty"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[WarrantyType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    period: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class File:
    class Meta:
        name = "file"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    limitation: Optional[Limitation] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "name",
            "type": "Attribute",
        },
    )
    version: Optional[FileVersion] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    enable: Optional[FileEnable] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    attachment_file_type: Optional[FileAttachmentFileType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    attachment_file_extension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    download_log: Optional[FileDownloadLog] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_enable: Optional[EnableValue] = field(
        default=None,
        metadata={
            "name": "enable",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_attachment_file_type: Optional[
        AttachmentFileTypeValue
    ] = field(
        default=None,
        metadata={
            "name": "attachment_file_type",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_attachment_file_extension: Optional[
        str
    ] = field(
        default=None,
        metadata={
            "name": "attachment_file_extension",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_download_log: Optional[
        DownloadLogValue
    ] = field(
        default=None,
        metadata={
            "name": "download_log",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )


@dataclass
class Large:
    class Meta:
        name = "large"

    image: List[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Parameter:
    class Meta:
        name = "parameter"

    value: List[Value] = field(
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
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[ParameterType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    distinction: Optional[ParameterDistinction] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    group_distinction: Optional[ParameterGroupDistinction] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hide: Optional[ParameterHide] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auction_template_hide: Optional[ParameterAuctionTemplateHide] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_context_id: Optional[
        ContextIdValue
    ] = field(
        default=None,
        metadata={
            "name": "context_id",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    context_id: Optional[ParameterContextId] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ProductValue:
    class Meta:
        name = "product_value"

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


@dataclass
class Promotion:
    class Meta:
        name = "promotion"

    price: Optional[Price] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    shown_in_the_zone: Optional[ShownInTheZone] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ending_date: Optional[str] = field(
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
    code_external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
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
    priority: Optional[Priority] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "code",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_code_producer: Optional[str] = field(
        default=None,
        metadata={
            "name": "code_producer",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )


@dataclass
class Version:
    class Meta:
        name = "version"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    name_attribute: Optional[object] = field(
        default=None,
        metadata={
            "name": "name",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Attachments:
    class Meta:
        name = "attachments"

    file: List[File] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Description:
    class Meta:
        name = "description"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    auction_name: List[AuctionName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    version: List[Version] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    short_desc: List[ShortDesc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    long_desc: List[LongDesc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    auction_long_desc: List[AuctionLongDesc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    meta_title: List[MetaTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    meta_description: List[MetaDescription] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    meta_keywords: List[MetaKeywords] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    search_keywords: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )


@dataclass
class GroupByParameter:
    class Meta:
        name = "group_by_parameter"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    product_value: List[ProductValue] = field(
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


@dataclass
class Images:
    class Meta:
        name = "images"

    large: List[Large] = field(
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


@dataclass
class Parameters:
    class Meta:
        name = "parameters"

    section: List[Section] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    parameter: List[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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
    group_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    group_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    size_list: Optional[str] = field(
        default=None,
        metadata={
            "name": "sizeList",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )


@dataclass
class Bundled:
    class Meta:
        name = "bundled"

    product: List["Bundled.Product"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: Optional[BundledType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Product:
        sizes: List[Sizes] = field(
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
        quantity: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"(-1(.[0]+)?)|(\d+([\.,]\d+)?)",
            },
        )
        type_value: Optional[ProductType] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class Group:
    class Meta:
        name = "group"

    group_by_parameter: Optional[GroupByParameter] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    first_product_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    code_external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_first_product_id: Optional[str] = (
        field(
            default=None,
            metadata={
                "name": "first_product_id",
                "type": "Attribute",
                "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
            },
        )
    )
    first_product_code_producer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    first_product_code_external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    first_product_code_iai: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )


@dataclass
class Product:
    class Meta:
        name = "product"

    producer: List[Producer] = field(  #
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    category: List[Category] = field(  #
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    category_translation: List[CategoryTranslation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    category_idosell: List[CategoryIdosell] = field(  #
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    iai_category: List[IaiCategory] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_category_translation: List[IaiCategoryTranslation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    unit: List[Unit] = field(  #
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    unit_translation: List[UnitTranslation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    series: List[Series] = field(  #
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    series_translation: List[SeriesTranslation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    card: List[Card] = field(  #
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    card_translation: List[CardTranslation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    description: List[Description] = field(  #
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    price: List[Price] = field(  #
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
    strikethrough_retail_price: List[StrikethroughRetailPrice] = field(  #
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    strikethrough_wholesale_price: List[StrikethroughWholesalePrice] = field(  #
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_strikethrough_wholesale_price: List[
        ExtensionsStrikethroughWholesalePrice
    ] = field(
        default_factory=list,
        metadata={
            "name": "strikethrough_wholesale_price",
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
            "nillable": True,
        },
    )
    promotion: List[Promotion] = field(
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
    images: List[Images] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    warranty: List[Warranty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    warranty_translation: List[WarrantyTranslation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    parameters: List[Parameters] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    attachments: List[Attachments] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    group: List[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    bundled: List[Bundled] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    meta_title: List[MetaTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    sell_by: List[SellBy] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    sold_by: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    inwrapper: List[Inwrapper] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    sold_in_carton: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    availability_management: List[AvailabilityManagement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    prices_configuration_for_shops: List[PricesConfigurationForShops] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    prices_config: List[PricesConfig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    price_retail: List[PriceRetail] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    price_wholesale: List[PriceWholesale] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    price_minimal: List[PriceMinimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    price_automatic_calculation: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    pricecomparator_price: List[PricecomparatorPrice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    auction_price: List[AuctionPrice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    pos_prices_config: List[PosPricesConfig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    enable_in_pos: List[EnableInPos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    price_pos: List[PricePos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    hotspots: List[Hotspots] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    loyalty_program: List[LoyaltyProgram] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    taxcode: List[Taxcode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    delivery_time: List[DeliveryTime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    sum_in_basket: List[SumInBasket] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    visibility: List[Visibility] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    navigation: List[Navigation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    priority: List[Priority] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    availability: List[Availability] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    last_purchase_price: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    average_purchase_price: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    pricecomparator_name: List[PricecomparatorName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    associated_products: List[AssociatedProducts] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    availability_profile: List[AvailabilityProfile] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    advance: List[Advance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    size_chart: List[SizeChart] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    deliverer: List[Deliverer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_srp: List[ExtensionsSrp] = field(
        default_factory=list,
        metadata={
            "name": "srp",
            "type": "Element",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    type_value: Optional[ProductType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    code_on_card: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    producer_code_standard: Optional[ProductProducerCodeStandard] = field(
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
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    product_free: Optional[ProductFreeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    product_shipment_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    save_serial_numbers: Optional[SaveSerialNumbersValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    rebate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    iai_shop_com_developers_iof_extensions_phtml_site: Optional[str] = field(
        default=None,
        metadata={
            "name": "site",
            "type": "Attribute",
            "namespace": "http://www.iai-shop.com/developers/iof/extensions.phtml",
        },
    )
    site: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    removed: Optional[ProductRemoved] = field(
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
            "pattern": r"[A-Z]{3,3}",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-z]{3,3}",
        },
    )
    iof_translation_generated: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
            "required": True,
        },
    )
