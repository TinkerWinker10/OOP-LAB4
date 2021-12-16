from abc import ABC
from abc import abstractmethod
import json
import os

class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @program.setter
    @abstractmethod
    def program(self, value):
        pass




class Course:
    def __init__(self, name, teacher, program):
   
        self.name = name
        self.teacher = teacher 
        self.program = program

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError("Name must be string")
        if not value:
            raise ValueError("Empty value")
        self.__name = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self,value):
        if not isinstance(value, Teacher):
            raise TypeError("value must be instance of Teacher class")
        if not value:
            raise ValueError("Empty value")
        self.__teacher = value

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self,value):
        if not all([isinstance(item, str)for item in value]):
            raise TypeError("Programm must be string")
        if not value:
            raise ValueError("Empty value")
        self.__program = value
    

    
    def __str__(self):
        return f'Name of course: {self.name}, Teacher: {self.teacher}, Programm: {self.program}'

class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass


class Teacher:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    @property 
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError("Name must be string")
        if not value:
            raise ValueError("Empty value")
        self.__name = value

    def __str__(self):
        return f'{self.name}' 

class ILocalCourse(ABC):
    @abstractmethod
    def __init__(self):
        pass


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name, teacher, program):
        super().__init__(name, teacher, program)
   
    


     
    def __str__(self):
        return f'Local course: {super().__str__()}'

class IOffciteCourse(ABC):
    @abstractmethod
    def __init__(self):
        pass

class OffsiteCourse(Course, IOffciteCourse):
    def __init__(self, name, teacher, program):
        super().__init__(name, teacher, program)
        


    
    def __str__(self):
        return f'Offsite course: {super().__str__()}'



class CoursesFactory:
    def __init__(self):
        pass

    def add_course(self):
        while True:
            type = input("What type of courses you want to create? 0 - local, 1 - offsite ")
            if type == "1" or type == "0": 
                break
        name = input("Enter name of course: ")
        
        teacher_name = input("Enter teacher's name: ")
        topics = []
        teacher = Teacher(teacher_name, topics)
        while True:
            n = int(input("Enter number of topics: "))
            if n>0:
                break
                 
        for item in range (0,n):
            value = input("Enter topic: ")
            topics.append(value)
        if type=="0":
            course =  LocalCourse(name, teacher, topics)
        else :
            course =  OffsiteCourse(name, teacher, topics)

        data = {
                "name": course.name,
                "teacher": teacher_name,
                "program": course.program,
                "type": course.__class__.__name__
                }
       

        if os.stat("Course\\file.json").st_size==0:
            json.dump(data, open ("Course\\file.json", "w"), indent=2)
        else: 
            self.add_to_base(data)
           
    def add_to_base(self, data):
            with open ("Course\\file.json", "r") as file:
                base = json.load(file)
                base.append(data)
            with open ("Course\\file.json", "w") as file:    
                json.dump(base, file, indent=2)
            

    def get_all_courses(self):
        with open ("Course\\file.json", "r") as file:
            base = json.load(file)
        return "\n".join(list(map(str, base)))

        

if __name__ == "__main__":
    x = CoursesFactory()
    print(x.add_course())
    print(x.get_all_courses())
            
        
        


