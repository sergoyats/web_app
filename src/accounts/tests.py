from django.test import TestCase
from faker import Faker
from django.urls import reverse
from datetime import datetime, date
from django.contrib.auth.models import User
from accounts.models import Profile
from django.test.client import Client

f = Faker()


class AccountsTestCase(TestCase):
    fixtures = ['test_auth.json']

    def setUp(self) -> None:
        pass

    def test_profiles_count(self):
        print(Profile.objects.all().count())
        self.assertEqual(1, 1)

    def test_create_user(self):
        email = f.email()
        user = User.objects.create_user(
            username=f.user_name(),
            email=email,
            password=f.password()
        )
        profile = Profile.objects.get(user_id=user.id)

        self.assertEqual(profile.nickname, email)

    def test_profile_age(self):
        birthdate = datetime(year=1996, day=14, month=10).date()

        def calculate_age(born):
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        profile = Profile(
            birth_date=birthdate
        )

        self.assertEqual(calculate_age(birthdate), profile.age)


class AccountsIntegrationTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    @staticmethod
    def list_view_fixture():
        profile = Profile(nickname='HelloWorld')
        profile.save()

    def test_list_view(self):
        self.list_view_fixture()
        resp = self.client.get(reverse('profiles:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'HelloWorld')

    def test_add_view_auth(self):
        resp = self.client.get(reverse('profiles:add'))
        self.assertRedirects(resp, '/account/login/?next=%2Fprofiles%2Fadd%2F')
