# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CaGaragingRiskScoreCalculateParams",
    "Vehicle",
    "VehicleGaragingLocation",
    "VehicleGaragingLocationLocationGps",
    "VehicleGaragingLocationLocationAddress",
    "VehicleGaragingLocationLocationStructuredAddress",
]


class CaGaragingRiskScoreCalculateParams(TypedDict, total=False):
    policy_holder_id: Required[str]
    """Unique identifier for the policyholder."""

    policy_start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start date of the policy."""

    vehicles: Required[Iterable[Vehicle]]
    """List of vehicles with their garaging locations."""

    version: Literal["v1"]
    """Version of the risk scoring model used."""


class VehicleGaragingLocationLocationGps(TypedDict, total=False):
    lat: Required[float]
    """Latitude range limited to U.S. boundaries (24.396308°N to 49.384358°N)"""

    long: Required[float]
    """Longitude range limited to U.S. boundaries (-125.0°W to -66.93457°W)"""

    coordinate_system: Literal["WGS84"]
    """Coordinate system used (World Geodetic System 1984)"""


class VehicleGaragingLocationLocationAddress(TypedDict, total=False):
    address: Required[str]
    """A valid address to geocode. Minimum length of 5 characters."""


class VehicleGaragingLocationLocationStructuredAddress(TypedDict, total=False):
    city: Required[str]
    """City name."""

    postal_code: Required[Optional[str]]
    """5 or 9 digit ZIP code."""

    state: Required[str]
    """State abbreviation."""

    street: Required[str]
    """Street name and number."""


VehicleGaragingLocation: TypeAlias = Union[
    VehicleGaragingLocationLocationGps,
    VehicleGaragingLocationLocationAddress,
    VehicleGaragingLocationLocationStructuredAddress,
]


class Vehicle(TypedDict, total=False):
    garaging_location: Required[VehicleGaragingLocation]
    """Location where the vehicle is primarily garaged."""

    vehicle_id: Required[str]
    """Unique identifier for the vehicle."""
