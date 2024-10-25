# Shared Types

```python
from crash_data_api.types import (
    BatchJobStatus,
    GaragingRiskScoreResponse,
    TelematicsRiskScoreResponse,
)
```

# AggregatedCrashes

Types:

```python
from crash_data_api.types import AggregatedCrashesResponse
```

Methods:

- <code title="post /v1/crash-data/aggregate">client.aggregated_crashes.<a href="./src/crash_data_api/resources/aggregated_crashes/aggregated_crashes.py">aggregate</a>(\*\*<a href="src/crash_data_api/types/aggregated_crash_aggregate_params.py">params</a>) -> <a href="./src/crash_data_api/types/aggregated_crashes_response.py">AggregatedCrashesResponse</a></code>

## Batch

Types:

```python
from crash_data_api.types.aggregated_crashes import BatchResultsResponse
```

Methods:

- <code title="get /v1/crash-data/aggregate/batch/{job_id}/results">client.aggregated_crashes.batch.<a href="./src/crash_data_api/resources/aggregated_crashes/batch.py">results</a>(job_id) -> <a href="./src/crash_data_api/types/aggregated_crashes/batch_results_response.py">BatchResultsResponse</a></code>
- <code title="get /v1/crash-data/aggregate/batch/{job_id}/status">client.aggregated_crashes.batch.<a href="./src/crash_data_api/resources/aggregated_crashes/batch.py">status</a>(job_id) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>
- <code title="post /v1/crash-data/aggregate/batch">client.aggregated_crashes.batch.<a href="./src/crash_data_api/resources/aggregated_crashes/batch.py">submit</a>(\*\*<a href="src/crash_data_api/types/aggregated_crashes/batch_submit_params.py">params</a>) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>

# CaGaragingRiskScores

Methods:

- <code title="post /v1/risk-score/ca-garaging">client.ca_garaging_risk_scores.<a href="./src/crash_data_api/resources/ca_garaging_risk_scores/ca_garaging_risk_scores.py">calculate</a>(\*\*<a href="src/crash_data_api/types/ca_garaging_risk_score_calculate_params.py">params</a>) -> <a href="./src/crash_data_api/types/shared/garaging_risk_score_response.py">GaragingRiskScoreResponse</a></code>

## Batch

Types:

```python
from crash_data_api.types.ca_garaging_risk_scores import BatchResultsResponse
```

Methods:

- <code title="get /v1/risk-score/ca-garaging/batch/{job_id}/results">client.ca_garaging_risk_scores.batch.<a href="./src/crash_data_api/resources/ca_garaging_risk_scores/batch.py">results</a>(job_id) -> <a href="./src/crash_data_api/types/ca_garaging_risk_scores/batch_results_response.py">BatchResultsResponse</a></code>
- <code title="get /v1/risk-score/ca-garaging/batch/{job_id}/status">client.ca_garaging_risk_scores.batch.<a href="./src/crash_data_api/resources/ca_garaging_risk_scores/batch.py">status</a>(job_id) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>
- <code title="post /v1/risk-score/ca-garaging/batch">client.ca_garaging_risk_scores.batch.<a href="./src/crash_data_api/resources/ca_garaging_risk_scores/batch.py">submit</a>(\*\*<a href="src/crash_data_api/types/ca_garaging_risk_scores/batch_submit_params.py">params</a>) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>

# CaTelematicsRiskScores

Methods:

- <code title="post /v1/risk-score/ca-telematics">client.ca_telematics_risk_scores.<a href="./src/crash_data_api/resources/ca_telematics_risk_scores/ca_telematics_risk_scores.py">calculate</a>(\*\*<a href="src/crash_data_api/types/ca_telematics_risk_score_calculate_params.py">params</a>) -> <a href="./src/crash_data_api/types/shared/telematics_risk_score_response.py">TelematicsRiskScoreResponse</a></code>

## Batch

Types:

```python
from crash_data_api.types.ca_telematics_risk_scores import BatchResultsResponse
```

Methods:

- <code title="get /v1/risk-score/ca-telematics/batch/{job_id}/results">client.ca_telematics_risk_scores.batch.<a href="./src/crash_data_api/resources/ca_telematics_risk_scores/batch.py">results</a>(job_id) -> <a href="./src/crash_data_api/types/ca_telematics_risk_scores/batch_results_response.py">BatchResultsResponse</a></code>
- <code title="get /v1/risk-score/ca-telematics/batch/{job_id}/status">client.ca_telematics_risk_scores.batch.<a href="./src/crash_data_api/resources/ca_telematics_risk_scores/batch.py">status</a>(job_id) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>
- <code title="post /v1/risk-score/ca-telematics/batch">client.ca_telematics_risk_scores.batch.<a href="./src/crash_data_api/resources/ca_telematics_risk_scores/batch.py">submit</a>(\*\*<a href="src/crash_data_api/types/ca_telematics_risk_scores/batch_submit_params.py">params</a>) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>

# PpaGaragingRiskScores

Methods:

- <code title="post /v1/risk-score/ppa-garaging">client.ppa_garaging_risk_scores.<a href="./src/crash_data_api/resources/ppa_garaging_risk_scores/ppa_garaging_risk_scores.py">create</a>(\*\*<a href="src/crash_data_api/types/ppa_garaging_risk_score_create_params.py">params</a>) -> <a href="./src/crash_data_api/types/shared/garaging_risk_score_response.py">GaragingRiskScoreResponse</a></code>

## Batch

Types:

```python
from crash_data_api.types.ppa_garaging_risk_scores import BatchResultsResponse
```

Methods:

- <code title="post /v1/risk-score/ppa-garaging/batch">client.ppa_garaging_risk_scores.batch.<a href="./src/crash_data_api/resources/ppa_garaging_risk_scores/batch.py">create</a>(\*\*<a href="src/crash_data_api/types/ppa_garaging_risk_scores/batch_create_params.py">params</a>) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>
- <code title="get /v1/risk-score/ppa-garaging/batch/{job_id}/results">client.ppa_garaging_risk_scores.batch.<a href="./src/crash_data_api/resources/ppa_garaging_risk_scores/batch.py">results</a>(job_id) -> <a href="./src/crash_data_api/types/ppa_garaging_risk_scores/batch_results_response.py">BatchResultsResponse</a></code>
- <code title="get /v1/risk-score/ppa-garaging/batch/{job_id}/status">client.ppa_garaging_risk_scores.batch.<a href="./src/crash_data_api/resources/ppa_garaging_risk_scores/batch.py">status</a>(job_id) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>

# PpaTelematicsRiskScores

Methods:

- <code title="post /v1/risk-score/ppa-telematics">client.ppa_telematics_risk_scores.<a href="./src/crash_data_api/resources/ppa_telematics_risk_scores/ppa_telematics_risk_scores.py">create</a>(\*\*<a href="src/crash_data_api/types/ppa_telematics_risk_score_create_params.py">params</a>) -> <a href="./src/crash_data_api/types/shared/telematics_risk_score_response.py">TelematicsRiskScoreResponse</a></code>

## Batch

Types:

```python
from crash_data_api.types.ppa_telematics_risk_scores import BatchResultsResponse
```

Methods:

- <code title="post /v1/risk-score/ppa-telematics/batch">client.ppa_telematics_risk_scores.batch.<a href="./src/crash_data_api/resources/ppa_telematics_risk_scores/batch.py">create</a>(\*\*<a href="src/crash_data_api/types/ppa_telematics_risk_scores/batch_create_params.py">params</a>) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>
- <code title="get /v1/risk-score/ppa-telematics/batch/{job_id}/results">client.ppa_telematics_risk_scores.batch.<a href="./src/crash_data_api/resources/ppa_telematics_risk_scores/batch.py">results</a>(job_id) -> <a href="./src/crash_data_api/types/ppa_telematics_risk_scores/batch_results_response.py">BatchResultsResponse</a></code>
- <code title="get /v1/risk-score/ppa-telematics/batch/{job_id}/status">client.ppa_telematics_risk_scores.batch.<a href="./src/crash_data_api/resources/ppa_telematics_risk_scores/batch.py">status</a>(job_id) -> <a href="./src/crash_data_api/types/shared/batch_job_status.py">BatchJobStatus</a></code>

# APIKeys

Types:

```python
from crash_data_api.types import StatusResponse
```

Methods:

- <code title="delete /v1/api-key/{key_id}">client.api_keys.<a href="./src/crash_data_api/resources/api_keys.py">delete</a>(key_id) -> <a href="./src/crash_data_api/types/status_response.py">StatusResponse</a></code>
