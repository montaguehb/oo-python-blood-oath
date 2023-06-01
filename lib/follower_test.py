import unittest
from lib.follower import Follower
from lib.bloodoath import BloodOath
from lib.cult import Cult

class FollowerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.scientology = Cult(name="scientology", location="California", founding_year=1990, slogan="We have Tom Cruise")
        self.Hazell = Cult(name="Hazell", location="Central Ardougne", founding_year=2002, slogan="What's your poison?")
        self.cult = Cult(name="Not a cult", location="Narnia", founding_year=1880, slogan="How do you like your tea?")
        self.follower = Follower(name="Follower", age=20, life_motto="I'm a follower", cult=self.cult)
        self.tom_cruise = Follower(name="Tom Cruise", age=50, life_motto="I'm a follower", cult=self.scientology)
        self.john_travolta = Follower(name="John Travolta", age=60, life_motto="I'm a follower", cult=self.scientology)
        self.bloodoath = BloodOath(follower=self.follower, cult=self.cult)
        self.bloodoath1 = BloodOath(follower=self.follower, cult=self.scientology)
        return super().setUp()
    
    def tearDown(self) -> None:
        Cult.all = []
        Follower.all = []
        BloodOath.all = []
        return super().tearDown()
    
    def test_follower_has_name(self):
        self.assertEqual(self.follower.name, "Follower")
    
    def test_name_is_str(self):
        with self.assertRaises(TypeError):
            self.follower.name = 5
    
    def test_follower_has_age(self):
        self.assertEqual(self.follower.age, 20)
    
    def test_age_is_int(self):
        with self.assertRaises(TypeError):
            self.follower.age = "20"
    
    def test_follower_has_life_motto(self):
        self.assertEqual(self.follower.life_motto, "I'm a follower")
    
    def test_life_motto_is_str(self):
        with self.assertRaises(TypeError):
            self.follower.life_motto = 5
    
    def test_follower_has_cult(self):
        self.assertCountEqual(self.follower.cult, self.cult)
    
    def test_join_cult(self):
        self.follower.join_cult(self.scientology)
        self.assertIn(self.follower, self.scientology.followers)
    
    def test_all_followers(self):
        self.assertEqual(Follower.all, [self.follower, self.tom_cruise, self.john_travolta])
    
    def test_of_a_certain_age(self):
        self.assertEqual(Follower.of_a_certain_age(50), [self.tom_cruise, self.john_travolta])
    
    def test_my_cults_slogans(self):
        self.assertEqual(self.follower.my_cults_slogans(), ["How do you like your tea?"])
    
    def test_most_active(self):
        self.assertEqual(Follower.most_active(), self.follower)
    
    def test_top_ten(self):
        self.assertEqual(Follower.top_ten(), [self.follower, self.tom_cruise, self.john_travolta])
    
    