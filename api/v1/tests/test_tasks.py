from django.test import TestCase

from base.models import Page
from api.v1.tasks import increase_content_counter


class CounterTest(TestCase):
    fixtures = [
        'initial_data.json'
    ]

    def test_empty_list(self):
        increase_content_counter(())
        self.assertTrue(True)

    def test_ok(self):
        page = Page.objects.get(id=1)

        content = page.content.all()
        self.assertEqual(len(content), 4)

        counters = {}

        for x in content:
            counters[(x.content_object.id, str(x.content_type))] = x.content_object.counter

        increase_content_counter(tuple(counters.keys()))

        for x in content:
            x.content_object.refresh_from_db()

            self.assertIn((x.content_object.id, str(x.content_type)), counters)
            self.assertEqual(x.content_object.counter, counters[(x.content_object.id, str(x.content_type))] + 1)
