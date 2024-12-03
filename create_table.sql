-- MySQL dump 10.13  Distrib 9.0.1, for macos15.0 (arm64)
--
-- Host: 127.0.0.1    Database: SDSC5003
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Classes`
--

DROP TABLE IF EXISTS `Classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Classes` (
  `class_id` varchar(10) NOT NULL,
  `class_name` varchar(50) DEFAULT NULL,
  `head_teacher` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Classes`
--

LOCK TABLES `Classes` WRITE;
/*!40000 ALTER TABLE `Classes` DISABLE KEYS */;
INSERT INTO `Classes` (`class_id`, `class_name`, `head_teacher`) VALUES ('C001','Class 1','Mr. Smith'),('C002','Class 2','Ms. Johnson'),('C003','Class 3','Dr. Adams'),('C004','Class 4','Dr. Miller');
/*!40000 ALTER TABLE `Classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Courses`
--

DROP TABLE IF EXISTS `Courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Courses` (
  `course_id` varchar(10) NOT NULL,
  `course_name` varchar(50) DEFAULT NULL,
  `credit` decimal(3,1) DEFAULT NULL,
  `course_type` varchar(10) DEFAULT NULL,
  `teacher_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`course_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `Courses_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `Teachers` (`teacher_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Courses`
--

LOCK TABLES `Courses` WRITE;
/*!40000 ALTER TABLE `Courses` DISABLE KEYS */;
INSERT INTO `Courses` (`course_id`, `course_name`, `credit`, `course_type`, `teacher_id`) VALUES ('C101','Mathematics',3.0,'Core','T001'),('C102','History',2.5,'Elective','T002'),('C103','Physics',4.0,'Core','T003'),('C104','Literature',3.0,'Elective','T004');
/*!40000 ALTER TABLE `Courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Scores`
--

DROP TABLE IF EXISTS `Scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Scores` (
  `score_id` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(10) DEFAULT NULL,
  `course_id` varchar(10) DEFAULT NULL,
  `score` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`score_id`),
  KEY `student_id` (`student_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `Scores_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE,
  CONSTRAINT `Scores_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Scores`
--

LOCK TABLES `Scores` WRITE;
/*!40000 ALTER TABLE `Scores` DISABLE KEYS */;
INSERT INTO `Scores` (`score_id`, `student_id`, `course_id`, `score`) VALUES (1,NULL,'C101',95.50),(2,'S002','C102',88.75),(3,'S003','C103',89.00),(4,'S004','C104',92.50);
/*!40000 ALTER TABLE `Scores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Students` (
  `student_id` varchar(10) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `class_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `class_id` (`class_id`),
  CONSTRAINT `Students_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `Classes` (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` (`student_id`, `name`, `gender`, `birth_date`, `class_id`) VALUES ('S001','Alice','F','2000-11-01','C001'),('S002','Jane Smith','F','2006-08-22','C002'),('S003','Chris Taylor','M','2007-03-21','C002'),('S004','Emily Davis','F','2006-12-15','C004');
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teachers`
--

DROP TABLE IF EXISTS `Teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Teachers` (
  `teacher_id` varchar(10) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teachers`
--

LOCK TABLES `Teachers` WRITE;
/*!40000 ALTER TABLE `Teachers` DISABLE KEYS */;
INSERT INTO `Teachers` (`teacher_id`, `name`, `gender`, `birth_date`, `title`) VALUES ('T001','Alice Brown','F','1980-05-20','Professor'),('T002','Bob White','M','1975-09-15','Associate Professor'),('T003','Charlie Green','M','1982-03-12','Senior Lecturer'),('T004','Diana Black','F','1988-11-30','Lecturer');
/*!40000 ALTER TABLE `Teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `username` varchar(50) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL,
  `student_id` varchar(10) DEFAULT NULL,
  `teacher_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `student_id` (`student_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `Users_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE,
  CONSTRAINT `Users_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `Teachers` (`teacher_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` (`username`, `password`, `role`, `student_id`, `teacher_id`) VALUES ('admin','$2b$12$Tl0NRruM567fZEit3/65VOuM4sAw6Ql9PnIGu0k7NDNrRkci2d0hq',NULL,NULL,NULL),('admin2','$2b$12$UATdYW7qXGuK5oiZ7teDMO2f/qhltO1oFyRwDXItac8vYZXQNaz3m','Teacher',NULL,'T001'),('alice_brown','$2b$12$Tl0NRruM567fZEit3/65VOuM4sAw6Ql9PnIGu0k7NDNrRkci2d0hq','Teacher',NULL,'T001'),('bob_white','$2b$12$Tl0NRruM567fZEit3/65VOuM4sAw6Ql9PnIGu0k7NDNrRkci2d0hq!','Teacher',NULL,'T002'),('charlie_green','$2b$12$Tl0NRruM567fZEit3/65VOuM4sAw6Ql9PnIGu0k7NDNrRkci2d0hq','Teacher',NULL,'T003'),('chris_taylor','$2b$12$Tl0NRruM567fZEit3/65VOuM4sAw6Ql9PnIGu0k7NDNrRkci2d0hq','Student','S003',NULL),('diana_black','$2b$12$Tl0NRruM567fZEit3/65VOuM4sAw6Ql9PnIGu0k7NDNrRkci2d0hq','Teacher',NULL,'T004'),('emily_davis','$2b$12$Tl0NRruM567fZEit3/65VOuM4sAw6Ql9PnIGu0k7NDNrRkci2d0hq','Student','S004',NULL),('jane_smith','$2b$12$Tl0NRruM567fZEit3/65VOuM4sAw6Ql9PnIGu0k7NDNrRkci2d0hq','Student','S002',NULL),('john_doe','$2b$12$Tl0NRruM567fZEit3/65VOuM4sAw6Ql9PnIGu0k7NDNrRkci2d0hq','Student',NULL,NULL);
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-04  6:26:38
