from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import csv
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'lottery'
    players_per_group = None
    with open('lottery/test-problems.csv') as prob_file:
        data = list(csv.DictReader(prob_file))
        total_rows = len(data)
        temp_arr_1 = [i for i in range(0,int(total_rows / 2))]
        temp_arr_10 = [i for i in range(int(total_rows / 2),total_rows)]

    check_cost = 5
    rows_per_condition = int(total_rows / 2)
    num_rounds = int(total_rows / 2 + total_rows / 20)

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['data'] = Constants.data.copy()
            for p in self.session.get_participants():
                p.vars['ind_cond_1'] = random.sample(Constants.temp_arr_1, int(Constants.total_rows / 2))
                p.vars['ind_cond_10'] = random.sample(Constants.temp_arr_10, int(Constants.total_rows / 2))

                paying_round = random.randint(1, Constants.rows_per_condition)
                p.vars['paying_round'] = paying_round

        if self.round_number <= Constants.rows_per_condition:
            for p in self.session.get_participants():
                lottery_number_cond_1 = p.vars['ind_cond_1'][self.round_number - 1]
                p.vars['current_lottery_cond_1'] = self.session.vars['data'][lottery_number_cond_1 - 1]
                for i in range(1,6):
                    p.vars['probA' + str(i)] = p.vars['current_lottery_cond_1']['probA' + str(i)]
                    p.vars['realA' + str(i)] = p.vars['current_lottery_cond_1']['realA' + str(i)]
                    p.vars['probB' + str(i)] = p.vars['current_lottery_cond_1']['probB' + str(i)]
                    p.vars['realB' + str(i)] = p.vars['current_lottery_cond_1']['realB' + str(i)]

            for player, p in zip(self.get_players(), self.session.get_participants()):
                player.probA1 = p.vars['probA1']
                player.realA1 = p.vars['realA1']
                player.probB1 = p.vars['probB1']
                player.realB1 = p.vars['realB1']

                player.probA2 = p.vars['probA2']
                player.realA2 = p.vars['realA2']
                player.probB2 = p.vars['probB2']
                player.realB2 = p.vars['realB2']

                player.probA3 = p.vars['probA3']
                player.realA3 = p.vars['realA3']
                player.probB3 = p.vars['probB3']
                player.realB3 = p.vars['realB3']

                player.probA4 = p.vars['probA4']
                player.realA4 = p.vars['realA4']
                player.probB4 = p.vars['probB4']
                player.realB4 = p.vars['realB4']

                player.probA5 = p.vars['probA5']
                player.realA5 = p.vars['realA5']
                player.probB5 = p.vars['probB5']
                player.realB5 = p.vars['realB5']

        else:
            first_lottery_ind_cond_10 = (self.round_number - Constants.rows_per_condition - 1) * 10
            
            for p in self.session.get_participants():
                lottery_number_cond_10 = p.vars['ind_cond_10'][first_lottery_ind_cond_10:first_lottery_ind_cond_10 + 10]

                for k in lottery_number_cond_10:
                    current_lottery_cond_10 = self.session.vars['data'][k - 1]

                    for i in range(1,6):
                        suffix = str(i) + '_' + str(lottery_number_cond_10.index(k) + 1)
                        p.vars['probA' + suffix] = current_lottery_cond_10['probA' + str(i)]
                        p.vars['realA' + suffix] = current_lottery_cond_10['realA' + str(i)]
                        p.vars['probB' + suffix] = current_lottery_cond_10['probB' + str(i)]
                        p.vars['realB' + suffix] = current_lottery_cond_10['realB' + str(i)]

            for player, p in zip(self.get_players(), self.session.get_participants()):
                player.probA1_1 = p.vars['probA1_1']
                player.realA1_1 = p.vars['realA1_1']
                player.probB1_1 = p.vars['probB1_1']
                player.realB1_1 = p.vars['realB1_1']

                player.probA2_1 = p.vars['probA2_1']
                player.realA2_1 = p.vars['realA2_1']
                player.probB2_1 = p.vars['probB2_1']
                player.realB2_1 = p.vars['realB2_1']

                player.probA3_1 = p.vars['probA3_1']
                player.realA3_1 = p.vars['realA3_1']
                player.probB3_1 = p.vars['probB3_1']
                player.realB3_1 = p.vars['realB3_1']

                player.probA4_1 = p.vars['probA4_1']
                player.realA4_1 = p.vars['realA4_1']
                player.probB4_1 = p.vars['probB4_1']
                player.realB4_1 = p.vars['realB4_1']

                player.probA5_1 = p.vars['probA5_1']
                player.realA5_1 = p.vars['realA5_1']
                player.probB5_1 = p.vars['probB5_1']
                player.realB5_1 = p.vars['realB5_1']

                player.probA1_2 = p.vars['probA1_2']
                player.realA1_2 = p.vars['realA1_2']
                player.probB1_2 = p.vars['probB1_2']
                player.realB1_2 = p.vars['realB1_2']

                player.probA2_2 = p.vars['probA2_2']
                player.realA2_2 = p.vars['realA2_2']
                player.probB2_2 = p.vars['probB2_2']
                player.realB2_2 = p.vars['realB2_2']

                player.probA3_2 = p.vars['probA3_2']
                player.realA3_2 = p.vars['realA3_2']
                player.probB3_2 = p.vars['probB3_2']
                player.realB3_2 = p.vars['realB3_2']

                player.probA4_2 = p.vars['probA4_2']
                player.realA4_2 = p.vars['realA4_2']
                player.probB4_2 = p.vars['probB4_2']
                player.realB4_2 = p.vars['realB4_2']

                player.probA5_2 = p.vars['probA5_2']
                player.realA5_2 = p.vars['realA5_2']
                player.probB5_2 = p.vars['probB5_2']
                player.realB5_2 = p.vars['realB5_2']

                player.probA1_3 = p.vars['probA1_3']
                player.realA1_3 = p.vars['realA1_3']
                player.probB1_3 = p.vars['probB1_3']
                player.realB1_3 = p.vars['realB1_3']

                player.probA2_3 = p.vars['probA2_3']
                player.realA2_3 = p.vars['realA2_3']
                player.probB2_3 = p.vars['probB2_3']
                player.realB2_3 = p.vars['realB2_3']

                player.probA3_3 = p.vars['probA3_3']
                player.realA3_3 = p.vars['realA3_3']
                player.probB3_3 = p.vars['probB3_3']
                player.realB3_3 = p.vars['realB3_3']

                player.probA4_3 = p.vars['probA4_3']
                player.realA4_3 = p.vars['realA4_3']
                player.probB4_3 = p.vars['probB4_3']
                player.realB4_3 = p.vars['realB4_3']

                player.probA5_3 = p.vars['probA5_3']
                player.realA5_3 = p.vars['realA5_3']
                player.probB5_3 = p.vars['probB5_3']
                player.realB5_3 = p.vars['realB5_3']

                player.probA1_4 = p.vars['probA1_4']
                player.realA1_4 = p.vars['realA1_4']
                player.probB1_4 = p.vars['probB1_4']
                player.realB1_4 = p.vars['realB1_4']

                player.probA2_4 = p.vars['probA2_4']
                player.realA2_4 = p.vars['realA2_4']
                player.probB2_4 = p.vars['probB2_4']
                player.realB2_4 = p.vars['realB2_4']

                player.probA3_4 = p.vars['probA3_4']
                player.realA3_4 = p.vars['realA3_4']
                player.probB3_4 = p.vars['probB3_4']
                player.realB3_4 = p.vars['realB3_4']

                player.probA4_4 = p.vars['probA4_4']
                player.realA4_4 = p.vars['realA4_4']
                player.probB4_4 = p.vars['probB4_4']
                player.realB4_4 = p.vars['realB4_4']

                player.probA5_4 = p.vars['probA5_4']
                player.realA5_4 = p.vars['realA5_4']
                player.probB5_4 = p.vars['probB5_4']
                player.realB5_4 = p.vars['realB5_4']

                player.probA1_5 = p.vars['probA1_5']
                player.realA1_5 = p.vars['realA1_5']
                player.probB1_5 = p.vars['probB1_5']
                player.realB1_5 = p.vars['realB1_5']

                player.probA2_5 = p.vars['probA2_5']
                player.realA2_5 = p.vars['realA2_5']
                player.probB2_5 = p.vars['probB2_5']
                player.realB2_5 = p.vars['realB2_5']

                player.probA3_5 = p.vars['probA3_5']
                player.realA3_5 = p.vars['realA3_5']
                player.probB3_5 = p.vars['probB3_5']
                player.realB3_5 = p.vars['realB3_5']

                player.probA4_5 = p.vars['probA4_5']
                player.realA4_5 = p.vars['realA4_5']
                player.probB4_5 = p.vars['probB4_5']
                player.realB4_5 = p.vars['realB4_5']

                player.probA5_5 = p.vars['probA5_5']
                player.realA5_5 = p.vars['realA5_5']
                player.probB5_5 = p.vars['probB5_5']
                player.realB5_5 = p.vars['realB5_5']

                player.probA1_6 = p.vars['probA1_6']
                player.realA1_6 = p.vars['realA1_6']
                player.probB1_6 = p.vars['probB1_6']
                player.realB1_6 = p.vars['realB1_6']

                player.probA2_6 = p.vars['probA2_6']
                player.realA2_6 = p.vars['realA2_6']
                player.probB2_6 = p.vars['probB2_6']
                player.realB2_6 = p.vars['realB2_6']

                player.probA3_6 = p.vars['probA3_6']
                player.realA3_6 = p.vars['realA3_6']
                player.probB3_6 = p.vars['probB3_6']
                player.realB3_6 = p.vars['realB3_6']

                player.probA4_6 = p.vars['probA4_6']
                player.realA4_6 = p.vars['realA4_6']
                player.probB4_6 = p.vars['probB4_6']
                player.realB4_6 = p.vars['realB4_6']

                player.probA5_6 = p.vars['probA5_6']
                player.realA5_6 = p.vars['realA5_6']
                player.probB5_6 = p.vars['probB5_6']
                player.realB5_6 = p.vars['realB5_6']

                player.probA1_7 = p.vars['probA1_7']
                player.realA1_7 = p.vars['realA1_7']
                player.probB1_7 = p.vars['probB1_7']
                player.realB1_7 = p.vars['realB1_7']

                player.probA2_7 = p.vars['probA2_7']
                player.realA2_7 = p.vars['realA2_7']
                player.probB2_7 = p.vars['probB2_7']
                player.realB2_7 = p.vars['realB2_7']

                player.probA3_7 = p.vars['probA3_7']
                player.realA3_7 = p.vars['realA3_7']
                player.probB3_7 = p.vars['probB3_7']
                player.realB3_7 = p.vars['realB3_7']

                player.probA4_7 = p.vars['probA4_7']
                player.realA4_7 = p.vars['realA4_7']
                player.probB4_7 = p.vars['probB4_7']
                player.realB4_7 = p.vars['realB4_7']

                player.probA5_7 = p.vars['probA5_7']
                player.realA5_7 = p.vars['realA5_7']
                player.probB5_7 = p.vars['probB5_7']
                player.realB5_7 = p.vars['realB5_7']

                player.probA1_8 = p.vars['probA1_8']
                player.realA1_8 = p.vars['realA1_8']
                player.probB1_8 = p.vars['probB1_8']
                player.realB1_8 = p.vars['realB1_8']

                player.probA2_8 = p.vars['probA2_8']
                player.realA2_8 = p.vars['realA2_8']
                player.probB2_8 = p.vars['probB2_8']
                player.realB2_8 = p.vars['realB2_8']

                player.probA3_8 = p.vars['probA3_8']
                player.realA3_8 = p.vars['realA3_8']
                player.probB3_8 = p.vars['probB3_8']
                player.realB3_8 = p.vars['realB3_8']

                player.probA4_8 = p.vars['probA4_8']
                player.realA4_8 = p.vars['realA4_8']
                player.probB4_8 = p.vars['probB4_8']
                player.realB4_8 = p.vars['realB4_8']

                player.probA5_8 = p.vars['probA5_8']
                player.realA5_8 = p.vars['realA5_8']
                player.probB5_8 = p.vars['probB5_8']
                player.realB5_8 = p.vars['realB5_8']

                player.probA1_9 = p.vars['probA1_9']
                player.realA1_9 = p.vars['realA1_9']
                player.probB1_9 = p.vars['probB1_9']
                player.realB1_9 = p.vars['realB1_9']

                player.probA2_9 = p.vars['probA2_9']
                player.realA2_9 = p.vars['realA2_9']
                player.probB2_9 = p.vars['probB2_9']
                player.realB2_9 = p.vars['realB2_9']

                player.probA3_9 = p.vars['probA3_9']
                player.realA3_9 = p.vars['realA3_9']
                player.probB3_9 = p.vars['probB3_9']
                player.realB3_9 = p.vars['realB3_9']

                player.probA4_9 = p.vars['probA4_9']
                player.realA4_9 = p.vars['realA4_9']
                player.probB4_9 = p.vars['probB4_9']
                player.realB4_9 = p.vars['realB4_9']

                player.probA5_9 = p.vars['probA5_9']
                player.realA5_9 = p.vars['realA5_9']
                player.probB5_9 = p.vars['probB5_9']
                player.realB5_9 = p.vars['realB5_9']

                player.probA1_10 = p.vars['probA1_10']
                player.realA1_10 = p.vars['realA1_10']
                player.probB1_10 = p.vars['probB1_10']
                player.realB1_10 = p.vars['realB1_10']

                player.probA2_10 = p.vars['probA2_10']
                player.realA2_10 = p.vars['realA2_10']
                player.probB2_10 = p.vars['probB2_10']
                player.realB2_10 = p.vars['realB2_10']

                player.probA3_10 = p.vars['probA3_10']
                player.realA3_10 = p.vars['realA3_10']
                player.probB3_10 = p.vars['probB3_10']
                player.realB3_10 = p.vars['realB3_10']

                player.probA4_10 = p.vars['probA4_10']
                player.realA4_10 = p.vars['realA4_10']
                player.probB4_10 = p.vars['probB4_10']
                player.realB4_10 = p.vars['realB4_10']

                player.probA5_10 = p.vars['probA5_10']
                player.realA5_10 = p.vars['realA5_10']
                player.probB5_10 = p.vars['probB5_10']
                player.realB5_10 = p.vars['realB5_10']

class Group(BaseGroup):
    pass

def make_field():
    return models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)


class Player(BasePlayer):
    age = models.IntegerField()
    gender = models.StringField(
        choices=['male', 'female'],
        widget=widgets.RadioSelectHorizontal
    )
    choice = make_field()
    actions_seq = models.StringField()
    real = models.IntegerField()
    checked = models.BooleanField(
        initial=False
    )

    def realization(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1, self.realA2, self.realA3, self.realA4, self.realA5]
            prob_arr = [self.probA1, self.probA2, self.probA3, self.probA4, self.probA5]
        else:
            real_arr = [self.realB1, self.realB2, self.realB3, self.realB4, self.realB5]
            prob_arr = [self.probB1, self.probB2, self.probB3, self.probB4, self.probB5]
        self.real = np.random.choice(real_arr, 1, p=prob_arr)

    def get_payoff(self, paying_round):
        selected_player = self.in_round(paying_round)
        if selected_player.checked:
            self.payoff = c((selected_player.real - Constants.check_cost) * 0.01)
        else: 
            self.payoff = c(selected_player.real * 0.01)

    submitted_answer_1 = make_field()
    submitted_answer_2 = make_field()
    submitted_answer_3 = make_field()
    submitted_answer_4 = make_field()
    submitted_answer_5 = make_field()
    submitted_answer_6 = make_field()
    submitted_answer_7 = make_field()
    submitted_answer_8 = make_field()
    submitted_answer_9 = make_field()
    submitted_answer_10 = make_field()

    actions_seq_1 = models.StringField()
    actions_seq_2 = models.StringField()
    actions_seq_3 = models.StringField()
    actions_seq_4 = models.StringField()
    actions_seq_5 = models.StringField()
    actions_seq_6 = models.StringField()
    actions_seq_7 = models.StringField()
    actions_seq_8 = models.StringField()
    actions_seq_9 = models.StringField()
    actions_seq_10 = models.StringField()

    real_1 = models.IntegerField()
    real_2 = models.IntegerField()
    real_3 = models.IntegerField()
    real_4 = models.IntegerField()
    real_5 = models.IntegerField()
    real_6 = models.IntegerField()
    real_7 = models.IntegerField()
    real_8 = models.IntegerField()
    real_9 = models.IntegerField()
    real_10 = models.IntegerField()

    checked_1 = models.BooleanField()
    checked_2 = models.BooleanField()
    checked_3 = models.BooleanField()
    checked_4 = models.BooleanField()
    checked_5 = models.BooleanField()
    checked_6 = models.BooleanField()
    checked_7 = models.BooleanField()
    checked_8 = models.BooleanField()
    checked_9 = models.BooleanField()
    checked_10 = models.BooleanField()

    probA1 = models.StringField()
    probA2 = models.StringField()
    probA3 = models.StringField()
    probA4 = models.StringField()
    probA5 = models.StringField()

    realA1 = models.StringField()
    realA2 = models.StringField()
    realA3 = models.StringField()
    realA4 = models.StringField()
    realA5 = models.StringField()

    probB1 = models.StringField()
    probB2 = models.StringField()
    probB3 = models.StringField()
    probB4 = models.StringField()
    probB5 = models.StringField()

    realB1 = models.StringField()
    realB2 = models.StringField()
    realB3 = models.StringField()
    realB4 = models.StringField()
    realB5 = models.StringField()
    
    choose_better_strategy = models.StringField(
        choices=['Always to click on "check"', 'Never to click on "check"'],
        widget=widgets.RadioSelectHorizontal
    )

    best_strategy_opinion = models.StringField()

    realA1_1 = models.StringField()
    probA1_1 = models.StringField()
    realA2_1 = models.StringField()
    probA2_1 = models.StringField()
    realA3_1 = models.StringField()
    probA3_1 = models.StringField()
    realA4_1 = models.StringField()
    probA4_1 = models.StringField()
    realA5_1 = models.StringField()
    probA5_1 = models.StringField()

    realB1_1 = models.StringField()
    probB1_1 = models.StringField()
    realB2_1 = models.StringField()
    probB2_1 = models.StringField()
    realB3_1 = models.StringField()
    probB3_1 = models.StringField()
    realB4_1 = models.StringField()
    probB4_1 = models.StringField()
    realB5_1 = models.StringField()
    probB5_1 = models.StringField()

    probA1_2 = models.StringField()
    realA1_2 = models.StringField()
    probA2_2 = models.StringField()
    realA2_2 = models.StringField()
    probA3_2 = models.StringField()
    realA3_2 = models.StringField()
    probA4_2 = models.StringField()
    realA4_2 = models.StringField()
    probA5_2 = models.StringField()
    realA5_2 = models.StringField()

    probB1_2 = models.StringField()
    realB1_2 = models.StringField()
    probB2_2 = models.StringField()
    realB2_2 = models.StringField()
    probB3_2 = models.StringField()
    realB3_2 = models.StringField()
    probB4_2 = models.StringField()
    realB4_2 = models.StringField()
    probB5_2 = models.StringField()
    realB5_2 = models.StringField()

    probA1_3 = models.StringField()
    realA1_3 = models.StringField()
    probA2_3 = models.StringField()
    realA2_3 = models.StringField()
    probA3_3 = models.StringField()
    realA3_3 = models.StringField()
    probA4_3 = models.StringField()
    realA4_3 = models.StringField()
    probA5_3 = models.StringField()
    realA5_3 = models.StringField()

    probB1_3 = models.StringField()
    realB1_3 = models.StringField()
    probB2_3 = models.StringField()
    realB2_3 = models.StringField()
    probB3_3 = models.StringField()
    realB3_3 = models.StringField()
    probB4_3 = models.StringField()
    realB4_3 = models.StringField()
    probB5_3 = models.StringField()
    realB5_3 = models.StringField()

    probA1_4 = models.StringField()
    realA1_4 = models.StringField()
    probA2_4 = models.StringField()
    realA2_4 = models.StringField()
    probA3_4 = models.StringField()
    realA3_4 = models.StringField()
    probA4_4 = models.StringField()
    realA4_4 = models.StringField()
    probA5_4 = models.StringField()
    realA5_4 = models.StringField()

    probB1_4 = models.StringField()
    realB1_4 = models.StringField()
    probB2_4 = models.StringField()
    realB2_4 = models.StringField()
    probB3_4 = models.StringField()
    realB3_4 = models.StringField()
    probB4_4 = models.StringField()
    realB4_4 = models.StringField()
    probB5_4 = models.StringField()
    realB5_4 = models.StringField()

    probA1_5 = models.StringField()
    realA1_5 = models.StringField()
    probA2_5 = models.StringField()
    realA2_5 = models.StringField()
    probA3_5 = models.StringField()
    realA3_5 = models.StringField()
    probA4_5 = models.StringField()
    realA4_5 = models.StringField()
    probA5_5 = models.StringField()
    realA5_5 = models.StringField()

    probB1_5 = models.StringField()
    realB1_5 = models.StringField()
    probB2_5 = models.StringField()
    realB2_5 = models.StringField()
    probB3_5 = models.StringField()
    realB3_5 = models.StringField()
    probB4_5 = models.StringField()
    realB4_5 = models.StringField()
    probB5_5 = models.StringField()
    realB5_5 = models.StringField()

    probA1_6 = models.StringField()
    realA1_6 = models.StringField()
    probA2_6 = models.StringField()
    realA2_6 = models.StringField()

    probA3_6 = models.StringField()
    realA3_6 = models.StringField()
    probA4_6 = models.StringField()
    realA4_6 = models.StringField()
    probA5_6 = models.StringField()
    realA5_6 = models.StringField()

    probB1_6 = models.StringField()
    realB1_6 = models.StringField()
    probB2_6 = models.StringField()
    realB2_6 = models.StringField()
    probB3_6 = models.StringField()
    realB3_6 = models.StringField()
    probB4_6 = models.StringField()
    realB4_6 = models.StringField()
    probB5_6 = models.StringField()
    realB5_6 = models.StringField()

    probA1_7 = models.StringField()
    realA1_7 = models.StringField()
    probA2_7 = models.StringField()
    realA2_7 = models.StringField()
    probA3_7 = models.StringField()
    realA3_7 = models.StringField()
    probA4_7 = models.StringField()
    realA4_7 = models.StringField()
    probA5_7 = models.StringField()
    realA5_7 = models.StringField()

    probB1_7 = models.StringField()
    realB1_7 = models.StringField()
    probB2_7 = models.StringField()
    realB2_7 = models.StringField()
    probB3_7 = models.StringField()
    realB3_7 = models.StringField()
    probB4_7 = models.StringField()
    realB4_7 = models.StringField()
    probB5_7 = models.StringField()
    realB5_7 = models.StringField()

    probA1_8 = models.StringField()
    realA1_8 = models.StringField()
    probA2_8 = models.StringField()
    realA2_8 = models.StringField()
    probA3_8 = models.StringField()
    realA3_8 = models.StringField()
    probA4_8 = models.StringField()
    realA4_8 = models.StringField()
    probA5_8 = models.StringField()
    realA5_8 = models.StringField()

    probB1_8 = models.StringField()
    realB1_8 = models.StringField()
    probB2_8 = models.StringField()
    realB2_8 = models.StringField()
    probB3_8 = models.StringField()
    realB3_8 = models.StringField()
    probB4_8 = models.StringField()
    realB4_8 = models.StringField()
    probB5_8 = models.StringField()
    realB5_8 = models.StringField()

    probA1_9 = models.StringField()
    realA1_9 = models.StringField()
    probA2_9 = models.StringField()
    realA2_9 = models.StringField()
    probA3_9 = models.StringField()
    realA3_9 = models.StringField()
    probA4_9 = models.StringField()
    realA4_9 = models.StringField()
    probA5_9 = models.StringField()
    realA5_9 = models.StringField()

    probB1_9 = models.StringField()
    realB1_9 = models.StringField()
    probB2_9 = models.StringField()
    realB2_9 = models.StringField()
    probB3_9 = models.StringField()
    realB3_9 = models.StringField()
    probB4_9 = models.StringField()
    realB4_9 = models.StringField()
    probB5_9 = models.StringField()
    realB5_9 = models.StringField()

    probA1_10 = models.StringField()
    realA1_10 = models.StringField()
    probA2_10 = models.StringField()
    realA2_10 = models.StringField()
    probA3_10 = models.StringField()
    realA3_10 = models.StringField()
    probA4_10 = models.StringField()
    realA4_10 = models.StringField()
    probA5_10 = models.StringField()
    realA5_10 = models.StringField()

    probB1_10 = models.StringField()
    realB1_10 = models.StringField()
    probB2_10 = models.StringField()
    realB2_10 = models.StringField()
    probB3_10 = models.StringField()
    realB3_10 = models.StringField()
    probB4_10 = models.StringField()
    realB4_10 = models.StringField()
    probB5_10 = models.StringField()
    realB5_10 = models.StringField()

    def realization_1(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_1, self.realA2_1, self.realA3_1, self.realA4_1, self.realA5_1]
            prob_arr = [self.probA1_1, self.probA2_1, self.probA3_1, self.probA4_1, self.probA5_1]
        else:
            real_arr = [self.realB1_1, self.realB2_1, self.realB3_1, self.realB4_1, self.realB5_1]
            prob_arr = [self.probB1_1, self.probB2_1, self.probB3_1, self.probB4_1, self.probB5_1]
        self.real_1 = np.random.choice(real_arr, 1, p=prob_arr)

    def realization_2(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_2, self.realA2_2, self.realA3_2, self.realA4_2, self.realA5_2]
            prob_arr = [self.probA1_2, self.probA2_2, self.probA3_2, self.probA4_2, self.probA5_2]
        else:
            real_arr = [self.realB1_2, self.realB2_2, self.realB3_2, self.realB4_2, self.realB5_2]
            prob_arr = [self.probB1_2, self.probB2_2, self.probB3_2, self.probB4_2, self.probB5_2]
        self.real_2 = np.random.choice(real_arr, 1, p=prob_arr)

    def realization_3(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_3, self.realA2_3, self.realA3_3, self.realA4_3, self.realA5_3]
            prob_arr = [self.probA1_3, self.probA2_3, self.probA3_3, self.probA4_3, self.probA5_3]
        else:
            real_arr = [self.realB1_3, self.realB2_3, self.realB3_3, self.realB4_3, self.realB5_3]
            prob_arr = [self.probB1_3, self.probB2_3, self.probB3_3, self.probB4_3, self.probB5_3]
        self.real_3 = np.random.choice(real_arr, 1, p=prob_arr)

    def realization_4(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_4, self.realA2_4, self.realA3_4, self.realA4_4, self.realA5_4]
            prob_arr = [self.probA1_4, self.probA2_4, self.probA3_4, self.probA4_4, self.probA5_4]
        else:
            real_arr = [self.realB1_4, self.realB2_4, self.realB3_4, self.realB4_4, self.realB5_4]
            prob_arr = [self.probB1_4, self.probB2_4, self.probB3_4, self.probB4_4, self.probB5_4]
        self.real_4 = np.random.choice(real_arr, 1, p=prob_arr)

    def realization_5(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_5, self.realA2_5, self.realA3_5, self.realA4_5, self.realA5_5]
            prob_arr = [self.probA1_5, self.probA2_5, self.probA3_5, self.probA4_5, self.probA5_5]
        else:
            real_arr = [self.realB1_5, self.realB2_5, self.realB3_5, self.realB4_5, self.realB5_5]
            prob_arr = [self.probB1_5, self.probB2_5, self.probB3_5, self.probB4_5, self.probB5_5]
        self.real_5 = np.random.choice(real_arr, 1, p=prob_arr)

    def realization_6(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_6, self.realA2_6, self.realA3_6, self.realA4_6, self.realA5_6]
            prob_arr = [self.probA1_6, self.probA2_6, self.probA3_6, self.probA4_6, self.probA5_6]
        else:
            real_arr = [self.realB1_6, self.realB2_6, self.realB3_6, self.realB4_6, self.realB5_6]
            prob_arr = [self.probB1_6, self.probB2_6, self.probB3_6, self.probB4_6, self.probB5_6]
        self.real_6 = np.random.choice(real_arr, 1, p=prob_arr)

    def realization_7(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_7, self.realA2_7, self.realA3_7, self.realA4_7, self.realA5_7]
            prob_arr = [self.probA1_7, self.probA2_7, self.probA3_7, self.probA4_7, self.probA5_7]
        else:
            real_arr = [self.realB1_7, self.realB2_7, self.realB3_7, self.realB4_7, self.realB5_7]
            prob_arr = [self.probB1_7, self.probB2_7, self.probB3_7, self.probB4_7, self.probB5_7]
        self.real_7 = np.random.choice(real_arr, 1, p=prob_arr)

    def realization_8(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_8, self.realA2_8, self.realA3_8, self.realA4_8, self.realA5_8]
            prob_arr = [self.probA1_8, self.probA2_8, self.probA3_8, self.probA4_8, self.probA5_8]
        else:
            real_arr = [self.realB1_8, self.realB2_8, self.realB3_8, self.realB4_8, self.realB5_8]
            prob_arr = [self.probB1_8, self.probB2_8, self.probB3_8, self.probB4_8, self.probB5_8]
        self.real_8 = np.random.choice(real_arr, 1, p=prob_arr)

    def realization_9(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_9, self.realA2_9, self.realA3_9, self.realA4_9, self.realA5_9]
            prob_arr = [self.probA1_9, self.probA2_9, self.probA3_9, self.probA4_9, self.probA5_9]
        else:
            real_arr = [self.realB1_9, self.realB2_9, self.realB3_9, self.realB4_9, self.realB5_9]
            prob_arr = [self.probB1_9, self.probB2_9, self.probB3_9, self.probB4_9, self.probB5_9]
        self.real_9 = np.random.choice(real_arr, 1, p=prob_arr)

    def realization_10(self):
        if (self.choice == 'A'):
            real_arr = [self.realA1_10, self.realA2_10, self.realA3_10, self.realA4_10, self.realA5_10]
            prob_arr = [self.probA1_10, self.probA2_10, self.probA3_10, self.probA4_10, self.probA5_10]
        else:
            real_arr = [self.realB1_10, self.realB2_10, self.realB3_10, self.realB4_10, self.realB5_10]
            prob_arr = [self.probB1_10, self.probB2_10, self.probB3_10, self.probB4_10, self.probB5_10]
        self.real_10 = np.random.choice(real_arr, 1, p=prob_arr)
