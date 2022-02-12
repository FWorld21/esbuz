command = '/home/admin/esbuz/venv/bin/gunicorn'
pythonpath = '/home/admin/esbuz/src'
bind = '127.0.0.1:8001'
workers = 5
user = 'admin'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=esbuz.settings'

