import os,django
import sys
from django.db import connection
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from polls.models import *

from mysite.tasks import *
id=add(1,2)
print id