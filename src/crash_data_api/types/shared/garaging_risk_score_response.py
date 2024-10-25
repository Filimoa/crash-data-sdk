# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GaragingRiskScoreResponse", "RiskScore"]


class RiskScore(BaseModel):
    risk_score: float
    """Risk score for the vehicle based on garaging location."""

    vehicle_id: str
    """Unique identifier for the vehicle."""


class GaragingRiskScoreResponse(BaseModel):
    aggregated_risk_score: float
    """Average risk score for the policyholder."""

    policy_holder_id: str
    """Unique identifier for the policyholder."""

    risk_scores: List[RiskScore]
    """Risk scores for each vehicle based on their garaging locations."""

    version: Optional[Literal["v1"]] = None
    """Version of the risk scoring model used."""
