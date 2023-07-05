class CourseBook:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if not name in self.__courses:
            self.__courses[name] = {"grade": None, "credits": None}
        
        self.__courses[name]["grade"] = grade
        self.__courses[name]["credits"] = credits

    def get_course(self, name: str):
        if not name in self.__courses:
            return None
        
        return self.__courses[name]
    
    def all_entries(self):
        return self.__courses
    
    def sum_courses(self):
        count = 0
        for item in self.__courses:
            count+=1
        return count
    
    def sum_credits(self):
        count = 0
        for item, details in self.__courses.items():
            count += details["credits"]

        return count
    
    def completed_courses(self):
        return f'{self.sum_courses()} completed courses, a total of {self.sum_credits()} credits'
    
    def mean(self):
        total_grades = 0
        for item, details in self.__courses.items():
            total_grades += details["grade"]

        mean = round(total_grades/self.sum_courses(), 1)

        return f'mean {mean}'
    
    def grade_distribution(self):
        grade_5 = 0
        grade_4 = 0
        grade_3 = 0
        grade_2 = 0
        grade_1 = 0

        for item, details in self.__courses.items():
            if details["grade"] == 5:
                grade_5 += 1
            elif details["grade"] == 4:
                grade_4 += 1            
            elif details["grade"] == 3:
                grade_3 += 1            
            elif details["grade"] == 2:
                grade_2 += 1
            elif details["grade"] == 1:
                grade_1 += 1

        mark = "x"

        result = "grade distribution\n"
        result += f'5: {mark * grade_5}\n'
        result += f'4: {mark * grade_4}\n'
        result += f'3: {mark * grade_3}\n'
        result += f'2: {mark * grade_2}\n'
        result += f'1: {mark * grade_1}\n'

        return result
    
class FileHandler():
    def __init__(self, filename: str):
        self.__filename = filename

    def load_file(self):
        courses = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, grade, credits = parts
                courses[name] = {"grade":grade, "credits": credits}

        return courses

    def save_file(self, coursebook: dict):
        with open(self.__filename, "w") as f:
            for name, details in coursebook.items():
                line = [name] + [str(details["grade"])] + [str(details["credits"])]
                f.write(";".join(line) + "\n")

class CourseBookApplication:
    def __init__(self) -> None:
        self.__coursebook = CourseBook()
        self.__filehandler = FileHandler("coursebook.txt")

        # add courses grades and credits from the file to the coursebook 
        for name, details in self.__filehandler.load_file().items():
            grade = int(details["grade"])
            credits = int(details["credits"])
            self.__coursebook.add_course(name, grade, credits)

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_entry(self):
        name = input("name: ")
        grade = input("grade: ")
        credits = input("credits: ")

        # check if grade is valid 
        course_details = self.__coursebook.get_course(name)
        if course_details == None:
            self.__coursebook.add_course(name, int(grade), int(credits))
        else:
            if int(grade) < course_details["grade"]:
                grade = course_details["grade"]
                self.__coursebook.add_course(name, int(grade), int(credits))
            else:
                self.__coursebook.add_course(name, int(grade), int(credits))



    def search(self):
        name = input("name: ")
        course_details = self.__coursebook.get_course(name)
        if course_details == None:
            print("Course unknown")
            return
        
        print(f'{name},({course_details["credits"]} cr), grade {course_details["grade"]}')

    def stats(self):
        print(self.__coursebook.completed_courses())
        print(self.__coursebook.grade_distribution())
        

    def exit(self):
        self.__filehandler.save_file(self.__coursebook.all_entries())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.stats()
            else:
                self.help()

application = CourseBookApplication()
application.execute()        
