# reviews/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Review


class ReviewCRUDTests(TestCase):
    def setUp(self):
        # Users
        self.owner = User.objects.create_user(username="owner", password="pass12345")
        self.other = User.objects.create_user(username="other", password="pass12345")

        # URLs
        self.list_url = reverse("reviews:review_list")

        # Seed one review by owner
        self.review = Review.objects.create(
            author=self.owner,
            title="Great place",
            rating=5,
            body="Loved it!",
        )
        self.update_url = reverse("reviews:review_update", args=[self.review.pk])
        self.delete_url = reverse("reviews:review_delete", args=[self.review.pk])

    # --- Create ---
    def test_create_requires_login(self):
        resp = self.client.post(self.list_url, {
            "title": "Anon Review",
            "rating": 4,
            "body": "Nice."
        })
        # Should redirect to login
        self.assertEqual(resp.status_code, 302)
        self.assertIn(reverse("account_login"), resp["Location"])
        self.assertEqual(Review.objects.count(), 1)  # unchanged

    def test_create_success(self):
        self.client.login(username="owner", password="pass12345")
        resp = self.client.post(self.list_url, {
            "title": "New Review",
            "rating": 4,
            "body": "Pretty good!"
        })
        # View redirects back to list on success
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, self.list_url)
        self.assertEqual(Review.objects.count(), 2)
        obj = Review.objects.latest("id")
        self.assertEqual(obj.author, self.owner)
        self.assertEqual(obj.title, "New Review")
        self.assertEqual(obj.rating, 4)

    # --- Read ---
    def test_list_shows_reviews(self):
        resp = self.client.get(self.list_url)
        self.assertContains(resp, "Great place")
        self.assertContains(resp, "Loved it!")

    # --- Update ---
    def test_update_by_owner(self):
        self.client.login(username="owner", password="pass12345")
        resp = self.client.post(self.update_url, {
            "title": "Updated Title",
            "rating": 3,
            "body": "It was fine."
        })
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, self.list_url)
        self.review.refresh_from_db()
        self.assertEqual(self.review.title, "Updated Title")
        self.assertEqual(self.review.rating, 3)
        self.assertEqual(self.review.body, "It was fine.")

    def test_update_by_non_owner_redirects(self):
        self.client.login(username="other", password="pass12345")
        original_title = self.review.title
        resp = self.client.post(self.update_url, {
            "title": "Hacked Title",
            "rating": 1,
            "body": "Nope."
        })
        # Your view redirects to list with an error message
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, self.list_url)
        self.review.refresh_from_db()
        self.assertEqual(self.review.title, original_title)  # unchanged

    # --- Delete ---
    def test_delete_by_owner(self):
        self.client.login(username="owner", password="pass12345")
        resp = self.client.post(self.delete_url)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, self.list_url)
        self.assertFalse(Review.objects.filter(pk=self.review.pk).exists())

    def test_delete_by_non_owner_redirects(self):
        self.client.login(username="other", password="pass12345")
        resp = self.client.post(self.delete_url)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, self.list_url)
        self.assertTrue(Review.objects.filter(pk=self.review.pk).exists())