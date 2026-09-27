import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock

spec = importlib.util.spec_from_file_location('collector', Path(__file__).parents[1] / 'scripts/collect_warera.py')
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)


class CollectorTests(unittest.TestCase):
    def test_get_only_and_secret_not_archived(self):
        with tempfile.TemporaryDirectory(dir=collector.ROOT) as directory:
            client = collector.Client('test-secret', Path(directory), 0)
            response = Mock()
            response.read.return_value = b'{"result":{"data":{"items":[],"nextCursor":null}}}'
            context = Mock()
            context.__enter__ = Mock(return_value=response)
            context.__exit__ = Mock(return_value=False)
            client.opener.open = Mock(return_value=context)
            client.get('article.getArticlesPaginated', {'type': 'last'})
            request = client.opener.open.call_args.args[0]
            self.assertEqual(request.get_method(), 'GET')
            self.assertIsNone(request.data)
            for path in Path(directory).rglob('*.json'):
                self.assertNotIn('test-secret', path.read_text(encoding='utf-8'))
            for endpoint in ('article.getArticleById', 'article.create', 'anything'):
                with self.assertRaises(RuntimeError):
                    client.get(endpoint, {})
            self.assertEqual(client.opener.open.call_count, 1)

    def test_redirect_refused(self):
        with self.assertRaises(RuntimeError):
            collector.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://other.example')

    def test_pagination_preserves_cursor_and_partial_status(self):
        with tempfile.TemporaryDirectory(dir=collector.ROOT) as directory:
            client = Mock(output=Path(directory))
            client.get.side_effect = [{'items': [{'id': 1}], 'nextCursor': 'next'},
                                      {'items': [{'id': 2}], 'nextCursor': 'more'}]
            result = collector.paginate(client, 'event.getEventsPaginated', {'limit': 100}, 2)
            self.assertEqual(client.get.call_args.args[1]['cursor'], 'next')
            self.assertEqual(result, {'records': 2, 'complete': False})
            archived = json.loads((Path(directory) / 'event.getEventsPaginated.json').read_text())
            self.assertEqual(archived['next_cursor'], 'more')


if __name__ == '__main__':
    unittest.main()
