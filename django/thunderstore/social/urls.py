from django.urls import path

from .views import LinkedAccountsView, DeleteAccountView

settings_urls = [
    path('linked-accounts/', LinkedAccountsView.as_view(), name="settings.linked-accounts"),
    path('delete-account/', DeleteAccountView.as_view(), name="settings.delete-account"),
]
