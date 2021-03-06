-- MySQL dump 10.13  Distrib 5.6.26, for Win64 (x86_64)
--
-- Host: localhost    Database: kroketweb
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
-- Table structure for table `klant`
--

DROP TABLE IF EXISTS `klant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `klant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `naam` varchar(72) NOT NULL,
  `adres` varchar(72) NOT NULL,
  `plaats` varchar(72) NOT NULL,
  `telefoonnummer` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `klant`
--

LOCK TABLES `klant` WRITE;
/*!40000 ALTER TABLE `klant` DISABLE KEYS */;
/*!40000 ALTER TABLE `klant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `omschrijving` varchar(72) NOT NULL,
  `voorraad` int(11) NOT NULL,
  `prijs` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Garnalenkroket ',18,1.20),(2,'Broodje Garnalenkroket ',18,1.80),(3,'Kroket',20,1.00),(4,'Broodje Kroket',20,1.80),(5,'Goulashkroket',0,1.40),(6,'Broodje Goulashkroket',0,1.80),(7,'Portie patat',3000,1.50),(8,'Portie raspatat',240,1.75),(9,'Portie bittelballen',32,4.00),(10,'Coca Cola zero 50cl',66,1.65),(11,'Coca Cola 50cl',37,1.65),(12,'Coca Cola light 50cl',12,1.65),(13,'Pepsi 33cl',0,0.95),(14,'Pepsi Light 33cl',0,0.95),(15,'Pepsi Max 50cl',0,2.00),(16,'Broodje hamburger',35,3.00),(17,'Broodje hamburger super speciaal',38,3.50),(18,'Broodje tartaar',3,3.00),(19,'Broodje warm vlees',27,3.90),(20,'Tosti ham/kaas',30,2.10),(21,'Tosti hawaii',7,2.40),(22,'Wiener Schnitzelschotel',9,9.90),(23,'Ei salade',9,1.90),(24,'Spa rood 50cl',55,1.65),(25,'Spa blauw 50cl',0,1.65),(26,'Portie mayonaise',366,0.50),(27,'Portie speciaal',38,0.75),(28,'Portie joppie',90,0.50),(29,'Portie satesaus',36,0.80),(30,'Portie oorlog',44,1.00),(31,'Fanta 50cl',80,1.90),(32,'7Up 50cl',34,1.80),(33,'Snickers',45,0.60),(34,'Mars',45,0.60),(35,'Bounty',45,0.55);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-21 21:57:14
