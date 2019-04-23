from django.test import TestCase

from base.models import Page
from api.v1.tasks import increase_content_counter


class CounterTest(TestCase):
    fixtures = [
        'initial_data.json'
    ]

    def test_empty_list(self):
        increase_content_counter({})
        self.assertTrue(True)

    def test_ok(self):
        page = Page.objects.get(id=1)

        data = page.content.all()
        self.assertEqual(len(data), 4)

        counters = {}
        content = {}
        for x in data:
            counters[(x.content_object.id, str(x.content_type))] = x.content_object.counter
            content.setdefault(x.content_type, set()).add(x.content_object.id)

        increase_content_counter(content)

        for x in data:
            x.content_object.refresh_from_db()

            self.assertIn((x.content_object.id, str(x.content_type)), counters)
            self.assertEqual(x.content_object.counter, counters[(x.content_object.id, str(x.content_type))] + 1)
