from django.db.models.fields import BooleanField
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task


class TaskTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = get_user_model().objects.create_user(
            username="testuser", password="pass"
        )
        testuser.save()

        test_task = Task.objects.create(
            author=testuser,
            title="Take a break",
            completed="False",
        )
        test_task.save()

    def test_task(self):
        task = Task.objects.get(id=1)
        actual_author = str(task.author)
        actual_title = str(task.title)
        actual_completed = str(task.completed)
        self.assertEqual(actual_author, "testuser")
        self.assertEqual(actual_title, "Take a break")
        self.assertEqual(actual_completed, "False")
