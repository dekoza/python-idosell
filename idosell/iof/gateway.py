from decimal import Decimal

import pendulum
from pydantic import HttpUrl, conlist
from pydantic_xml.model import BaseXmlModel, element, attr, wrapped
import datetime as dt


class ShowcaseImage(BaseXmlModel, tag="showcase_image"):
    url: HttpUrl = attr()


class Address(BaseXmlModel, tag="address"):
    street: str | None = element(default=None)
    zipcode: str | None = element(default=None)
    city: str | None = element(default=None)
    country: str | None = element(default=None)
    province: str | None = element(default=None)


class Offer(BaseXmlModel, tag="offer"):
    created: dt.datetime | None = attr(default=None)
    expires: dt.datetime | None = attr(default=None)


class Time(BaseXmlModel, tag="time"):
    # offers: list[Offer]
    offers: conlist(Offer, min_length=2, max_length=2)


class Meta(BaseXmlModel, tag="meta"):
    long_name: str | None = element(default=None)
    short_name: str = element()
    showcase_image: ShowcaseImage | None = element(default=None)
    email: str = element()
    tel: str | None = element(default=None)
    fax: str | None = element(default=None)
    www: str | None = element(default=None)
    address: Address | None = element(default=None)
    time: Time


class HashChangedUrl(BaseXmlModel):
    url: HttpUrl = attr()
    hash: str = attr()
    changed: dt.datetime | None = attr(default=None)


class Change(HashChangedUrl, tag="change"):
    pass


class LinkedFull(HashChangedUrl, tag="full"):
    changes: list[Change] = wrapped("changes", element(tag="change"))


class Gateway(BaseXmlModel, tag="provider_description", search_mode="unordered"):
    file_format: str | None = attr(default="IOF")
    version: Decimal | None = attr(default=Decimal("3.0"))
    generated_by: str | None = attr(default=None)
    generated: dt.datetime | None = attr(default_factory=pendulum.now)
    meta: Meta
    full: LinkedFull | None = element(default=None)
    light: HashChangedUrl | None = element(default=None)
    categories: HashChangedUrl
    sizes: HashChangedUrl | None = element(default=None)
    producers: HashChangedUrl | None = element(default=None)
    units: HashChangedUrl | None = element(default=None)
    parameters: HashChangedUrl | None = element(default=None)
    stocks: HashChangedUrl | None = element(default=None)
    series: HashChangedUrl | None = element(default=None)
    warranties: HashChangedUrl | None = element(default=None)
    preset: HashChangedUrl | None = element(default=None)
