from django_seed import Seed
from users.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from Post.models import Question, Category
import random
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
        users = User.objects.all()
        categories = Category.objects.all()
        faker = Faker(["ko_KR"])
        for user in users:
            for _ in range(total):
                questions = Question.objects.create(Author_id=user.id, Question_category1 = random.choice(categories))
                questions.Question_title=  faker.unique.bs()
                questions.Question_content = faker.unique.bs()
                questions.save()
        self.stdout.write(self.style.SUCCESS(f"{len(users) * total}개의 question이 생성되었습니다."))