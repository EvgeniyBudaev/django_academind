from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


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
  return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)
  except:
    return HttpResponseNotFound("This not page 404")

