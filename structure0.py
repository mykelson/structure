class Student():
    """ Creates a student object """
    def __init__(self, name, id_no):
        """ initialize the class """
        self.name = name
        self.id = id_no

    def changeID(self, id_no):
        """ update the value of the id """
        self.id = id_no
    
    def print(self):
        """ display the student's info """
        print("{} id no is {}".format(self.name, self.id))
