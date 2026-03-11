# Movie.py

class Movie:
    def __init__(self, movieName, director, year, rating = None):
        self.movieName = movieName.upper()
        self.director = director.upper()
        self.year = year
        self.rating = rating

    def getMovieName(self):
        return self.movieName
    
    def getDirector(self):
        return self.director
    
    def getYear(self):
        return self.year
    
    def getRating(self):
        return self.rating
    
    def getMovieDetails(self):
        splitName = self.getDirector().split(", ")
        return "{} directed by {} {} ({}), Rating: {}"\
            .format(self.movieName, splitName[1], splitName[0], self.year, self.rating)
    
    def __gt__(self, rhs):
        if self.director > rhs.director:
            return True
        elif self.director == rhs.director:
            if self.year > rhs.year:
                return True
            elif self.year == self.year:
                if self.movieName > rhs.movieName:
                    return True
        return False
    

# m1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
# m2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968)
# print(m1.getMovieDetails())
# print(m2.getMovieDetails())
