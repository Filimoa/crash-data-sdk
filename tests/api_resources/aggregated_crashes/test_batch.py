# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from crash_data_api import CrashDataAPI, AsyncCrashDataAPI
from crash_data_api._utils import parse_datetime
from crash_data_api.types.shared import BatchJobStatus
from crash_data_api.types.aggregated_crashes import BatchResultsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_results(self, client: CrashDataAPI) -> None:
        batch = client.aggregated_crashes.batch.results(
            "job_id",
        )
        assert_matches_type(BatchResultsResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_results(self, client: CrashDataAPI) -> None:
        response = client.aggregated_crashes.batch.with_raw_response.results(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResultsResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_results(self, client: CrashDataAPI) -> None:
        with client.aggregated_crashes.batch.with_streaming_response.results(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResultsResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_results(self, client: CrashDataAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.aggregated_crashes.batch.with_raw_response.results(
                "",
            )

    @parametrize
    def test_method_status(self, client: CrashDataAPI) -> None:
        batch = client.aggregated_crashes.batch.status(
            "job_id",
        )
        assert_matches_type(BatchJobStatus, batch, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: CrashDataAPI) -> None:
        response = client.aggregated_crashes.batch.with_raw_response.status(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchJobStatus, batch, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: CrashDataAPI) -> None:
        with client.aggregated_crashes.batch.with_streaming_response.status(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchJobStatus, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: CrashDataAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.aggregated_crashes.batch.with_raw_response.status(
                "",
            )

    @parametrize
    def test_method_submit(self, client: CrashDataAPI) -> None:
        batch = client.aggregated_crashes.batch.submit(
            body=[
                {
                    "distance_km": 2,
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert_matches_type(BatchJobStatus, batch, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: CrashDataAPI) -> None:
        response = client.aggregated_crashes.batch.with_raw_response.submit(
            body=[
                {
                    "distance_km": 2,
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchJobStatus, batch, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: CrashDataAPI) -> None:
        with client.aggregated_crashes.batch.with_streaming_response.submit(
            body=[
                {
                    "distance_km": 2,
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchJobStatus, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_results(self, async_client: AsyncCrashDataAPI) -> None:
        batch = await async_client.aggregated_crashes.batch.results(
            "job_id",
        )
        assert_matches_type(BatchResultsResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_results(self, async_client: AsyncCrashDataAPI) -> None:
        response = await async_client.aggregated_crashes.batch.with_raw_response.results(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResultsResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_results(self, async_client: AsyncCrashDataAPI) -> None:
        async with async_client.aggregated_crashes.batch.with_streaming_response.results(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResultsResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_results(self, async_client: AsyncCrashDataAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.aggregated_crashes.batch.with_raw_response.results(
                "",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncCrashDataAPI) -> None:
        batch = await async_client.aggregated_crashes.batch.status(
            "job_id",
        )
        assert_matches_type(BatchJobStatus, batch, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncCrashDataAPI) -> None:
        response = await async_client.aggregated_crashes.batch.with_raw_response.status(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchJobStatus, batch, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncCrashDataAPI) -> None:
        async with async_client.aggregated_crashes.batch.with_streaming_response.status(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchJobStatus, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncCrashDataAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.aggregated_crashes.batch.with_raw_response.status(
                "",
            )

    @parametrize
    async def test_method_submit(self, async_client: AsyncCrashDataAPI) -> None:
        batch = await async_client.aggregated_crashes.batch.submit(
            body=[
                {
                    "distance_km": 2,
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert_matches_type(BatchJobStatus, batch, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncCrashDataAPI) -> None:
        response = await async_client.aggregated_crashes.batch.with_raw_response.submit(
            body=[
                {
                    "distance_km": 2,
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchJobStatus, batch, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncCrashDataAPI) -> None:
        async with async_client.aggregated_crashes.batch.with_streaming_response.submit(
            body=[
                {
                    "distance_km": 2,
                    "end_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "location": {
                        "lat": 24.396308,
                        "long": -125,
                    },
                    "start_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchJobStatus, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
