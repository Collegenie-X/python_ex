class Person : 
    def __init__(self , name , job ):
        self.name = name 
        self.job = job 
        
    def introduce(self) : 
        print(f"제 이름은 {self.name} 입니다. 직업은 {self.job} 입니다.")
        

class Actor(Person) : 
    def __init__ (self,name,best_movie) : 
        super().__init__(name, "배우") 
        self.best_movie = best_movie
    
    def filmography(self) :         
        print(f"대표 작품은 {self.best_movie} 입니다.")
        

if __name__ == "__main__" : 
    
    jungkook = Person("정국", "학생") 
    jungkook.introduce() 
    
    actor = Actor("박명수", "betman") 
    actor.introduce() 
    actor.filmography()