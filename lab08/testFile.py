# testFile.py

from Event import Event
from CourseCatalogNode import CourseCatalogNode
from CourseCatalog import CourseCatalog

# Event.py tests

def test_event_attributes():
    e = Event("MW", (1000, 1100), "UCSB Library")
    assert e.day == "MW"
    assert e.time == (1000, 1100)
    assert e.location == "UCSB LIBRARY"

def test_event_str():
    e = Event("MW", (1000, 1100), "UCSB Library")
    assert e.__str__() == "MW 10:00 - 11:00, UCSB LIBRARY"
    assert e.__str__() != "MW 10:00 - 11:00, UCSB Library"

def test_event_eq():
    e1 = Event("MW", (1000, 1100), "UCSB Library")
    e2 = Event("MW", (1000, 1100), "UCSB Library")
    e3 = Event("TR", (1000, 1100), "UCSB Library")
    e4 = Event("MW", (1000, 1200), "UCSB Library")
    e5 = Event("MW", (1000, 1100), "srb")
    e6 = Event("TR", (1000, 1200), "UCSB Library")
    e7 = Event("MW", (1000, 1200), "srb")
    e8 = Event("TR", (1000, 1200), "srb")

    assert e1 == e2
    assert e1 != e3
    assert e1 != e4
    assert e1 != e5
    assert e1 != e6
    assert e1 != e7
    assert e1 != e8

# CourseCatalogNode.py tests

def test_CourseCatalogNode_attributes():
    cs9 = Event("TR", (1530, 1645), "buchanan hall 1910")
    e1 = Event("W", (1400, 1450), "ssms 1310")
    sections = [e1]
    cc = CourseCatalogNode("cmpsc", 9, "intermediate python", cs9, sections)

    assert cc.department == "CMPSC"
    assert cc.courseId == 9
    assert cc.courseName == "INTERMEDIATE PYTHON"
    assert cc.lecture == Event("TR", (1530, 1645), "buchanan hall 1910")
    assert cc.lecture.__str__() == "TR 15:30 - 16:45, BUCHANAN HALL 1910"
    assert cc.sections == [Event("W", (1400, 1450), "ssms 1310")]
    assert cc.parent == None
    assert cc.left == None
    assert cc.right == None

def test_CourseCatalogNode_str():
    lecture = Event("TR", (1530, 1645), "td-w 1701")

    # create four section events
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]

    # initialize a CMPSC 9 course node
    node = CourseCatalogNode("cmpsc", 9, "intermediate python", lecture, sections)

    assert node.__str__() == \
"CMPSC 9: INTERMEDIATE PYTHON\n\
 * Lecture: TR 15:30 - 16:45, TD-W 1701\n\
 + Section: W 14:00 - 14:50, NORTH HALL 1109\n\
 + Section: W 15:00 - 15:50, NORTH HALL 1109\n\
 + Section: W 16:00 - 16:50, NORTH HALL 1109\n\
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112\n"
    
def test_CourseCatalogNode_links():
    lecture1 = Event("TR", (1530, 1645), "td-w 1701")
    lecture2 = Event("TR", (1300, 1550), "arts 2628")
    sections = []

    course1 = CourseCatalogNode("cmpsc", 9, "intermediate python", lecture1, sections)
    course2 = CourseCatalogNode("art", 10, "introduction to painting", lecture2, sections)

    course1.left = course2
    course2.parent = course1

    assert course1.left.department == "ART"
    assert course2.parent.department == "CMPSC"

# CourseCatalog.py tests

def test_CourseCatalog_add():
    cc = CourseCatalog()

    # add a new course: cmpsc 9
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    assert True == cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    # add a new section to cmpsc 9
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    assert True == cc.addSection("cmpsc", 9, section5)

    # add a new course: art 10
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    assert True == cc.addCourse("art", 10, "introduction to painting", lecture, sections)

def test_CourseCatalog_inOrder():
    cc = CourseCatalog()

    # add a new course: cmpsc 9
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    # add a new section to cmpsc 9
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("cmpsc", 9, section5)

    # add a new course: art 10
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    cc.addCourse("art", 10, "introduction to painting", lecture, sections)
    
    assert cc.inOrder() == \
"ART 10: INTRODUCTION TO PAINTING\n\
 * Lecture: TR 13:00 - 15:50, ARTS 2628\n\
CMPSC 9: INTERMEDIATE PYTHON\n\
 * Lecture: TR 15:30 - 16:45, TD-W 1701\n\
 + Section: W 14:00 - 14:50, NORTH HALL 1109\n\
 + Section: W 15:00 - 15:50, NORTH HALL 1109\n\
 + Section: W 16:00 - 16:50, NORTH HALL 1109\n\
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112\n\
 + Section: F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101\n"

def test_CourseCatalog_preOrder():
    cc = CourseCatalog()

    # add a new course: cmpsc 9
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    # add a new section to cmpsc 9
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("cmpsc", 9, section5)

    # add a new course: art 10
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    cc.addCourse("art", 10, "introduction to painting", lecture, sections)
    
    assert cc.preOrder() == \
"CMPSC 9: INTERMEDIATE PYTHON\n\
 * Lecture: TR 15:30 - 16:45, TD-W 1701\n\
 + Section: W 14:00 - 14:50, NORTH HALL 1109\n\
 + Section: W 15:00 - 15:50, NORTH HALL 1109\n\
 + Section: W 16:00 - 16:50, NORTH HALL 1109\n\
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112\n\
 + Section: F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101\n\
ART 10: INTRODUCTION TO PAINTING\n\
 * Lecture: TR 13:00 - 15:50, ARTS 2628\n"
    
def test_CourseCatalog_postOrder():
    cc = CourseCatalog()

    # add a new course: cmpsc 9
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    # add a new section to cmpsc 9
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("cmpsc", 9, section5)

    # add a new course: art 10
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    cc.addCourse("art", 10, "introduction to painting", lecture, sections)
    
    assert cc.postOrder() == \
"ART 10: INTRODUCTION TO PAINTING\n\
 * Lecture: TR 13:00 - 15:50, ARTS 2628\n\
CMPSC 9: INTERMEDIATE PYTHON\n\
 * Lecture: TR 15:30 - 16:45, TD-W 1701\n\
 + Section: W 14:00 - 14:50, NORTH HALL 1109\n\
 + Section: W 15:00 - 15:50, NORTH HALL 1109\n\
 + Section: W 16:00 - 16:50, NORTH HALL 1109\n\
 + Section: W 17:00 - 17:50, GIRVETZ HALL 1112\n\
 + Section: F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101\n"

def test_getAttendableSections():
    cc = CourseCatalog()

    # add a new course: cmpsc 9
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    # add a new section to cmpsc 9
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("cmpsc", 9, section5)

    # add a new course: art 10
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    cc.addCourse("art", 10, "introduction to painting", lecture, sections)

    assert cc.getAttendableSections("cmpsc", 9, "W", (1500, 1700)) == \
"W 15:00 - 15:50, NORTH HALL 1109\n\
W 16:00 - 16:50, NORTH HALL 1109\n"

def test_countCoursesByDepartment():
    cc = CourseCatalog()

    # add a new course: cmpsc 9
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    # add a new section to cmpsc 9
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("cmpsc", 9, section5)

    # add a new course: art 10
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    cc.addCourse("art", 10, "introduction to painting", lecture, sections)

    assert cc.countCoursesByDepartment() == {'ART': 1, 'CMPSC': 1}