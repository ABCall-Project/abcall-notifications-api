from typing import List
from ..domain.models import Notification
import requests
from ..domain.interfaces.notification_repository import NotificationRepository
from ..infrastructure.mappers import NotificationMapper
import uuid
from datetime import datetime
from ..utils import Logger
from  config import Config

class NotificationService:
    def __init__(self, notification_repository: NotificationRepository=None):
        self.log = Logger()
        self.notification_repository=notification_repository

    