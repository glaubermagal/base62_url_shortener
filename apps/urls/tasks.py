import requests
from bs4 import BeautifulSoup
from celery import shared_task
from django.utils.html import strip_tags


@shared_task
def get_html_title(url):
    try:
        response = requests.get(url, timeout=10000)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = strip_tags(soup.title)
        
        if title_tag:
            return title_tag
        
        return ""
    except requests.RequestException as e:
        return f"Error: {str(e)}"
