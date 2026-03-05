### Tim simple django auto-reloader

Based on django channels and a simple include script

Install/use:
- `pip install git+https://github.com/tbscode/django-simple-reload.git`
- `INSTALLED_APPS += ["channels", "django_simple_reload"]`, set `USE_AUTO_RELOAD = True`
- urls: `path("", include("django_simple_reload.api"))`
- ASGI websockets: `path("ws/reload", ReloadConsumer.as_asgi())` in `websocket_urlpatterns` (import from `django_simple_reload.consumer`)
- template: `{% load reload_script_utils %}{% get_reload_script_tag %}` to inject the client
- run the update watcher in your entry script: `<your-python-package-path>/django_simple_reload/update_watcher.py`

Config: only `USE_AUTO_RELOAD` (bool) to toggle the script without removing the setup

> Currently the 'update_watcher.py' is customized to be used for webpack-stats files, adjust accordingly to your use-case