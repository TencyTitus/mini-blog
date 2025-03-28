from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Creates test blog posts, comments, and likes'

    def handle(self, *args, **kwargs):
        # Get all users
        users = User.objects.all()
        
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create some users first.'))
            return
            
        # Sample blog post content
        posts_data = [
            {
                'title': 'Getting Started with Django',
                'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.'
            },
            {
                'title': 'Python Tips and Tricks',
                'content': 'Python is known for its simplicity and readability. Here are some tips and tricks to make your Python code more efficient and elegant. List comprehensions, generator expressions, and the zip function are just a few examples of Python\'s powerful features.'
            },
            {
                'title': 'Web Development Best Practices',
                'content': 'When developing web applications, it\'s important to follow best practices for security, performance, and maintainability. This includes proper error handling, input validation, and following the DRY (Don\'t Repeat Yourself) principle.'
            },
            {
                'title': 'Understanding Database Design',
                'content': 'Good database design is crucial for building scalable applications. This includes proper normalization, indexing, and understanding relationships between tables. PostgreSQL offers many advanced features for complex data modeling.'
            },
            {
                'title': 'Frontend Development with Modern Tools',
                'content': 'Modern frontend development involves various tools and frameworks. Understanding HTML5, CSS3, and JavaScript is essential. Popular frameworks like React and Vue.js help in building interactive user interfaces.'
            }
        ]
        
        # Sample comments
        comments_data = [
            "Great article! Very informative and well-written.",
            "Thanks for sharing these insights. I learned a lot.",
            "This is exactly what I was looking for. Well explained!",
            "Interesting perspective. Would love to see more content like this.",
            "Very helpful tutorial. Keep up the great work!",
            "Clear and concise explanation. Perfect for beginners.",
            "I've been using these techniques and they work great.",
            "Looking forward to more articles from you!",
            "This helped me solve a problem I was stuck on. Thank you!",
            "Excellent breakdown of complex concepts."
        ]
        
        # Create posts
        posts_created = 0
        all_posts = []
        for post_data in posts_data:
            # Randomly select a user as the author
            author = random.choice(users)
            
            # Create the post
            post = Post.objects.create(
                title=post_data['title'],
                content=post_data['content'],
                author=author,
                date_posted=timezone.now()
            )
            all_posts.append(post)
            posts_created += 1
            
            # Add random likes to the post
            num_likes = random.randint(1, len(users))
            liking_users = random.sample(list(users), num_likes)
            post.likes.set(liking_users)
            
            # Add random comments
            num_comments = random.randint(2, 5)
            for _ in range(num_comments):
                commenter = random.choice(users)
                comment_text = random.choice(comments_data)
                Comment.objects.create(
                    post=post,
                    author=commenter,
                    content=comment_text,
                    date_posted=timezone.now()
                )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Created post: {post.title} by {author.username} '
                    f'with {num_comments} comments and {num_likes} likes'
                )
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {posts_created} test posts with comments and likes'
            )
        ) 