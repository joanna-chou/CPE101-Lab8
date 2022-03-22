# Lab 8 - hidden program

# Name: Joanna Chou
# Instructor: S. Einakian 
# Section: 07
# Date: 2/23/2022

# This function reads a ppm file and returns information about it.
def file_open(file_name: str) -> tuple:
    coded_picture = open(file_name, "r")

    lines = coded_picture.readlines()
    lst = []

    for line in lines:
        line = line.strip()
        if " " in line:
            splited_line = line.split()
            for value in splited_line:
                lst.append(value)
        else:
            lst.append(line)
    coded_picture.close()

    width = int(lst[1])
    height = int(lst[2])
    print(height)
    RGB_values = width * height * 3 + 4
    line_start = 4

    return (width, height, RGB_values, line_start, lst)

# This function uses information given to find lines where each RGB value is written.
def file_decode(info: tuple) -> tuple:
    header = "P3\n" + str(info[0]) + " " + str(info[1]) + "\n255\n"
    red_line_range = range(info[3],info[2],3)
    green_line_range = range(info[3]+1,info[2],3)
    blue_line_range = range(info[3]+2,info[2],3)
    return(header, red_line_range, green_line_range, blue_line_range)

# This function writes in a ppm file given information about another function and the RGB line ranges.
def file_write(file_name: str, info: tuple, decode: tuple) -> None:
    decoded_picture = open(file_name, "w")
    decoded_picture.write(decode[0])

    for num in range(info[3],info[2]):
        if num in decode[1]:
            red_line = int(info[4][num]) *10
            if red_line > 255:
                red_line = 255
            red_line = str(red_line)
            decoded_picture.write(red_line + "\n")
        elif num in decode[2] or num in decode[3]:
            green_blue_line = red_line
            decoded_picture.write(str(green_blue_line) + "\n")
    decoded_picture.close()
    
# This function runs the above functions.
def main():
    info = file_open('hidden.ppm')
    decode = file_decode(info)
    file_write('discovered.ppm', info, decode)

if __name__ == "__main__":
    main()
