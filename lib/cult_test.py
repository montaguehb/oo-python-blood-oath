import unittest
from lib.follower import Follower
from lib.bloodoath import BloodOath
from lib.cult import Cult

class CultTest(unittest.TestCase):
    def setUp(self) -> None:
        self.scientology = Cult(name="scientology", location="California", founding_year=1990, slogan="We have Tom Cruise")
        self.Hazell = Cult(name="Hazell", location="Central Ardougne", founding_year=2002, slogan="What's your poison?")
        self.cult = Cult(name="Not a cult", location="California", founding_year=1880, slogan="How do you like your tea?")
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
    
    def test_cult_has_name(self):
        self.assertEqual(self.scientology.name, "scientology")
    
    def test_name_is_str(self):
        with self.assertRaises(Exception):
            self.scientology.name = 5
            
    def test_cult_has_location(self):
        self.assertEqual(self.scientology.location, "California")
    
    def test_location_is_str(self):
        with self.assertRaises(Exception):
            self.scientology.location = 5
    
    def test_cult_has_founding_year(self):
        self.assertEqual(self.scientology.founding_year, 1990)
    
    def test_founding_year_is_int(self):
        with self.assertRaises(Exception):
            self.scientology.founding_year = "1990"
    
    def test_cult_has_slogan(self):
        self.assertEqual(self.scientology.slogan, "We have Tom Cruise")
    
    def test_slogan_is_str(self):
        with self.assertRaises(Exception):
            self.scientology.slogan = 5
    
    def test_cult_recruits_follower(self):
        self.scientology.recruit_follower(self.follower)
        self.assertIn(self.follower, self.scientology.followers)
    
    def test_cult_population(self):
        self.scientology.recruit_follower(self.follower)
        self.assertEqual(self.scientology.cult_population(), 1)
    
    def test_cult_class_has_all(self):
        self.assertIsInstance(Cult.all, list)
        self.assertCountEqual([self.scientology, self.Hazell, self.cult], Cult.all)
    
    def test_find_by_name(self):
        self.assertEqual(Cult.find_by_name("scientology"), self.scientology)
    
    def test_find_by_location(self):
        self.assertEqual(Cult.find_by_location("Central Ardougne"), self.Hazell)
    
    def test_find_by_founding_year(self):
        self.assertEqual(Cult.find_by_founding_year(1880), self.cult)
    
    def test_average_age(self):
        self.assertAlmostEqual(self.scientology.average_age(), 55, delta=1)
    
    def test_average_age_is_float(self):
        self.assertIsInstance(self.scientology.average_age(), float)
    
    def test_my_followers_mottos(self):
        self.assertCountEqual(self.scientology.my_followers_mottos(), ["I'm a follower", "I'm a follower"])
    
    def test_least_popular_cult(self):
        self.assertEqual(Cult.least_popular(), self.cult)
    
    def test_most_common_location(self):
        self.assertEqual(Cult.most_common_location(), "California")
    
    