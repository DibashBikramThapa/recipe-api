from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """test new user with email"""
        email = "dwasthapa172@gmail.com"
        password = 'hi123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailized(self):
        """new user normalized"""
        email = 'dwasthapa172@GMaIl.com'
        user = get_user_model().objects.create_user(email, 'abc')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test new user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'axc')

    def test_Create_new_superuser(self):
        """test new user created"""
        user = get_user_model().objects.create_superuser(
            'dwasthapa172@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
