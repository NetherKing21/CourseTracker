import sqlite3

def main():
    #Set up
    userID = None
    userName = None
    conn = sqlite3.connect('ComputerScienceCoursesTaken.db')
    cursor = conn.cursor()
    run = True
    options = ["Make New Student", "Set User", "Display All Courses", "Add Course to Plan", "Display Plan", "Delete Course from Plan", "Delete User", "Quit"]

    
    while run:
        displayMenu(options)
        userInput = getInt(" > ", len(options))
        if(userInput > 0 and userInput < len(options)):
            if (userInput == 1):
                makeNewUser(conn, cursor)
            elif (userInput == 2):
                userInfo = setUser(cursor)
                userID = userInfo[0]
                userName = userInfo[1]
                print(f"You are now set as student #{userID} {userName}")
            elif (userInput == 3):
                displayAllCourses(conn)
            elif (userInput == 4):
                addCourseToPlan(conn, cursor, userName, userID)
            elif (userInput == 5):
                displayPlan(cursor, userID)
            elif (userInput == 6):
                deleteCourse(conn, cursor, userName, userID)
            elif (userInput == 7):
                deleteUser(conn, cursor)
        elif(userInput == len(options)):
            run = False
        else:
            print("Invalid Response")

    conn.close()

def displayMenu(options):
    print("Chose an option")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    

def makeNewUser(conn, cursor):
    new_student = input("Enter full name of Student: ")
    insert_query = f"INSERT INTO Students (studentName) VALUES ('{new_student}');"
    cursor.execute(insert_query)
    conn.commit()

def setUser(cursor):
    databaseInfo = cursor.execute("SELECT * FROM Students")
    keys = []
    all_students = {}
    for row in databaseInfo:
        keys.append(row[0])
        all_students[row[0]] = row[1]

    for i in range(len(keys)):
        print(f" {i+1}. {all_students[keys[i]]}")
    userInput = getInt("Enter user number: ", len(all_students), 1) - 1
    userInfo = (keys[userInput], all_students[keys[userInput]])
    return userInfo

def displayAllCourses(cursor):
    databaseInfo = cursor.execute("SELECT courseID, courseName FROM Courses")
    courseIDs = {}
    for (i, row) in enumerate(databaseInfo, 1):
        courseIDs[i] = row
        print(f'{i}. {row}')
    return courseIDs

def displayPlan(cursor, userID):
    if (userID is not None):
        databaseInfo = cursor.execute(f"SELECT SC.courseID, courseName, status FROM 'Students have Courses' AS SC JOIN Courses ON Courses.courseID = SC.courseID WHERE studentID = {userID}")
        plan = {}
        for (i, row) in enumerate(databaseInfo, 0):
            plan[i] = row
        if (len(plan) > 0):
            for ii in range(len(plan)):
                print(f"{ii+1}. {plan[ii]}")
            return plan
        else:
            print("You don't have any courses in your plan")
    else:
        print("Must Set User before to Display Plan")

def addCourseToPlan(conn, cursor, userName, userID):
    if (userName is not None and userID is not None):
        courses = displayAllCourses(cursor)
        userInput = getInt("Enter the number of course you want to add: ", len(courses), 1)
        courseInfo = courses.get(userInput)
        courseID = courseInfo[0]
        status = getStatus()
        insert_query = f"INSERT INTO 'Students have Courses' (studentID, courseID, status) VALUES ({userID}, '{courseID}', {status});"
        cursor.execute(insert_query)
        conn.commit()
        print(f"{courseID} Status:{status} has been added to {userName}'s Plan")
    else:
        print("Must Set User before you can add a course")

def deleteCourse(conn, cursor, userName, userID):
    if (userName is not None and userID is not None):
        courses = displayPlan(cursor, userID)
        if (len(courses) > 0):
            userInput = getInt("Enter the number of course you want to delete: ", len(courses), 1) - 1
            courseInfo = courses.get(userInput)
            courseID = courseInfo[0]
            status = courseInfo[2]
            delete_query = f"DELETE FROM 'Students have Courses' WHERE (studentID = {userID} AND courseID = '{courseID}' AND status = '{status}');"
            cursor.execute(delete_query)
            conn.commit()
            print(f"{courseID} Status:{status} has been removed from {userName}'s Plan")
        else:
            print(f"There are no courses to delete")
    else:
        print("Must Set User before you can delete a course")

def deleteUser(conn, cursor):
    databaseInfo = cursor.execute("SELECT * FROM Students")
    keys = []
    all_students = {}
    for row in databaseInfo:
        keys.append(row[0])
        all_students[row[0]] = row[1]

    for i in range(len(keys)):
        print(f" {i+1}. {all_students[keys[i]]}")
    userInput = getInt("Enter user number: ", len(all_students), 1) - 1
    studentID = keys[userInput]
    studentName = all_students.get(keys[userInput])
    print(f"Are you sure you want to delete student #{studentID} {studentName}?")
    print(f"This will also delete all associated data regarding this student")
    confirmation = input("Type DELETE to confirm (anything else will cancel the operation): ")
    if (confirmation == 'DELETE'):
        delete_query = f"DELETE FROM 'Students have Courses' WHERE studentID = {studentID}"
        cursor.execute(delete_query)
        delete_query = f"DELETE FROM Students WHERE studentID = {studentID}"
        cursor.execute(delete_query)
        conn.commit()
    else:
        print("Deletion has been canceled")


def getInt(message, maxInput, minInput = 0):
    flag = False
    while not flag:
        try:
            userInput = int(input(message))
            if (userInput < minInput or userInput > maxInput):
                raise Exception
            flag = True
            return userInput
        except:
            print("Invalid response")

def getStatus():
    flag = False
    while not flag:
        try:
            userInput = input("Have you already TAKEN, currently TAKING this course or is it just PLANNED? ")
            if (userInput.lower() == "planned"  or userInput.lower() == "taking" or userInput.lower() == "taken"):
                flag = True
                return f"'{userInput.upper()}'"
            else:
                raise Exception
        except:
            print("Invalid response")

if __name__ == "__main__":
    main()