-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: iot
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `path`
--

DROP TABLE IF EXISTS `path`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `path` (
  `id` varchar(45) NOT NULL,
  `runner_id` varchar(45) DEFAULT NULL,
  `path_x` float DEFAULT NULL,
  `path_y` float DEFAULT NULL,
  `speed` float DEFAULT NULL,
  `heart_rate` int DEFAULT NULL,
  `distance` float DEFAULT NULL,
  `path_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `runner_id_idx` (`runner_id`),
  CONSTRAINT `runner_id` FOREIGN KEY (`runner_id`) REFERENCES `runner` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `path`
--

LOCK TABLES `path` WRITE;
/*!40000 ALTER TABLE `path` DISABLE KEYS */;
INSERT INTO `path` VALUES ('01093476-a133-4a1a-8a19-cf16d1e638b5','milos_veljkovic@gmail.com',2769,226,4.94757,109,2.81,'My First Exercise'),('03bfdda9-32e9-40b4-b458-a02de66b336d','milos_veljkovic@gmail.com',3542,222,4.29854,103,3.59,'My First Exercise'),('061ec3fc-2354-46bd-b0ec-1bad484f12d1','milos_veljkovic@gmail.com',4857,209,5.19058,112,4.93,'My First Exercise'),('07647d05-0633-4cec-9190-b6d635e85a4c','predrag_antic@gmail.com',1066,226,4.61928,106,0.83,'First time'),('07accf6b-baeb-4875-a1c0-2945e5f6b750','milos_veljkovic@gmail.com',4300,203,3.82746,98,4.36,'My First Exercise'),('21389ecc-9d51-4464-a72e-f6b4ea74a7e5','milos_veljkovic@gmail.com',2215,200,4.89158,109,2.25,'My First Exercise'),('27ec75fa-6a56-4ec1-8346-cca7eb68e5bd','milos_veljkovic@gmail.com',1397,210,4.38434,104,1.42,'My First Exercise'),('33c4d1cc-b0ed-4d85-a0c4-5d33793f8fab','milos_veljkovic@gmail.com',263,245,4.27773,103,0.26,'My First Exercise'),('3744b888-e66e-4d11-972d-ba4233bb80a3','milos_veljkovic@gmail.com',688,243,3.53315,95,0.69,'My First Exercise'),('461c86e1-ca28-4976-8306-68d58d257ab0','predrag_antic@gmail.com',250,250,0,60,0,'First time'),('54229632-5233-4a8b-b588-8dc3eca50d42','milos_veljkovic@gmail.com',4075,215,3.97999,100,4.13,'My First Exercise'),('6e334ee7-f588-4826-a7da-2a230b9c408f','predrag_antic@gmail.com',505,237,4.31427,103,0.26,'First time'),('7826edf4-852d-4be3-a348-f3ea6ba01809','milos_veljkovic@gmail.com',3840,227,5.03151,110,3.89,'My First Exercise'),('84f71587-a3f4-4f8b-b796-a614b8f10375','milos_veljkovic@gmail.com',3025,227,4.33623,103,3.07,'My First Exercise'),('8c3c55f1-f9a3-4bf5-a1f1-064ee53c8e70','milos_veljkovic@gmail.com',1925,204,5.00974,110,1.95,'My First Exercise'),('8d2e9cc8-2b59-41e1-9e32-b5eef6ada8b2','test@gmail.com',798,13,4.3571,104,0.8,'testPath'),('8d42febc-56d7-420c-bee9-9d41064b7541','predrag_antic@gmail.com',792,238,4.8244,108,0.55,'First time'),('98414a15-d12f-4d37-b5b7-690362dc931f','test@gmail.com',10,10,0,60,0,'testPath'),('a66b3dd2-6301-40af-83ca-c541e68e9551','milos_veljkovic@gmail.com',1139,235,3.88696,99,1.15,'My First Exercise'),('b4717508-1ec8-4455-804d-e9372752c035','milos_veljkovic@gmail.com',2475,220,4.39742,104,2.51,'My First Exercise'),('b9c5b4cc-3944-4cc0-8978-472d0bbbc798','test@gmail.com',270,14,4.38244,104,0.26,'testPath'),('cd05c5a4-09ab-4247-9459-7738ce7391a0','milos_veljkovic@gmail.com',4548,212,4.20828,102,4.62,'My First Exercise'),('cea1a74c-3d4d-435d-bd62-1e908a92e68f','predrag_antic@gmail.com',1238,226,2.91335,89,1,'First time'),('d33487fd-1ff6-4755-8097-41d6545d8d38','milos_veljkovic@gmail.com',3288,222,4.44889,104,3.33,'My First Exercise'),('da595a07-9d85-4649-854e-7a6e01029d89','test@gmail.com',540,22,4.55894,106,0.54,'testPath'),('df73b2cd-6ef1-45cb-b020-56932e2e60a9','milos_veljkovic@gmail.com',911,242,3.80555,98,0.92,'My First Exercise'),('f0b99705-f4eb-42ac-9516-01fd1de9e228','milos_veljkovic@gmail.com',10,250,0,60,0,'My First Exercise'),('f36a29f3-b710-4afc-ad67-12189d93f89b','milos_veljkovic@gmail.com',1629,203,3.93531,99,1.65,'My First Exercise'),('f39e11b8-3dd7-4063-9937-f5bf5fd9c527','milos_veljkovic@gmail.com',481,248,3.72391,97,0.48,'My First Exercise');
/*!40000 ALTER TABLE `path` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-17 18:35:18
