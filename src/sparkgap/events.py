from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from typing import Any

logger = logging.getLogger("sparkgap.events")


def emit_event(event_type: str, request_id: str, **payload: Any) -> None:
    event = {
        "event_id": f"{event_type}:{request_id}",
        "event_type": event_type,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "request_id": request_id,
        **payload,
    }
    logger.info("event=%s", json.dumps(event, sort_keys=True, default=str))
