from urllib.request import Request

from starlette.middleware.base import BaseHTTPMiddleware

class ContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request, call_next):
        request.state.user_role = request.headers.get(
            "x-user-role",
            "USER"
        )

        request.state.tenant = request.headers.get(
            "x-tenant-id",
            "STANDARD"
        )

        request.state.device = request.headers.get(
            "x-device-type",
            "WEB"
        )

        # noinspection PyCompatibility
        response = await call_next(request)

        return response