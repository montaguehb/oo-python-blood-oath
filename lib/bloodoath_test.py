import unittest
import datetime
from follower import Follower
from bloodoath import BloodOath
from cult import Cult

class BloodoathTest(unittest.TestCase):
    def setUp(self) -> None:
        self.scientology = Cult(name="scientology", location="California", founding_year=1990, slogan="We have Tom Cruise")
        self.Hazell = Cult(name="Hazell", location="Central Ardougne", founding_year=2002, slogan="What's your poison?")
        self.cult = Cult(name="Not a cult", location="Narnia", founding_year=1880, slogan="How do you like your tea?")
        self.follower = Follower(name="Follower", age=20, life_motto="I'm a follower", cult=self.cult)
        self.tom_cruise = Follower(name="Tom Cruise", age=50, life_motto="I'm a follower", cult=self.scientology)
        self.john_travolta = Follower(name="John Travolta", age=60, life_motto="I'm a follower", cult=self.scientology)
        self.bloodoath = BloodOath(follower=self.follower, cult=self.cult)
        return super().setUp()
    
    def tearDown(self) -> None:
        Cult.all = []
        Follower.all = []
        BloodOath.all = []
        return super().tearDown()
    
    def test_has_initiation_date(self):
        self.assertEqual(self.bloodoath.initiation_date, datetime.date.today().strftime("%m/%d/%Y"))
    
    def test_initiation_date_is_str(self):
        self.assertIsInstance(self.bloodoath.initiation_date, str)
    
    def test_bloodoath_class_has_all(self):
        self.assertCountEqual(BloodOath.all, [self.bloodoath])
    
    
    
    
    