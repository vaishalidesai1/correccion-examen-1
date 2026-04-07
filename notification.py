from abc import ABC, abstractmethod
from enum import Enum


class NotificationEvent(Enum):
    TASK_CREATED = "TASK_CREATED"
    STATUS_CHANGED = "STATUS_CHANGED"
    TASK_DONE = "TASK_DONE"


# Interface

class NotificationPolicy(ABC):

    @abstractmethod
    def should_notify(self, event: NotificationEvent) -> bool:
        pass


# Strategies

class AlwaysNotify(NotificationPolicy):

    def should_notify(self, event: NotificationEvent) -> bool:
        return event in {
            NotificationEvent.TASK_CREATED,
            NotificationEvent.STATUS_CHANGED,
            NotificationEvent.TASK_DONE,
        }


class NotifyOnDoneOnly(NotificationPolicy):

    def should_notify(self, event: NotificationEvent) -> bool:
        return event == NotificationEvent.TASK_DONE


# Service

class NotificationService:

    def __init__(self, policy: NotificationPolicy):
        self._policy = policy

    def notify(self, event: NotificationEvent, task_id: str) -> None:
        if self._policy.should_notify(event):
            print(f"[NOTIFICATION] event={event.value} task_id={task_id}")
        else:
            print(f"[SKIPPED] event={event.value} task_id={task_id}")
