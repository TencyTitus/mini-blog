from django.contrib.auth.models import User
from django.db.models import Count
import logging

logger = logging.getLogger('blog')

def bloggers_processor(request):
    """
    Context processor that adds the list of bloggers to all templates.
    """
    try:
        # Get users who have at least one post, annotated with their post count
        bloggers = User.objects.annotate(
            post_count=Count('post')
        ).filter(
            post_count__gt=0
        ).order_by('username')
        
        logger.info(f'Found {bloggers.count()} bloggers in context processor')
        return {
            'bloggers': bloggers,
        }
    except Exception as e:
        logger.error(f'Error in bloggers_processor: {str(e)}', exc_info=True)
        return {
            'bloggers': [],
        } 