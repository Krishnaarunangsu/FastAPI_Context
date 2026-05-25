from pydantic import BaseModel
from typing import Optional


class NotificationRequest(BaseModel):
    type: str
    recipient: str
    message: str
    metadata: Optional[dict] = None