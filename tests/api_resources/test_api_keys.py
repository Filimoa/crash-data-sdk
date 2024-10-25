# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from crash_data_api import CrashDataAPI, AsyncCrashDataAPI
from crash_data_api.types import StatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: CrashDataAPI) -> None:
        api_key = client.api_keys.delete(
            "key_id",
        )
        assert_matches_type(StatusResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: CrashDataAPI) -> None:
        response = client.api_keys.with_raw_response.delete(
            "key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(StatusResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: CrashDataAPI) -> None:
        with client.api_keys.with_streaming_response.delete(
            "key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(StatusResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: CrashDataAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.api_keys.with_raw_response.delete(
                "",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncCrashDataAPI) -> None:
        api_key = await async_client.api_keys.delete(
            "key_id",
        )
        assert_matches_type(StatusResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCrashDataAPI) -> None:
        response = await async_client.api_keys.with_raw_response.delete(
            "key_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(StatusResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCrashDataAPI) -> None:
        async with async_client.api_keys.with_streaming_response.delete(
            "key_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(StatusResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCrashDataAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.api_keys.with_raw_response.delete(
                "",
            )
