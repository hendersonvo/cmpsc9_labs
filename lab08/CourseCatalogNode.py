# CourseCatalogNode.py

from Event import Event

class CourseCatalogNode:
    '''represent one course in a Binary Search Tree'''
    def __init__(self, department, courseId, courseName, lecture, sections):
        self.department = department.upper()
        self.courseId = courseId
        self.courseName = courseName.upper()
        self.lecture = lecture
        self.sections = sections
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        output = f"{self.department} {self.courseId}: {self.courseName}\n"
        output += " * Lecture: " + self.lecture.__str__() + "\n"
        if len(self.sections) > 0:
            for section in self.sections:
                output += " + Section: " + section.__str__() + "\n"
        return output
    
# # create one lecture event
# lecture = Event("TR", (1530, 1645), "td-w 1701")

# # create four section events
# section1 = Event("W", (1400, 1450), "north hall 1109")
# section2 = Event("W", (1500, 1550), "north hall 1109")
# section3 = Event("W", (1600, 1650), "north hall 1109")
# section4 = Event("W", (1700, 1750), "girvetz hall 1112")
# sections = [section1, section2, section3, section4]

# # initialize a CMPSC 9 course node
# node = CourseCatalogNode("cmpsc", 9, "intermediate python", lecture, sections)

# print(node)
