# CourseCatalog.py

from Event import Event
from CourseCatalogNode import CourseCatalogNode

class CourseCatalog:
    def __init__(self):
        self.root = None

    def addCourse(self, department, courseId, courseName, lecture, sections):
        department = department.upper()
        if self.get(department, courseId):
            return False
        else:
            self.put(department, courseId, CourseCatalogNode(department, courseId, courseName, lecture, sections))
            return True
        
    def addSection(self, department, courseId, section):
        department = department.upper()
        if self.get(department, courseId):
            self.get(department, courseId).sections.append(section)
            return True
        else:
            return False

    def inOrder(self):
        return self._inOrder(self.root)
    
    def _inOrder(self, tree):
        ret = ""
        if tree != None:
            ret += self._inOrder(tree.left)
            ret += tree.__str__()
            ret += self._inOrder(tree.right)
        return ret
    
    def preOrder(self):
        return self._preOrder(self.root)
    
    def _preOrder(self, tree):
        ret = ""
        if tree != None:
            ret += tree.__str__()
            ret += self._preOrder(tree.left)
            ret += self._preOrder(tree.right)
        return ret

    def postOrder(self):
        return self._postOrder(self.root)
    
    def _postOrder(self, tree):
        ret = ""
        if tree != None:
            ret += self._postOrder(tree.left)
            ret += self._postOrder(tree.right)
            ret += tree.__str__()
        return ret
    
    def getAttendableSections(self, department, courseId, availableDay, availableTime):
        department = department.upper()
        output = ""
        if self.get(department, courseId):
            for section in self.get(department, courseId).sections:
                if section.day == availableDay and section.time[0] >= availableTime[0] and section.time[1] <= availableTime[1]:
                    output += section.__str__() + "\n"
        
        return output
    
    def countCoursesByDepartment(self):
        output = {}
        return self._countCoursesByDepartment(self.root, output)
    
    def _countCoursesByDepartment(self, tree, output):
        course_dict = output
        if tree != None:
            self._countCoursesByDepartment(tree.left, course_dict)
            if tree.department not in course_dict:
                course_dict[tree.department] = 1
            else:
                course_dict[tree.department] += 1
            self._countCoursesByDepartment(tree.right, course_dict)
        return course_dict

    def put(self, department, courseId, courseNode):
        if self.root:
            self._put(department, courseId, courseNode, self.root)
        else:
            self.root = courseNode

    def _put(self, department, courseId, courseNode, currentNode):
        if department < currentNode.department:
            if currentNode.left:
                self._put(department, courseId, courseNode, currentNode.left)
            else:
                currentNode.left = courseNode
                currentNode.left.parent = currentNode
        elif department > currentNode.department:
            if currentNode.right:
                self._put(department, courseId, courseNode, currentNode.right)
            else:
                currentNode.right = courseNode
                currentNode.right.parent = currentNode
        else:
            if courseId < currentNode.courseId:
                if currentNode.left:
                    self._put(department, courseId, courseNode, currentNode.left)
                else:
                    currentNode.left = courseNode
                    currentNode.left.parent = currentNode
            else:
                if currentNode.right:
                    self._put(department, courseId, courseNode, currentNode.right)
                else:
                    currentNode.right = courseNode
                    currentNode.right.parent = currentNode                

    def get(self, department, courseId): # return the payload for a key if it exists
        if self.root:
            result = self._get(department, courseId, self.root) # return Node with matching dept and courseId if it exists, None otherwise
            if result:
                return result # payload is the Node itself
            else:
                return None
        else:
            return None
        
    def _get(self, department, courseId, currentNode):
        if not currentNode:
            return None
        elif currentNode.department == department and currentNode.courseId == courseId:
            return currentNode
        elif currentNode.department != department:
            if department < currentNode.department:
                return self._get(department, courseId, currentNode.left)
            else:
                return self._get(department, courseId, currentNode.right)
        elif currentNode.department == department and currentNode.courseId != courseId:
            if courseId < currentNode.courseId:
                return self._get(department, courseId, currentNode.left)
            else:
                return self._get(department, courseId, currentNode.right)
            

# cc = CourseCatalog()

# # add a new course: cmpsc 9
# lecture = Event("TR", (1530, 1645), "td-w 1701")
# section1 = Event("W", (1400, 1450), "north hall 1109")
# section2 = Event("W", (1500, 1550), "north hall 1109")
# section3 = Event("W", (1600, 1650), "north hall 1109")
# section4 = Event("W", (1700, 1750), "girvetz hall 1112")
# sections = [section1, section2, section3, section4]
# assert True == cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

# # add a new section to cmpsc 9
# section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
# assert True == cc.addSection("cmpsc", 9, section5)

# # add a new course: art 10
# lecture = Event("TR", (1300, 1550), "arts 2628")
# sections = []
# assert True == cc.addCourse("art", 10, "introduction to painting", lecture, sections)

# print("----- in-order traversal -----")
# print(cc.inOrder())

# print("----- pre-order traversal -----")
# print(cc.preOrder())

# print("----- post-order traversal -----")
# print(cc.postOrder())

# print("Task: find all cmpsc 9 sections held on Wednesday and within 15:00 - 17:00 time period")
# print(cc.getAttendableSections("cmpsc", 9, "W", (1500, 1700)))

# print("Task: count courses by department")
# print(cc.countCoursesByDepartment())
            