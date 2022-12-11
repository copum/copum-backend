from django_seed import Seed
from users.models import User
from django.core.management.base import BaseCommand
from faker import Faker
class Command(BaseCommand):
    help = "이 커맨드를 통해 랜덤한 테스트 유저 데이터를 만듭니다."

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="몇 명의 유저를 만드나"
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            total,
            {
                "user_id": lambda x: Faker(['ko_KR']).name(),
                "profile_image": '',
                "password": '',
                "email": lambda x: seeder.faker.email(),
                "login_type" : ''
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total}명의 유저가 작성되었습니다."))