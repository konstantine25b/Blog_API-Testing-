from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from blog.models import Post , Comment , Tag

from faker import Faker
import random


class Command(BaseCommand):
    help = "populated dummy data to the database"
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        
        
        
        for _ in range(10):
            User.objects.create_user(username= fake.user_name() , email = fake.email() , password = 'password')
            
        users = User.objects.all()
        
        tags =[]
        for _ in range(7):
            tag, _ =Tag.objects.get_or_create(name = fake.word())
            tags.append(tag) 
            
            
        for _ in range(70):
            post = Post.objects.create(
                
                title = fake.sentence(),
                content = " ".json(fake.paragraphs(nb=3)),
                author = random.choice(users),
            )
            post.tags.set(random.sample(tags,random.randint(1,len(tags)-1)))
        for _ in range(470):
            Comment.objects.create(
                content = fake.paragraph(),
                author = random.choice(users),
                post = random.choice(post)
            ) 
            
        self.stdout.write(self.style.SUCCESS('database populated with dummy dataaa'))
        
