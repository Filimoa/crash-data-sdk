# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...types import aggregated_crash_aggregate_params
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
from ...types.aggregated_crashes_response import AggregatedCrashesResponse

__all__ = ["AggregatedCrashesResource", "AsyncAggregatedCrashesResource"]


class AggregatedCrashesResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AggregatedCrashesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Filimoa/crash-data-sdk#accessing-raw-response-data-eg-headers
        """
        return AggregatedCrashesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AggregatedCrashesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Filimoa/crash-data-sdk#with_streaming_response
        """
        return AggregatedCrashesResourceWithStreamingResponse(self)

    def aggregate(
        self,
        *,
        distance_km: float,
        end_date: Union[str, datetime],
        location: aggregated_crash_aggregate_params.Location,
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AggregatedCrashesResponse:
        """Get aggregated crash statistics for a specific location and time period.

        Returns
        statistics within the specified radius.

        Args:
          distance_km: Distance in kilometers from the location for aggregation (1-500 km).

          end_date: End date of the aggregation period.

          location: Address or GPS coordinates to center the aggregation on.

          start_date: Start date of the aggregation period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/crash-data/aggregate",
            body=maybe_transform(
                {
                    "distance_km": distance_km,
                    "end_date": end_date,
                    "location": location,
                    "start_date": start_date,
                },
                aggregated_crash_aggregate_params.AggregatedCrashAggregateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AggregatedCrashesResponse,
        )


class AsyncAggregatedCrashesResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAggregatedCrashesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Filimoa/crash-data-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAggregatedCrashesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAggregatedCrashesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Filimoa/crash-data-sdk#with_streaming_response
        """
        return AsyncAggregatedCrashesResourceWithStreamingResponse(self)

    async def aggregate(
        self,
        *,
        distance_km: float,
        end_date: Union[str, datetime],
        location: aggregated_crash_aggregate_params.Location,
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AggregatedCrashesResponse:
        """Get aggregated crash statistics for a specific location and time period.

        Returns
        statistics within the specified radius.

        Args:
          distance_km: Distance in kilometers from the location for aggregation (1-500 km).

          end_date: End date of the aggregation period.

          location: Address or GPS coordinates to center the aggregation on.

          start_date: Start date of the aggregation period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/crash-data/aggregate",
            body=await async_maybe_transform(
                {
                    "distance_km": distance_km,
                    "end_date": end_date,
                    "location": location,
                    "start_date": start_date,
                },
                aggregated_crash_aggregate_params.AggregatedCrashAggregateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AggregatedCrashesResponse,
        )


class AggregatedCrashesResourceWithRawResponse:
    def __init__(self, aggregated_crashes: AggregatedCrashesResource) -> None:
        self._aggregated_crashes = aggregated_crashes

        self.aggregate = to_raw_response_wrapper(
            aggregated_crashes.aggregate,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._aggregated_crashes.batch)


class AsyncAggregatedCrashesResourceWithRawResponse:
    def __init__(self, aggregated_crashes: AsyncAggregatedCrashesResource) -> None:
        self._aggregated_crashes = aggregated_crashes

        self.aggregate = async_to_raw_response_wrapper(
            aggregated_crashes.aggregate,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._aggregated_crashes.batch)


class AggregatedCrashesResourceWithStreamingResponse:
    def __init__(self, aggregated_crashes: AggregatedCrashesResource) -> None:
        self._aggregated_crashes = aggregated_crashes

        self.aggregate = to_streamed_response_wrapper(
            aggregated_crashes.aggregate,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._aggregated_crashes.batch)


class AsyncAggregatedCrashesResourceWithStreamingResponse:
    def __init__(self, aggregated_crashes: AsyncAggregatedCrashesResource) -> None:
        self._aggregated_crashes = aggregated_crashes

        self.aggregate = async_to_streamed_response_wrapper(
            aggregated_crashes.aggregate,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._aggregated_crashes.batch)
