from lib.bloodoath import BloodOath

class Cult:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f'{key}', value)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str):
            self._location = location
        else:
            raise TypeError
    
    @property
    def founding_year(self):
        return self._founding_year
    
    @founding_year.setter
    def founding_year(self, founding_year):
        if isinstance(founding_year, int):
            self._founding_year = founding_year
        else:
            raise TypeError
    
    @property
    def slogan(self):
        return self._slogan
    
    @slogan.setter
    def slogan(self, slogan):
        if isinstance(slogan, str):
            self._slogan = slogan
        else:
            raise TypeError