from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

def get_items(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT a, b FROM some_table")
    items = cursor.fetchall()
    return items