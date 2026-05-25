from pydantic import BaseModel
from typing import Optional

class NotificationResponse(BaseModel):
    status: str
    recipient: str
    channel: str
    message: str
    tenant: Optional[str] = None
    debug: Optional[dict] = None

    premium_support: Optional[bool] = None
    compact: Optional[bool] = None