"""Unit tests for Tasks"""

from datetime import timedelta

import pytest

from lib.scheduler import Scheduler
from lib.tasks import Task


def test_instantiates_correctly():
    make_coffee = Task("make-coffee", timedelta(seconds=5), timedelta(seconds=115))
    make_toast = Task("make-toast", timedelta(seconds=5), timedelta(seconds=55))

    test_scheduler = Scheduler("prepare-breakfast", [make_coffee, make_toast])
    assert test_scheduler.name == "prepare-breakfast"
    assert test_scheduler.tasks == [make_coffee, make_toast]
    assert test_scheduler.schedule is None


# def test_schedules_tasks():
#
#     test_scheduler = Scheduler("prepare-breakfast")
#     test_scheduler.schedule([make_coffee, make_toast])
#     assert test_scheduler.tasks == [
#         make_coffee,
#         make_toast,
#     ]
