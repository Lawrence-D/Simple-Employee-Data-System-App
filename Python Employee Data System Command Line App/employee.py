#Name:Lawrence D'Addio
#Date:3/23/16
#Description: Class that creates employee objects



class Employee:

    #Initializes attributes
    def __init__(self, name, id_num, department, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__job_title = job_title

    #Sets name attribute
    def set_name(name):
        self.__name = name

    #Sets id num attribute
    def set_id_num(id_num):
        self.__id_num = id_num

    #Sets department attribute
    def set_department(department):
        self.__department = department

    #Sets job title attribute
    def set_job_title(job_title):
        self.__job_title = job_title

    #Gets name attribute
    def get_name():
        return self.__name

    #Gets id num attribute
    def id_num():
        return self.__id_num

    #Gets department attribute
    def get_department():
        return self.__department

    #Gets job title attribute
    def get_job_title():
        return self.__job_title

    def __str__(self):
        return "Name: " + self.__name + \
               "\nID Number: " + self.__id_num + \
               "\nDepartment: " + self.__department + \
               "\nJob Title: " + self.__job_title + \
               "\n"
    
