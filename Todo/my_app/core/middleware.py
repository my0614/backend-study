 # app/core/middleware.py
import time
import logging
from fastapi import Request
logger = logging.getLogger(__name__)

async def logging_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = (time.time() - start) * 1000  # ms
    logger.info(
        f"{request.method} {request.url.path} "
        f"→ {response.status_code} ({duration:.1f}ms)"
    )
    return response