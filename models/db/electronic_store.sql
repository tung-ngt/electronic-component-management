-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: electronic
-- ------------------------------------------------------
-- Server version	8.0.30
create database electronic;
use electronic;
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
-- Table structure for table `capacitor`
--

DROP TABLE IF EXISTS `capacitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capacitor` (
  `part_number` varchar(255) NOT NULL,
  `mnf_id` varchar(255) NOT NULL,
  `price` bigint NOT NULL,
  `inventory_date` varchar(255) NOT NULL,
  `status` int NOT NULL,
  `guarantee` int NOT NULL,
  `capacitance` varchar(255) NOT NULL,
  `sub_category` varchar(255) NOT NULL,
  `stock` bigint NOT NULL,
  PRIMARY KEY (`part_number`),
  KEY `mnf_id` (`mnf_id`),
  CONSTRAINT `capacitor_ibfk_1` FOREIGN KEY (`mnf_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capacitor`
--

LOCK TABLES `capacitor` WRITE;
/*!40000 ALTER TABLE `capacitor` DISABLE KEYS */;
INSERT INTO `capacitor` VALUES ('PRT012','KLM789',170,'2022-03-27',1,3,'9.2NF','CAP FILM',700),('PRT123','BCD890',110,'2022-03-24',0,5,'9.4NF','CAP NIOB OXID',650),('PRT124','FGH890',230,'2022-04-03',0,5,'4.7NF','CAP ALUM POLY',550),('PRT232','JKL012',210,'2022-03-18',1,4,'6.2NF','CAP CER RAD',1050),('PRT233','STU901',70,'2022-03-21',1,2,'7.3NF','CAP TANT POLY',1200),('PRT234','WXY901',150,'2022-03-31',0,12,'3.3NF','CAP ALUM POLY',400),('PRT344','ABC123',90,'2022-03-15',0,12,'5.1NF','CAP TRIMMER ',500),('PRT345','NOP012',60,'2022-03-28',1,4,'9.3NF','CAP FILM',950),('PRT456','EFG123',220,'2022-03-25',1,10,'4.1NF','CAP NIOB OXID',1100),('PRT566','VWX234',140,'2022-03-22',1,3,'4.5NF','CAP TANT POLY',450),('PRT567','ZAB234',40,'2022-04-01',1,3,'10.3NF','CAP ALUM POLY',750),('PRT672','DEF456',160,'2022-03-16',1,12,'4.7NF','CAP TRIMMER ',950),('PRT673','MNO345',50,'2022-03-19',0,5,'6.8NF','CAP CER RAD',900),('PRT674','QRS345',200,'2022-03-29',1,5,'5.3NF','CAP FILM',500),('PRT789','HIJ456',90,'2022-03-26',1,5,'4.8NF','OXICAP',350),('PRT890','YZA567',30,'2022-03-23',1,4,'8.2NF','CAP TANT POLY',800),('PRT891','CDE567',120,'2022-04-02',1,4,'4.6NF','CAP ALUM POLY',100),('PRT901','GHI789',30,'2022-03-17',0,3,'5.6NF','CAP TRIMMER',700),('PRT902','PQR678',190,'2022-03-20',1,8,'4.9NF','CAP CER RAD',600),('PRT903','TUV678',80,'2022-03-30',1,10,'2.3NF','CAP ALUM POLY',850);
/*!40000 ALTER TABLE `capacitor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ic`
--

DROP TABLE IF EXISTS `ic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ic` (
  `part_number` varchar(255) NOT NULL,
  `mnf_id` varchar(255) NOT NULL,
  `price` bigint NOT NULL,
  `inventory_date` varchar(255) NOT NULL,
  `status` int NOT NULL,
  `guarantee` int NOT NULL,
  `clock` varchar(255) NOT NULL,
  `sub_category` varchar(255) NOT NULL,
  `stock` bigint NOT NULL,
  PRIMARY KEY (`part_number`),
  KEY `mnf_id` (`mnf_id`),
  CONSTRAINT `ic_ibfk_1` FOREIGN KEY (`mnf_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ic`
--

LOCK TABLES `ic` WRITE;
/*!40000 ALTER TABLE `ic` DISABLE KEYS */;
INSERT INTO `ic` VALUES ('PRT0123','BCD890',160,'2022-04-01',1,6,'1.6GHZ','IC CLK BUFFER',506),('PRT0123A','CDE567',120,'2022-01-02',1,4,'1.9GHZ','IC ADC',100),('PRT1234','ABC123',90,'2022-03-31',0,6,'1.7GHZ','IC MODULATOR',409),('PRT1234B','FGH890',230,'2022-08-03',0,5,'2.0GHZ','IC ADC',552),('PRT2345','DEF456',40,'2022-04-01',1,3,'1.8GHZ','IC AUDIO ',754),('PRT2345A','EFG123',110,'2022-04-02',1,4,'2.3GHZ','IC CLK BUFFER',804),('PRT3456','GHI789',120,'2022-04-02',0,4,'1.9GHZ','IC SAMPLE RATE',1003),('PRT3456A','HIJ456',260,'2022-05-03',1,7,'1.8GHZ','IC FANOUT BUFFER',353),('PRT4567','JKL012',230,'2022-04-03',1,5,'2.0GHZ','IC AUDIO SIGNAL PROCESSOR ',551),('PRT4567A','KLM789',70,'2022-09-30',0,2,'1.1GHZ','IC FANOUT BUFFER',204),('PRT5678','MNO345',140,'2022-03-31',0,6,'1.7GHZ','IC VOLUME CONTROL ',407),('PRT5678A','NOP012',150,'2022-02-01',0,5,'1.4GHZ','IC CLK MULTPX',600),('PRT6789','PQR678',270,'2022-05-01',1,3,'2.5GHZ','IC MODULATOR',458),('PRT6789A','QRS345',220,'2022-04-02',0,6,'2.1GHZ','IC CLK MULTPX',901),('PRT7890','STU901',130,'2022-04-02',0,5,'2.2GHZ','IC AUDIO RECEIVER',655),('PRT7890A','TUV678',100,'2022-09-03',1,3,'1.3GHZ','IC CLK MULTIPLXR ',303),('PRT8901','VWX234',190,'2022-03-03',1,8,'1.5GHZ','IC LINE DRIVER',307),('PRT8901A','WXY901',180,'2022-03-31',1,2,'1.5GHZ','IC CLK MULTIPLXR ',704),('PRT9012','YZA567',80,'2022-03-31',0,9,'1.2GHZ','IC CLK BUFFER',254),('PRT9012A','ZAB234',40,'2022-02-01',0,3,'1.8GHZ','IC ADC',751);
/*!40000 ALTER TABLE `ic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inductor`
--

DROP TABLE IF EXISTS `inductor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inductor` (
  `part_number` varchar(255) NOT NULL,
  `mnf_id` varchar(255) NOT NULL,
  `price` bigint NOT NULL,
  `inventory_date` varchar(255) NOT NULL,
  `status` int NOT NULL,
  `guarantee` int NOT NULL,
  `inductance` varchar(255) NOT NULL,
  `sub_category` varchar(255) NOT NULL,
  `stock` bigint NOT NULL,
  PRIMARY KEY (`part_number`),
  KEY `mnf_id` (`mnf_id`),
  CONSTRAINT `inductor_ibfk_1` FOREIGN KEY (`mnf_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inductor`
--

LOCK TABLES `inductor` WRITE;
/*!40000 ALTER TABLE `inductor` DISABLE KEYS */;
INSERT INTO `inductor` VALUES ('PRT0545','BCD890',342,'2022-04-23',0,3,'10UH','FIXED IND 10UH ',390),('PRT0710','FGH890',235,'2022-08-13',0,2,'100NH','FIXED IND 100NH',559),('PRT1004','CDE567',141,'2022-09-17',1,5,'100NH','FIXED IND 100NH',102),('PRT1200','HIJ456',219,'2022-04-04',0,1,'10UH','FIXED IND 10UH',345),('PRT1203','YZA567',332,'2022-03-21',1,2,'18NH','FIXED IND 18NH ',950),('PRT1204','NOP012',281,'2022-01-29',1,7,'1UH','FIXED IND 1UH ',620),('PRT1205','EFG123',325,'2022-02-27',0,9,'10UH','FIXED IND 10UH',420),('PRT2013','QRS345',295,'2022-04-29',1,6,'1UH','FIXED IND 1UH ',910),('PRT2013A','TUV678',119,'2022-02-22',1,3,'4.7UH','FIXED IND 4.7UH ',329),('PRT2033','JKL012',544,'2022-02-01',1,12,'2.2UH','FIXED IND 2.2UH ',120),('PRT2034','DEF456',230,'2022-04-02',0,5,'10UH','FIXED IND 10UH  ',589),('PRT2035','MNO345',232,'2022-03-09',1,2,'2.2UH','FIXED IND 2.2UH  ',490),('PRT2504','ZAB234',421,'2022-03-20',0,10,'4.7UH','FIXED IND 4.7UH',755),('PRT3040','GHI789',123,'2022-04-13',1,7,'10UH','FIXED IND 10UH  ',345),('PRT3045','ABC123',234,'2022-03-12',1,2,'10UH','FIXED IND 10UH  ',123),('PRT3201','PQR678',540,'2022-04-23',1,9,'2.2UH','FIXED IND 2.2UH  ',495),('PRT3245','VWX234',388,'2022-04-13',0,1,'18NH','FIXED IND 18NH  ',123),('PRT5453','WXY901',123,'2022-03-21',1,7,'4.7UH','FIXED IND 4.7UH',710),('PRT7460','STU901',124,'2022-04-12',0,2,'18NH','FIXED IND 18NH  ',235),('PRT8054','KLM789',254,'2022-02-12',0,2,'1UH','FIXED IND 1UH',201);
/*!40000 ALTER TABLE `inductor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturer`
--

DROP TABLE IF EXISTS `manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturer` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturer`
--

LOCK TABLES `manufacturer` WRITE;
/*!40000 ALTER TABLE `manufacturer` DISABLE KEYS */;
INSERT INTO `manufacturer` VALUES ('ABC123','ABC Manufacturing','USA'),('BCD890','BCD Manufacturing','UK'),('CDE567','CDE Manufacturing','India'),('DEF456','DEF Manufacturing','Canada'),('EFG123','EFG Manufacturing','Ukraine'),('FGH890','FGH Manufacturing','Qatar'),('GHI789','GHI Manufacturing','Germany'),('HIJ456','HIJ Manufacturing','Vietnam'),('JKL012','JKL Manufacturing','Japan'),('KLM789','KLM Manufacturing','Thailand'),('MNO345','MNO Manufacturing','USA'),('NOP012','NOP Manufacturing','Laos'),('PQR678','PQR Manufacturing','Canada'),('QRS345','QRS Manufacturing','Cambodia'),('STU901','STU Manufacturing','France'),('TUV678','TUV Manufacturing','Singapore'),('VWX234','VWX Manufacturing','Poland'),('WXY901','WXY Manufacturing','South Korea'),('YZA567','YZA Manufacturing','Philippines'),('ZAB234','ZAB Manufacturing','Nepal');
/*!40000 ALTER TABLE `manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resistor`
--

DROP TABLE IF EXISTS `resistor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resistor` (
  `part_number` varchar(255) NOT NULL,
  `mnf_id` varchar(255) NOT NULL,
  `price` bigint NOT NULL,
  `inventory_date` varchar(255) NOT NULL,
  `status` int NOT NULL,
  `guarantee` int NOT NULL,
  `resistance` varchar(255) NOT NULL,
  `sub_category` varchar(255) NOT NULL,
  `stock` bigint NOT NULL,
  PRIMARY KEY (`part_number`),
  KEY `mnf_id` (`mnf_id`),
  CONSTRAINT `resistor_ibfk_1` FOREIGN KEY (`mnf_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resistor`
--

LOCK TABLES `resistor` WRITE;
/*!40000 ALTER TABLE `resistor` DISABLE KEYS */;
INSERT INTO `resistor` VALUES ('PRT0123','BCD890',305,'2022-01-23',0,24,'1.69K','RES 1.69K OHM ',390),('PRT0123A','CDE567',129,'2022-04-17',1,4,'43.2K','RES 43.2K OHM',102),('PRT1234','ABC123',59,'2022-03-23',0,5,'120K','RES 120K OHM ',123),('PRT1234B','FGH890',232,'2022-12-13',0,5,'43.2K','RES 43.2K OHM',559),('PRT2345','DEF456',43,'2022-04-09',0,7,'120K','RES 120K OHM  ',589),('PRT2345A','EFG123',308,'2022-03-27',1,12,'2.8K','RES 2.8K OHM',420),('PRT3456','GHI789',132,'2022-04-12',1,8,'88.7K','RES 88.7K OHM ',345),('PRT3456A','HIJ456',250,'2022-04-20',0,8,'2.8K','RES 2.8K OHM',345),('PRT4567','JKL012',492,'2022-02-04',1,12,'88.7K','RES 88.7K OHM',120),('PRT4567A','KLM789',70,'2022-03-12',0,4,'2.8K','RES 2.8K OHM',201),('PRT5678','MNO345',123,'2022-03-05',0,8,'88.7K','RES 88.7K OHM ',490),('PRT5678A','NOP012',160,'2022-02-26',0,7,'9.09K','RES 9.09K OHM ',620),('PRT6789','PQR678',580,'2022-04-21',1,24,'120K','RES 120K OHM ',495),('PRT6789A','QRS345',230,'2022-08-29',1,3,'9.09K','RES 9.09K OHM ',910),('PRT7890','STU901',124,'2022-01-30',0,12,'120K','RES 120K OHM ',235),('PRT7890A','TUV678',127,'2022-06-22',0,5,'13.8K','RES 13.8K OHM ',329),('PRT8901','VWX234',389,'2022-03-31',0,4,'1.69K','RES 1.69K OHM ',123),('PRT8901A','WXY901',198,'2022-07-21',1,9,'13.8K','RES 13.8K OHM ',710),('PRT9012','YZA567',302,'2022-03-28',0,9,'1.69K','RES 1.69K OHM',950),('PRT9012A','ZAB234',494,'2022-09-20',1,12,'43.2K','RES 43.2K OHM',755);
/*!40000 ALTER TABLE `resistor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor`
--

DROP TABLE IF EXISTS `sensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sensor` (
  `part_number` varchar(255) NOT NULL,
  `mnf_id` varchar(255) NOT NULL,
  `price` bigint NOT NULL,
  `inventory_date` varchar(255) NOT NULL,
  `status` int NOT NULL,
  `guarantee` int NOT NULL,
  `sensor_type` varchar(255) NOT NULL,
  `sub_category` varchar(255) NOT NULL,
  `stock` bigint NOT NULL,
  PRIMARY KEY (`part_number`),
  KEY `mnf_id` (`mnf_id`),
  CONSTRAINT `sensor_ibfk_1` FOREIGN KEY (`mnf_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor`
--

LOCK TABLES `sensor` WRITE;
/*!40000 ALTER TABLE `sensor` DISABLE KEYS */;
INSERT INTO `sensor` VALUES ('PRT0712','JKL012',204,'2022-05-20',1,9,'Liquid conduction','FLOW SENSOR MEMS ',543),('PRT1111','FGH890',212,'2022-09-14',1,12,'Liquid conduction','FLOW SENSOR MEMS 20L/MIN',510),('PRT1231','NOP012',291,'2022-02-22',1,12,'Gas','FSENSOR GAS FLOW TYPE 0-1L/MIN  ',605),('PRT1294','KLM789',224,'2022-08-10',1,24,'Gas','SENSOR GAS FLOW TYPE 0-1L/MIN ',249),('PRT2042','QRS345',215,'2022-08-27',0,7,'Gas','SENSOR GAS FLOW TYPE 0-1L/MIN  ',802),('PRT2121','TUV678',129,'2022-11-20',1,2,'Liquid conduction','SENSOR MICRO-FLOW ',323),('PRT2301','VWX234',312,'2022-05-05',1,2,'Gas','SENSOR GAS FLOW  ',185),('PRT2302','EFG123',323,'2022-01-09',0,5,'Temperature','AIRFLOW SENSOR',412),('PRT2304','ABC123',123,'2022-02-13',0,1,'Temperature','DIGITAL FLOW SENSOR ',124),('PRT2903','DEF456',850,'2022-06-05',1,5,'Temperature','DIGITAL FLOW SENSOR  ',232),('PRT2909','GHI789',392,'2022-02-10',0,5,'Temperature','DIGITAL FLOW SENSOR ',215),('PRT3021','PQR678',493,'2022-09-27',1,12,'Liquid conduction','FLOW SENSOR MEMS ',491),('PRT3040','YZA567',395,'2022-06-12',0,3,'Gas','SENSOR GAS FLOW',912),('PRT4304','STU901',144,'2022-03-04',1,7,'Gas','SENSOR GAS FLOW ',221),('PRT4400','CDE567',111,'2022-10-18',0,9,'Liquid conduction','FLOW SENSOR MEMS 20L/MIN',129),('PRT5345','BCD890',321,'2022-08-13',1,12,'Temperature','AIRFLOW SENSOR ',360),('PRT5454','WXY901',106,'2022-07-30',0,5,'Liquid conduction','SENSOR MICRO-FLOW',769),('PRT5940','MNO345',123,'2022-01-22',0,2,'Liquid conduction','FLOW SENSOR MEMS',499),('PRT8542','HIJ456',212,'2022-03-03',0,2,'Temperature','AIRFLOW SENSOR',345),('PRT9922','ZAB234',481,'2022-12-12',1,8,'Liquid conduction','SENSOR MICRO-FLOW',723);
/*!40000 ALTER TABLE `sensor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-30  9:54:06
