from abc import ABC
from abc import abstractmethod



class ICourse(ABC):
    """Interface for Course class"""
    @property
    @abstractmethod
    def name(self):
        """Getter method for name value"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """Setter method for name value"""
        pass

    @property
    @abstractmethod
    def teacher(self):
        """Getter method for teacher value"""
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        """Setter method for teacher value"""
        pass

    @property
    @abstractmethod
    def program(self):
        """Getter method for programm value"""
        pass

    @program.setter
    @abstractmethod
    def program(self, value):
        """Setter method for program value"""
        pass




class ITeacher(ABC):
    """Interface for Teacher class"""
    @property
    @abstractmethod
    def name(self):
        """Getter method for name value"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """Setter method for name value"""
        pass



class ILocalCourse(ABC):
    """Interface for LocalCourse class"""
    @abstractmethod
    def __init__(self):
        pass


class IOffciteCourse(ABC):
    """Interface for IOffsiteCourse"""
    @abstractmethod
    def __init__(self):
        pass

class ICourseFactory(ABC):
    """Interface for ICourseFactory"""
    @abstractmethod
    def add_info(self):
        """Method which pulls data to database"""
        pass

    @abstractmethod
    def drop_table(self):
        """Method which is used to destroy tables from database"""
        pass

    @abstractmethod
    def get_info(self):
        """Methon which get data about Course

        Returns: 
        LocalCourse: Returning class instance
        OffsiteCourse: Returning class instance
        
        """
        pass
    
    @abstractmethod
    def show_all_info(self):
        """Method which returns courses info
        
        Returns: 
        str: Returning courses_db as string or return empty error

        """
        pass

    @abstractmethod
    def show_info_by_teacher_name(self):
        """Method which returns teachers info
        
        Returns: 
        str: Returning teacher_db as string or return empty error
        
        """
        pass

    @abstractmethod
    def menu(self):
        """Simple menu to navigate through the programm"""
        pass