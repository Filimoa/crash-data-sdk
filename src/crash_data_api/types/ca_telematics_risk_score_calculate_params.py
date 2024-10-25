# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CaTelematicsRiskScoreCalculateParams", "Vehicle", "VehicleEvent", "VehicleEventLocation"]


class CaTelematicsRiskScoreCalculateParams(TypedDict, total=False):
    policy_holder_id: Required[str]
    """Unique identifier for the policyholder."""

    vehicles: Required[Iterable[Vehicle]]
    """List of vehicles with their telematics data."""

    version: Literal["v1"]
    """Version of the risk scoring model used."""


class VehicleEventLocation(TypedDict, total=False):
    lat: Required[float]
    """Latitude range limited to U.S. boundaries (24.396308°N to 49.384358°N)"""

    long: Required[float]
    """Longitude range limited to U.S. boundaries (-125.0°W to -66.93457°W)"""

    coordinate_system: Literal["WGS84"]
    """Coordinate system used (World Geodetic System 1984)"""


class VehicleEvent(TypedDict, total=False):
    location: Required[VehicleEventLocation]
    """Location of the event."""

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Exact date and time the event occurred."""


class Vehicle(TypedDict, total=False):
    events: Required[Iterable[VehicleEvent]]
    """Telematics events for the vehicle."""

    vehicle_id: Required[str]
    """Unique identifier for the vehicle."""
