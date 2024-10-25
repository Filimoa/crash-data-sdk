# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from crash_data_api import CrashDataAPI, AsyncCrashDataAPI
from crash_data_api.types import AggregatedCrashesResponse
from crash_data_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAggregatedCrashes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_aggregate(self, client: CrashDataAPI) -> None:
        aggregated_crash = client.aggregated_crashes.aggregate(
            distance_km=2,
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location={
                "lat": 24.396308,
                "long": -125,
            },
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AggregatedCrashesResponse, aggregated_crash, path=["response"])

    @parametrize
    def test_method_aggregate_with_all_params(self, client: CrashDataAPI) -> None:
        aggregated_crash = client.aggregated_crashes.aggregate(
            distance_km=2,
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location={
                "lat": 24.396308,
                "long": -125,
                "coordinate_system": "WGS84",
            },
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AggregatedCrashesResponse, aggregated_crash, path=["response"])

    @parametrize
    def test_raw_response_aggregate(self, client: CrashDataAPI) -> None:
        response = client.aggregated_crashes.with_raw_response.aggregate(
            distance_km=2,
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location={
                "lat": 24.396308,
                "long": -125,
            },
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregated_crash = response.parse()
        assert_matches_type(AggregatedCrashesResponse, aggregated_crash, path=["response"])

    @parametrize
    def test_streaming_response_aggregate(self, client: CrashDataAPI) -> None:
        with client.aggregated_crashes.with_streaming_response.aggregate(
            distance_km=2,
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location={
                "lat": 24.396308,
                "long": -125,
            },
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregated_crash = response.parse()
            assert_matches_type(AggregatedCrashesResponse, aggregated_crash, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAggregatedCrashes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_aggregate(self, async_client: AsyncCrashDataAPI) -> None:
        aggregated_crash = await async_client.aggregated_crashes.aggregate(
            distance_km=2,
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location={
                "lat": 24.396308,
                "long": -125,
            },
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AggregatedCrashesResponse, aggregated_crash, path=["response"])

    @parametrize
    async def test_method_aggregate_with_all_params(self, async_client: AsyncCrashDataAPI) -> None:
        aggregated_crash = await async_client.aggregated_crashes.aggregate(
            distance_km=2,
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location={
                "lat": 24.396308,
                "long": -125,
                "coordinate_system": "WGS84",
            },
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AggregatedCrashesResponse, aggregated_crash, path=["response"])

    @parametrize
    async def test_raw_response_aggregate(self, async_client: AsyncCrashDataAPI) -> None:
        response = await async_client.aggregated_crashes.with_raw_response.aggregate(
            distance_km=2,
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location={
                "lat": 24.396308,
                "long": -125,
            },
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregated_crash = await response.parse()
        assert_matches_type(AggregatedCrashesResponse, aggregated_crash, path=["response"])

    @parametrize
    async def test_streaming_response_aggregate(self, async_client: AsyncCrashDataAPI) -> None:
        async with async_client.aggregated_crashes.with_streaming_response.aggregate(
            distance_km=2,
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            location={
                "lat": 24.396308,
                "long": -125,
            },
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregated_crash = await response.parse()
            assert_matches_type(AggregatedCrashesResponse, aggregated_crash, path=["response"])

        assert cast(Any, response.is_closed) is True
