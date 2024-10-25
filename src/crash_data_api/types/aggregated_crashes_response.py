# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AggregatedCrashesResponse"]


class AggregatedCrashesResponse(BaseModel):
    distance_km: float
    """Distance in kilometers from the central location."""

    end_date: datetime
    """End date of the aggregation."""

    lat: float
    """Latitude of the central location."""

    long: float
    """Longitude of the central location."""

    start_date: datetime
    """Start date of the aggregation."""

    total_crashes: int
    """Total number of crashes."""

    total_fatalities: int
    """Total number of fatalities."""

    total_injuries: int
    """Total number of injuries."""
