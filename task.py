from interface import *
import sqlite3
from config import *

class Course(ABC):
    """Class which helds data about courses"""
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



class Teacher(ITeacher):
    """Class which helds data about teacher"""
    def __init__(self, name, courses):
        self.name = name
        self.courses = ", ".join(courses)
        self.add_to_base()
    
    def add_to_base(self):
        """Method which pulls teacher's data to the teacher_db"""
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS teacher_db(Name TEXT ,'
        'Courses TEXT )')
        con.commit()
        cur.execute('INSERT INTO teacher_db VALUES (?,?)', (self.name, self.courses))
        con.commit()
        cur.close()
        con.close()
       
    
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



class LocalCourse(Course, ILocalCourse):
    """Class which inherited Course class"""
    def __init__(self, name, teacher, program):
        super().__init__(name, teacher, program)

    def __str__(self):
        return f'Local course: {super().__str__()}'




class OffsiteCourse(Course, IOffciteCourse):
    """Class which inherited Course class"""
    def __init__(self, name, teacher, program):
        super().__init__(name, teacher, program)
        
    
    def __str__(self):
        return f'Offsite course: {super().__str__()}'

class CourseFactory(ABC):
    """Main class of the programm, which create instances of LocalCourse and OffsiteCourse and work with them"""
    def __init__(self):
       self.menu()
    

    def menu(self):
        """Simple menu to navigate through the programm"""
        while(1==1):
            type = input("1 - Add courses\n 2 - Show teacher's database\n 3 - Show all Courses\n 4 - Drop tables\n 0 - exit\n Your choise: ")
            if type == "1":
                self.add_info()
            elif type == "2":
                print("Teachers info: ")
                print(self.show_info_about_teachers())
            elif type == "3":
                print("Courses info: ")
                print(self.show_all_info())
            elif type == "4":
                self.drop_tables()
                print("TABLES DELETED!")
            elif type == "0":
                quit()

    def drop_tables(self):
        """Method which is used to destroy tables from database"""
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS courses_db")
        con.commit()
        cur.execute("DROP TABLE IF EXISTS  teacher_db")
        con.commit()
        cur.close()
        con.close()

    def add_info(self):
        """Method which pulls data to database"""
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        obj = self.get_info()
        cur.execute('CREATE TABLE IF NOT EXISTS courses_db(Name TEXT ,'
        'Teacher TEXT, '
        'Topics TEXT, '
        'Type TEXT )') 
        cur.execute('INSERT INTO courses_db(Name, Teacher, Topics, Type) VALUES (?,?,?,?)', (obj.name,obj.teacher.name, ", ".join(list(obj.program)), obj.__class__.__name__))
        con.commit()
        cur.close()
        con.close()
       

    def get_info(self):
        """Methon which get data about Course

        Returns: 
        LocalCourse: Returning class instance
        OffsiteCourse: Returning class instance
        
        """
        while 1==1:
            type = input("Enter type of course(1 - local, 0 - Offsite): ")
            if type == "1" or type =="0":
                break
        name = input("Enter name of course: ")
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        teacher_name = input("Enter teacher's info: ")
        if not isinstance(teacher_name, str):
            raise TypeError("Teacher name must be string")
        number = input("Enter number of courses: ")
        if int(number) <= 0:
            raise ValueError("Number must be >0")
        courses = []
        for i in range(0, int(number)):
            value = input()
            if not isinstance(value, str):
                raise TypeError("Course topic must be a string")
            courses.append(value)
            
        teacher = Teacher(teacher_name, courses)
        if type == "1":
            return LocalCourse(name, teacher, courses)
        else: 
            return OffsiteCourse(name, teacher, courses)
        

    def show_all_info(self):
        """Method which returns courses info
        
        Returns: 
        str: Returning courses_db as string or return empty error

        """
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='courses_db' ''')
        if cur.fetchone()[0]==1:
            cur.execute("SELECT * FROM courses_db")
            result = cur.fetchall()
            cur.close()
            con.close()
            return "\n".join(list(map(str, result)))
        return f"Empty table"

    def show_info_about_teachers(self):
        """Method which returns teachers info
        
        Returns: 
        str: Returning teacher_db as string or return empty error
        
        """
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='teacher_db' ''')
        if cur.fetchone()[0]==1:
            cur.execute("SELECT * FROM teacher_db")
            result = cur.fetchall()
            cur.close()
            con.close()
            return "\n".join(list(map(str, result)))
        return f"Empty table"



if __name__ == '__main__':
    x = CourseFactory()
    
  

