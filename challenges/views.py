from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenge(request, month):
  challenge_text = None

  if month == 'january':
    challenge_text = "This is january"
  elif month == 'february':
    challenge_text = "This is february!"
  elif month == 'march':
    challenge_text = "This is march!"
  else:
    return HttpResponseNotFound("This month is not supported!")
  return HttpResponse(challenge_text)
