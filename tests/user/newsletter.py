from django.contrib.auth.models import User
from django.test import TestCase

from mocks.newsletter import NewsletterServiceMock


class NewsletterLogic(TestCase):
    def setUp(self) -> None:
        self.service = NewsletterServiceMock()
        self.test_tue = "tosti@student.tue.nl"
        self.test_alt = "tosti@gmail.com"
        self.test_user: User = User.objects.create_user(
            username=self.test_tue,
            email=self.test_alt,
        )

    def tearDown(self) -> None:
        User.objects.get(username=self.test_tue).delete()
        super().tearDown()

    def test_is_subscribed_false(self):
        result = self.service.is_subscribed(self.test_user.username)
        self.assertFalse(result, msg="is_subscribed false")

    def test_is_subscribed_true(self):
        self.service.add_subscription(self.test_alt, self.test_user.first_name, self.test_user.last_name)
        result = self.service.is_subscribed(self.test_alt)
        self.assertTrue(result)

    def test_add(self):
        result = self.service.add_subscription(self.test_alt, self.test_user.first_name, self.test_user.last_name)
        self.assertTrue(result)

    def test_remove_empty_db(self):
        self.service.remove_subscription(self.test_alt)
        result = self.service.is_subscribed(self.test_alt)
        self.assertFalse(result)

    def test_remove_filled_db(self):
        self.service.add_subscription(self.test_alt, self.test_user.first_name, self.test_user.last_name)
        self.service.remove_subscription(self.test_alt)
        result = self.service.is_subscribed(self.test_alt)
        self.assertFalse(result)

    def test_update_unsub_user(self):
        self.service.update_newsletter_preferences(self.test_user.profile)
        result = self.service.is_subscribed(self.test_tue)
        self.assertFalse(result)

    def test_update_new_user(self):
        self.test_user.profile.subscribed_newsletter = True
        self.service.update_newsletter_preferences(self.test_user.profile)

        result = self.service.is_subscribed(self.test_tue)
        self.assertTrue(result)

    def test_update_old_user_no_change(self):
        self.test_user.profile.subscribed_newsletter = True
        self.service.update_newsletter_preferences(self.test_user.profile)

        self.test_user.profile.subscribed_newsletter = True
        self.test_user.profile.old_subscribed_newsletter = True
        self.service.update_newsletter_preferences(self.test_user.profile)

        result = self.service.is_subscribed(self.test_tue)
        self.assertTrue(result)

    def test_update_old_user_change_to_alt_email(self):
        self.test_user.profile.subscribed_newsletter = True
        self.test_user.profile.newsletter_recipient = "TUE"
        self.service.update_newsletter_preferences(self.test_user.profile)

        self.test_user.profile.old_subscribed_newsletter = True
        self.test_user.profile.subscribed_newsletter = True
        self.test_user.profile.old_newsletter_recipient = "TUE"
        self.test_user.profile.newsletter_recipient = "ALT"
        self.service.update_newsletter_preferences(self.test_user.profile)

        self.assertFalse(self.service.is_subscribed(self.test_tue))
        self.assertTrue(self.service.is_subscribed(self.test_alt))

    def test_update_old_user_change_to_tue_email(self):
        self.test_user.profile.subscribed_newsletter = True
        self.test_user.profile.newsletter_recipient = "ALT"
        self.service.update_newsletter_preferences(self.test_user.profile)

        self.test_user.profile.old_subscribed_newsletter = True
        self.test_user.profile.subscribed_newsletter = True
        self.test_user.profile.old_newsletter_recipient = "ALT"
        self.test_user.profile.newsletter_recipient = "TUE"
        self.service.update_newsletter_preferences(self.test_user.profile)

        self.assertFalse(self.service.is_subscribed(self.test_alt))
        self.assertTrue(self.service.is_subscribed(self.test_tue))
