from dataclasses import field
from decimal import Decimal
from typing import Optional

from pydantic.dataclasses import dataclass
from xsdata.models.datatype import XmlDateTime


@dataclass
class Preset:
    """
    :ivar long_name:
    :ivar short_name:
    :ivar showcase_image_url:
    :ivar description:
    :ivar email:
    :ivar tel:
    :ivar fax:
    :ivar www:
    :ivar address_street:
    :ivar address_zipcode:
    :ivar address_city:
    :ivar address_country:
    :ivar currency:
    :ivar url:
    :ivar full:
    :ivar light:
    :ivar categories:
    :ivar sizes:
    :ivar categories_auto_mapping:
    :ivar selected:
    :ivar remote_gateway:
    :ivar fully_configured:
    :ivar external_program:
    :ivar external_program_xml_path:
    :ivar producers:
    :ivar units:
    :ivar parameters:
    :ivar stocks:
    :ivar series:
    :ivar traits:
    :ivar sizes_auto_mapping:
    :ivar series_auto_mapping:
    :ivar units_auto_mapping:
    :ivar size_code_prefix:
    :ivar old_size_code_prefix:
    :ivar size_code_producer_prefix:
    :ivar old_size_code_producer_prefix:
    :ivar iai_shop_deliverer_id:
    :ivar plugin_id:
    :ivar size_code_auto:
    :ivar size_code_code_size:
    :ivar update_name:
    :ivar update_short_description:
    :ivar update_long_description:
    :ivar update_version_name:
    :ivar update_series:
    :ivar update_producer:
    :ivar update_category:
    :ivar update_unit:
    :ivar update_price:
    :ivar update_icon:
    :ivar update_images:
    :ivar update_quantities:
    :ivar products_allowed_operations:
    :ivar update_code_producer:
    :ivar update_deliverer:
    :ivar version_mode:
    :ivar debug_product_import:
    :ivar debug_product_update:
    :ivar debug_product_always_import:
    :ivar debug_product_always_update:
    :ivar gateway_generated_on:
    :ivar full_last_modified:
    :ivar light_last_modified:
    :ivar categories_last_modified:
    :ivar sizes_last_modified:
    :ivar producers_last_modified:
    :ivar units_last_modified:
    :ivar series_last_modified:
    :ivar warranties_last_modified:
    :ivar provider_image_last_modified:
    :ivar image_hash:
    :ivar offer_created:
    :ivar offer_expires:
    :ivar categories_xml_generated:
    :ivar producers_xml_generated:
    :ivar series_xml_generated:
    :ivar sizes_xml_generated:
    :ivar units_xml_generated:
    :ivar warranties_xml_generated:
    :ivar full_xml_generated:
    :ivar light_xml_generated:
    :ivar warranties:
    :ivar cloned_products_mode:
    :ivar update_ext_sys_code_pending:
    :ivar overwrite_products:
    :ivar update_weight:
    :ivar update_visibility:
    :ivar srp_price:
    :ivar stp_price:
    :ivar offer_from_bridge:
    :ivar update_size:
    :ivar culture_info:
    :ivar file_format: Format: IOF
    :ivar version: IOF version: major.minor
    :ivar generated: Date generated: YYYY-MM-DD 00:00:00
    """

    class Meta:
        name = "preset"

    long_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    showcase_image_url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    tel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    www: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    address_street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    address_zipcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    address_city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    address_country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    full: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    light: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    categories: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sizes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    categories_auto_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    selected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    remote_gateway: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    fully_configured: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    external_program: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    external_program_xml_path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    producers: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameters: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    stocks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    traits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sizes_auto_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    series_auto_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    units_auto_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_code_prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    old_size_code_prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_code_producer_prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    old_size_code_producer_prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    iai_shop_deliverer_id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    plugin_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_code_auto: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    size_code_code_size: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_name: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_short_description: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_long_description: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_version_name: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_series: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_producer: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_category: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_unit: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_price: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_icon: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_images: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_quantities: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    products_allowed_operations: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_code_producer: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_deliverer: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    version_mode: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    debug_product_import: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    debug_product_update: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    debug_product_always_import: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    debug_product_always_update: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    gateway_generated_on: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "gatewayGeneratedOn",
            "type": "Element",
            "namespace": "",
        },
    )
    full_last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "full_lastModified",
            "type": "Element",
            "namespace": "",
        },
    )
    light_last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "light_lastModified",
            "type": "Element",
            "namespace": "",
        },
    )
    categories_last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "categories_lastModified",
            "type": "Element",
            "namespace": "",
        },
    )
    sizes_last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "sizes_lastModified",
            "type": "Element",
            "namespace": "",
        },
    )
    producers_last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "producers_lastModified",
            "type": "Element",
            "namespace": "",
        },
    )
    units_last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "units_lastModified",
            "type": "Element",
            "namespace": "",
        },
    )
    series_last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "series_lastModified",
            "type": "Element",
            "namespace": "",
        },
    )
    warranties_last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "warranties_lastModified",
            "type": "Element",
            "namespace": "",
        },
    )
    provider_image_last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "providerImageLastModified",
            "type": "Element",
            "namespace": "",
        },
    )
    image_hash: Optional[str] = field(
        default=None,
        metadata={
            "name": "imageHash",
            "type": "Element",
            "namespace": "",
        },
    )
    offer_created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "offerCreated",
            "type": "Element",
            "namespace": "",
        },
    )
    offer_expires: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "offerExpires",
            "type": "Element",
            "namespace": "",
        },
    )
    categories_xml_generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    producers_xml_generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    series_xml_generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sizes_xml_generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    units_xml_generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    warranties_xml_generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    full_xml_generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    light_xml_generated: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    warranties: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    cloned_products_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "clonedProductsMode",
            "type": "Element",
            "namespace": "",
        },
    )
    update_ext_sys_code_pending: Optional[int] = field(
        default=None,
        metadata={
            "name": "updateExtSysCodePending",
            "type": "Element",
            "namespace": "",
        },
    )
    overwrite_products: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_weight: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_visibility: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    srp_price: Optional[int] = field(
        default=None,
        metadata={
            "name": "SRP_price",
            "type": "Element",
            "namespace": "",
        },
    )
    stp_price: Optional[int] = field(
        default=None,
        metadata={
            "name": "STP_price",
            "type": "Element",
            "namespace": "",
        },
    )
    offer_from_bridge: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    update_size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    culture_info: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}",
        },
    )
