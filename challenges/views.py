from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


monthly_challenges_text = {
    "january": "This is month of January",
    "february": "This is month of February",
    "march": "This is month of March",
    "april": "This is My Birthday",
    "may": "This is month of May",
    "june": "This is month Of June",
    "july": "This is month of July",
    "august": "This is month of August",
    "september": "This is month of September",
    "october": "This is month of October",
    "november": "This is month of November",
    "december": "This is month of December"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges_text.keys())

    for month in months:
        capitalize_month = month.capitalize()
        url_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{url_path}'>{capitalize_month}</a></li>"
    response = f'<ul>{list_items}</ul>'
    return HttpResponse(response)


def monthly_challenges_by_number(request, month):
    try:
        selected_month = list(monthly_challenges_text.keys())[month - 1]
        correct_month = reverse("month-challenge", args=[selected_month])
        return HttpResponseRedirect(correct_month)
    except:
        return HttpResponseNotFound("Url not found")


def monthly_challenges(request, month):
    try:
        return render(request, 'challenges/challenges.html')
    except:
        return HttpResponseNotFound("Url not found")
