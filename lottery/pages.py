from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants


class Initial(Page):
  def is_displayed(self):
    return self.round_number == 1
  form_model = 'player'
  form_fields = ['age', 'gender']

class Condition1(Page):
  form_model = 'player'
  form_fields = ['choice', 'actions_seq']
  def is_displayed(self):
    return self.round_number <= (Constants.rows_per_condition)
  def before_next_page(self):   
    self.player.checked = 'C' in self.player.actions_seq
    self.player.realization()

class Condition10(Page):
  form_model = 'player'
  form_fields = ['submitted_answer_1', 'submitted_answer_2', 'submitted_answer_3',\
                  'submitted_answer_4', 'submitted_answer_5', 'submitted_answer_6',\
                  'submitted_answer_7', 'submitted_answer_8', 'submitted_answer_9', 'submitted_answer_10',\
                  'actions_seq_1', 'actions_seq_2', 'actions_seq_3',\
                  'actions_seq_4', 'actions_seq_5', 'actions_seq_6',\
                  'actions_seq_7', 'actions_seq_8', 'actions_seq_9', 'actions_seq_10']
  def is_displayed(self):
    return self.round_number > (Constants.rows_per_condition)
  def vars_for_template(self):
    return dict(
      question_number = self.round_number - Constants.rows_per_condition,
      total_questions_number = int(Constants.rows_per_condition / 10),
    )

class BetweenConditions(Page):
  def is_displayed(self):
    return self.round_number == (Constants.rows_per_condition + 1)

class ShortQuestionnarie(Page):
  form_model = 'player'
  form_fields = ['best_strategy_opinion','choose_better_strategy']
  def is_displayed(self):
    return self.round_number == Constants.num_rounds
  def before_next_page(self):
    self.player.get_payoff(self.participant.vars['paying_round'])

class EndGame(Page):
  def is_displayed(self):
    return self.round_number == Constants.num_rounds
  def vars_for_template(self):
    paying_round = self.participant.vars['paying_round']
    player = self.player.in_round(paying_round)
    choice = player.choice
    real = player.real
    checked = player.checked
    return dict(
      paying_round=paying_round,
      choice=choice,
      real=real,
      checked=checked
    )


page_sequence = [
  Initial,
  Condition1,
  BetweenConditions,
  Condition10,
  ShortQuestionnarie,
  EndGame
]
