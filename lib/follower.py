from lib.bloodoath import BloodOath

class Follower:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f'{key}', value)
