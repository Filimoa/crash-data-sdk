# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...types import ppa_garaging_risk_score_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.garaging_risk_score_response import GaragingRiskScoreResponse

__all__ = ["PpaGaragingRiskScoresResource", "AsyncPpaGaragingRiskScoresResource"]


class PpaGaragingRiskScoresResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> PpaGaragingRiskScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Filimoa/crash-data-sdk#accessing-raw-response-data-eg-headers
        """
        return PpaGaragingRiskScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PpaGaragingRiskScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Filimoa/crash-data-sdk#with_streaming_response
        """
        return PpaGaragingRiskScoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        policy_holder_id: str,
        policy_start: Union[str, datetime],
        vehicles: Iterable[ppa_garaging_risk_score_create_params.Vehicle],
        version: Literal["v1"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GaragingRiskScoreResponse:
        """
        Calculate the risk score for a PPA policy with garaging data.

        Args:
          policy_holder_id: Unique identifier for the policyholder.

          policy_start: Start date of the policy.

          vehicles: List of vehicles with their garaging locations.

          version: Version of the risk scoring model used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/risk-score/ppa-garaging",
            body=maybe_transform(
                {
                    "policy_holder_id": policy_holder_id,
                    "policy_start": policy_start,
                    "vehicles": vehicles,
                    "version": version,
                },
                ppa_garaging_risk_score_create_params.PpaGaragingRiskScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GaragingRiskScoreResponse,
        )


class AsyncPpaGaragingRiskScoresResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPpaGaragingRiskScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Filimoa/crash-data-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPpaGaragingRiskScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPpaGaragingRiskScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Filimoa/crash-data-sdk#with_streaming_response
        """
        return AsyncPpaGaragingRiskScoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        policy_holder_id: str,
        policy_start: Union[str, datetime],
        vehicles: Iterable[ppa_garaging_risk_score_create_params.Vehicle],
        version: Literal["v1"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GaragingRiskScoreResponse:
        """
        Calculate the risk score for a PPA policy with garaging data.

        Args:
          policy_holder_id: Unique identifier for the policyholder.

          policy_start: Start date of the policy.

          vehicles: List of vehicles with their garaging locations.

          version: Version of the risk scoring model used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/risk-score/ppa-garaging",
            body=await async_maybe_transform(
                {
                    "policy_holder_id": policy_holder_id,
                    "policy_start": policy_start,
                    "vehicles": vehicles,
                    "version": version,
                },
                ppa_garaging_risk_score_create_params.PpaGaragingRiskScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GaragingRiskScoreResponse,
        )


class PpaGaragingRiskScoresResourceWithRawResponse:
    def __init__(self, ppa_garaging_risk_scores: PpaGaragingRiskScoresResource) -> None:
        self._ppa_garaging_risk_scores = ppa_garaging_risk_scores

        self.create = to_raw_response_wrapper(
            ppa_garaging_risk_scores.create,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._ppa_garaging_risk_scores.batch)


class AsyncPpaGaragingRiskScoresResourceWithRawResponse:
    def __init__(self, ppa_garaging_risk_scores: AsyncPpaGaragingRiskScoresResource) -> None:
        self._ppa_garaging_risk_scores = ppa_garaging_risk_scores

        self.create = async_to_raw_response_wrapper(
            ppa_garaging_risk_scores.create,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._ppa_garaging_risk_scores.batch)


class PpaGaragingRiskScoresResourceWithStreamingResponse:
    def __init__(self, ppa_garaging_risk_scores: PpaGaragingRiskScoresResource) -> None:
        self._ppa_garaging_risk_scores = ppa_garaging_risk_scores

        self.create = to_streamed_response_wrapper(
            ppa_garaging_risk_scores.create,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._ppa_garaging_risk_scores.batch)


class AsyncPpaGaragingRiskScoresResourceWithStreamingResponse:
    def __init__(self, ppa_garaging_risk_scores: AsyncPpaGaragingRiskScoresResource) -> None:
        self._ppa_garaging_risk_scores = ppa_garaging_risk_scores

        self.create = async_to_streamed_response_wrapper(
            ppa_garaging_risk_scores.create,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._ppa_garaging_risk_scores.batch)
