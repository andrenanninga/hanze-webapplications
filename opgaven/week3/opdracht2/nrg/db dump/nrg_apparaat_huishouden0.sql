-- MySQL dump 10.13  Distrib 5.6.24, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: nrg
-- ------------------------------------------------------
-- Server version	5.6.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `apparaat_huishouden`
--

DROP TABLE IF EXISTS `apparaat_huishouden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apparaat_huishouden` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `huishouden_fk` int(10) unsigned DEFAULT NULL,
  `apparaat_fk` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hh_idx` (`huishouden_fk`),
  KEY `app_idx` (`apparaat_fk`),
  CONSTRAINT `apparaat_huishouden_ibfk_1` FOREIGN KEY (`huishouden_fk`) REFERENCES `huishouden` (`id`),
  CONSTRAINT `apparaat_huishouden_ibfk_2` FOREIGN KEY (`apparaat_fk`) REFERENCES `apparaat` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=194 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apparaat_huishouden`
--

LOCK TABLES `apparaat_huishouden` WRITE;
/*!40000 ALTER TABLE `apparaat_huishouden` DISABLE KEYS */;
INSERT INTO `apparaat_huishouden` VALUES (65,63,1),(67,64,2),(68,64,4),(69,64,4),(71,64,4),(72,64,1),(73,64,3),(74,64,1),(76,65,2),(77,65,3),(78,65,2),(79,65,2),(80,65,4),(81,65,1),(82,65,7),(83,65,3),(84,65,2),(87,66,2),(89,66,3),(92,67,1),(93,68,2),(94,68,1),(95,68,6),(96,69,2),(97,69,4),(98,69,1),(99,69,5),(100,69,6),(101,70,1),(102,70,1),(103,70,6),(104,70,2),(105,70,4),(106,70,5),(107,70,5),(108,70,7),(109,71,5),(110,71,5),(111,71,5),(112,71,6),(113,71,3),(114,71,7),(115,72,3),(116,72,6),(117,72,1),(118,72,6),(119,72,1),(120,72,4),(121,72,7),(122,72,3),(123,73,6),(124,73,1),(125,73,7),(126,73,2),(127,73,5),(128,73,3),(129,73,3),(130,73,3),(131,73,1),(132,74,2),(133,74,6),(134,74,2),(135,74,6),(136,74,4),(137,74,2),(138,74,2),(139,74,2),(140,75,4),(141,75,4),(142,75,7),(143,75,7),(144,75,5),(145,75,6),(146,75,4),(147,75,6),(148,75,4),(149,76,4),(150,76,7),(151,77,7),(152,77,1),(153,77,4),(154,77,2),(155,77,2),(156,77,6),(157,78,4),(158,78,1),(159,78,4),(160,79,6),(161,79,7),(162,80,1),(163,80,7),(164,80,6),(165,80,5),(166,80,4),(167,80,6),(168,80,5),(169,80,5),(170,81,5),(171,81,2),(172,81,1),(173,81,7),(174,81,6),(175,81,5),(176,82,6),(177,82,7),(178,82,7),(179,82,4),(180,83,2),(181,83,5),(182,83,3),(183,83,3),(184,83,2),(185,83,3),(186,83,3),(190,66,1);
/*!40000 ALTER TABLE `apparaat_huishouden` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-07 18:40:26
