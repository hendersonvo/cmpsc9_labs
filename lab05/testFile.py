# testFile.py

from Movie import Movie
from MovieCollectionNode import MovieCollectionNode
from MovieCollection import MovieCollection


def test_movieMethods():
        m0 = Movie("title", "person, a", 2026)
        assert m0.getMovieName() == "TITLE"
        assert m0.getDirector() == "PERSON, A"
        assert m0.getYear() == 2026
        assert m0.getRating() == None
        assert m0.getMovieDetails() == "TITLE directed by A PERSON (2026), Rating: None"
        m0.rating = 9.6
        assert m0.getRating() == 9.6
        assert m0.getMovieDetails() == "TITLE directed by A PERSON (2026), Rating: 9.6"
        
        m1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
        assert m0 > m1
        assert not (m1 > m0)

        m2 = Movie("None", "None", None, None)
        assert m2.getMovieName() == "NONE"
        assert m2.getDirector() == "NONE"
        assert m2.getRating() == None
        assert m2.getYear() == None


def test_MovieCollectionNodeMethods():
        m1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
        m2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968)

        movieNode = MovieCollectionNode(m1)
        assert movieNode.getData() == m1
        assert movieNode.getData().getMovieDetails() == m1.getMovieDetails()
        assert movieNode.getNext() == None
        movieNode.setNext(m2)
        assert movieNode.getNext() == m2
        assert movieNode.getNext().getMovieDetails() == m2.getMovieDetails()


def test_MovieCollectionMethods():
        m6 = Movie("Casablanca", "Curtiz, Michael", 1942, 8.8)
        m1 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2)
        m2 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)
        m3 = Movie("Work", "Chaplin, Charlie", 1915, 6.2)
        m4 = Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9)
        m5 = Movie("City Lights", "Chaplin, Charlie", 1931, 9.0)
        m0 = Movie("The Champion", "Chaplin, Charlie", 1915, 6.7)
        mc = MovieCollection()
        assert mc.isEmpty() == True
        mc.insertMovie(m0)
        mc.insertMovie(m1)
        mc.insertMovie(m2)
        mc.insertMovie(m3)
        mc.insertMovie(m4)
        mc.insertMovie(m5)
        mc.insertMovie(m6)
        assert mc.recursiveSearchMovie("City Lights", mc.head) == True
        assert mc.getNumberOfMovies() == 7
        assert mc.avgDirectorRating("Chaplin, Charlie") == 7.7
        assert mc.getMoviesByDirector("Wachowski, Lana") == "THE MATRIX directed by LANA WACHOWSKI (1999), Rating: 9.1\n"
        mc.removeDirector("Chaplin, Charlie")
        assert mc.getNumberOfMovies() == 3
        assert mc.avgDirectorRating("Chaplin, Charlie") == None
        assert mc.getMoviesByDirector("Chaplin, Charlie") == ""
        assert mc.recursiveSearchMovie("City Lights", mc.head) == False

# def test_MovieCollectionMethods2():
        
