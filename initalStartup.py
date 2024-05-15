import sqlite3

conn = sqlite3.connect('ComputerScienceCoursesTaken.db')
cursor = conn.cursor()

# Adding courses to 
insert_query = "INSERT INTO Courses VALUES ('CSE100', 'Introduction to Computing', 'https://www.byui.edu/catalog/#/courses/rJuLFSw3X?bc=true&bcCurrent=CSE100%20-%20Introduction%20to%20Computing&bcGroup=Computer%20Science&bcItemType=courses'), ('CSE110', 'Introduction to Programming', 'https://www.byui.edu/catalog/#/courses/rkrSeUvn7?bc=true&bcCurrent=CSE110%20-%20Introduction%20to%20Programming&bcGroup=Computer%20Science&bcItemType=courses'), ('CSE111', 'Programming with Functions', 'https://www.byui.edu/catalog/#/courses/H1EmfUvn7?bc=true&bcCurrent=CSE111%20-%20Programming%20with%20Functions&bcGroup=Computer%20Science&bcItemType=courses'), ('CSE210', 'Programming with Classes', 'https://www.byui.edu/catalog/#/courses/HyO0xBP3X?bc=true&bcCurrent=CSE210%20-%20Programming%20with%20Classes&bcGroup=Computer%20Science&bcItemType=courses');"
cursor.execute(insert_query)
conn.commit()

conn.close()