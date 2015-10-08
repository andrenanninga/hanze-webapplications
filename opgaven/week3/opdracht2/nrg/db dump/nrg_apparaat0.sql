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
-- Table structure for table `apparaat`
--

DROP TABLE IF EXISTS `apparaat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apparaat` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `naam` varchar(64) DEFAULT NULL,
  `max` int(11) DEFAULT NULL,
  `merk` varchar(45) DEFAULT NULL,
  `apparaat_type_fk` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `apparaat_type_fk1_idx` (`apparaat_type_fk`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apparaat`
--

LOCK TABLES `apparaat` WRITE;
/*!40000 ALTER TABLE `apparaat` DISABLE KEYS */;
INSERT INTO `apparaat` VALUES (1,'roeimachine',20,NULL,2),(2,'zonnepaneel op dak',4000,NULL,0),(3,'mobiel zonnepaneel',100,NULL,0),(4,'groot zonnepaneel',6000,NULL,0),(5,'windmolen op dak',4500,NULL,1),(6,'windmolen in tuin',4200,NULL,1),(7,'windmolen op akker',6000,NULL,1),(24,'a',NULL,'a',0);
/*!40000 ALTER TABLE `apparaat` ENABLE KEYS */;
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
