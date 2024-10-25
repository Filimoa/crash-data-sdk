# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..aggregated_crashes_response import AggregatedCrashesResponse

__all__ = ["BatchResultsResponse"]

BatchResultsResponse: TypeAlias = List[AggregatedCrashesResponse]
