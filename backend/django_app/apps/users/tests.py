from django.test import TestCase
from .models import User


class UserModelTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com",
            password="password123",
            first_name="Test",
            last_name="User"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("password123"))