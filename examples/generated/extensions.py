from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from pydantic.dataclasses import dataclass

from .xml import LangValue

__NAMESPACE__ = "http://www.iai-shop.com/developers/iof/extensions.phtml"


@dataclass
class Advance:
    class Meta:
        name = "advance"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    rate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AssociatedProducts:
    class Meta:
        name = "associated_products"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    product: List["AssociatedProducts.Product"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Product:
        id: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class AvailabilityManagement:
    class Meta:
        name = "availability_management"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AvailabilityProfile:
    class Meta:
        name = "availability_profile"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    id: Optional[int] = field(
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
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Deliverer:
    class Meta:
        name = "deliverer"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DeliveryTime:
    class Meta:
        name = "delivery_time"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    mode: List["DeliveryTime.Mode"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    time: List["DeliveryTime.Time"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Mode:
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
            },
        )

    @dataclass
    class Time:
        days: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


class EnableInPosEnabled(Enum):
    YES = "yes"
    NO = "no"


class FlagType(Enum):
    PROMOTION = "promotion"
    DISCOUNT = "discount"
    DISTINGUISHED = "distinguished"
    SPECIAL = "special"
    BESTSELLER = "bestseller"
    NEWPRODUCT = "newproduct"


class FlagVisible(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class IaiCategory:
    class Meta:
        name = "iai_category"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Icons:
    class Meta:
        name = "icons"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    auction_icon: List["Icons.AuctionIcon"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    group_icon: List["Icons.GroupIcon"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class AuctionIcon:
        url: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        date_changed: Optional[str] = field(
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

    @dataclass
    class GroupIcon:
        url: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        date_changed: Optional[str] = field(
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


@dataclass
class Inwrapper:
    class Meta:
        name = "inwrapper"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    quantity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Navigation:
    class Meta:
        name = "navigation"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["Navigation.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        menu: List["Navigation.Site.Menu"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

        @dataclass
        class Menu:
            item: List["Navigation.Site.Menu.Item"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                },
            )

            @dataclass
            class Item:
                textid: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    },
                )


@dataclass
class Note:
    class Meta:
        name = "note"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Price:
    class Meta:
        name = "price"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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
    normal_price: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    wholesale_price: Optional[str] = field(
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
    enabled: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    promotion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    discount: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    distinguished: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    special: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class PriceComparatorVisible(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class PriceMinimal:
    class Meta:
        name = "price_minimal"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["PriceMinimal.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        size_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
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
class PricePos:
    class Meta:
        name = "price_pos"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    price: List["PricePos.Price"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Price:
        size_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
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
class PriceRetail:
    class Meta:
        name = "price_retail"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["PriceRetail.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        size_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
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
class PriceWholesale:
    class Meta:
        name = "price_wholesale"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["PriceWholesale.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        size_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
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
class PricecomparatorPrice:
    class Meta:
        name = "pricecomparator_price"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["PricecomparatorPrice.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        service_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
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


class PricesConfigurationForShopsValue(Enum):
    COMPETITIVE_PRICES = "competitive_prices"
    SAME_PRICES = "same_prices"


@dataclass
class Priority:
    class Meta:
        name = "priority"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    level: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SellBy:
    class Meta:
        name = "sell_by"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    retail: List["SellBy.Retail"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    wholesale: List["SellBy.Wholesale"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Retail:
        quantity: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Wholesale:
        quantity: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


class SiteClients(Enum):
    RETAILERS = "retailers"
    WHOLESALERS = "wholesalers"
    BOTH = "both"
    NOBODY = "nobody"


class SiteManualConfig(Enum):
    YES = "yes"
    NO = "no"
    Y = "y"
    N = "n"


class SiteOperation(Enum):
    COUNT_COST = "count_cost"
    CLIENT_AWARD = "client_award"


class SitePriceType(Enum):
    BUY_NOW = "buy_now"
    MINIMAL = "minimal"
    START = "start"


class SiteType(Enum):
    WHOLESALE_EQUALS_RETAIL = "wholesale_equals_retail"
    WHOLESALE_NOTEQUALS_RETAIL = "wholesale_notequals_retail"
    ALL_PRICES_EQUALS_ZERO = "all_prices_equals_zero"
    RETAIL_PRICE_EQUALS_ZERO = "retail_price_equals_zero"
    RETAIL_EQUALS_SUGGESTED = "retail_equals_suggested"
    AUTOMATICALLY_CALCULATED = "automatically_calculated"
    DEFAULT_PRICES = "default_prices"
    ALL_PRICES_UNDEFINED = "all_prices_undefined"
    RETAIL_PRICE_UNDEFINED = "retail_price_undefined"


class SiteValue(Enum):
    YES = "yes"
    NO = "no"


class SiteVisible(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class Srp:
    class Meta:
        name = "srp"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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
class StrikethroughRetailPrice:
    class Meta:
        name = "strikethrough_retail_price"
        nillable = True
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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
class StrikethroughWholesalePrice:
    class Meta:
        name = "strikethrough_wholesale_price"
        nillable = True
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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


class SumInBasketValue(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class Taxcode:
    class Meta:
        name = "taxcode"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AuctionLongDesc:
    class Meta:
        name = "auction_long_desc"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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
class AuctionName:
    class Meta:
        name = "auction_name"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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
class AuctionPrice:
    class Meta:
        name = "auction_price"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["AuctionPrice.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        service_group_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        service_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        price_type: Optional[SitePriceType] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        size_id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
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
class Availability:
    class Meta:
        name = "availability"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["Availability.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        value: Optional[SiteValue] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class CardTranslation:
    class Meta:
        name = "card_translation"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CategoryIdosellTranslation:
    class Meta:
        name = "category_idosell_translation"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CategoryTranslation:
    class Meta:
        name = "category_translation"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EnableInPos:
    class Meta:
        name = "enable_in_pos"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    enabled: Optional[EnableInPosEnabled] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Hotspots:
    class Meta:
        name = "hotspots"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["Hotspots.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Site:
        flag: List["Hotspots.Site.Flag"] = field(
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
        manual_config: Optional[SiteManualConfig] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

        @dataclass
        class Flag:
            type_value: Optional[FlagType] = field(
                default=None,
                metadata={
                    "name": "type",
                    "type": "Attribute",
                },
            )
            visible: Optional[FlagVisible] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )


@dataclass
class IaiCategoryTranslation:
    class Meta:
        name = "iai_category_translation"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LoyaltyProgram:
    class Meta:
        name = "loyalty_program"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["LoyaltyProgram.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        operation: Optional[SiteOperation] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        clients: Optional[SiteClients] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        points: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class MetaDescription:
    class Meta:
        name = "meta_description"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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
class MetaKeywords:
    class Meta:
        name = "meta_keywords"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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
class MetaTitle:
    class Meta:
        name = "meta_title"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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
class PosPricesConfig:
    class Meta:
        name = "pos_prices_config"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["PosPricesConfig.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        price_type: Optional[SitePriceType] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class PricecomparatorName:
    class Meta:
        name = "pricecomparator_name"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

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
class PricesConfig:
    class Meta:
        name = "prices_config"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["PricesConfig.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Site:
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        type_value: Optional[SiteType] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class PricesConfigurationForShops:
    class Meta:
        name = "prices_configuration_for_shops"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    value: Optional[PricesConfigurationForShopsValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SeriesTranslation:
    class Meta:
        name = "series_translation"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SizeChart:
    class Meta:
        name = "size_chart"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    id: Optional[str] = field(
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SumInBasket:
    class Meta:
        name = "sum_in_basket"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    value: Optional[SumInBasketValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class UnitTranslation:
    class Meta:
        name = "unit_translation"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Visibility:
    class Meta:
        name = "visibility"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    site: List["Visibility.Site"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    price_comparator: List["Visibility.PriceComparator"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Site:
        visible: Optional[SiteVisible] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class PriceComparator:
        visible: Optional[PriceComparatorVisible] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class WarrantyTranslation:
    class Meta:
        name = "warranty_translation"
        namespace = "http://www.iai-shop.com/developers/iof/extensions.phtml"

    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
