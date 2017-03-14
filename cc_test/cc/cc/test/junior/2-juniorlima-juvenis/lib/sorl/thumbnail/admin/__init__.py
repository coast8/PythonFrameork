try:
    from django.forms import ClearableFileInput
except ImportError:
    from lib.sorl.thumbnail.admin.compat import AdminImageMixin
else:
    from lib.sorl.thumbnail.admin.current import AdminImageMixin

AdminInlineImageMixin = AdminImageMixin # backwards compatibility

