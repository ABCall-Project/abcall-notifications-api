from typing import List, Optional
from uuid import UUID
from ..models.notification import Notification

class NotificationRepository:
    def list(self) -> List[Notification]:
        raise NotImplementedError