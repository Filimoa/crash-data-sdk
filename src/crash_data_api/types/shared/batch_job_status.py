# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BatchJobStatus"]


class BatchJobStatus(BaseModel):
    job_id: str
    """Unique identifier for the batch job"""

    status: Literal["processing", "completed", "failed"]
    """Current status of the job"""

    error_message: Optional[str] = None
    """Error message if job failed"""
