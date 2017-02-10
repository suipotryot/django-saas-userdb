from django.core.management.base import BaseCommand, CommandError
from string import Template


class Command(BaseCommand):

    help = 'Add a database to the database file'

    flag = "###ADD_DATABASE"

    template = Template("""'$alias': {
        'ENGINE': '$engine',
        'NAME': '$dbname',
        'USER': '$user',
        'PASSWORD': '$password',
        'HOST': '$host',
        'PORT': '$port',
    },
    ###ADD_DATABASE""")

    ENGINES = {
        0: 'django.db.backends.postgresql',
        1: 'django.db.backends.mysql',
        2: 'django.db.backends.sqlite3',
        3: 'django.db.backends.oracle',
    }

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--file',
            default='',
            dest = 'file',
            help='The file with database settings and ###ADD_DATABASE flag'
        )
        parser.add_argument(
            '--fileout',
            default='',
            dest = 'fileout',
            help='The file to write new database settings in'
        )
        parser.add_argument(
            '--alias',
            default='',
            dest = 'alias',
            help='The DB alias'
        )
        parser.add_argument(
            '--dbname',
            default='',
            dest = 'dbname',
            help='The DB name'
        )
        parser.add_argument(
            '--user',
            default='',
            dest = 'user',
            help='The DB username'
        )
        parser.add_argument(
            '--pwd',
            default='',
            dest = 'password',
            help='The DB password for this user'
        )
        parser.add_argument(
            '--host',
            default='localhost',
            dest = 'host',
            help='The DB host (default localhost)'
        )
        parser.add_argument(
            '--port',
            default='',
            dest = 'port',
            help='The DB port'
        )
        parser.add_argument(
            '--engine',
            default=2,
            dest = 'engine',
            help='The DB engine (0=postgres, 1=mysql, 2=sqlite3, 3=oracle)'
        )


    def handle(self, *args, **options):
        options['engine'] = self.ENGINES[int(options['engine'])]
        tpl = self.template.substitute(options)
        with open(options['file'], 'r') as f:
            filecontent = f.read()
        res = filecontent.replace(self.flag, tpl)
        if options['fileout']:
            with open(options['fileout'], 'w') as f:
                f.write(res)
        else:
            return res
