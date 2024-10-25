# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "BatchSubmitParams",
    "Body",
    "BodyLocation",
    "BodyLocationLocationGps",
    "BodyLocationLocationAddress",
    "BodyLocationLocationStructuredAddress",
]


class BatchSubmitParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyLocationLocationGps(TypedDict, total=False):
    lat: Required[float]
    """Latitude range limited to U.S. boundaries (24.396308°N to 49.384358°N)"""

    long: Required[float]
    """Longitude range limited to U.S. boundaries (-125.0°W to -66.93457°W)"""

    coordinate_system: Literal["WGS84"]
    """Coordinate system used (World Geodetic System 1984)"""


class BodyLocationLocationAddress(TypedDict, total=False):
    address: Required[str]
    """A valid address to geocode. Minimum length of 5 characters."""


class BodyLocationLocationStructuredAddress(TypedDict, total=False):
    city: Required[str]
    """City name."""

    postal_code: Required[Optional[str]]
    """5 or 9 digit ZIP code."""

    state: Required[str]
    """State abbreviation."""

    street: Required[str]
    """Street name and number."""


BodyLocation: TypeAlias = Union[
    BodyLocationLocationGps, BodyLocationLocationAddress, BodyLocationLocationStructuredAddress
]


class Body(TypedDict, total=False):
    distance_km: Required[float]
    """Distance in kilometers from the location for aggregation (1-500 km)."""

    end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End date of the aggregation period."""

    location: Required[BodyLocation]
    """Address or GPS coordinates to center the aggregation on."""

    start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date of the aggregation period."""
