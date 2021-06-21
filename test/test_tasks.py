"""Unit tests for Tasks"""

from datetime import timedelta

import pytest

from lib.tasks import Task


def test_instantiates_correctly():
    test_task = Task("make-coffee", timedelta(seconds=5), timedelta(seconds=115))
    assert test_task.task_name == "make-coffee"
    assert test_task.active_time == timedelta(seconds=5)
    assert test_task.passive_time == timedelta(seconds=115)
