from urllib import response
from celery import shared_task
import requests, uuid
from django.conf import settings

@shared_task
def download_a_cat_img():
    response = requests.get("https://cataas.com/cat/cute")
    file_ext = response.headers.get("Content-Type").split('/')[1]
    file_name = settings.BASE_DIR / 'cats' / (str(uuid.uuid4()) + "." + file_ext)
    print(file_name)
    with open(file_name, "wb") as f:
        f.write(response.content)
    return True

