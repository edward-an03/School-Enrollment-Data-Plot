# school_enrollment_data_plot.py
# Edward An
# A terminal-based application to process and plot data based on given user input and provided csv files.

import numpy as np
import matplotlib.pyplot as plt
import math

class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


# Import data here
school_data_2018_2019 = np.genfromtxt("SchoolData_2018-2019.csv", delimiter = ",", skip_header = True)
school_data_2019_2020 = np.genfromtxt("SchoolData_2019-2020.csv", delimiter = ",", skip_header = True)
school_data_2020_2021 = np.genfromtxt("SchoolData_2020-2021.csv", delimiter = ",", skip_header = True)

# Hint: Create a dictionary for all school names and codes
school_dictionary = {"1224":"Centennial High School", "1679":"Robert Thirsk School", "9626":"Louise Dean School",\
                "9806":"Queen Elizabeth High School", "9813":"Forest Lawn High School", "9815":"Crescent Heights High School",\
                "9816":"Western Canada High School", "9823":"Central Memorial High School", "9825":"James Fowler High School",\
                "9826":"Ernest Manning High School", "9829":"William Aberhart High School", "9830":"National Sport School",\
                "9836":"Henry Wise Wood High School", "9847":"Bowness High School", "9850":"Lord Beaverbrook High School",\
                "9856":"Jack James High School", "9857":"Sir Winston Churchill High School", "9858":"Dr. E. P. Scarlett High School",\
                "9860":"John G Diefenbaker High School" ,"9865":"Lester B. Pearson High School"}

# Hint: Create a list of school codes to help with index look-up in arrays
school_codes_list = list(school_dictionary.keys()) 
school_names_list = list(school_dictionary.values())

def calculate_mean_enrollment(school_code, grade):
    """A function that calculates the average enrollment. 
    It returns the calculated value after rounding it down to the nearest integer

        Parameters: school_code (str), grade (int)
        Return: enrollment_mean (int)
    """
    row_index = school_codes_list.index(school_code) #school is determined by this index
    column_index = grade - 9 #grade level is determined by this index
    enrollment_2018_2019 = school_data_2018_2019[row_index][column_index] #gets enrollment values for all three years
    enrollment_2019_2020 = school_data_2019_2020[row_index][column_index]
    enrollment_2020_2021 = school_data_2020_2021[row_index][column_index]
    enrollment_mean = math.floor((enrollment_2018_2019 + enrollment_2019_2020 + enrollment_2020_2021)/3) #average calculation
    return enrollment_mean

def alumni_2019_2021(school_code):
    """A function that calculates the total number of alumnis from 2019-2021. 
    It adds up all the grade 12 students in each year

        Parameters: school_code(str)
        Return: total_alumni (int)
    """
    index = school_codes_list.index(school_code) #school is determined by this index
    alumni_2019 = school_data_2018_2019[index][3] #gets number of grade 12 students for all three years
    alumni_2020 = school_data_2019_2020[index][3]
    alumni_2021 = school_data_2020_2021[index][3]
    total_alumni = math.floor(alumni_2019 + alumni_2020 + alumni_2021) #finds the total
    return total_alumni

def create_y_values_figure_1(school_code, year):
    """A function that creates a list to be used as y values for a graph in figure 1 
    The list contains a number of students for each grade level in a given year

        Parameters: school_code(str), year (num)
        Return: y_values (list)
    """
    index = school_codes_list.index(school_code) #school is determined by this index
    y_values = []
    if year == 2019: #depending on the year passed as the argument, the file specific to that year is used
        y_values.append(school_data_2018_2019[index][1])
        y_values.append(school_data_2018_2019[index][2])
        y_values.append(school_data_2018_2019[index][3])
    elif year == 2020:
        y_values.append(school_data_2019_2020[index][1])
        y_values.append(school_data_2019_2020[index][2])
        y_values.append(school_data_2019_2020[index][3])
    elif year == 2021:
        y_values.append(school_data_2020_2021[index][1])
        y_values.append(school_data_2020_2021[index][2])
        y_values.append(school_data_2020_2021[index][3])
    return y_values

def create_y_values_figure_2(school_code, grade):
    """A function that creates a list to be used as y values for a graph in figure 2
    The list contains a number of students for each year in a given grade

        Parameters: school_code(str), grade (num)
        Return: y_values (list)
    """
    row_index = school_codes_list.index(school_code) #school is determined by this index
    column_index = grade - 9 #grade level is determined by this index
    y_values = []
    y_values.append(school_data_2018_2019[row_index][column_index])
    y_values.append(school_data_2019_2020[row_index][column_index])
    y_values.append(school_data_2020_2021[row_index][column_index])
    return y_values

# Add your code within the main function. A docstring is not required for this function.
def main(): 
    print("Welcome to School Enrollment Statistics\n")

    # Print array data here
    print("Array data for 2020-2021:")
    print(school_data_2020_2021)
    print()
    print("Array data for 2019-2020:")
    print(school_data_2019_2020)
    print()
    print("Array data for 2018-2019:")
    print(school_data_2018_2019)

    # Add request for user input here
    repeat=True
    school_name = ""
    school_code = ""
    while (repeat == True):
        user_input = input("Please enter the high school name or school code: ")
        if user_input in school_names_list: # If the user provides the school_name
            repeat = False
            school_name = user_input
        elif user_input in school_codes_list: # If the user provides the school_code
            repeat = False
            school_code = user_input
        else: # If the user provided name or the code doesn't exist in the data. The user is prompted to re-enter their input
            print("You must enter a valid school name or code.")
            repeat == True

    # If the user provided the school code instead of the school name, the corresponding school name is found
    if school_name == "":
        school_name = school_dictionary[school_code]
    # If the user provided the school name instead of the school code, the corresponding school code is found
    else: 
        index = school_names_list.index(school_name)
        school_code = school_codes_list[index]

    print("\n***Requested School Statistics***\n")
    
    # Print school name and code using the given class
    school1 = School(school_name, school_code)
    school1.print_all_stats() #printing school name and school code

    # Add data processing and plotting here
    grade10_enrollment_mean = calculate_mean_enrollment(school_code, 10)
    grade11_enrollment_mean = calculate_mean_enrollment(school_code, 11)
    grade12_enrollment_mean = calculate_mean_enrollment(school_code, 12)
    total_alumni = alumni_2019_2021(school_code)

    # Mean enrollment for each grade and total number of graduates
    print("Mean enrollment for Grade 10: {}".format(grade10_enrollment_mean))
    print("Mean enrollment for Grade 11: {}".format(grade11_enrollment_mean))
    print("Mean enrollment for Grade 12: {}".format(grade12_enrollment_mean))
    print("Total number of students who graduated in the past three years: {}".format(total_alumni))

    # Data Plotting

    # x and y values for FIGURE 1
    grade = list(range(10, 13))
    y_values_2019 = create_y_values_figure_1(school_code, 2019)
    y_values_2020 = create_y_values_figure_1(school_code, 2020)
    y_values_2021 = create_y_values_figure_1(school_code, 2021)

    #FIGURE 1
    plt.figure()
    plt.plot(grade, y_values_2019, 'ro', label = "2019 Enrollment")
    plt.plot(grade, y_values_2020, 'go', label = "2020 Enrollment")
    plt.plot(grade, y_values_2021, 'bo', label = "2021 Enrollment")
    plt.xticks(grade)
    plt.title("Grade Enrollment by Year")
    plt.xlabel("Grade Level")
    plt.ylabel("Number of Students")
    plt.legend(loc = "upper left")

    # x and y values for FIGURE 2
    year = list(range(2019, 2022))
    y_values_10 = create_y_values_figure_2(school_code, 10)
    y_values_11 = create_y_values_figure_2(school_code, 11)
    y_values_12 = create_y_values_figure_2(school_code, 12)

    #FIGURE 2
    plt.figure()

    #Subplot 1 in FIGURE 2
    plt.subplot(3, 1, 1) 
    plt.plot(year, y_values_10, 'y--', label = "Grade 10")
    plt.xticks(year)
    plt.ylabel("Number of Students")
    plt.legend(loc = "upper right")
    plt.title("Enrollment by Grade")

    #Subplot 2 in FIGURE 2
    plt.subplot(3, 1, 2)
    plt.plot(year, y_values_11, 'm--', label = "Grade 11")
    plt.xticks(year)
    plt.ylabel("Number of Students")
    plt.legend(loc = "upper right")

    #Subplot 3 in FIGURE 2
    plt.subplot(3, 1, 3)
    plt.plot(year, y_values_12, 'c--', label = "Grade 12")
    plt.xticks(year)
    plt.ylabel("Number of Students")
    plt.xlabel("Enrollment Year")
    plt.legend(loc = "upper right")

    plt.show()

if __name__ == '__main__':
    main()
