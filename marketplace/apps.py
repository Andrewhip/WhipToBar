from django.apps import AppConfig

<<<<<<< HEAD
class MarketplaceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketplace'

    def ready(self):
        import marketplace.signals
=======

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketplace'
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
