# deve conter os imports no url principal e depois 
# deves conter no settings segundo script.


########### urls.py -- principal ################
from django.conf import settings
admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.SITE_TITLE
admin.site.index_title = settings.INDEX_TITLE





#################### settings.py ###########################
# adm Django config
    # Text to put in each page's <h1> (and above login form).
ADMIN_SITE_HEADER = "Administração de Contas"
    # Text to put at the end of each page's <title>.
SITE_TITLE = "Contas"
    # Text to put at the top of the admin index page.
INDEX_TITLE = "Bem - Vindo ao nosso site"