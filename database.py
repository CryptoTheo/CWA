import uuid

import mongoengine as db
from datetime import datetime
from random import random
import itertools
import pymongo
from mongoengine import connect


def calculate_division(score):
    if score == 0:
        div_label = 'First Timer'
    if 0.1 <= score < 20.0:
        div_label = 'Beginner'
    if 20.0 <= score < 40.0:
        div_label = 'Novice'
    if 40 <= score < 60:
        div_label = 'Intermediate'
    if 60 <= score < 90:
        div_label = 'Advanced'
    if score >= 90:
        div_label = 'Pro'
    return div_label


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


def Average(lst):
    for item in lst:
        if item is None:
            return 0
    if len(lst) is 0:
        return 0
    return sum(lst) / len(lst)


class Rider(db.Document):
    date_created = db.DateTimeField(default=datetime.today)
    first_name = db.StringField(required=True)
    last_name = db.StringField(require=True)
    date_of_birth = db.StringField()
    home_park = db.StringField()
    image = db.DynamicField()
    stance = db.StringField()
    display_name = db.StringField()
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
    overall_kickers = db.FloatField()
    overall_rails = db.FloatField()
    overall_airtricks = db.FloatField()
    recent_overall = db.FloatField()
    recent_execution = db.FloatField()
    recent_creativity = db.FloatField()
    recent_difficulty = db.FloatField()
    recent_section = db.FloatField()
    kicker_division = db.FloatField()
    airtrick_division = db.FloatField()
    rail_division = db.FloatField()
    kicker_div_label = db.StringField()
    rail_div_label = db.StringField()
    airtrick_div_label = db.StringField()

    def get_display_name(self):
        name = f'{self.first_name[0].upper()}. {self.last_name}'
        self.display_name = name
        self.save()
        return self.display_name

    def get_division(self, contest_id):
        rider_scorecards = ScoreCards.objects(contest=contest_id, rider_id=str(self.id), landed=True)

        lst = []
        for rider in rider_scorecards:
            lst.append(rider['division'])
        if len(lst) > 0:
            div = sum(lst) / len(lst)
        else:
            div = 0

        div_label = calculate_division(div)

        self.div_score = div
        self.division = div_label

        return self.division

    def get_overall_scores(self, contest_id):
        rider_scorecards = ScoreCards.objects(contest=contest_id, rider_id=str(self.id), landed=True)
        self.overall = rider_scorecards.average('average')
        kickers = []
        rails = []
        airtricks = []
        kicker_div_list = []
        rail_div_list = []
        airtrick_div_list = []

        for trick in rider_scorecards:
            if trick.section == 'Kicker':
                kickers.append(trick.average)
                kicker_div_list.append(trick.division)
            if trick.section == 'Rail':
                rails.append(trick.average)
                rail_div_list.append(trick.division)
            if trick.section == 'Air Trick':
                airtricks.append(trick.average)
                airtrick_div_list.append(trick.division)

        division = self.get_division(contest_id)
        if len(kickers) == 0:
            self.overall_kickers = 0
            self.kicker_division = 0
            self.kicker_div_label = calculate_division(0)
            self.save()
        elif len(kickers) > 0:
            self.overall_kickers = Average(kickers)
            self.kicker_division = sum(kicker_div_list) / len(kicker_div_list)
            self.kicker_div_label = calculate_division(self.kicker_division)
            self.save()

        if len(rails) == None:
            self.overall_rails = 0
            self.rail_division = 0
            self.rail_div_label = calculate_division(0)
            self.save()
        elif len(rails) > 0:
            self.overall_rails = Average(rails)
            self.rail_division = sum(rail_div_list) / len(rail_div_list)
            self.rail_div_label = calculate_division(self.rail_division)
            self.save()

        if len(airtricks) <= 1:
            self.overall_airtricks = 0
            self.airtrick_division = 0
            self.airtrick_div_label = calculate_division(0)
            self.save()

        elif len(airtricks) > 0:
            self.overall_airtricks = Average(airtricks)
            self.airtrick_division = (sum(airtrick_div_list) / len(airtrick_div_list))
            self.airtrick_div_label = calculate_division(self.airtrick_division)

            self.save()

        self.save()
        return [self.overall, self.overall_kickers, self.overall_rails, self.overall_airtricks]

    def get_trick_count(self, contest_id):
        return len(ScoreCards.objects(contest=contest_id, rider_id=str(self.id), landed=True))

    def get_recent_scores(self, contest_id):

        recent = ScoreCards.objects(contest=contest_id, rider_id=str(self.id), landed=True).order_by('-id').first()
        if recent is not None:
            self.recent_overall = recent.average
            (print(recent.average))
            print(recent.display_name)
            self.recent_execution = recent.execution
            self.recent_creativity = recent.creativity
            self.recent_difficulty = recent.difficulty
            self.recent_section = recent.section

            return [self.recent_overall, self.recent_execution, self.recent_creativity, self.recent_difficulty,
                    self.recent_section]
