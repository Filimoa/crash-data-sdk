# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.garaging_risk_score_response import GaragingRiskScoreResponse

__all__ = ["BatchResultsResponse"]

BatchResultsResponse: TypeAlias = List[GaragingRiskScoreResponse]
