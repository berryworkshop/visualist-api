from django.contrib import admin
from .models import (
    # Contact,
    Vocabulary,
    Term,
    )

admin.site.register(Vocabulary)
admin.site.register(Term)
