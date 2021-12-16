-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: school_manigement
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `settings`
--

DROP TABLE IF EXISTS `settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `settings` (
  `object` varchar(15) NOT NULL,
  `answer` varchar(100) NOT NULL,
  PRIMARY KEY (`object`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `settings`
--

LOCK TABLES `settings` WRITE;
/*!40000 ALTER TABLE `settings` DISABLE KEYS */;
INSERT INTO `settings` VALUES ('1','0'),('10','0'),('2','0'),('3','0'),('4','0'),('5','0'),('6','2'),('7','2'),('8','2'),('9','2'),('api','0'),('background_mode',' white'),('defoult_devise','0'),('defoult_sim','1'),('mounth','Jan,Fab,Mar,Apr,May,Jun,July,Agu,Sep,Oct,Nov,Dec'),('school_name','School Name or/nanything');
/*!40000 ALTER TABLE `settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_info`
--

DROP TABLE IF EXISTS `staff_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_info` (
  `First_Name` varchar(30) NOT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Guardian` varchar(45) NOT NULL,
  `D_O_B` varchar(45) NOT NULL,
  `ID_No` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `Subjects` varchar(45) NOT NULL,
  `Phone_No` varchar(45) NOT NULL,
  `religion` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  PRIMARY KEY (`First_Name`,`ID_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_info`
--

LOCK TABLES `staff_info` WRITE;
/*!40000 ALTER TABLE `staff_info` DISABLE KEYS */;
INSERT INTO `staff_info` VALUES ('a bb','a','a','a','333333','Male','0w','8','m','p\n\n');
/*!40000 ALTER TABLE `staff_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_info`
--

DROP TABLE IF EXISTS `students_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students_info` (
  `First_Name` varchar(45) NOT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Guardian` varchar(45) NOT NULL,
  `Phone_No` varchar(45) DEFAULT NULL,
  `Class` varchar(10) DEFAULT NULL,
  `Roll_No` varchar(45) NOT NULL,
  `Religion` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `D_o_B` varchar(45) NOT NULL,
  `P_o_B` varchar(45) NOT NULL,
  `Lact_School` varchar(45) DEFAULT NULL,
  `D_O_A` varchar(45) DEFAULT NULL,
  `C_A` varchar(45) DEFAULT NULL,
  `Progress` varchar(45) DEFAULT NULL,
  `Conduct` varchar(45) DEFAULT NULL,
  `D_o_L` varchar(45) DEFAULT NULL,
  `C_L_F` varchar(45) DEFAULT NULL,
  `R_o_L` varchar(50) DEFAULT NULL,
  `Fee_Mounth01` varchar(10) DEFAULT NULL,
  `Fee_Mounth02` varchar(10) DEFAULT NULL,
  `Fee_Mounth03` varchar(10) DEFAULT NULL,
  `Fee_Mounth04` varchar(10) DEFAULT NULL,
  `Fee_Mounth05` varchar(10) DEFAULT NULL,
  `Fee_Mounth06` varchar(10) DEFAULT NULL,
  `Fee_Mounth07` varchar(10) DEFAULT NULL,
  `Fee_Mounth08` varchar(10) DEFAULT NULL,
  `Fee_Mounth09` varchar(10) DEFAULT NULL,
  `Fee_Mounth10` varchar(10) DEFAULT NULL,
  `Fee_Mounth11` varchar(10) DEFAULT NULL,
  `Fee_Mounth12` varchar(10) DEFAULT NULL,
  `Fee_Note` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`First_Name`,`Roll_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_info`
--

LOCK TABLES `students_info` WRITE;
/*!40000 ALTER TABLE `students_info` DISABLE KEYS */;
INSERT INTO `students_info` VALUES ('Abdul Hadi','Rajput','Father','3174010084','9','210902','M','Male','0000-00-00','Tando Jan M','------------------------','0000-00-00','0','----------','-------------','','','','1400','1400','1400','1400','1400','1400','1400','1400','1400','1400','1400','1400','None\n\n\n\n\n\n\n'),('Abdul Wahab','Rana','Abdul Ghafoor','3174010084','9','210901','M','Male','2004-08-26','Tando Jan M','------------------------','0000-00-00','0','----------','-------------','','','','1400','1400',NULL,'1400',NULL,NULL,NULL,'1400','0',NULL,'1400',NULL,'None\n\n\n\n\n\n'),('ee','-----','-----------','3174010084','8','210802','M','Male','0000-00-00','-----------','------------------------','0000-00-00','0','----------','-------------','','','','1400',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'None\n'),('Old','--------','-------------','3174010084','5','210501','M','Male','0000-00-00','------------------','-------------------','0000-00-00','0','----------','--------','0000-00-00','0','------',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('Old Student','--------','--------------','3174010084','10','211001','M','Male','0000-00-00','------------------','-------------------','0000-00-00','0','----------','--------','0000-00-00','0','------',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('rr','-----','-----------','3174010084','8','210801','M','Male','0000-00-00','-----------','------------------------','0000-00-00','0','----------','-------------','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('tt','-----','-----------','3174010084','7','210702','M','Male','0000-00-00','-----------','------------------------','0000-00-00','0','----------','-------------','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('uu','-----','-----------','3174010084','6','210602','M','Male','0000-00-00','-----------','------------------------','0000-00-00','0','----------','-------------','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('ww','-----','-----------','3174010084','6','210601','M','Male','0000-00-00','-----------','------------------------','0000-00-00','0','----------','-------------','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('yy','-----','-----------','3174010084','7','210701','M','Male','0000-00-00','-----------','------------------------','0000-00-00','0','----------','-------------','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `students_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-25 14:43:40
