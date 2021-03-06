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
  form_fields = ['choice', 'actions_seq', 'real']

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
    self.player.is_exp = self.player.most_expected == self.player.choice
    if self.player.is_exp:
      self.participant.vars['is_exp_counter'] = self.participant.vars['is_exp_counter'] + 1
    self.participant.vars['sum_real'] = self.participant.vars['sum_real'] + self.player.real


class Condition10(Page):
  form_model = 'player'
  form_fields = ['submitted_answer_1', 'submitted_answer_2', 'submitted_answer_3',\
                  'submitted_answer_4', 'submitted_answer_5', 'submitted_answer_6',\
                  'submitted_answer_7', 'submitted_answer_8', 'submitted_answer_9', 'submitted_answer_10',\
                  'actions_seq_1', 'actions_seq_2', 'actions_seq_3',\
                  'actions_seq_4', 'actions_seq_5', 'actions_seq_6',\
                  'actions_seq_7', 'actions_seq_8', 'actions_seq_9', 'actions_seq_10',\
                  'real_sum_10']
  
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

    temp_counter = 1 if self.player.most_expected_1 == self.player.submitted_answer_1 else 0
    temp_counter = temp_counter + 1 if self.player.most_expected_2 == self.player.submitted_answer_2 else temp_counter
    temp_counter = temp_counter + 1 if self.player.most_expected_3 == self.player.submitted_answer_3 else temp_counter
    temp_counter = temp_counter + 1 if self.player.most_expected_4 == self.player.submitted_answer_4 else temp_counter
    temp_counter = temp_counter + 1 if self.player.most_expected_5 == self.player.submitted_answer_5 else temp_counter
    temp_counter = temp_counter + 1 if self.player.most_expected_6 == self.player.submitted_answer_6 else temp_counter
    temp_counter = temp_counter + 1 if self.player.most_expected_7 == self.player.submitted_answer_7 else temp_counter
    temp_counter = temp_counter + 1 if self.player.most_expected_8 == self.player.submitted_answer_8 else temp_counter
    temp_counter = temp_counter + 1 if self.player.most_expected_9 == self.player.submitted_answer_9 else temp_counter
    temp_counter = temp_counter + 1 if self.player.most_expected_10 == self.player.submitted_answer_10 else temp_counter

    self.participant.vars['is_exp_counter'] = self.participant.vars['is_exp_counter'] + temp_counter

    self.participant.vars['sum_real'] = self.participant.vars['sum_real'] + self.player.real_sum_10


class BetweenConditions(Page):
  def is_displayed(self):
    return (self.round_number == (Constants.rows_per_condition + 1)) and self.participant.vars['ind_cond_1_first'] \
    or (self.round_number == (int(Constants.rows_per_condition / 10) + 1)) and not self.participant.vars['ind_cond_1_first']


class ShortQuestionnaire(Page):
  form_model = 'player'
  form_fields = ['best_strategy_opinion','choose_better_strategy']
  
  def is_displayed(self):
    return self.round_number == Constants.num_rounds
  
  def before_next_page(self):
    self.player.get_payoff(\
      self.participant.vars['paying_round'], self.participant.vars['is_exp_counter'], self.participant.vars['sum_real']\
    )


class EndGamePaymStruct1(Page):
  def is_displayed(self):
    return self.round_number == Constants.num_rounds and Constants.payment_structure == 1
  
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


class EndGamePaymStruct2(Page):
  def is_displayed(self):
    return self.round_number == Constants.num_rounds and Constants.payment_structure == 2

  def vars_for_template(self):
    exp_counter = self.participant.vars['is_exp_counter']
    return dict(exp_counter = exp_counter)


class EndGamePaymStruct3(Page):
  def is_displayed(self):
    return self.round_number == Constants.num_rounds and Constants.payment_structure == 3

  def vars_for_template(self):
    sum_real = self.participant.vars['sum_real']
    return dict(sum_real = sum_real)

page_sequence = [
  Initial,
  Instructions,
  BetweenConditions,
  Condition1,
  Condition10,
  ShortQuestionnaire,
  EndGamePaymStruct1,
  EndGamePaymStruct2,
  EndGamePaymStruct3
]
