from django.conf import settings

import threading
import logging

request_user = threading.local()

try:
    attrs = settings.SAAS_DBNAME_FIELD.split('.')
except AttributeError:
    raise AttributeError('SAAS_DBNAME_FIELD is not defined in the settings file')

try:
    auth_apps = settings.SAAS_IGNORED_APPS
except AttributeError:
    raise AttributeError('SAAS_IGNORED_APPS is not defined in the settings file')


class RouterMiddleware(object):
    """
    This router set the database name to be used
    """

    def process_request(self, request):

        res = request.user
        if not res.is_authenticated():
            return

        try:
            for attr in attrs:
                res = getattr(res, attr)
        except AttributeError:
            raise AttributeError("Attribute '%s' in 'User.%s' was not found" % (attr, settings.SAAS_DBNAME_FIELD))
        request_user.dbname = res


class AuthRouter(object):
    """
    A router to control database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read to any i.
        """
        logging.info("db_for_read is %s" % model._meta.app_label)
        if model._meta.app_label in auth_apps:
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models => auth_db.
        """
        logging.info("db_for_write is %s" % model._meta.app_label)
        if model._meta.app_label in auth_apps:
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        logging.info("allow_relation for %s" % app_label)
        if obj1._meta.app_label in auth_apps or \
                obj2._meta.app_label in auth_apps:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db' database.
        """
        logging.info("allow_migrate for %s" % app_label)
        if app_label in auth_apps:
            return db == 'auth_db'
        return None


class DatabaseRouter(object):
    """
    Router selecting the database depending on the user
    User field used for comparaison can be changed in settings.
    """

    def _default_db(self):
        if hasattr(request_user, 'dbname') and request_user.dbname != "":
            logging.info("DB is %s" % request_user.dbname)
            return request_user.dbname
        logging.info("DB is default")
        return 'default'

    def db_for_read(self, model, **hints):
        return self._default_db()

    def db_for_write(self, model, **hints):
        return self._default_db()

