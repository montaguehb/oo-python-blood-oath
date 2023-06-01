class BloodOath:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f'{key}', value)