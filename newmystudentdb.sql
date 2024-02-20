-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: mystudentdb
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `books1`
--

DROP TABLE IF EXISTS `books1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books1` (
  `Sr no.` int NOT NULL AUTO_INCREMENT,
  `Books` varchar(100) NOT NULL,
  `Qty` int DEFAULT NULL,
  `HSN No.` int NOT NULL,
  `Price` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Sr no.`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books1`
--

LOCK TABLES `books1` WRITE;
/*!40000 ALTER TABLE `books1` DISABLE KEYS */;
INSERT INTO `books1` VALUES (1,'Jurassic Park',49,8501,'Rs 200'),(2,'Dune',49,8502,'Rs 200'),(3,'Nineteen Eighty Four',50,8503,'Rs 200'),(4,'The Name of the Wind',50,8504,'Rs 200'),(5,'The Way of Kings',50,8505,'Rs 200'),(6,'The Fifth Season',50,8506,'Rs 200'),(7,'Pride and Prejudice',50,8507,'Rs 200'),(8,'Red White and Royal Blue',50,8508,'Rs 200'),(9,'Jane Eyre',50,8509,'Rs 200'),(10,'Vicious',50,8510,'Rs 200'),(11,'Vengeful',50,8511,'Rs 200'),(12,'Wolf Hall',50,8512,'Rs 200'),(13,'HHhH',55,8513,'Rs 200'),(14,'I, Claudius',50,8514,'Rs 200'),(15,'Frankenstein',50,8515,'Rs 200'),(16,'Dracula',50,8516,'Rs 200'),(17,'The Shining',55,8517,'Rs 200'),(18,'In Cold Blood',50,8518,'Rs 200'),(19,'Murder On The Orient Express',50,8519,'Rs 200'),(20,'Silence of the lambs',55,8520,'Rs 200');
/*!40000 ALTER TABLE `books1` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `books1_BEFORE_INSERT` BEFORE INSERT ON `books1` FOR EACH ROW BEGIN

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `books3`
--

DROP TABLE IF EXISTS `books3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books3` (
  `Sr no` int NOT NULL,
  `Months` varchar(45) DEFAULT NULL,
  `Sales` varchar(45) DEFAULT NULL,
  `Membership Buy-Ins` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Sr no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books3`
--

LOCK TABLES `books3` WRITE;
/*!40000 ALTER TABLE `books3` DISABLE KEYS */;
INSERT INTO `books3` VALUES (1,'January','50000','Rs 20000'),(2,'February','70000','Rs 20000'),(3,'March','45000','Rs 20000'),(4,'April','34000','Rs 20000'),(5,'May','12000','Rs 20000'),(6,'June','34000','Rs 20000'),(7,'July','100000','Rs 20000'),(8,'August','200000','Rs 20000'),(9,'September','45000','Rs 20000'),(10,'October','34000','Rs 20000'),(11,'November','20000','Rs 20000'),(12,'December','30000','Rs 20000');
/*!40000 ALTER TABLE `books3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books4`
--

DROP TABLE IF EXISTS `books4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books4` (
  `Sr no` int NOT NULL,
  `Months` varchar(45) DEFAULT NULL,
  `Sales` varchar(45) DEFAULT NULL,
  `Memberships` varchar(45) DEFAULT NULL,
  `Merchandise` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Sr no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books4`
--

LOCK TABLES `books4` WRITE;
/*!40000 ALTER TABLE `books4` DISABLE KEYS */;
INSERT INTO `books4` VALUES (1,'January','35000','Rs 10000','Rs 5000'),(2,'February','67000','Rs 10000','Rs 5000'),(3,'March','55000','Rs 10000','Rs 5000'),(4,'April','13000','Rs 10000','Rs 5000'),(5,'May','56000','Rs 10000','Rs 5000'),(6,'June','56000','Rs 10000','Rs 5000'),(7,'July','560000','Rs 10000','Rs 5000'),(8,'August','45000','Rs 10000','Rs 5000'),(9,'September','56890','Rs 10000','Rs 5000'),(10,'October','45000','Rs 10000','Rs 5000'),(11,'November','56000','Rs 10000','Rs 5000'),(12,'December','90000','Rs 10000','Rs 5000');
/*!40000 ALTER TABLE `books4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `Unique Code` int NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Duration of Membership` int DEFAULT NULL,
  `State` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Delays` int DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  PRIMARY KEY (`Unique Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (3911,'Uttara K',88,'HP','MALE',35,44,'fdfss@gmail.com','1987-12-06'),(4911,'Jenny P',90,'Kerala','FEMALE',23,67,'ffg@gmail.com','1996-01-21'),(5911,'Anuj L',45,'Punjab','MALE',34,34,'fdfd@gmail.com','1985-07-12'),(6911,'Bilal J',500,'UP','MALE',28,77,'ffdf@gmail.com','1986-07-18'),(7911,'Efraim G',100,'J&K','MALE',39,0,'ffdddds@gmail.com','1975-08-16'),(8911,'Tarun U',30,'MP','MALE',40,19,'sd@gmail.com','1975-09-10'),(9911,'Uttam J',70,'UK','MALE',23,10,'hjhj@gmail.com','1996-09-15');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score`
--

DROP TABLE IF EXISTS `score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `score` (
  `Sr No` int NOT NULL AUTO_INCREMENT,
  `Months` varchar(45) DEFAULT NULL,
  `Vedant Khare` varchar(45) DEFAULT NULL,
  `Mohit Soni` varchar(45) DEFAULT NULL,
  `Pritam Rana` varchar(45) DEFAULT NULL,
  `Parv Dhar` varchar(45) DEFAULT NULL,
  `Garima Dua` varchar(45) DEFAULT NULL,
  `Aparna Mittal` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Sr No`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score`
--

LOCK TABLES `score` WRITE;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
INSERT INTO `score` VALUES (1,'January','Rs 62000','Rs 67000','Rs 89000','Rs 54000','Rs 55000','Rs 66000'),(2,'February','Rs 90000','Rs 56000','Rs 89000','Rs 34000','Rs 23000','Rs 45400'),(3,'March','Rs 100000','Rs 33000','Rs 89000','Rs 45000','Rs 67500','Rs 56000'),(4,'April','Rs 67000','Rs 45000','Rs 67000','Rs 67000','Rs 4440','Rs 6700'),(5,'May','Rs 60000','Rs 12000','Rs 56000','Rs 77000','Rs 12000','Rs 78000'),(6,'June','Rs 56000','Rs 45000','Rs 23780','Rs 89009','Rs 44000','Rs 239090'),(7,'July','Rs 77000','Rs 89000','Rs 67500','Rs 33000','Rs 23000','Rs 5688'),(8,'August','Rs 230000','Rs 12000','Rs 45000','Rs 76000','Rs 45000','Rs 78000'),(9,'September','Rs 120000','Rs 67110','Rs 43000','Rs 44000','Rs 55000','Rs 45000'),(10,'October','Rs 200000','Rs 12000','Rs 70000','Rs 12000','Rs 54900','Rs 54900'),(11,'November','Rs 56900','Rs 83333','Rs 56000','Rs 23000','Rs 99000','Rs 56000'),(12,'December','Rs 78000','Rs 67000','Rs 34000','Rs 100000','Rs 120000','Rs 54900');
/*!40000 ALTER TABLE `score` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-01 16:23:18
