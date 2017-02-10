from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO
from django.conf import settings


class AddDatabaseTest(TestCase):

    def test_command_output_valid(self):

        expected = """# Do not remove the \"###\" flag (used by add_database command)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'example',
    },
    'newly_added': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'foo',
        'USER': 'bar',
        'PASSWORD': 'foobar',
        'HOST': 'barfoo',
        'PORT': 'far',
    },
    ###ADD_DATABASE
}
"""
        out = StringIO()
        call_command('add_database',
                "--file=userdb/management/commands/testfile.py",
                "--alias=newly_added",
                "--dbname=foo",
                "--user=bar",
                "--pwd=foobar",
                "--host=barfoo",
                "--port=far",
                "--engine=1",
                stdout=out)
        self.maxDiff = None
        self.assertEqual(expected, out.getvalue())
