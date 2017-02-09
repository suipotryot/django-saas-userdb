# django-saas-userdb
A lightweight application to use Django as SaaS (Software as a Service). It separates users databases for the same Django instance.

## Installation

```
pip install django-saas-userdb
```

## Configuration

In your settings: 
```
DATABASE_ROUTERS = ['poc_noe_saas.routers.AuthRouter', 'poc_noe_saas.routers.DatabaseRouter']
```
