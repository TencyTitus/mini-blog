# Generated by Django 5.1.7 on 2025-03-25 08:00

from django.db import migrations
from django.utils import timezone
from django.contrib.auth.hashers import make_password
import random

def create_test_data(apps, schema_editor):
    # Get the models
    User = apps.get_model('auth', 'User')
    Post = apps.get_model('blog', 'Post')
    Comment = apps.get_model('blog', 'Comment')
    
    # Delete existing test data
    Post.objects.all().delete()
    
    # Create test users if they don't exist
    test_users_data = [
        {'username': 'JohnDoe', 'email': 'john@example.com'},
        {'username': 'JaneSmith', 'email': 'jane@example.com'},
        {'username': 'TechWriter', 'email': 'tech@example.com'},
        {'username': 'CodeMaster', 'email': 'code@example.com'},
        {'username': 'WebDev', 'email': 'web@example.com'},
    ]
    
    # Get existing users or create new ones
    users = []
    for user_data in test_users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'password': make_password('testpass123'),
                'is_active': True,
                'is_staff': True  # Make them staff so they can create posts
            }
        )
        if created:
            print(f"Created new user: {user.username}")
        users.append(user)
    
    # If no users were created/found, use any existing users
    if not users:
        users = list(User.objects.all())
        if not users:
            # Create at least one user if none exist
            admin_user = User.objects.create(
                username='admin',
                email='admin@example.com',
                password=make_password('admin123'),
                is_active=True,
                is_staff=True,
                is_superuser=True
            )
            users.append(admin_user)
            print("Created admin user")
    
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
    
    # Create posts and comments
    posts_created = 0
    for post_data in posts_data:
        try:
            # Randomly select an author
            author = random.choice(users)
            
            # Create post
            post = Post.objects.create(
                title=post_data['title'],
                content=post_data['content'],
                author=author,
                date_posted=timezone.now()
            )
            posts_created += 1
            print(f"Created post: {post.title} by {author.username}")
            
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
        except Exception as e:
            print(f"Error creating post: {str(e)}")
    
    print(f"Successfully created {posts_created} posts with comments")

def remove_test_data(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_category_alter_post_options_post_likes_and_more'),
    ]

    operations = [
        migrations.RunPython(create_test_data, remove_test_data),
    ]
