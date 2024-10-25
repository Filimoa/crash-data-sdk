# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TelematicsRiskScoreResponse", "RiskScore", "RiskScoreDetails"]


class RiskScoreDetails(BaseModel):
    end: datetime
    """End time of the analyzed data period."""

    exposure_seconds: int
    """Total driving or exposure time in seconds."""

    num_trips: int
    """Total number of trips recorded."""

    start: datetime
    """Start time of the analyzed data period."""

    states: Optional[List[str]] = None
    """List of U.S. states where driving occurred, if available."""


class RiskScore(BaseModel):
    risk_score: float
    """Risk score for the vehicle."""

    vehicle_id: str
    """Unique identifier for the vehicle."""

    details: Optional[RiskScoreDetails] = None
    """Additional details about the risk score."""


class TelematicsRiskScoreResponse(BaseModel):
    aggregated_risk_score: float
    """Aggregated risk score for the policyholder. Weighted by exposure."""

    policy_holder_id: str
    """Unique identifier for the policyholder."""

    risk_scores: List[RiskScore]
    """Risk scores for each vehicle."""

    version: Optional[Literal["v1"]] = None
    """Version of the risk scoring model used."""
