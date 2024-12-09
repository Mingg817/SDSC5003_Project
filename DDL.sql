CREATE TABLE Users (
    Username VARCHAR(50) PRIMARY KEY,
    Password VARCHAR(255),
    Role VARCHAR(20),
    StudentID VARCHAR(10),
    TeacherID VARCHAR(10),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID) ON DELETE CASCADE
);

CREATE TABLE Teachers (
    TeacherID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(50),
    Gender CHAR(1),
    BirthDate DATE,
    Title VARCHAR(50)
);

CREATE TABLE Students (
    StudentID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(50),
    Gender CHAR(1),
    BirthDate DATE,
    ClassID VARCHAR(10),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
);

CREATE TABLE Classes (
    ClassID VARCHAR(10) PRIMARY KEY,
    ClassName VARCHAR(50),
    HeadTeacher VARCHAR(50)
);

CREATE TABLE Courses (
    CourseID VARCHAR(10) PRIMARY KEY,
    CourseName VARCHAR(50),
    Credit DECIMAL(3,1),
    CourseType VARCHAR(10),
    TeacherID VARCHAR(10),
    FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID) ON DELETE CASCADE
);

CREATE TABLE Scores (
    ScoreID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID VARCHAR(10),
    CourseID VARCHAR(10),
    Score DECIMAL(5,2),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);