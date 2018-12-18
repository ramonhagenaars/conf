import warnings
from unittest import TestCase
import conf


class TestConfg(TestCase):

    def test_read_yml(self):
        conf.load('test_resources/conf1.yml')
        self.assertEqual(conf.get('message'), 'this is yml')

    def test_get_default(self):
        conf.load('test_resources/conf1.yml')
        self.assertEqual(conf.get('key_does_not_exist'), None)
        self.assertEqual(conf.get('key_does_not_exist', 'some_value'),
                         'some_value')

    def test_read_yaml(self):
        conf.load('test_resources/conf2.yaml')
        self.assertEqual(conf.get('message'), 'this is yml')

    def test_read_yaml_uppercases(self):
        conf.load('test_resources/conf3.YaMl')
        self.assertEqual(conf.get('message'), 'this is yml')

    def test_read_json(self):
        conf.load('test_resources/conf4.json')
        self.assertEqual(conf.get('message'), 'this is json')

    def test_read_ini(self):
        conf.load('test_resources/conf6.ini')
        self.assertEqual(conf.get('main_section')['message'],
                         'this is ini')

    def test_read_default(self):
        conf.load('test_resources/default_python_conf')
        self.assertEqual(conf.get('main_section')['message'],
                         'this is default')

    def test_warn_if_file_not_found(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            conf.load('no_way_this_file_exists.yml')
            assert len(w) == 1
            assert 'not found' in str(w[-1].message)

    def test_warn_if_file_cannot_be_parsed(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            conf.load('test_resources/conf.chuck_norris')
            assert len(w) == 1
            assert 'cannot parse' in str(w[-1].message)

    def test_warn_if_file_cannot_be_parsed_due_to_content(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            conf.load('test_resources/conf5.json')
            assert len(w) == 1
            assert 'failed to parse' in str(w[-1].message)

    def test_warn_if_filename_is_empty(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            conf.load('')
            assert len(w) == 1
            assert 'empty filename' in str(w[-1].message)
