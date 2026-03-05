### Tim simple django auto-reloader

Based on django channels and a simple include script

Install/use:
- `pip install git+https://github.com/tbscode/django-simple-reload.git`
- `INSTALLED_APPS += ["channels", "django_simple_reload"]`, set `USE_AUTO_RELOAD = True`
- urls: `path("", include(django_simple_reload.api.urlpatters))`
- ASGI websockets: `path("ws/reload", ReloadConsumer.as_asgi())` in `websocket_urlpatterns`
- template: `{% load reload_script_utils %}{% get_reload_script_tag %}` to inject the client

Config: only `USE_AUTO_RELOAD` (bool) to toggle the script without removing the setup
