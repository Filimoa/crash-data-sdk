# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import api_keys
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, CrashDataAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.aggregated_crashes import aggregated_crashes
from .resources.ca_garaging_risk_scores import ca_garaging_risk_scores
from .resources.ppa_garaging_risk_scores import ppa_garaging_risk_scores
from .resources.ca_telematics_risk_scores import ca_telematics_risk_scores
from .resources.ppa_telematics_risk_scores import ppa_telematics_risk_scores

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "CrashDataAPI",
    "AsyncCrashDataAPI",
    "Client",
    "AsyncClient",
]


class CrashDataAPI(SyncAPIClient):
    aggregated_crashes: aggregated_crashes.AggregatedCrashesResource
    ca_garaging_risk_scores: ca_garaging_risk_scores.CaGaragingRiskScoresResource
    ca_telematics_risk_scores: ca_telematics_risk_scores.CaTelematicsRiskScoresResource
    ppa_garaging_risk_scores: ppa_garaging_risk_scores.PpaGaragingRiskScoresResource
    ppa_telematics_risk_scores: ppa_telematics_risk_scores.PpaTelematicsRiskScoresResource
    api_keys: api_keys.APIKeysResource
    with_raw_response: CrashDataAPIWithRawResponse
    with_streaming_response: CrashDataAPIWithStreamedResponse

    # client options
    auth_token: str
    access_token: str

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous crash-data-api client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `auth_token` from `AUTH_TOKEN`
        - `access_token` from `ACCESS_TOKEN`
        """
        if auth_token is None:
            auth_token = os.environ.get("AUTH_TOKEN")
        if auth_token is None:
            raise CrashDataAPIError(
                "The auth_token client option must be set either by passing auth_token to the client or by setting the AUTH_TOKEN environment variable"
            )
        self.auth_token = auth_token

        if access_token is None:
            access_token = os.environ.get("ACCESS_TOKEN")
        if access_token is None:
            raise CrashDataAPIError(
                "The access_token client option must be set either by passing access_token to the client or by setting the ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("CRASH_DATA_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.matrisk.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.aggregated_crashes = aggregated_crashes.AggregatedCrashesResource(self)
        self.ca_garaging_risk_scores = ca_garaging_risk_scores.CaGaragingRiskScoresResource(self)
        self.ca_telematics_risk_scores = ca_telematics_risk_scores.CaTelematicsRiskScoresResource(self)
        self.ppa_garaging_risk_scores = ppa_garaging_risk_scores.PpaGaragingRiskScoresResource(self)
        self.ppa_telematics_risk_scores = ppa_telematics_risk_scores.PpaTelematicsRiskScoresResource(self)
        self.api_keys = api_keys.APIKeysResource(self)
        self.with_raw_response = CrashDataAPIWithRawResponse(self)
        self.with_streaming_response = CrashDataAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_token: str | None = None,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCrashDataAPI(AsyncAPIClient):
    aggregated_crashes: aggregated_crashes.AsyncAggregatedCrashesResource
    ca_garaging_risk_scores: ca_garaging_risk_scores.AsyncCaGaragingRiskScoresResource
    ca_telematics_risk_scores: ca_telematics_risk_scores.AsyncCaTelematicsRiskScoresResource
    ppa_garaging_risk_scores: ppa_garaging_risk_scores.AsyncPpaGaragingRiskScoresResource
    ppa_telematics_risk_scores: ppa_telematics_risk_scores.AsyncPpaTelematicsRiskScoresResource
    api_keys: api_keys.AsyncAPIKeysResource
    with_raw_response: AsyncCrashDataAPIWithRawResponse
    with_streaming_response: AsyncCrashDataAPIWithStreamedResponse

    # client options
    auth_token: str
    access_token: str

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async crash-data-api client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `auth_token` from `AUTH_TOKEN`
        - `access_token` from `ACCESS_TOKEN`
        """
        if auth_token is None:
            auth_token = os.environ.get("AUTH_TOKEN")
        if auth_token is None:
            raise CrashDataAPIError(
                "The auth_token client option must be set either by passing auth_token to the client or by setting the AUTH_TOKEN environment variable"
            )
        self.auth_token = auth_token

        if access_token is None:
            access_token = os.environ.get("ACCESS_TOKEN")
        if access_token is None:
            raise CrashDataAPIError(
                "The access_token client option must be set either by passing access_token to the client or by setting the ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("CRASH_DATA_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.matrisk.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.aggregated_crashes = aggregated_crashes.AsyncAggregatedCrashesResource(self)
        self.ca_garaging_risk_scores = ca_garaging_risk_scores.AsyncCaGaragingRiskScoresResource(self)
        self.ca_telematics_risk_scores = ca_telematics_risk_scores.AsyncCaTelematicsRiskScoresResource(self)
        self.ppa_garaging_risk_scores = ppa_garaging_risk_scores.AsyncPpaGaragingRiskScoresResource(self)
        self.ppa_telematics_risk_scores = ppa_telematics_risk_scores.AsyncPpaTelematicsRiskScoresResource(self)
        self.api_keys = api_keys.AsyncAPIKeysResource(self)
        self.with_raw_response = AsyncCrashDataAPIWithRawResponse(self)
        self.with_streaming_response = AsyncCrashDataAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_token: str | None = None,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CrashDataAPIWithRawResponse:
    def __init__(self, client: CrashDataAPI) -> None:
        self.aggregated_crashes = aggregated_crashes.AggregatedCrashesResourceWithRawResponse(client.aggregated_crashes)
        self.ca_garaging_risk_scores = ca_garaging_risk_scores.CaGaragingRiskScoresResourceWithRawResponse(
            client.ca_garaging_risk_scores
        )
        self.ca_telematics_risk_scores = ca_telematics_risk_scores.CaTelematicsRiskScoresResourceWithRawResponse(
            client.ca_telematics_risk_scores
        )
        self.ppa_garaging_risk_scores = ppa_garaging_risk_scores.PpaGaragingRiskScoresResourceWithRawResponse(
            client.ppa_garaging_risk_scores
        )
        self.ppa_telematics_risk_scores = ppa_telematics_risk_scores.PpaTelematicsRiskScoresResourceWithRawResponse(
            client.ppa_telematics_risk_scores
        )
        self.api_keys = api_keys.APIKeysResourceWithRawResponse(client.api_keys)


class AsyncCrashDataAPIWithRawResponse:
    def __init__(self, client: AsyncCrashDataAPI) -> None:
        self.aggregated_crashes = aggregated_crashes.AsyncAggregatedCrashesResourceWithRawResponse(
            client.aggregated_crashes
        )
        self.ca_garaging_risk_scores = ca_garaging_risk_scores.AsyncCaGaragingRiskScoresResourceWithRawResponse(
            client.ca_garaging_risk_scores
        )
        self.ca_telematics_risk_scores = ca_telematics_risk_scores.AsyncCaTelematicsRiskScoresResourceWithRawResponse(
            client.ca_telematics_risk_scores
        )
        self.ppa_garaging_risk_scores = ppa_garaging_risk_scores.AsyncPpaGaragingRiskScoresResourceWithRawResponse(
            client.ppa_garaging_risk_scores
        )
        self.ppa_telematics_risk_scores = (
            ppa_telematics_risk_scores.AsyncPpaTelematicsRiskScoresResourceWithRawResponse(
                client.ppa_telematics_risk_scores
            )
        )
        self.api_keys = api_keys.AsyncAPIKeysResourceWithRawResponse(client.api_keys)


class CrashDataAPIWithStreamedResponse:
    def __init__(self, client: CrashDataAPI) -> None:
        self.aggregated_crashes = aggregated_crashes.AggregatedCrashesResourceWithStreamingResponse(
            client.aggregated_crashes
        )
        self.ca_garaging_risk_scores = ca_garaging_risk_scores.CaGaragingRiskScoresResourceWithStreamingResponse(
            client.ca_garaging_risk_scores
        )
        self.ca_telematics_risk_scores = ca_telematics_risk_scores.CaTelematicsRiskScoresResourceWithStreamingResponse(
            client.ca_telematics_risk_scores
        )
        self.ppa_garaging_risk_scores = ppa_garaging_risk_scores.PpaGaragingRiskScoresResourceWithStreamingResponse(
            client.ppa_garaging_risk_scores
        )
        self.ppa_telematics_risk_scores = (
            ppa_telematics_risk_scores.PpaTelematicsRiskScoresResourceWithStreamingResponse(
                client.ppa_telematics_risk_scores
            )
        )
        self.api_keys = api_keys.APIKeysResourceWithStreamingResponse(client.api_keys)


class AsyncCrashDataAPIWithStreamedResponse:
    def __init__(self, client: AsyncCrashDataAPI) -> None:
        self.aggregated_crashes = aggregated_crashes.AsyncAggregatedCrashesResourceWithStreamingResponse(
            client.aggregated_crashes
        )
        self.ca_garaging_risk_scores = ca_garaging_risk_scores.AsyncCaGaragingRiskScoresResourceWithStreamingResponse(
            client.ca_garaging_risk_scores
        )
        self.ca_telematics_risk_scores = (
            ca_telematics_risk_scores.AsyncCaTelematicsRiskScoresResourceWithStreamingResponse(
                client.ca_telematics_risk_scores
            )
        )
        self.ppa_garaging_risk_scores = (
            ppa_garaging_risk_scores.AsyncPpaGaragingRiskScoresResourceWithStreamingResponse(
                client.ppa_garaging_risk_scores
            )
        )
        self.ppa_telematics_risk_scores = (
            ppa_telematics_risk_scores.AsyncPpaTelematicsRiskScoresResourceWithStreamingResponse(
                client.ppa_telematics_risk_scores
            )
        )
        self.api_keys = api_keys.AsyncAPIKeysResourceWithStreamingResponse(client.api_keys)


Client = CrashDataAPI

AsyncClient = AsyncCrashDataAPI
