# Lab 8 - in.txt program

# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07
# Date: 2/23/2022

# This function would read each line in a text file, and prints the line number, the number of characters, and the line.
def read_file(file_name: str) -> None:
    file = open(file_name, 'r')

    lines_count = 0
    for line in file:
        line = line.strip("\n")
        charac_count = 0
        lines_count += 1
        charac_count += len(line)
        print("Line " + str(lines_count) + " (" + str(charac_count) + " chars): " + str(line))
    file.close()

# This function runs the read_file function.
def main():
    read_file('in.txt')

if __name__ == "__main__":
    main()