class temperature:
    """Scrapes the current temperature of the web site
    timeanddate.com/weather based on location of the user.
    """

    def __init__(self, country, city):
        self.city = city
        self.country = country

    def get(self):
        pass