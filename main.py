# Author: Woosung Lim wml5207@psu.print
def getGradePoint(grade1, grade2, grade3):

  if grade1 == "A":
    return 4.0
  elif grade1 == "A-":
    return 3.67
  elif grade1 == "B+":
    return 3.33
  elif grade1 == "B":
    return 3.0 
  elif grade1 == "B-":
    return 2.67
  elif grade1 == "C+":
    return 2.33
  elif grade1 == "C":
    return 2.0
  elif grade1 == "D":
    return 1.0
  else:
    return 0.0

  if grade2 == "A":
    return 4.0
  elif grade2 == "A-":
    return 3.67
  elif grade2 == "B+":
    return 3.33
  elif grade2 == "B":
    return 3.0 
  elif grade2 == "B-":
    return 2.67
  elif grade2 == "C+":
    return 2.33
  elif grade2 == "C":
    return 2.0
  elif grade2 == "D":
    return 1.0
  else:
    return 0.0

  if grade3 == "A":
    return 4.0
  elif grade3 == "A-":
    return 3.67
  elif grade3 == "B+":
    return 3.33
  elif grade3 == "B":
    return 3.0 
  elif grade3 == "B-":
    return 2.67
  elif grade3 == "C+":
    return 2.33
  elif grade3 == "C":
    return 2.0
  elif grade3 == "D":
    return 1.0
  else:
    return 0.0
 
def run():
  grade1 = input("Enter your course1 letter grade: ")
  credit1 = input("Enter your course 1 credit: ")
  print(f"Grade point for course 1 is: {getGradePoint(grade1)}")

  grade2 = input("Enter your course2 letter grade: ")
  credit2 = input("Enter your course 2 credit: ")
  print(f"Grade point for course 2 is: {getGradePoint(grade2)}")

  grade3 = input("Enter your course3 letter grade: ")
  credit3 = input("Enter your course 3 credit: ")
  print(f"Grade point for course 3 is: {getGradePoint(grade3)}")

  credit1 = float(credit1)
  credit2 = float(credit2)
  credit3 = float(credit3)
  GPA = (({grade1} * credit1) + (grade2 * credit2) + (grade3 * credit3))/(credit1 + credit2 + credit3)

  print("Your GPA is: " + str(GPA))

if __name__ == "__main__":
  run()


