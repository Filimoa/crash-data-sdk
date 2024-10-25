# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from crash_data_api import CrashDataAPI, AsyncCrashDataAPI
from crash_data_api._utils import parse_datetime
from crash_data_api.types.shared import GaragingRiskScoreResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCaGaragingRiskScores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_calculate(self, client: CrashDataAPI) -> None:
        ca_garaging_risk_score = client.ca_garaging_risk_scores.calculate(
            policy_holder_id="policy-holder-123",
            policy_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            vehicles=[
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
            ],
        )
        assert_matches_type(GaragingRiskScoreResponse, ca_garaging_risk_score, path=["response"])

    @parametrize
    def test_method_calculate_with_all_params(self, client: CrashDataAPI) -> None:
        ca_garaging_risk_score = client.ca_garaging_risk_scores.calculate(
            policy_holder_id="policy-holder-123",
            policy_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            vehicles=[
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                        "coordinate_system": "WGS84",
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                        "coordinate_system": "WGS84",
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                        "coordinate_system": "WGS84",
                    },
                    "vehicle_id": "vehicle-123",
                },
            ],
            version="v1",
        )
        assert_matches_type(GaragingRiskScoreResponse, ca_garaging_risk_score, path=["response"])

    @parametrize
    def test_raw_response_calculate(self, client: CrashDataAPI) -> None:
        response = client.ca_garaging_risk_scores.with_raw_response.calculate(
            policy_holder_id="policy-holder-123",
            policy_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            vehicles=[
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ca_garaging_risk_score = response.parse()
        assert_matches_type(GaragingRiskScoreResponse, ca_garaging_risk_score, path=["response"])

    @parametrize
    def test_streaming_response_calculate(self, client: CrashDataAPI) -> None:
        with client.ca_garaging_risk_scores.with_streaming_response.calculate(
            policy_holder_id="policy-holder-123",
            policy_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            vehicles=[
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ca_garaging_risk_score = response.parse()
            assert_matches_type(GaragingRiskScoreResponse, ca_garaging_risk_score, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCaGaragingRiskScores:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_calculate(self, async_client: AsyncCrashDataAPI) -> None:
        ca_garaging_risk_score = await async_client.ca_garaging_risk_scores.calculate(
            policy_holder_id="policy-holder-123",
            policy_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            vehicles=[
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
            ],
        )
        assert_matches_type(GaragingRiskScoreResponse, ca_garaging_risk_score, path=["response"])

    @parametrize
    async def test_method_calculate_with_all_params(self, async_client: AsyncCrashDataAPI) -> None:
        ca_garaging_risk_score = await async_client.ca_garaging_risk_scores.calculate(
            policy_holder_id="policy-holder-123",
            policy_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            vehicles=[
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                        "coordinate_system": "WGS84",
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                        "coordinate_system": "WGS84",
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                        "coordinate_system": "WGS84",
                    },
                    "vehicle_id": "vehicle-123",
                },
            ],
            version="v1",
        )
        assert_matches_type(GaragingRiskScoreResponse, ca_garaging_risk_score, path=["response"])

    @parametrize
    async def test_raw_response_calculate(self, async_client: AsyncCrashDataAPI) -> None:
        response = await async_client.ca_garaging_risk_scores.with_raw_response.calculate(
            policy_holder_id="policy-holder-123",
            policy_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            vehicles=[
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ca_garaging_risk_score = await response.parse()
        assert_matches_type(GaragingRiskScoreResponse, ca_garaging_risk_score, path=["response"])

    @parametrize
    async def test_streaming_response_calculate(self, async_client: AsyncCrashDataAPI) -> None:
        async with async_client.ca_garaging_risk_scores.with_streaming_response.calculate(
            policy_holder_id="policy-holder-123",
            policy_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            vehicles=[
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
                {
                    "garaging_location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "vehicle_id": "vehicle-123",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ca_garaging_risk_score = await response.parse()
            assert_matches_type(GaragingRiskScoreResponse, ca_garaging_risk_score, path=["response"])

        assert cast(Any, response.is_closed) is True
