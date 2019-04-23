import logging

from django.contrib.contenttypes.models import ContentType
from django.db.models import F
from django.db import transaction

from project.celeryconf import app


logger = logging.getLogger(__name__)


@app.task(queue='content_counter')
def increase_content_counter(content: dict):
    with transaction.atomic():
        for t, ids in content.items():
            logger.info(f"Content type: {t}, for ids: {ids} increasing counter")
            model_type = ContentType.objects.get(app_label='base', model=t)
            model = model_type.model_class()
            model.objects.filter(id__in=ids).update(counter=F('counter') + 1)
