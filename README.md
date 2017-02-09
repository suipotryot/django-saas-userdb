# django-saas-userdb
A lightweight application to use Django as SaaS (Software as a Service). It separates users databases for the same Django instance.

## Installation

```
pip install django-saas-userdb
```

## Configuration

In your settings: 
```
DATABASE_ROUTERS = ['userdb.routers.AuthRouter', 'userdb.routers.DatabaseRouter']
```

You must configure the field used in request.user to determine the used database. For example, this code :
```
SAAS_DBNAME_FIELD = 'username'
```
will need a Database for each user, postfixed with "_db" (for example users named "foo" and "bar" will be using databases with names "foo_db", "bar_db").

Note: For any user with no database configured for him, it will fallback to 'default' database.

An example of database configuration in your settings (following previous example):
```
DATABASES = {
    # The default database
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'default.sqlite3'),
    },
    # The database for users (must be separated to allow registration before DB choice)
    'auth_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'users.sqlite3'),
    },
    # The database for "foo" user
    'foo_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'foo.sqlite3'),
    },
    # The database for "bar" user
    'bar_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'bar.sqlite3'),
    },
}
```
