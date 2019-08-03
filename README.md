THE GEO APP (WITH REDIS)
--------------------------------------------------------------------------------------------------------------------

Aplicación web desarrollada con Django 2.2 que almacena información de continentes, paises y ciudades.

La aplicación se conecta a una base de datos PostgreSQL utilizando las librerias psycopg2 y dj_database_url.

Se utiliza la librería django-redis para manejar la información de continentes, paises y ciudades en cache  
Redis, disminuyendo la cantidad de accesos a base de datos.

--------------------------------------------------------------------------------------------------------------------

**Se debe definir la variable de ambiente "DATABASE_URL" que es utilizada**
**por la librería dj-database-url para acceder a la base de datos:**

```

DATABASE_URL="postgres://user:password@localhost/nombre-db"

```

**Configuración de base de datos PostgreSQL en archivo setting.py:**

```
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

```

--------------------------------------------------------------------------------------------------------------------

**Configuración de Redis en archivo settings:**

```

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

```

--------------------------------------------------------------------------------------------------------------------

Pantalla principal de la aplicación:

![Screenshot Main](screenshots/the_geo_app_main.png)

--------------------------------------------------------------------------------------------------------------------

Pantalla principal de la sección Continents:

![Screenshot Continents](screenshots/the_geo_app_continents.png)

--------------------------------------------------------------------------------------------------------------------

Se revisan las llaves almacenadas en Redis por medio de redis-cli:

![Screenshot Keys](screenshots/redis-cli-keys.png)

--------------------------------------------------------------------------------------------------------------------

Si bien la cantidad de registros en la vista continentes es pequeña, al realizar la comparación de rendimiento 
con loadtest, la cache tiene una mejor performance que el acceso a base de datos.

Rendimiento usando solo base de datos:

![Screenshot Bd](screenshots/loadtest-using-db.png)

Rendimiento usando solo cache Redis:

![Screenshot Cache](screenshots/loadtest-using-cache.png)

--------------------------------------------------------------------------------------------------------------------


