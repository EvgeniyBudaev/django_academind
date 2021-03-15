from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
  'january': "This is january",
  'february': "This is february!",
  'march': "This is march!"
}


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
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("<h1>This month is not supported!</h1>")

