from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTests(TestCase):

    def test_create_user(self):
        user = get_user_model().objects.create(
            username = 'user',
            email='user@email.com',
            password='testpass123',
        )

        self.assertEqual(user.username, 'user')
        self.assertEqual(user.email, 'user@email.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)


    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            username = 'superuser',
            email='superuser@email.com',
            password='testpass123',
        )

        self.assertEqual(user.username, 'superuser')
        self.assertEqual(user.email, 'superuser@email.com')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)