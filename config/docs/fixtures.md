# dumpdata tablas

## Que es dumpdata?

> Dumpdata es un comando de gestión de django, el cual se puede usar para respaldar datos de una bdd.

## Verifica tu código

### Comando

> Para traer los datos de toda las tablas

```terminal
python manage.py dumpdata > app/fixtures/backup.json
```

> Para traer los datos de una tabla en especifica

```terminal
python manage.py dumpdata app.*model* > app/fixtures/*nombre del modelo*.json
```
