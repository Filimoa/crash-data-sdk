# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatchSubmitParams", "Body", "BodyVehicle", "BodyVehicleEvent", "BodyVehicleEventLocation"]


class BatchSubmitParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyVehicleEventLocation(TypedDict, total=False):
    lat: Required[float]
    """Latitude range limited to U.S. boundaries (24.396308°N to 49.384358°N)"""

    long: Required[float]
    """Longitude range limited to U.S. boundaries (-125.0°W to -66.93457°W)"""

    coordinate_system: Literal["WGS84"]
    """Coordinate system used (World Geodetic System 1984)"""


class BodyVehicleEvent(TypedDict, total=False):
    location: Required[BodyVehicleEventLocation]
    """Location of the event."""

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Exact date and time the event occurred."""


class BodyVehicle(TypedDict, total=False):
    events: Required[Iterable[BodyVehicleEvent]]
    """Telematics events for the vehicle."""

    vehicle_id: Required[str]
    """Unique identifier for the vehicle."""


class Body(TypedDict, total=False):
    policy_holder_id: Required[str]
    """Unique identifier for the policyholder."""

    vehicles: Required[Iterable[BodyVehicle]]
    """List of vehicles with their telematics data."""

    version: Literal["v1"]
    """Version of the risk scoring model used."""
