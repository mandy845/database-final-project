-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: LS_Login
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

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
-- Table structure for table `Admin_user`
--

DROP TABLE IF EXISTS `Admin_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Admin_user` (
  `userid` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(15) DEFAULT NULL,
  `password` varchar(8) NOT NULL,
  `sign_in_date` date DEFAULT NULL,
  `sign_in_time` time DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin_user`
--

LOCK TABLES `Admin_user` WRITE;
/*!40000 ALTER TABLE `Admin_user` DISABLE KEYS */;
INSERT INTO `Admin_user` VALUES (1,'Amanda','mandy','2021-07-08','16:23:01'),(2,'Avela','Myoyo',NULL,NULL);
/*!40000 ALTER TABLE `Admin_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Login`
--

DROP TABLE IF EXISTS `Login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Login` (
  `Name` varchar(100) NOT NULL,
  `Surname` varchar(100) NOT NULL,
  `ID_number` varchar(13) NOT NULL,
  `Contact_number` varchar(10) NOT NULL,
  `Next_of_kin_name` varchar(100) NOT NULL,
  `Next_of_kin_number` varchar(10) NOT NULL,
  `username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `sign_in_date` date DEFAULT NULL,
  `sign_in_time` time DEFAULT NULL,
  `sign_out_time` time DEFAULT NULL,
  PRIMARY KEY (`ID_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Login`
--

LOCK TABLES `Login` WRITE;
/*!40000 ALTER TABLE `Login` DISABLE KEYS */;
INSERT INTO `Login` VALUES ('','','','','','','','','2021-07-10','22:29:00',NULL),('Atang','Makara','0001118007108','0639851235','Relebohile','0749864125','Princess','Ati',NULL,NULL,NULL),('qsdfgy','aasdfgh','0123495687092','072 978697','fghjnlkjmlkjnkl','0879686574','Nina','Kay',NULL,NULL,NULL),('Mombilo','Benina','0123496754093','0720738232','Kayficient','0655542498','Kay','12345678',NULL,NULL,NULL),('xdtcfyvub','uigyuftydr','0987654321084','0987654321','sxdfcg','0789654321','Avela','Myoyo',NULL,'11:37:00','11:43:00'),('rxtcfgvy','sxrdtcfvgbh','09876609876','0789654321','rxdtcfvgbjh','0967854312','khuselwa','qwashu','2021-07-10','16:06:00','16:07:00'),('rftghj','sdfg','1234567890123','0876584321','werergerg','0759784320','Atang','princess',NULL,NULL,NULL),('musa','simba','632091038456','0682956645','ethel','0652319067','simba','Sunjamjnr@$99',NULL,'14:45:00',NULL);
/*!40000 ALTER TABLE `Login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 11:41:52
