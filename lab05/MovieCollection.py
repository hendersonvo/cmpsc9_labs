# MovieCollection.py
from Movie import Movie
from MovieCollectionNode import MovieCollectionNode

class MovieCollection:
    def __init__(self):
        self.head = None    # create a new collection with no head

    def isEmpty(self):
        return self.head == None    # return true if empty, false if not

    def getNumberOfMovies(self):
        count = 0
        temp = self.head

        while temp != None:
            count += 1
            temp = temp.getNext()

        return count
    
    def insertMovie(self, movie):
        current = self.head                 # set current position to head
        previous = None                     # there is nothing behind the head
        mNode = MovieCollectionNode(movie)  # create a movie node with our new movie

        while current != None:              # while we are not at the end of the list, or the list is not empty,
            if movie > current.getData():   # if our movie is gt our current position,
                previous = current          # move previous and current positions forward one step
                current = current.getNext()
            else:
                break                       # if our list is not empty, but our movie is not gt our current position, exit the loop

        if previous == None:                # if we are at the start of the list
            mNode.setNext(current)          # insert our movie at the start of the list
            self.head = mNode
        else:
            previous.setNext(mNode)         # otherwise, fit it between our previous and current positions
            mNode.setNext(current)

    def getAllMoviesInCollection(self):
        temp = self.head
        output = ""

        if self.isEmpty() == False:
            while temp != None:
                output += temp.getData().getMovieDetails() + "\n"
                temp = temp.getNext()
        return output
        
    def getMoviesByDirector(self, director):
        temp = self.head
        output = ""

        if self.isEmpty() == False:
            while temp != None:
                if temp.getData().getDirector() == director.upper():
                    output += temp.getData().getMovieDetails() + "\n"
                temp = temp.getNext()
            return output
        
    def removeDirector(self, director):
        current = self.head
        previous = None

        if self.isEmpty() == True:
            return
        
        while current.getData().getDirector() != director.upper():  # while the current position's director does not match
            previous = current                                      # march previous and current positions forward
            current = current.getNext()
            if current == None:                                     # if we march to the end of the list without finding the director
                break                                               # return without changes
            
        while current.getData().getDirector() == director.upper():  # now, while the current position's director does match
            current = current.getNext()                             # march only the current position forward until it does not match anymore
            if current == None:                                     # if we reach the end of the list without encountering a mismatch,
                previous.setNext(None)
                break                                               # set previous position's next to None
        
        if previous == None:
            self.head = current                                     # case 1: if there were no nodes before the matching director, make current position the new head
        else:
            previous.setNext(current)                               # case 2: connect previous position to current position (ahead of all matching director nodes)

    def avgDirectorRating(self, director):
        current = self.head
        total = 0
        count = 0

        if self.isEmpty() == True:
            return None

        while current.getData().getDirector() != director.upper(): 
            current = current.getNext()
            if current == None:
                return None
            
        while current.getData().getDirector() == director.upper():  
            rating = current.getData().getRating()
            if rating == None:
                pass
            else:
                count += 1
                total += rating
            current = current.getNext()

        if count == 0:
            return None
        else:
            return round(total/count, 2)
            

    def recursiveSearchMovie(self, movieName, movieNode):
        temp = movieNode

        if temp.getNext() == None:  # base case: if this node is the last one in the list, and it doesn't match the movie title, return False
            if temp.getData().getMovieName() != movieName.upper():
                return False
        
        if temp.getData().getMovieName() == movieName.upper():  # otherwise, if the names match, return True
            return True
            
        temp = temp.getNext()   # if the names did not match, and it is not the end of the list, move onto the next node
        return self.recursiveSearchMovie(movieName, temp)