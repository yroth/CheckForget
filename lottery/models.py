from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import csv
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'lottery'
    players_per_group = None
    with open('lottery/problems.csv') as prob_file:
        data = list(csv.DictReader(prob_file))
        total_rows = len(data)
        temp_arr_1 = [i for i in range(1,int(total_rows / 2) + 1)]
        temp_arr_10 = [i for i in range(int(total_rows / 2) + 1,total_rows + 1)]
        ind_cond_1 = random.sample(temp_arr_1, int(total_rows / 2))
        ind_cond_10 = random.sample(temp_arr_10, int(total_rows / 2))

    num_rounds = int(total_rows / 2)

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['data'] = Constants.data.copy()
            self.session.vars['ind_cond_1'] = Constants.ind_cond_1.copy()
            self.session.vars['ind_cond_10'] = Constants.ind_cond_10.copy()

        lottery_number_cond_1 = self.session.vars['ind_cond_1'][self.round_number - 1]
        self.session.vars['current_lottery_cond_1'] = self.session.vars['data'][lottery_number_cond_1 - 1]

        for i in range(1,6):
            self.session.vars['probA' + str(i)] = self.session.vars['current_lottery_cond_1']['probA' + str(i)]
            self.session.vars['realA' + str(i)] = self.session.vars['current_lottery_cond_1']['realA' + str(i)]
            self.session.vars['probB' + str(i)] = self.session.vars['current_lottery_cond_1']['probB' + str(i)]
            self.session.vars['realB' + str(i)] = self.session.vars['current_lottery_cond_1']['realB' + str(i)]

        for player in self.get_players():
            player.probA1 = self.session.vars['probA1']
            player.realA1 = self.session.vars['realA1']
            player.probB1 = self.session.vars['probB1']
            player.realB1 = self.session.vars['realB1']

            player.probA2 = self.session.vars['probA2']
            player.realA2 = self.session.vars['realA2']
            player.probB2 = self.session.vars['probB2']
            player.realB2 = self.session.vars['realB2']

            player.probA3 = self.session.vars['probA3']
            player.realA3 = self.session.vars['realA3']
            player.probB3 = self.session.vars['probB3']
            player.realB3 = self.session.vars['realB3']

            player.probA4 = self.session.vars['probA4']
            player.realA4 = self.session.vars['realA4']
            player.probB4 = self.session.vars['probB4']
            player.realB4 = self.session.vars['realB4']

            player.probA5 = self.session.vars['probA5']
            player.realA5 = self.session.vars['realA5']
            player.probB5 = self.session.vars['probB5']
            player.realB5 = self.session.vars['realB5']

class Group(BaseGroup):
    pass

def make_field():
    return models.StringField(
        choices=['A', 'B'],
        initial='A',
        widget=widgets.RadioSelectHorizontal)


class Player(BasePlayer):
    age = models.IntegerField()
    gender = models.StringField(
        choices=['male', 'female'],
        widget=widgets.RadioSelectHorizontal
    )
    choice = make_field()

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

    reA1_1 = models.IntegerField()
    prA1_1 = models.FloatField()
    reA2_1 = models.IntegerField()
    prA2_1 = models.FloatField()
    reA3_1 = models.IntegerField()
    prA3_1 = models.FloatField()
    reA4_1 = models.IntegerField()
    prA4_1 = models.FloatField()
    reA5_1 = models.IntegerField()
    prA5_1 = models.FloatField()

    reB1_1 = models.IntegerField()
    prB1_1 = models.FloatField()
    reB2_1 = models.IntegerField()
    prB2_1 = models.FloatField()
    reB3_1 = models.IntegerField()
    prB3_1 = models.FloatField()
    reB4_1 = models.IntegerField()
    prB4_1 = models.FloatField()
    reB5_1 = models.IntegerField()
    prB5_1 = models.FloatField()

    submitted_answer_2 = models.StringField()

    prA1_2 = models.FloatField()
    reA1_2 = models.IntegerField()
    prA2_2 = models.FloatField()
    reA2_2 = models.IntegerField()
    prA3_2 = models.FloatField()
    reA3_2 = models.IntegerField()
    prA4_2 = models.FloatField()
    reA4_2 = models.IntegerField()
    prA5_2 = models.FloatField()
    reA5_2 = models.IntegerField()

    prB1_2 = models.FloatField()
    reB1_2 = models.IntegerField()
    prB2_2 = models.FloatField()
    reB2_2 = models.IntegerField()
    prB3_2 = models.FloatField()
    reB3_2 = models.IntegerField()
    prB4_2 = models.FloatField()
    reB4_2 = models.IntegerField()
    prB5_2 = models.FloatField()
    reB5_2 = models.IntegerField()

    submitted_answer_3 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)

    prA1_3 = models.FloatField()
    reA1_3 = models.IntegerField()
    prA2_3 = models.FloatField()
    reA2_3 = models.IntegerField()
    prA3_3 = models.FloatField()
    reA3_3 = models.IntegerField()
    prA4_3 = models.FloatField()
    reA4_3 = models.IntegerField()
    prA5_3 = models.FloatField()
    reA5_3 = models.IntegerField()

    prB1_3 = models.FloatField()
    reB1_3 = models.IntegerField()
    prB2_3 = models.FloatField()
    reB2_3 = models.IntegerField()
    prB3_3 = models.FloatField()
    reB3_3 = models.IntegerField()
    prB4_3 = models.FloatField()
    reB4_3 = models.IntegerField()
    prB5_3 = models.FloatField()
    reB5_3 = models.IntegerField()

    submitted_answer_4 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)

    prA1_4 = models.FloatField()
    reA1_4 = models.IntegerField()
    prA2_4 = models.FloatField()
    reA2_4 = models.IntegerField()
    prA3_4 = models.FloatField()
    reA3_4 = models.IntegerField()
    prA4_4 = models.FloatField()
    reA4_4 = models.IntegerField()
    prA5_4 = models.FloatField()
    reA5_4 = models.IntegerField()

    prB1_4 = models.FloatField()
    reB1_4 = models.IntegerField()
    prB2_4 = models.FloatField()
    reB2_4 = models.IntegerField()
    prB3_4 = models.FloatField()
    reB3_4 = models.IntegerField()
    prB4_4 = models.FloatField()
    reB4_4 = models.IntegerField()
    prB5_4 = models.FloatField()
    reB5_4 = models.IntegerField()

    submitted_answer_5 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)

    prA1_5 = models.FloatField()
    reA1_5 = models.IntegerField()
    prA2_5 = models.FloatField()
    reA2_5 = models.IntegerField()
    prA3_5 = models.FloatField()
    reA3_5 = models.IntegerField()
    prA4_5 = models.FloatField()
    reA4_5 = models.IntegerField()
    prA5_5 = models.FloatField()
    reA5_5 = models.IntegerField()

    prB1_5 = models.FloatField()
    reB1_5 = models.IntegerField()
    prB2_5 = models.FloatField()
    reB2_5 = models.IntegerField()
    prB3_5 = models.FloatField()
    reB3_5 = models.IntegerField()
    prB4_5 = models.FloatField()
    reB4_5 = models.IntegerField()
    prB5_5 = models.FloatField()
    reB5_5 = models.IntegerField()

    submitted_answer_6 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)

    prA1_6 = models.FloatField()
    reA1_6 = models.IntegerField()
    prA2_6 = models.FloatField()
    reA2_6 = models.IntegerField()

    prA3_6 = models.FloatField()
    reA3_6 = models.IntegerField()
    prA4_6 = models.FloatField()
    reA4_6 = models.IntegerField()
    prA5_6 = models.FloatField()
    reA5_6 = models.IntegerField()

    prB1_6 = models.FloatField()
    reB1_6 = models.IntegerField()
    prB2_6 = models.FloatField()
    reB2_6 = models.IntegerField()
    prB3_6 = models.FloatField()
    reB3_6 = models.IntegerField()
    prB4_6 = models.FloatField()
    reB4_6 = models.IntegerField()
    prB5_6 = models.FloatField()
    reB5_6 = models.IntegerField()

    submitted_answer_7 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)

    prA1_7 = models.FloatField()
    reA1_7 = models.IntegerField()
    prA2_7 = models.FloatField()
    reA2_7 = models.IntegerField()
    prA3_7 = models.FloatField()
    reA3_7 = models.IntegerField()
    prA4_7 = models.FloatField()
    reA4_7 = models.IntegerField()
    prA5_7 = models.FloatField()
    reA5_7 = models.IntegerField()

    prB1_7 = models.FloatField()
    reB1_7 = models.IntegerField()
    prB2_7 = models.FloatField()
    reB2_7 = models.IntegerField()
    prB3_7 = models.FloatField()
    reB3_7 = models.IntegerField()
    prB4_7 = models.FloatField()
    reB4_7 = models.IntegerField()
    prB5_7 = models.FloatField()
    reB5_7 = models.IntegerField()

    submitted_answer_8 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)

    prA1_8 = models.FloatField()
    reA1_8 = models.IntegerField()
    prA2_8 = models.FloatField()
    reA2_8 = models.IntegerField()
    prA3_8 = models.FloatField()
    reA3_8 = models.IntegerField()
    prA4_8 = models.FloatField()
    reA4_8 = models.IntegerField()
    prA5_8 = models.FloatField()
    reA5_8 = models.IntegerField()

    prB1_8 = models.FloatField()
    reB1_8 = models.IntegerField()
    prB2_8 = models.FloatField()
    reB2_8 = models.IntegerField()
    prB3_8 = models.FloatField()
    reB3_8 = models.IntegerField()
    prB4_8 = models.FloatField()
    reB4_8 = models.IntegerField()
    prB5_8 = models.FloatField()
    reB5_8 = models.IntegerField()

    submitted_answer_9 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)

    prA1_9 = models.FloatField()
    reA1_9 = models.IntegerField()
    prA2_9 = models.FloatField()
    reA2_9 = models.IntegerField()
    prA3_9 = models.FloatField()
    reA3_9 = models.IntegerField()
    prA4_9 = models.FloatField()
    reA4_9 = models.IntegerField()
    prA5_9 = models.FloatField()
    reA5_9 = models.IntegerField()

    prB1_9 = models.FloatField()
    reB1_9 = models.IntegerField()
    prB2_9 = models.FloatField()
    reB2_9 = models.IntegerField()
    prB3_9 = models.FloatField()
    reB3_9 = models.IntegerField()
    prB4_9 = models.FloatField()
    reB4_9 = models.IntegerField()
    prB5_9 = models.FloatField()
    reB5_9 = models.IntegerField()

    submitted_answer_0 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelectHorizontal)

    prA1_0 = models.FloatField()
    reA1_0 = models.IntegerField()
    prA2_0 = models.FloatField()
    reA2_0 = models.IntegerField()
    prA3_0 = models.FloatField()
    reA3_0 = models.IntegerField()
    prA4_0 = models.FloatField()
    reA4_0 = models.IntegerField()
    prA5_0 = models.FloatField()
    reA5_0 = models.IntegerField()

    prB1_0 = models.FloatField()
    reB1_0 = models.IntegerField()
    prB2_0 = models.FloatField()
    reB2_0 = models.IntegerField()
    prB3_0 = models.FloatField()
    reB3_0 = models.IntegerField()
    prB4_0 = models.FloatField()
    reB4_0 = models.IntegerField()
    prB5_0 = models.FloatField()
    reB5_0 = models.IntegerField()
