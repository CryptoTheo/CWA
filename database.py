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

class Division(db.DynamicDocument):
    contest = db.ReferenceField(Contest)
    name = db.StringField(required=True)
    riders = db.ListField()


class Format(db.EmbeddedDocument):
    contest_id = db.ObjectIdField()
    name = db.StringField()

    heats = db.BooleanField()
    lcq = db.BooleanField()
    multi_factor_judging = db.BooleanField()
    sections = db.BooleanField()
    bibs = db.BooleanField()
    timer = db.BooleanField()

    heats_matter = db.BooleanField()
    heat_advance = db.IntField()
    riders_per_heat = db.IntField()

    number_factors = db.IntField()
    factor_names = db.ListField()
    factor_weights = db.ListField()

    section_names = db.ListField()
    section_weights = db.ListField()

    bibs_colors = db.ListField()

    default_time = db.FloatField()

    lcq_advance = db.IntField()


class Location(db.DynamicDocument):
    name = db.StringField()
    address = db.StringField()
    logo_url = db.URLField()
    website = db.URLField()


class Rider(db.Document):
    date_created = db.DateTimeField(default=datetime.today)
    # userhxashtag = db.StringField(required=False, default=random.randrange(1,100), unique=True)
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
