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
    "december": None
}


def index(request):
    months = list(monthly_challenges_text.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    try:
        selected_month = list(monthly_challenges_text.keys())[month - 1]
        correct_month = reverse("month-challenge", args=[selected_month])
        return HttpResponseRedirect(correct_month)
    except:
        return HttpResponseNotFound("Url not found")


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_text[month]
        return render(request, 'challenges/challenges.html', {
            "challenges_text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("Url not found")
