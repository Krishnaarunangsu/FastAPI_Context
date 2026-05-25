from pydantic import BaseModel
from typing import Literal, Union


# ==========================================
# BASE REQUEST
# ==========================================

class BaseNotificationRequest(BaseModel):
    type: str
    recipient: str
    message: str


# ==========================================
# EMAIL REQUEST
# ==========================================

class EmailRequest(BaseNotificationRequest):

    type: Literal["EMAIL"]

    weather: str

    color: str


# ==========================================
# SMS REQUEST
# ==========================================

class SMSRequest(BaseNotificationRequest):

    type: Literal["SMS"]

    food: str


# ==========================================
# PUSH REQUEST
# ==========================================

class PushRequest(BaseNotificationRequest):

    type: Literal["PUSH"]

    clothes: str


# ==========================================
# POLYMORPHIC UNION
# ==========================================

NotificationRequest = Union[
    EmailRequest,
    SMSRequest,
    PushRequest
]