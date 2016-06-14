from django.shortcuts import render
import logging
# Create your views here.
from django.http import HttpResponse
from mysite.tasks import *

def x():
    id=add.delay(1,2)
    return id

def index(request):
    logger=logging.getLogger("abacus")
    logger.debug("HERE")
    logger.debug("HERE")
    logger.debug("HERE")
    logger.debug("HERE")
    a={}
    try:
       task=x()
    except Exception as e:
        logger.exception("DOne bad")
    return HttpResponse("Hello, world. You're at the polls index.")
