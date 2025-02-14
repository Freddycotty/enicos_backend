# PEP8 Formateo

## Que es PEP8?

> PEP8 es una guía de estilo para código Python. Es un conjunto de reglas para escribir código Python que los humanos pueden leer.

## Verifica tu código

### Requirements

- Instalar Flake8

```terminal
pip install flake8
```

### Comando

```terminal
flake8 --exclude=.git,.venv,env,.tox,dist,doc,*egg,build,.vscode,*migrations/*.py,*.
```