# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
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
from ...types import ppa_telematics_risk_score_create_params
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
from ...types.shared.telematics_risk_score_response import TelematicsRiskScoreResponse

__all__ = ["PpaTelematicsRiskScoresResource", "AsyncPpaTelematicsRiskScoresResource"]


class PpaTelematicsRiskScoresResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> PpaTelematicsRiskScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/crash-data-api-python#accessing-raw-response-data-eg-headers
        """
        return PpaTelematicsRiskScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PpaTelematicsRiskScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/crash-data-api-python#with_streaming_response
        """
        return PpaTelematicsRiskScoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        policy_holder_id: str,
        vehicles: Iterable[ppa_telematics_risk_score_create_params.Vehicle],
        version: Literal["v1"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelematicsRiskScoreResponse:
        """
        Calculate the risk score for a PPA policy with telematics data.

        Args:
          policy_holder_id: Unique identifier for the policyholder.

          vehicles: List of vehicles with their telematics data.

          version: Version of the risk scoring model used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/risk-score/ppa-telematics",
            body=maybe_transform(
                {
                    "policy_holder_id": policy_holder_id,
                    "vehicles": vehicles,
                    "version": version,
                },
                ppa_telematics_risk_score_create_params.PpaTelematicsRiskScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelematicsRiskScoreResponse,
        )


class AsyncPpaTelematicsRiskScoresResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPpaTelematicsRiskScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/crash-data-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPpaTelematicsRiskScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPpaTelematicsRiskScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/crash-data-api-python#with_streaming_response
        """
        return AsyncPpaTelematicsRiskScoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        policy_holder_id: str,
        vehicles: Iterable[ppa_telematics_risk_score_create_params.Vehicle],
        version: Literal["v1"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelematicsRiskScoreResponse:
        """
        Calculate the risk score for a PPA policy with telematics data.

        Args:
          policy_holder_id: Unique identifier for the policyholder.

          vehicles: List of vehicles with their telematics data.

          version: Version of the risk scoring model used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/risk-score/ppa-telematics",
            body=await async_maybe_transform(
                {
                    "policy_holder_id": policy_holder_id,
                    "vehicles": vehicles,
                    "version": version,
                },
                ppa_telematics_risk_score_create_params.PpaTelematicsRiskScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelematicsRiskScoreResponse,
        )


class PpaTelematicsRiskScoresResourceWithRawResponse:
    def __init__(self, ppa_telematics_risk_scores: PpaTelematicsRiskScoresResource) -> None:
        self._ppa_telematics_risk_scores = ppa_telematics_risk_scores

        self.create = to_raw_response_wrapper(
            ppa_telematics_risk_scores.create,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._ppa_telematics_risk_scores.batch)


class AsyncPpaTelematicsRiskScoresResourceWithRawResponse:
    def __init__(self, ppa_telematics_risk_scores: AsyncPpaTelematicsRiskScoresResource) -> None:
        self._ppa_telematics_risk_scores = ppa_telematics_risk_scores

        self.create = async_to_raw_response_wrapper(
            ppa_telematics_risk_scores.create,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._ppa_telematics_risk_scores.batch)


class PpaTelematicsRiskScoresResourceWithStreamingResponse:
    def __init__(self, ppa_telematics_risk_scores: PpaTelematicsRiskScoresResource) -> None:
        self._ppa_telematics_risk_scores = ppa_telematics_risk_scores

        self.create = to_streamed_response_wrapper(
            ppa_telematics_risk_scores.create,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._ppa_telematics_risk_scores.batch)


class AsyncPpaTelematicsRiskScoresResourceWithStreamingResponse:
    def __init__(self, ppa_telematics_risk_scores: AsyncPpaTelematicsRiskScoresResource) -> None:
        self._ppa_telematics_risk_scores = ppa_telematics_risk_scores

        self.create = async_to_streamed_response_wrapper(
            ppa_telematics_risk_scores.create,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._ppa_telematics_risk_scores.batch)
