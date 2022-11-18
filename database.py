import uuid

import mongoengine as db
from datetime import datetime
from random import random
import itertools
import pymongo
from mongoengine import connect


class ScoreCards(db.Document):
    contest = db.StringField()
    date = db.DateTimeField(default=datetime.now())
    rider_id = db.StringField()
    display_name = db.StringField()
    section = db.StringField()
    bib_color = db.StringField()
    division = db.FloatField()
    execution = db.FloatField()
    creativity = db.FloatField()
    difficulty = db.FloatField()
    landed = db.BooleanField()
    average = db.FloatField()

    def calc_average(self):
        scores = [self.execution, self.creativity, self.difficulty]
        self.average = sum(scores) / len(scores)
        return self.average


class Contest(db.Document):
    date_created = db.DateTimeField(default=datetime.today)
    event_name = db.StringField(required=True)
    date = db.StringField()
    start_time = db.StringField()
    datetime = db.DateField()
    location = db.StringField()
    description = db.StringField()
    registered_riders = db.ListField()
    live = db.BooleanField(default=False)
    completed = db.BooleanField(default=False)
    format = db.StringField()
    image_link = db.StringField()
    uid = db.ObjectIdField()

    # id = db.UUIDField(default=uuid.uuid1())

    def riders_list(self):
        registered = list(Rider.objects(registered_contest=self.app.active_contest))
        rider_list = []

        for rider in registered:
            rider_list.append(rider.id)

        self.registered_riders = rider_list
        return self.registered_riders


# class Division(db.DynamicDocument):
#     contest = db.ReferenceField(Contest)
#     name = db.StringField(required=True)
#     riders = db.ListField()


# class Format(db.EmbeddedDocument):
#     contest_id = db.ObjectIdField()
#     name = db.StringField()
#
#     heats = db.BooleanField()
#     lcq = db.BooleanField()
#     multi_factor_judging = db.BooleanField()
#     sections = db.BooleanField()
#     bibs = db.BooleanField()
#     timer = db.BooleanField()
#
#     heats_matter = db.BooleanField()
#     heat_advance = db.IntField()
#     riders_per_heat = db.IntField()
#
#     number_factors = db.IntField()
#     factor_names = db.ListField()
#     factor_weights = db.ListField()
#
#     section_names = db.ListField()
#     section_weights = db.ListField()
#
#     bibs_colors = db.ListField()
#
#     default_time = db.FloatField()
#
#     lcq_advance = db.IntField()


# class Location(db.DynamicDocument):
#     name = db.StringField()
#     address = db.StringField()
#     logo_url = db.URLField()
#     website = db.URLField()


class Rider(db.Document):
    date_created = db.DateTimeField(default=datetime.today)
    first_name = db.StringField(required=True)
    last_name = db.StringField(require=True)
    date_of_birth = db.StringField()
    home_park = db.StringField()
    bio = db.StringField()
    image = db.DynamicField()
    stance = db.StringField()
    display_name = db.StringField()
    full_name = db.StringField()
    email = db.StringField()
    registered_contest = db.ListField()
    on_water = db.BooleanField(default=False)
    registered_division = db.ListField()
    athlete = db.BooleanField()
    judge = db.BooleanField()
    admin = db.BooleanField()
    bib_color = db.StringField(default='white')
    div_score = db.FloatField(default=0)
    division = db.StringField(default='First Timer')
    overall = db.FloatField()
    overall_kickers = db.FloatField
    overall_rails = db.FloatField
    overall_airtricks = db.FloatField

    def get_display_name(self):
        name = f'{self.first_name[0].upper()}. {self.last_name}'
        self.display_name = name
        return self.display_name

    def get_division(self, contest_id):
        rider_scorecards = ScoreCards.objects(contest=contest_id, rider_id=str(self.id))

        lst = []
        for rider in rider_scorecards:
            lst.append(rider['division'])
        div = sum(lst) / len(lst)

        if 0.0 <= div < 20.0:
            div_label = 'Beginner'
        if 20.0 <= div < 40.0:
            div_label = 'Novice'
        if 40 <= div < 60:
            div_label = 'Intermediate'
        if 60 <= div < 90:
            div_label = 'Advanced'
        if div >= 90:
            div_label = 'Pro'

        self.div_score = div
        self.division = div_label

        return self.division

    def get_overall_scores(self, contest_id):
        rider_scorecards = ScoreCards.objects(contest=contest_id, rider_id=str(self.id))

        kickers = []
        rails = []
        airtricks = []

        for trick in rider_scorecards:
            if trick.section == 'Kicker':
                kickers.append(trick.average)
            if trick.section == 'Rail':
                rails.append(trick.average)
            if trick.section == 'Air Trick':
                airtricks.append(trick.average)

        self.overall_kickers = sum(kickers) / len(kickers)
        self.overall_rails = sum(rails) / len(rails)
        self.overall_airtricks = sum(airtricks) / len(airtricks)

        return self.overall, self.overall_kickers, self.overall_rails, self.overall_airtricks
