# Mini Blog

A modern, feature-rich blog application built with Django.

## Features

- User authentication and registration
- Create, read, update, and delete blog posts
- Comment system on posts
- Like/unlike posts
- User profiles
- Category system
- Responsive design
- Modern UI with animations

## Tech Stack

- Python 3.x
- Django
- SQLite
- HTML5/CSS3
- JavaScript

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TencyTitus/mini-blog.git
cd mini-blog
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your browser

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 