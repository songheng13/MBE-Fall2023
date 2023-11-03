from otree.api import *


doc = """
Participants choose whether they love to share
"""


class C(BaseConstants):
    NAME_IN_URL = 'sharing_decision'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.BooleanField(
        label="Do you want to share?",
        choices=[
            [True, "Yes"],
            [False, "No"],
        ]
    )


# PAGES
class MakingDecision(Page):
    form_model = 'player'
    form_fields = ['decision']


class Results(Page):
    pass


page_sequence = [MakingDecision]
