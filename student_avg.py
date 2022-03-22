# Lab 8 - student_avg program

# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07
# Date: 2/23/2022

# This function computes the average given a total and a count.
def avg(total: float, count: int) -> float:
    return total/count

# This function reads a text file, finds GPAs for EE, CPE, and all students, and returns the averages for each GPA.
def file_open(file_name: str) -> tuple:
    file = open(file_name, "r")
    
    EE_total = 0
    EE_count = 0
    CPE_total = 0
    CPE_count = 0
    student_total = 0
    student_count = 0

    for line in file:
        words = line.split()
        student_count += 1
        student_total += float(words[3])
        if words[2] == "EE":
            EE_count += 1
            EE_total += float(words[3])
        elif words[2] == "CPE":
            CPE_count += 1
            CPE_total += float(words[3])
    file.close()
    return (avg(EE_total, EE_count), avg(CPE_total, CPE_count) , avg(student_total, student_count))

# This function copies the grades to a new text file.
def file_write_grades(new_file: str, old_file: str) -> None:
    file1 = open(new_file, "w")
    file2 = open(old_file, "r")
    for line in file2:
        text = line
        file1.write(text)
    file1.close()
    file2.close()

# This function appends the calculated averages into the new text file.
def file_write_avg(file_name: str, info: tuple) -> None:
    file1 = open(file_name, "a")
    text = "\n\n" + "EE average = " + str("{:.2f}".format(info[0])) + "\n" + "CPE average = " + str("{:.2f}".format(info[1])) + "\n" + "Total average = " + str("{:.2f}".format(info[2]))
    file1.write(text)
    file1.close()
        
# This function runs the above functions.
def main():
    file_write_grades('student_avg.txt', 'std_info.txt')
    file_write_avg('student_avg.txt', (file_open('std_info.txt')))

if __name__ == "__main__":
    main()
