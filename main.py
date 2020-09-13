# Author: Woosung Lim wml5207@psu.print
def getGradePoint(grade):

  if grade == "A":
    return 4.0
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0 
  elif grade == "B-":
    return 2.67
  elif grade == "C+":
    return 2.33
  elif grade == "C":
    return 2.0
  elif grade == "D":
    return 1.0
  else:
    return 0.0

def run():
  grade = input("Enter your course 1 letter grade: ")
  grade1 = getGradePoint(grade)
  credit1 = input("Enter your course 1 credit: ")
  print(f"Grade point for course 1 is: {getGradePoint(grade)}")

  grade = input("Enter your course 2 letter grade: ")
  grade2 = getGradePoint(grade)
  credit2 = input("Enter your course 2 credit: ")
  print(f"Grade point for course 2 is: {getGradePoint(grade)}")

  grade = input("Enter your course 3 letter grade: ")
  grade3 = getGradePoint(grade)
  credit3 = input("Enter your course 3 credit: ")
  print(f"Grade point for course 3 is: {getGradePoint(grade)}")

  credit1 = float(credit1)
  credit2 = float(credit2)
  credit3 = float(credit3)
  GPA = ((grade1 * credit1) + (grade2 * credit2) + (grade3 * credit3))/(credit1 + credit2 + credit3)

  print("Your GPA is: " + str(GPA))

if __name__ == "__main__":
  run()


