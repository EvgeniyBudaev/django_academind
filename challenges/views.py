from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse


monthly_challenges = {
  'january': "This is january",
  'february': "This is february!",
  'march': "This is march!",
  'april': None
}


def index(request):
  months = list(monthly_challenges.keys())
  return render(request, "challenges/index.html", {
    "months": months
  })


def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())
  if month > len(months):
    return HttpResponseNotFound("Invalid month")
  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month])  # challenge/january
  return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return render(request, "challenges/challenge.html", {
      "text": challenge_text,
      "month_name": month
    })
  except:
    raise Http404()

