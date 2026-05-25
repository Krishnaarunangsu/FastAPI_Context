from fastapi import APIRouter, Request

from app.models.request_models import NotificationRequest
from app.models.response_models import NotificationResponse

from app.services.notification_service import NotificationService

router = APIRouter()


@router.post(
    "/notify",
    response_model=NotificationResponse
)
async def send_notification(
    request: Request,
    payload: NotificationRequest
):

    context = {
        "role": request.state.user_role,
        "tenant": request.state.tenant,
        "device": request.state.device
    }

    result = NotificationService.process_notification(
        payload,
        context
    )

    return result