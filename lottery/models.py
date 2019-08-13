from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import csv

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'lottery'
    players_per_group = None
    with open('lottery/problems.csv') as prob_file:
        data = list(csv.DictReader(prob_file))

    num_rounds = 10


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['data'] = Constants.data.copy()


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




    