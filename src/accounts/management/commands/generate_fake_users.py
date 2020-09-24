from django.conf import settings
from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from faker import Faker

# from polls.models import Question as Poll

f = Faker()


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
        group = Group(name=settings.ADMIN_GROUP)
        group.save()
        for _ in range(options["count"][0]):

            user = User.objects.create_user(
                username=f.user_name(),
                email=f.email(),
                password=f.password()
            )
            group.user_set.add(user)
