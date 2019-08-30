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
        arr_200 = [i for i in range(1,201)]
        shuffle = random.sample(arr_200, 200)

    num_rounds = 10

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['data'] = Constants.data.copy()
            self.session.vars['shuffle'] = Constants.shuffle.copy()

        lottery_number = self.session.vars['shuffle'][self.round_number - 1]
        self.session.vars['lottery'] = lottery_number
        self.session.vars['current_lottery'] = self.session.vars['data'][lottery_number - 1]

        for i in range(1,6):
            self.session.vars['probA' + str(i)] = self.session.vars['current_lottery']['probA' + str(i)]
            self.session.vars['realA' + str(i)] = self.session.vars['current_lottery']['realA' + str(i)]
            self.session.vars['probB' + str(i)] = self.session.vars['current_lottery']['probB' + str(i)]
            self.session.vars['realB' + str(i)] = self.session.vars['current_lottery']['realB' + str(i)]

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