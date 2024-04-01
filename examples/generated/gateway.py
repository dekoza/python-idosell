from dataclasses import field
from decimal import Decimal
from typing import List, Optional

from pydantic.dataclasses import dataclass


@dataclass
class Categories:
    """
    :ivar url: URL: to the categories.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "categories"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class Change:
    """
    :ivar url: URL: to the full.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "change"
        nillable = True

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class City:
    """
    Provider's city.
    """

    class Meta:
        name = "city"
        nillable = True

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Country:
    """
    Provider's country.
    """

    class Meta:
        name = "country"
        nillable = True

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Email:
    """
    Provider's adress emial.
    """

    class Meta:
        name = "email"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Fax:
    """
    Provider's fax number.
    """

    class Meta:
        name = "fax"
        nillable = True

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Light:
    """
    :ivar url: URL: to the light.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "light"
        nillable = True

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    changed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class LongName:
    """Provider's long name.

    Only white-spaces can be used and a-z,A-Z,_,- range chars
    """

    class Meta:
        name = "long_name"
        nillable = True

    value: Optional[str] = field(
        default="",
        metadata={
            "pattern": r"[a-zA-Z0-9_ \-]+",
            "nillable": True,
        },
    )


@dataclass
class Parameters:
    """
    :ivar url: URL: to the parameters.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "parameters"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class Preset:
    """
    :ivar url: URL: to the preset.xml offer file. File generated by
        additional applications.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "preset"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class Producers:
    """
    :ivar url: URL: to the producers.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "producers"
        nillable = True

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class Province:
    """
    Provider's province.
    """

    class Meta:
        name = "province"
        nillable = True

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Series:
    """
    :ivar url: URL: to the series.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "series"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class ShortName:
    """Provider's short name.

    Only white-spaces can be used and a-z,A-Z,_,- range chars
    """

    class Meta:
        name = "short_name"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[a-zA-Z0-9_ \-]+",
        },
    )


@dataclass
class ShowcaseImage:
    """
    :ivar url: URL to supplier's logo. Formats: JPG/JPEG, GIF, PNG
    :ivar hash:
    :ivar date_changed:
    """

    class Meta:
        name = "showcase_image"
        nillable = True

    url: Optional[str] = field(
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
    date_changed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class Sizes:
    """
    :ivar url: URL: to the sizes.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "sizes"
        nillable = True

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class Stocks:
    """
    :ivar url: URL: to the stocks.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "stocks"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class Street:
    """
    Provider's street.
    """

    class Meta:
        name = "street"
        nillable = True

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Tel:
    """
    Provider's telephone number.
    """

    class Meta:
        name = "tel"
        nillable = True

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Time:
    class Meta:
        name = "time"

    offer: List["Time.Offer"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 2,
            "nillable": True,
        },
    )

    @dataclass
    class Offer:
        created: Optional[str] = field(
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
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class Units:
    """
    :ivar url: URL: to the units.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "units"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class Warranties:
    """
    :ivar url: URL: to the warranties.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "warranties"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class Www:
    """
    Provider's WWW site.
    """

    class Meta:
        name = "www"
        nillable = True

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Zipcode:
    """
    Provider's zip code.
    """

    class Meta:
        name = "zipcode"
        nillable = True

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Address:
    """
    Holds basic information about given provider's location.
    """

    class Meta:
        name = "address"
        nillable = True

    street: List[Street] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    zipcode: List[Zipcode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    city: List[City] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    country: List[Country] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    province: List[Province] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class Changes:
    class Meta:
        name = "changes"

    change: List[Change] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )


@dataclass
class Full:
    """
    :ivar changes:
    :ivar url: URL: to the full.xml offer file.
    :ivar hash: HASH: calculated MD5 value of the offer file
    :ivar changed: Last modifie: the date of the last modification of
        the offer file
    """

    class Meta:
        name = "full"
        nillable = True

    changes: List[Changes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    hash: Optional[str] = field(
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
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )


@dataclass
class MetaType:
    """
    Metadata describing the provider.
    """

    class Meta:
        name = "meta"

    long_name: Optional[LongName] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    short_name: Optional[ShortName] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    showcase_image: Optional[ShowcaseImage] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    email: Optional[Email] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    tel: Optional[Tel] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    fax: Optional[Fax] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    www: Optional[Www] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    time: Optional[Time] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ProviderDescription:
    """Internet Offer Format 3.0 (https://www.idosell.com/pl/shop/developers/formats/iof/internet-offer-format-iof).
    Describes the gateway.xml file.
    It is the main file needed to fetch all data relating to provider.
    It holds address, short name and URLs to other data files, such as full.xml, light.xml, categories.xml and sizes.xml. These files are required by the IOF 3.0 format.

    :ivar meta:
    :ivar full:
    :ivar light:
    :ivar categories:
    :ivar sizes:
    :ivar producers:
    :ivar units:
    :ivar parameters:
    :ivar stocks:
    :ivar series:
    :ivar warranties:
    :ivar preset:
    :ivar file_format: Format: IOF
    :ivar version: IOF version: major.minor
    :ivar generated: Date generated: YYYY-MM-DD 00:00:00
    :ivar generated_by: Generated by: information about the application
        from which the offer was generated
    """

    class Meta:
        name = "provider_description"

    meta: Optional[MetaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    full: Optional[Full] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    light: Optional[Light] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    categories: Optional[Categories] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sizes: Optional[Sizes] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    producers: Optional[Producers] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        },
    )
    units: Optional[Units] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    stocks: Optional[Stocks] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    series: Optional[Series] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    warranties: Optional[Warranties] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    preset: Optional[Preset] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    file_format: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([0-9]{4}[\-|\.][0-9]{2}[\-|\.][0-9]{2}[T| ]?[0-9]{2}:[0-9]{2}:[0-9]{2})((\+[0-9]{2}:[0-9]{2})|Z)?",
        },
    )
    generated_by: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
