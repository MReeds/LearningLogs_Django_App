from django.contrib import admin
from .models import Topic
from .models import Entry

# Register your models here.
try:
    admin.site.register(Topic, order_insertion_by='name')
except Topic.AlreadyRegistered:
    pass

try:
    admin.site.register(Entry, order_insertion_by='name')
except Entry.AlreadyRegistered:
    pass