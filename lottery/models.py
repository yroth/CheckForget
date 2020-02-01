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
        temp_arr_1 = [i for i in range(1, int(total_rows / 2) + 1)]
        temp_arr_10 = [i for i in range(int(total_rows / 2) + 1, total_rows + 1)]

    # payments info
    check_cost = 5
    base_payment = 0
    # payment_structure should be one of {1, 2, 3}
    # 1: one randomly selected trial + base_payment
    # 2: accumulated points are chance for a 1$ bonus
    # 3: accumulated cents + base_payment
    payment_structure = 3

    # initial choice could be 'A' or 'B'
    # to disable static initial choice, set it to empty string
    initial_choice = ''

    # initial choice could be 'higher', 'worst' or 'prob_default'
    # to disable static initial choice, set it to empty string
    initial_ev_choice = ''

    # could be True or False
    # to disable it, set it to False
    show_feedback = True

    rows_per_condition = int(total_rows / 2)
    num_rounds = int(total_rows / 2 + total_rows / 20)

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['data'] = Constants.data.copy()
            for p in self.session.get_participants():
                p.vars['ind_cond_1_first'] = random.choice([True, False])

                p.vars['ind_cond_1'] = random.sample(Constants.temp_arr_1, int(Constants.total_rows / 2))
                p.vars['ind_cond_10'] = random.sample(Constants.temp_arr_10, int(Constants.total_rows / 2))

                num_cond_10_rounds = int(Constants.rows_per_condition / 10)

                paying_round = random.randint(1, Constants.rows_per_condition) if p.vars['ind_cond_1_first'] \
                else random.randint(num_cond_10_rounds + 1, num_cond_10_rounds + Constants.rows_per_condition)
                # for payment_structure == 1
                p.vars['paying_round'] = paying_round
                # for payment_structure == 2
                p.vars['is_exp_counter'] = 0
                # for payment_structure == 3
                p.vars['sum_real'] = 0

        for p in self.session.get_participants():
            if p.vars['ind_cond_1_first']:
                if self.round_number <= Constants.rows_per_condition:
                    lottery_number_cond_1 = p.vars['ind_cond_1'][self.round_number - 1]
                    self.fill_cond_1(lottery_number_cond_1, p)
                else:
                    first_lottery_ind_cond_10 = (self.round_number - Constants.rows_per_condition - 1) * 10
                    self.fill_cond_10(first_lottery_ind_cond_10, p)
            else:
                if self.round_number <= Constants.rows_per_condition / 10:
                    first_lottery_ind_cond_10 = (self.round_number - 1) * 10
                    self.fill_cond_10(first_lottery_ind_cond_10, p)
                else:
                    lottery_number_cond_1 = p.vars['ind_cond_1'][self.round_number - int(Constants.rows_per_condition / 10) - 1]
                    self.fill_cond_1(lottery_number_cond_1, p)


    def ev(self, p1, r1, p2, r2, p3, r3, p4, r4, p5, r5):
        return float(p1) * float(r1) + float(p2) * float(r2) + \
                    float(p3) * float(r3) + float(p4) * float(r4) + float(p5) * float(r5)
    
    def fill_cond_1(self, lottery_number_cond_1, p):
        p.vars['current_lottery_cond_1'] = self.session.vars['data'][lottery_number_cond_1 - 1]
        for i in range(1,6):
            p.vars['probA' + str(i)] = p.vars['current_lottery_cond_1']['probA' + str(i)]
            p.vars['realA' + str(i)] = p.vars['current_lottery_cond_1']['realA' + str(i)]
            p.vars['probB' + str(i)] = p.vars['current_lottery_cond_1']['probB' + str(i)]
            p.vars['realB' + str(i)] = p.vars['current_lottery_cond_1']['realB' + str(i)]

        # random initial choice for condition-1
        # to enable it, uncomment next three lines 
        # for player in self.get_players():
        #     if p == player.participant:
        #         player.random_initial_choice = random.choice(['A', 'B'])

        for player in self.get_players():
            if p == player.participant:
                player.probA1 = '{:.2f}'.format(float(p.vars['probA1']))
                player.realA1 = p.vars['realA1']
                player.probB1 = '{:.2f}'.format(float(p.vars['probB1']))
                player.realB1 = p.vars['realB1']

                player.probA2 = '{:.2f}'.format(float(p.vars['probA2']))
                player.realA2 = p.vars['realA2']
                player.probB2 = '{:.2f}'.format(float(p.vars['probB2']))
                player.realB2 = p.vars['realB2']

                player.probA3 = '{:.2f}'.format(float(p.vars['probA3']))
                player.realA3 = p.vars['realA3']
                player.probB3 = '{:.2f}'.format(float(p.vars['probB3']))
                player.realB3 = p.vars['realB3']

                player.probA4 = '{:.2f}'.format(float(p.vars['probA4']))
                player.realA4 = p.vars['realA4']
                player.probB4 = '{:.2f}'.format(float(p.vars['probB4']))
                player.realB4 = p.vars['realB4']

                player.probA5 = '{:.2f}'.format(float(p.vars['probA5']))
                player.realA5 = p.vars['realA5']
                player.probB5 = '{:.2f}'.format(float(p.vars['probB5']))
                player.realB5 = p.vars['realB5']

                player.ev_a = self.ev(player.probA1, player.realA1, player.probA2, player.realA2,\
                    player.probA3, player.realA3, player.probA4, player.realA4, player.probA5, player.realA5)
                player.ev_b = self.ev(player.probB1, player.realB1, player.probB2, player.realB2,\
                    player.probB3, player.realB3, player.probB4, player.realB4, player.probB5, player.realB5)

                # for payment_structure == 2
                player.most_expected = 'A' if player.ev_a > player.ev_b else 'B'

                if (Constants.initial_ev_choice == 'higher'):
                    player.initial_choice_ev = 'A' if player.ev_a > player.ev_b else 'B'
                elif (Constants.initial_ev_choice == 'worst'):
                    player.initial_choice_ev = 'A' if player.ev_a <= player.ev_b else 'B'
                elif (Constants.initial_ev_choice == 'prob_default'):
                    higher = 'A' if player.ev_a > player.ev_b else 'B'
                    worst = 'A' if player.ev_a <= player.ev_b else 'B'
                    player.initial_choice_ev = higher if self.round_number < Constants.rows_per_condition * 0.8 else worst

    def fill_cond_10(self, first_lottery_ind_cond_10, p):
        lottery_number_cond_10 = p.vars['ind_cond_10'][first_lottery_ind_cond_10:first_lottery_ind_cond_10 + 10]

        for k in lottery_number_cond_10:
            current_lottery_cond_10 = self.session.vars['data'][k - 1]

            for i in range(1,6):
                suffix = str(i) + '_' + str(lottery_number_cond_10.index(k) + 1)
                p.vars['probA' + suffix] = current_lottery_cond_10['probA' + str(i)]
                p.vars['realA' + suffix] = current_lottery_cond_10['realA' + str(i)]
                p.vars['probB' + suffix] = current_lottery_cond_10['probB' + str(i)]
                p.vars['realB' + suffix] = current_lottery_cond_10['realB' + str(i)]

        # random initial choice for condition-10
        # to enable it, uncomment next 12 lines 
        # for player in self.get_players():
        #     if p == player.participant:
        #         player.random_initial_choice_1 = random.choice(['A', 'B'])
        #         player.random_initial_choice_2 = random.choice(['A', 'B'])
        #         player.random_initial_choice_3 = random.choice(['A', 'B'])
        #         player.random_initial_choice_4 = random.choice(['A', 'B'])
        #         player.random_initial_choice_5 = random.choice(['A', 'B'])
        #         player.random_initial_choice_6 = random.choice(['A', 'B'])
        #         player.random_initial_choice_7 = random.choice(['A', 'B'])
        #         player.random_initial_choice_8 = random.choice(['A', 'B'])
        #         player.random_initial_choice_9 = random.choice(['A', 'B'])
        #         player.random_initial_choice_10 = random.choice(['A', 'B'])

        for player in self.get_players():
            if p == player.participant:
                player.probA1_1 = '{:.2f}'.format(float(p.vars['probA1_1']))
                player.realA1_1 = p.vars['realA1_1']
                player.probB1_1 = '{:.2f}'.format(float(p.vars['probB1_1']))
                player.realB1_1 = p.vars['realB1_1']

                player.probA2_1 = '{:.2f}'.format(float(p.vars['probA2_1']))
                player.realA2_1 = p.vars['realA2_1']
                player.probB2_1 = '{:.2f}'.format(float(p.vars['probB2_1']))
                player.realB2_1 = p.vars['realB2_1']

                player.probA3_1 = '{:.2f}'.format(float(p.vars['probA3_1']))
                player.realA3_1 = p.vars['realA3_1']
                player.probB3_1 = '{:.2f}'.format(float(p.vars['probB3_1']))
                player.realB3_1 = p.vars['realB3_1']

                player.probA4_1 = '{:.2f}'.format(float(p.vars['probA4_1']))
                player.realA4_1 = p.vars['realA4_1']
                player.probB4_1 = '{:.2f}'.format(float(p.vars['probB4_1']))
                player.realB4_1 = p.vars['realB4_1']

                player.probA5_1 = '{:.2f}'.format(float(p.vars['probA5_1']))
                player.realA5_1 = p.vars['realA5_1']
                player.probB5_1 = '{:.2f}'.format(float(p.vars['probB5_1']))
                player.realB5_1 = p.vars['realB5_1']

                player.probA1_2 = '{:.2f}'.format(float(p.vars['probA1_2']))
                player.realA1_2 = p.vars['realA1_2']
                player.probB1_2 = '{:.2f}'.format(float(p.vars['probB1_2']))
                player.realB1_2 = p.vars['realB1_2']

                player.probA2_2 = '{:.2f}'.format(float(p.vars['probA2_2']))
                player.realA2_2 = p.vars['realA2_2']
                player.probB2_2 = '{:.2f}'.format(float(p.vars['probB2_2']))
                player.realB2_2 = p.vars['realB2_2']

                player.probA3_2 = '{:.2f}'.format(float(p.vars['probA3_2']))
                player.realA3_2 = p.vars['realA3_2']
                player.probB3_2 = '{:.2f}'.format(float(p.vars['probB3_2']))
                player.realB3_2 = p.vars['realB3_2']

                player.probA4_2 = '{:.2f}'.format(float(p.vars['probA4_2']))
                player.realA4_2 = p.vars['realA4_2']
                player.probB4_2 = '{:.2f}'.format(float(p.vars['probB4_2']))
                player.realB4_2 = p.vars['realB4_2']

                player.probA5_2 = '{:.2f}'.format(float(p.vars['probA5_2']))
                player.realA5_2 = p.vars['realA5_2']
                player.probB5_2 = '{:.2f}'.format(float(p.vars['probB5_2']))
                player.realB5_2 = p.vars['realB5_2']

                player.probA1_3 = '{:.2f}'.format(float(p.vars['probA1_3']))
                player.realA1_3 = p.vars['realA1_3']
                player.probB1_3 = '{:.2f}'.format(float(p.vars['probB1_3']))
                player.realB1_3 = p.vars['realB1_3']

                player.probA2_3 = '{:.2f}'.format(float(p.vars['probA2_3']))
                player.realA2_3 = p.vars['realA2_3']
                player.probB2_3 = '{:.2f}'.format(float(p.vars['probB2_3']))
                player.realB2_3 = p.vars['realB2_3']

                player.probA3_3 = '{:.2f}'.format(float(p.vars['probA3_3']))
                player.realA3_3 = p.vars['realA3_3']
                player.probB3_3 = '{:.2f}'.format(float(p.vars['probB3_3']))
                player.realB3_3 = p.vars['realB3_3']

                player.probA4_3 = '{:.2f}'.format(float(p.vars['probA4_3']))
                player.realA4_3 = p.vars['realA4_3']
                player.probB4_3 = '{:.2f}'.format(float(p.vars['probB4_3']))
                player.realB4_3 = p.vars['realB4_3']

                player.probA5_3 = '{:.2f}'.format(float(p.vars['probA5_3']))
                player.realA5_3 = p.vars['realA5_3']
                player.probB5_3 = '{:.2f}'.format(float(p.vars['probB5_3']))
                player.realB5_3 = p.vars['realB5_3']

                player.probA1_4 = '{:.2f}'.format(float(p.vars['probA1_4']))
                player.realA1_4 = p.vars['realA1_4']
                player.probB1_4 = '{:.2f}'.format(float(p.vars['probB1_4']))
                player.realB1_4 = p.vars['realB1_4']

                player.probA2_4 = '{:.2f}'.format(float(p.vars['probA2_4']))
                player.realA2_4 = p.vars['realA2_4']
                player.probB2_4 = '{:.2f}'.format(float(p.vars['probB2_4']))
                player.realB2_4 = p.vars['realB2_4']

                player.probA3_4 = '{:.2f}'.format(float(p.vars['probA3_4']))
                player.realA3_4 = p.vars['realA3_4']
                player.probB3_4 = '{:.2f}'.format(float(p.vars['probB3_4']))
                player.realB3_4 = p.vars['realB3_4']

                player.probA4_4 = '{:.2f}'.format(float(p.vars['probA4_4']))
                player.realA4_4 = p.vars['realA4_4']
                player.probB4_4 = '{:.2f}'.format(float(p.vars['probB4_4']))
                player.realB4_4 = p.vars['realB4_4']

                player.probA5_4 = '{:.2f}'.format(float(p.vars['probA5_4']))
                player.realA5_4 = p.vars['realA5_4']
                player.probB5_4 = '{:.2f}'.format(float(p.vars['probB5_4']))
                player.realB5_4 = p.vars['realB5_4']

                player.probA1_5 = '{:.2f}'.format(float(p.vars['probA1_5']))
                player.realA1_5 = p.vars['realA1_5']
                player.probB1_5 = '{:.2f}'.format(float(p.vars['probB1_5']))
                player.realB1_5 = p.vars['realB1_5']

                player.probA2_5 = '{:.2f}'.format(float(p.vars['probA2_5']))
                player.realA2_5 = p.vars['realA2_5']
                player.probB2_5 = '{:.2f}'.format(float(p.vars['probB2_5']))
                player.realB2_5 = p.vars['realB2_5']

                player.probA3_5 = '{:.2f}'.format(float(p.vars['probA3_5']))
                player.realA3_5 = p.vars['realA3_5']
                player.probB3_5 = '{:.2f}'.format(float(p.vars['probB3_5']))
                player.realB3_5 = p.vars['realB3_5']

                player.probA4_5 = '{:.2f}'.format(float(p.vars['probA4_5']))
                player.realA4_5 = p.vars['realA4_5']
                player.probB4_5 = '{:.2f}'.format(float(p.vars['probB4_5']))
                player.realB4_5 = p.vars['realB4_5']

                player.probA5_5 = '{:.2f}'.format(float(p.vars['probA5_5']))
                player.realA5_5 = p.vars['realA5_5']
                player.probB5_5 = '{:.2f}'.format(float(p.vars['probB5_5']))
                player.realB5_5 = p.vars['realB5_5']

                player.probA1_6 = '{:.2f}'.format(float(p.vars['probA1_6']))
                player.realA1_6 = p.vars['realA1_6']
                player.probB1_6 = '{:.2f}'.format(float(p.vars['probB1_6']))
                player.realB1_6 = p.vars['realB1_6']

                player.probA2_6 = '{:.2f}'.format(float(p.vars['probA2_6']))
                player.realA2_6 = p.vars['realA2_6']
                player.probB2_6 = '{:.2f}'.format(float(p.vars['probB2_6']))
                player.realB2_6 = p.vars['realB2_6']

                player.probA3_6 = '{:.2f}'.format(float(p.vars['probA3_6']))
                player.realA3_6 = p.vars['realA3_6']
                player.probB3_6 = '{:.2f}'.format(float(p.vars['probB3_6']))
                player.realB3_6 = p.vars['realB3_6']

                player.probA4_6 = '{:.2f}'.format(float(p.vars['probA4_6']))
                player.realA4_6 = p.vars['realA4_6']
                player.probB4_6 = '{:.2f}'.format(float(p.vars['probB4_6']))
                player.realB4_6 = p.vars['realB4_6']

                player.probA5_6 = '{:.2f}'.format(float(p.vars['probA5_6']))
                player.realA5_6 = p.vars['realA5_6']
                player.probB5_6 = '{:.2f}'.format(float(p.vars['probB5_6']))
                player.realB5_6 = p.vars['realB5_6']

                player.probA1_7 = '{:.2f}'.format(float(p.vars['probA1_7']))
                player.realA1_7 = p.vars['realA1_7']
                player.probB1_7 = '{:.2f}'.format(float(p.vars['probB1_7']))
                player.realB1_7 = p.vars['realB1_7']

                player.probA2_7 = '{:.2f}'.format(float(p.vars['probA2_7']))
                player.realA2_7 = p.vars['realA2_7']
                player.probB2_7 = '{:.2f}'.format(float(p.vars['probB2_7']))
                player.realB2_7 = p.vars['realB2_7']

                player.probA3_7 = '{:.2f}'.format(float(p.vars['probA3_7']))
                player.realA3_7 = p.vars['realA3_7']
                player.probB3_7 = '{:.2f}'.format(float(p.vars['probB3_7']))
                player.realB3_7 = p.vars['realB3_7']

                player.probA4_7 = '{:.2f}'.format(float(p.vars['probA4_7']))
                player.realA4_7 = p.vars['realA4_7']
                player.probB4_7 = '{:.2f}'.format(float(p.vars['probB4_7']))
                player.realB4_7 = p.vars['realB4_7']

                player.probA5_7 = '{:.2f}'.format(float(p.vars['probA5_7']))
                player.realA5_7 = p.vars['realA5_7']
                player.probB5_7 = '{:.2f}'.format(float(p.vars['probB5_7']))
                player.realB5_7 = p.vars['realB5_7']

                player.probA1_8 = '{:.2f}'.format(float(p.vars['probA1_8']))
                player.realA1_8 = p.vars['realA1_8']
                player.probB1_8 = '{:.2f}'.format(float(p.vars['probB1_8']))
                player.realB1_8 = p.vars['realB1_8']

                player.probA2_8 = '{:.2f}'.format(float(p.vars['probA2_8']))
                player.realA2_8 = p.vars['realA2_8']
                player.probB2_8 = '{:.2f}'.format(float(p.vars['probB2_8']))
                player.realB2_8 = p.vars['realB2_8']

                player.probA3_8 = '{:.2f}'.format(float(p.vars['probA3_8']))
                player.realA3_8 = p.vars['realA3_8']
                player.probB3_8 = '{:.2f}'.format(float(p.vars['probB3_8']))
                player.realB3_8 = p.vars['realB3_8']

                player.probA4_8 = '{:.2f}'.format(float(p.vars['probA4_8']))
                player.realA4_8 = p.vars['realA4_8']
                player.probB4_8 = '{:.2f}'.format(float(p.vars['probB4_8']))
                player.realB4_8 = p.vars['realB4_8']

                player.probA5_8 = '{:.2f}'.format(float(p.vars['probA5_8']))
                player.realA5_8 = p.vars['realA5_8']
                player.probB5_8 = '{:.2f}'.format(float(p.vars['probB5_8']))
                player.realB5_8 = p.vars['realB5_8']

                player.probA1_9 = '{:.2f}'.format(float(p.vars['probA1_9']))
                player.realA1_9 = p.vars['realA1_9']
                player.probB1_9 = '{:.2f}'.format(float(p.vars['probB1_9']))
                player.realB1_9 = p.vars['realB1_9']

                player.probA2_9 = '{:.2f}'.format(float(p.vars['probA2_9']))
                player.realA2_9 = p.vars['realA2_9']
                player.probB2_9 = '{:.2f}'.format(float(p.vars['probB2_9']))
                player.realB2_9 = p.vars['realB2_9']

                player.probA3_9 = '{:.2f}'.format(float(p.vars['probA3_9']))
                player.realA3_9 = p.vars['realA3_9']
                player.probB3_9 = '{:.2f}'.format(float(p.vars['probB3_9']))
                player.realB3_9 = p.vars['realB3_9']

                player.probA4_9 = '{:.2f}'.format(float(p.vars['probA4_9']))
                player.realA4_9 = p.vars['realA4_9']
                player.probB4_9 = '{:.2f}'.format(float(p.vars['probB4_9']))
                player.realB4_9 = p.vars['realB4_9']

                player.probA5_9 = '{:.2f}'.format(float(p.vars['probA5_9']))
                player.realA5_9 = p.vars['realA5_9']
                player.probB5_9 = '{:.2f}'.format(float(p.vars['probB5_9']))
                player.realB5_9 = p.vars['realB5_9']

                player.probA1_10 = '{:.2f}'.format(float(p.vars['probA1_10']))
                player.realA1_10 = p.vars['realA1_10']
                player.probB1_10 = '{:.2f}'.format(float(p.vars['probB1_10']))
                player.realB1_10 = p.vars['realB1_10']

                player.probA2_10 = '{:.2f}'.format(float(p.vars['probA2_10']))
                player.realA2_10 = p.vars['realA2_10']
                player.probB2_10 = '{:.2f}'.format(float(p.vars['probB2_10']))
                player.realB2_10 = p.vars['realB2_10']

                player.probA3_10 = '{:.2f}'.format(float(p.vars['probA3_10']))
                player.realA3_10 = p.vars['realA3_10']
                player.probB3_10 = '{:.2f}'.format(float(p.vars['probB3_10']))
                player.realB3_10 = p.vars['realB3_10']

                player.probA4_10 = '{:.2f}'.format(float(p.vars['probA4_10']))
                player.realA4_10 = p.vars['realA4_10']
                player.probB4_10 = '{:.2f}'.format(float(p.vars['probB4_10']))
                player.realB4_10 = p.vars['realB4_10']

                player.probA5_10 = '{:.2f}'.format(float(p.vars['probA5_10']))
                player.realA5_10 = p.vars['realA5_10']
                player.probB5_10 = '{:.2f}'.format(float(p.vars['probB5_10']))
                player.realB5_10 = p.vars['realB5_10']

                player.ev_a_1 = self.ev(player.probA1_1, player.realA1_1, player.probA2_1, player.realA2_1, \
                    player.probA3_1, player.realA3_1, player.probA4_1, player.realA4_1, player.probA5_1, player.realA5_1)
                player.ev_b_1 = self.ev(player.probB1_1, player.realB1_1, player.probB2_1, player.realB2_1, \
                    player.probB3_1, player.realB3_1, player.probB4_1, player.realB4_1, player.probB5_1, player.realB5_1)

                player.ev_a_2 = self.ev(player.probA1_2, player.realA1_2, player.probA2_2, player.realA2_2, \
                    player.probA3_2, player.realA3_2, player.probA4_2, player.realA4_2, player.probA5_2, player.realA5_2)
                player.ev_b_2 = self.ev(player.probB1_2, player.realB1_2, player.probB2_2, player.realB2_2, \
                    player.probB3_2, player.realB3_2, player.probB4_2, player.realB4_2, player.probB5_2, player.realB5_2)

                player.ev_a_3 = self.ev(player.probA1_3, player.realA1_3, player.probA2_3, player.realA2_3, \
                    player.probA3_3, player.realA3_3, player.probA4_3, player.realA4_3, player.probA5_3, player.realA5_3)
                player.ev_b_3 = self.ev(player.probB1_3, player.realB1_3, player.probB2_3, player.realB2_3, \
                    player.probB3_3, player.realB3_3, player.probB4_3, player.realB4_3, player.probB5_3, player.realB5_3)

                player.ev_a_4 = self.ev(player.probA1_4, player.realA1_4, player.probA2_4, player.realA2_4, \
                    player.probA3_4, player.realA3_4, player.probA4_4, player.realA4_4, player.probA5_4, player.realA5_4)
                player.ev_b_4 = self.ev(player.probB1_4, player.realB1_4, player.probB2_4, player.realB2_4, \
                    player.probB3_4, player.realB3_4, player.probB4_4, player.realB4_4, player.probB5_4, player.realB5_4)

                player.ev_a_5 = self.ev(player.probA1_5, player.realA1_5, player.probA2_5, player.realA2_5, \
                    player.probA3_5, player.realA3_5, player.probA4_5, player.realA4_5, player.probA5_5, player.realA5_5)
                player.ev_b_5 = self.ev(player.probB1_5, player.realB1_5, player.probB2_5, player.realB2_5, \
                    player.probB3_5, player.realB3_5, player.probB4_5, player.realB4_5, player.probB5_5, player.realB5_5)

                player.ev_a_6 = self.ev(player.probA1_6, player.realA1_6, player.probA2_6, player.realA2_6, \
                    player.probA3_6, player.realA3_6, player.probA4_6, player.realA4_6, player.probA5_6, player.realA5_6)
                player.ev_b_6 = self.ev(player.probB1_6, player.realB1_6, player.probB2_6, player.realB2_6, \
                    player.probB3_6, player.realB3_6, player.probB4_6, player.realB4_6, player.probB5_6, player.realB5_6)

                player.ev_a_7 = self.ev(player.probA1_7, player.realA1_7, player.probA2_7, player.realA2_7, \
                    player.probA3_7, player.realA3_7, player.probA4_7, player.realA4_7, player.probA5_7, player.realA5_7)
                player.ev_b_7 = self.ev(player.probB1_7, player.realB1_7, player.probB2_7, player.realB2_7, \
                    player.probB3_7, player.realB3_7, player.probB4_7, player.realB4_7, player.probB5_7, player.realB5_7)

                player.ev_a_8 = self.ev(player.probA1_8, player.realA1_8, player.probA2_8, player.realA2_8, \
                    player.probA3_8, player.realA3_8, player.probA4_8, player.realA4_8, player.probA5_8, player.realA5_8)
                player.ev_b_8 = self.ev(player.probB1_8, player.realB1_8, player.probB2_8, player.realB2_8, \
                    player.probB3_8, player.realB3_8, player.probB4_8, player.realB4_8, player.probB5_8, player.realB5_8)

                player.ev_a_9 = self.ev(player.probA1_9, player.realA1_9, player.probA2_9, player.realA2_9, \
                    player.probA3_9, player.realA3_9, player.probA4_9, player.realA4_9, player.probA5_9, player.realA5_9)
                player.ev_b_9 = self.ev(player.probB1_9, player.realB1_9, player.probB2_9, player.realB2_9, \
                    player.probB3_9, player.realB3_9, player.probB4_9, player.realB4_9, player.probB5_9, player.realB5_9)

                player.ev_a_10 = self.ev(player.probA1_10, player.realA1_10, player.probA2_10, player.realA2_10, \
                    player.probA3_10, player.realA3_10, player.probA4_10, player.realA4_10, player.probA5_10, player.realA5_10)
                player.ev_b_10 = self.ev(player.probB1_10, player.realB1_10, player.probB2_10, player.realB2_10, \
                    player.probB3_10, player.realB3_10, player.probB4_10, player.realB4_10, player.probB5_10, player.realB5_10)

                # for payment_structure == 2
                player.most_expected_1 = 'A' if player.ev_a_1 > player.ev_b_1 else 'B'
                player.most_expected_2 = 'A' if player.ev_a_2 > player.ev_b_2 else 'B'
                player.most_expected_3 = 'A' if player.ev_a_3 > player.ev_b_3 else 'B'
                player.most_expected_4 = 'A' if player.ev_a_4 > player.ev_b_4 else 'B'
                player.most_expected_5 = 'A' if player.ev_a_5 > player.ev_b_5 else 'B'
                player.most_expected_6 = 'A' if player.ev_a_6 > player.ev_b_6 else 'B'
                player.most_expected_7 = 'A' if player.ev_a_7 > player.ev_b_7 else 'B'
                player.most_expected_8 = 'A' if player.ev_a_8 > player.ev_b_8 else 'B'
                player.most_expected_9 = 'A' if player.ev_a_9 > player.ev_b_9 else 'B'
                player.most_expected_10 = 'A' if player.ev_a_10 > player.ev_b_10 else 'B'

                if (Constants.initial_ev_choice == 'higher'):
                    player.initial_choice_ev_1 = 'A' if player.ev_a_1 > player.ev_b_1 else 'B'
                    player.initial_choice_ev_2 = 'A' if player.ev_a_2 > player.ev_b_2 else 'B'
                    player.initial_choice_ev_3 = 'A' if player.ev_a_3 > player.ev_b_3 else 'B'
                    player.initial_choice_ev_4 = 'A' if player.ev_a_4 > player.ev_b_4 else 'B'
                    player.initial_choice_ev_5 = 'A' if player.ev_a_5 > player.ev_b_5 else 'B'
                    player.initial_choice_ev_6 = 'A' if player.ev_a_6 > player.ev_b_6 else 'B'
                    player.initial_choice_ev_7 = 'A' if player.ev_a_7 > player.ev_b_7 else 'B'
                    player.initial_choice_ev_8 = 'A' if player.ev_a_8 > player.ev_b_8 else 'B'
                    player.initial_choice_ev_9 = 'A' if player.ev_a_9 > player.ev_b_9 else 'B'
                    player.initial_choice_ev_10 = 'A' if player.ev_a_10 > player.ev_b_10 else 'B'
                elif (Constants.initial_ev_choice == 'worst'):
                    player.initial_choice_ev_1 = 'A' if player.ev_a_1 <= player.ev_b_1 else 'B'
                    player.initial_choice_ev_2 = 'A' if player.ev_a_2 <= player.ev_b_2 else 'B'
                    player.initial_choice_ev_3 = 'A' if player.ev_a_3 <= player.ev_b_3 else 'B'
                    player.initial_choice_ev_4 = 'A' if player.ev_a_4 <= player.ev_b_4 else 'B'
                    player.initial_choice_ev_5 = 'A' if player.ev_a_5 <= player.ev_b_5 else 'B'
                    player.initial_choice_ev_6 = 'A' if player.ev_a_6 <= player.ev_b_6 else 'B'
                    player.initial_choice_ev_7 = 'A' if player.ev_a_7 <= player.ev_b_7 else 'B'
                    player.initial_choice_ev_8 = 'A' if player.ev_a_8 <= player.ev_b_8 else 'B'
                    player.initial_choice_ev_9 = 'A' if player.ev_a_9 <= player.ev_b_9 else 'B'
                    player.initial_choice_ev_10 = 'A' if player.ev_a_10 <= player.ev_b_10 else 'B'
                elif (Constants.initial_ev_choice == 'prob_default'):
                    higher_1 = 'A' if player.ev_a_1 > player.ev_b_1 else 'B'
                    worst_1 = 'A' if player.ev_a_1 <= player.ev_b_1 else 'B'
                    higher_2 = 'A' if player.ev_a_2 > player.ev_b_2 else 'B'
                    worst_2 = 'A' if player.ev_a_2 <= player.ev_b_2 else 'B'
                    higher_3 = 'A' if player.ev_a_3 > player.ev_b_3 else 'B'
                    worst_3 = 'A' if player.ev_a_3 <= player.ev_b_3 else 'B'
                    higher_4 = 'A' if player.ev_a_4 > player.ev_b_4 else 'B'
                    worst_4 = 'A' if player.ev_a_4 <= player.ev_b_4 else 'B'
                    higher_5 = 'A' if player.ev_a_5 > player.ev_b_5 else 'B'
                    worst_5 = 'A' if player.ev_a_5 <= player.ev_b_5 else 'B'
                    higher_6 = 'A' if player.ev_a_6 > player.ev_b_6 else 'B'
                    worst_6 = 'A' if player.ev_a_6 <= player.ev_b_6 else 'B'
                    higher_7 = 'A' if player.ev_a_7 > player.ev_b_7 else 'B'
                    worst_7 = 'A' if player.ev_a_7 <= player.ev_b_7 else 'B'
                    higher_8 = 'A' if player.ev_a_8 > player.ev_b_8 else 'B'
                    worst_8 = 'A' if player.ev_a_8 <= player.ev_b_8 else 'B'
                    higher_9 = 'A' if player.ev_a_9 > player.ev_b_9 else 'B'
                    worst_9 = 'A' if player.ev_a_9 <= player.ev_b_9 else 'B'
                    higher_10 = 'A' if player.ev_a_10 > player.ev_b_10 else 'B'
                    worst_10 = 'A' if player.ev_a_10 <= player.ev_b_10 else 'B'
                    player.initial_choice_ev_1 = higher_1 if self.round_number <= 8 else worst_1
                    player.initial_choice_ev_2 = higher_2 if self.round_number <= 8 else worst_2
                    player.initial_choice_ev_3 = higher_3 if self.round_number <= 8 else worst_3
                    player.initial_choice_ev_4 = higher_4 if self.round_number <= 8 else worst_4
                    player.initial_choice_ev_5 = higher_5 if self.round_number <= 8 else worst_5
                    player.initial_choice_ev_6 = higher_6 if self.round_number <= 8 else worst_6
                    player.initial_choice_ev_7 = higher_7 if self.round_number <= 8 else worst_7
                    player.initial_choice_ev_8 = higher_8 if self.round_number <= 8 else worst_8
                    player.initial_choice_ev_9 = higher_9 if self.round_number <= 8 else worst_9
                    player.initial_choice_ev_10 = higher_10 if self.round_number <= 8 else worst_10

class Group(BaseGroup):
    pass

def make_field():
    return models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)

class Player(BasePlayer):
    age = models.IntegerField()
    gender = models.StringField(
        choices=['Male', 'Female'],
        widget=widgets.RadioSelectHorizontal
    )
    random_initial_choice = models.StringField()
    choice = make_field()
    actions_seq = models.StringField()
    real = models.IntegerField()
    checked = models.BooleanField(
        initial=False
    )
    ev_a = models.FloatField()
    ev_b = models.FloatField()
    initial_choice_ev = models.StringField()
    most_expected = models.StringField()
    is_exp = models.BooleanField()
    real_sum_10 = models.IntegerField()

    def get_payoff(self, paying_round, is_exp_counter, sum_real):
        if Constants.payment_structure == 1:
            selected_player = self.in_round(paying_round)
            if selected_player.checked:
                self.payoff = c(Constants.base_payment + selected_player.real - Constants.check_cost)
            else: 
                self.payoff = c(Constants.base_payment + selected_player.real)
        if Constants.payment_structure == 2:
            prob = is_exp_counter / Constants.total_rows
            bonus = np.random.choice([100, 0], 1, p=[prob, 1 - prob])[0]
            self.payoff = c(Constants.base_payment + int(bonus))
        if Constants.payment_structure == 3:
            self.payoff = c(Constants.base_payment + sum_real)

    ev_a_1 = models.FloatField()
    ev_a_2 = models.FloatField()
    ev_a_3 = models.FloatField()
    ev_a_4 = models.FloatField()
    ev_a_5 = models.FloatField()
    ev_a_6 = models.FloatField()
    ev_a_7 = models.FloatField()
    ev_a_8 = models.FloatField()
    ev_a_9 = models.FloatField()
    ev_a_10 = models.FloatField()

    ev_b_1 = models.FloatField()
    ev_b_2 = models.FloatField()
    ev_b_3 = models.FloatField()
    ev_b_4 = models.FloatField()
    ev_b_5 = models.FloatField()
    ev_b_6 = models.FloatField()
    ev_b_7 = models.FloatField()
    ev_b_8 = models.FloatField()
    ev_b_9 = models.FloatField()
    ev_b_10 = models.FloatField()

    initial_choice_ev_1 = models.StringField()
    initial_choice_ev_2 = models.StringField()
    initial_choice_ev_3 = models.StringField()
    initial_choice_ev_4 = models.StringField()
    initial_choice_ev_5 = models.StringField()
    initial_choice_ev_6 = models.StringField()
    initial_choice_ev_7 = models.StringField()
    initial_choice_ev_8 = models.StringField()
    initial_choice_ev_9 = models.StringField()
    initial_choice_ev_10 = models.StringField()

    most_expected_1 = models.StringField()
    most_expected_2 = models.StringField()
    most_expected_3 = models.StringField()
    most_expected_4 = models.StringField()
    most_expected_5 = models.StringField()
    most_expected_6 = models.StringField()
    most_expected_7 = models.StringField()
    most_expected_8 = models.StringField()
    most_expected_9 = models.StringField()
    most_expected_10 = models.StringField()

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

    random_initial_choice_1 = models.StringField()
    random_initial_choice_2 = models.StringField()
    random_initial_choice_3 = models.StringField()
    random_initial_choice_4 = models.StringField()
    random_initial_choice_5 = models.StringField()
    random_initial_choice_6 = models.StringField()
    random_initial_choice_7 = models.StringField()
    random_initial_choice_8 = models.StringField()
    random_initial_choice_9 = models.StringField()
    random_initial_choice_10 = models.StringField()
    
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
