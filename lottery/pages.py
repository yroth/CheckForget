from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants


class Initial(Page):
  def is_displayed(self):
    return self.round_number == 1
  form_model = 'player'
  form_fields = ['age', 'gender']


class Results(Page):
  def is_displayed(self):
    return self.round_number == 10

class Condition1(Page):
  form_model = 'player'
  form_fields = ['choice']

class ShortQuestionnarie(Page):
  form_model = 'player'
  form_fields = ['best_strategy_opinion','choose_better_strategy']
  def is_displayed(self):
    return self.round_number == 10

class EndGame(Page):
  def is_displayed(self):
    return self.round_number == 10


page_sequence = [
  Initial,
  Condition1,
  ShortQuestionnarie,
  EndGame,
  Results
]
