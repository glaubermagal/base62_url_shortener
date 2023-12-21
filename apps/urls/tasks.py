import requests
from bs4 import BeautifulSoup
from celery import shared_task
from django.utils.html import strip_tags


@shared_task
def fetch_html_title(url_id):
    from .models import URLs
    url_instance = URLs.objects.get(id=url_id)
    html_title = get_html_title(url_instance.long_url)
    
    url_instance.title = strip_tags(html_title)
    url_instance.save()

def get_html_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.title
        if title_tag:
            return title_tag.string.strip()
        else:
            return "No title found"
    except requests.RequestException as e:
        return f"Error: {str(e)}"
