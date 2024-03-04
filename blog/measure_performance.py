import os 
import django 
from timeit import timeit
from .models import Post

def query_posts_ordered_by_created_at():
    return list(Post.objects.order_by('created_at'))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogapi.settings')
django.setup()

number_of_executions = 200

time_taken = timeit('query_posts_ordered_by_created_at', globals=globals(), number = number_of_executions)
average_time = time_taken / number_of_executions
print(f"avg time per ordered query: {number_of_executions} from {average_time} seconds")
