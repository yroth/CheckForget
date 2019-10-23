from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants


class Initial(Page):
  def is_displayed(self):
    return self.round_number == 1
  form_model = 'player'
  form_fields = ['age', 'gender']

class Instructions(Page):
  def is_displayed(self):
    return self.round_number == 1

class Condition1(Page):
  form_model = 'player'
  form_fields = ['choice', 'actions_seq']

  def is_displayed(self):
    return self.participant.vars['ind_cond_1_first'] and (self.round_number <= Constants.rows_per_condition) or \
    not self.participant.vars['ind_cond_1_first'] and (self.round_number > int(Constants.rows_per_condition / 10))

  def vars_for_template(self):
    return dict(
      question_number = self.round_number if self.participant.vars['ind_cond_1_first'] \
      else self.round_number - int(Constants.rows_per_condition / 10),
    )

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
    return self.participant.vars['ind_cond_1_first'] and (self.round_number > Constants.rows_per_condition) or \
    not self.participant.vars['ind_cond_1_first'] and (self.round_number <= int(Constants.rows_per_condition / 10))

  def vars_for_template(self):
    return dict(
      question_number = self.round_number - Constants.rows_per_condition \
        if self.participant.vars['ind_cond_1_first'] else self.round_number,
      total_questions_number = int(Constants.rows_per_condition / 10),
    )
  
  def before_next_page(self):
    self.player.checked_1 = 'C' in self.player.actions_seq_1
    self.player.checked_2 = 'C' in self.player.actions_seq_2
    self.player.checked_3 = 'C' in self.player.actions_seq_3
    self.player.checked_4 = 'C' in self.player.actions_seq_4
    self.player.checked_5 = 'C' in self.player.actions_seq_5
    self.player.checked_6 = 'C' in self.player.actions_seq_6
    self.player.checked_7 = 'C' in self.player.actions_seq_7
    self.player.checked_8 = 'C' in self.player.actions_seq_8
    self.player.checked_9 = 'C' in self.player.actions_seq_9
    self.player.checked_10 = 'C' in self.player.actions_seq_10
    self.player.realization_1()
    self.player.realization_2()
    self.player.realization_3()
    self.player.realization_4()
    self.player.realization_5()
    self.player.realization_6()
    self.player.realization_7()
    self.player.realization_8()
    self.player.realization_9()
    self.player.realization_10()


class BetweenConditions(Page):
  def is_displayed(self):
    return (self.round_number == (Constants.rows_per_condition + 1)) and self.participant.vars['ind_cond_1_first'] \
    or (self.round_number == (int(Constants.rows_per_condition / 10) + 1)) and not self.participant.vars['ind_cond_1_first']


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
  Instructions,
  BetweenConditions,
  Condition1,
  Condition10,
  ShortQuestionnarie,
  EndGame
]
