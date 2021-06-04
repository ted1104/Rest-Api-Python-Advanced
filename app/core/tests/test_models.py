from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):
    """Models test"""

    def test_create_user_with_email_successful(self):
        """create user with email"""

        email = "teddy@connectis.co"
        password = "Testpass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if email is normalized"""
        email = "teddy@CONNECTIS.CO"

        user = get_user_model().objects.create_user(
            email=email
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with invalid email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
