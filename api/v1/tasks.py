import logging

from django.db.models import F
from django.db import transaction


from project.celeryconf import app
from base.models import PageContent


logger = logging.getLogger(__name__)


@app.task(queue='content_counter')
def increase_content_counter(content: tuple):
    with transaction.atomic():
        for i, t in content:
            logger.info(f"Content, id: {i}, type: {t}, increasing counter")
            pc = PageContent.objects.filter(object_id=i, content_type__app_label='base', content_type__model=t).first()
            pc.content_object.counter = F('counter') + 1
            pc.content_object.save()
