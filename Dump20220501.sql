-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dbmsproject
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address` (
  `address_id` char(8) NOT NULL,
  `customer_id` char(8) DEFAULT NULL,
  `locality` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `pincode` char(6) DEFAULT NULL,
  PRIMARY KEY (`address_id`),
  KEY `addressCustomerID` (`customer_id`),
  CONSTRAINT `addressCustomerID` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES ('addr_001','cust_044','9','Manufacturers','Agraharam','Andhra Pradesh','India','532663'),('addr_002','cust_029','94797','Starling','R S','Gujarat','India','395003'),('addr_003','cust_131','56','Sycamore','R S','Gujarat','India','395003'),('addr_004','cust_058','098','Division','Agraharam','Andhra Pradesh','India','532663'),('addr_005','cust_059','9661','Butternut','R S','Gujarat','India','395003'),('addr_006','cust_023','02549','Independence','Agraharam','Andhra Pradesh','India','532663'),('addr_007','cust_110','1','Chive','R S','Gujarat','India','395003'),('addr_008','cust_030','3','Gulseth','Agraharam','Andhra Pradesh','India','532663'),('addr_009','cust_168','146','Northview','R S','Gujarat','India','395003'),('addr_010','cust_104','6041','Oxford','Agraharam','Andhra Pradesh','India','532663'),('addr_011','cust_087','012','Ronald Regan','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_012','cust_172','08652','Manitowish','R S','Gujarat','India','395003'),('addr_013','cust_124','6147','Roxbury','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_014','cust_126','242','Merrick','R S','Gujarat','India','395003'),('addr_015','cust_059','6','Merrick','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_016','cust_129','011','Heath','R S','Gujarat','India','395003'),('addr_017','cust_123','3','Ohio','R S','Gujarat','India','395003'),('addr_018','cust_047','43304','Darwin','Agraharam','Andhra Pradesh','India','532663'),('addr_019','cust_067','11171','Spohn','Agraharam','Andhra Pradesh','India','532663'),('addr_020','cust_057','38096','Jackson','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_021','cust_113','3283','Melby','R S','Gujarat','India','395003'),('addr_022','cust_019','42','Buell','Agraharam','Andhra Pradesh','India','532663'),('addr_023','cust_154','72353','Basil','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_024','cust_114','3300','Acker','R S','Gujarat','India','395003'),('addr_025','cust_175','4','Elmside','R S','Gujarat','India','395003'),('addr_026','cust_173','16','Maywood','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_027','cust_134','2746','Holy Cross','R S','Gujarat','India','395003'),('addr_028','cust_166','513','Johnson','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_029','cust_076','52','Grover','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_030','cust_059','47','Fieldstone','Agraharam','Andhra Pradesh','India','532663'),('addr_031','cust_190','04','Steensland','R S','Gujarat','India','395003'),('addr_032','cust_007','6','Nobel','R S','Gujarat','India','395003'),('addr_033','cust_017','67','Prairie Rose','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_034','cust_171','79','Scott','Agraharam','Andhra Pradesh','India','532663'),('addr_035','cust_126','60860','Meadow Vale','Agraharam','Andhra Pradesh','India','532663'),('addr_036','cust_086','7996','Basil','Agraharam','Andhra Pradesh','India','532663'),('addr_037','cust_042','93554','Heath','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_038','cust_145','05338','David','R S','Gujarat','India','395003'),('addr_039','cust_120','8','Sutherland','R S','Gujarat','India','395003'),('addr_040','cust_185','400','Miller','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_041','cust_035','31561','Warbler','Agraharam','Andhra Pradesh','India','532663'),('addr_042','cust_175','79055','Hollow Ridge','Agraharam','Andhra Pradesh','India','532663'),('addr_043','cust_076','21','Sycamore','R S','Gujarat','India','395003'),('addr_044','cust_074','6025','North','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_045','cust_062','6','Lighthouse Bay','Agraharam','Andhra Pradesh','India','532663'),('addr_046','cust_053','9887','John Wall','R S','Gujarat','India','395003'),('addr_047','cust_190','9','Del Sol','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_048','cust_180','4','Autumn Leaf','Agraharam','Andhra Pradesh','India','532663'),('addr_049','cust_014','614','Lunder','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_050','cust_102','25800','Hoepker','Agraharam','Andhra Pradesh','India','532663'),('addr_051','cust_070','22','Browning','R S','Gujarat','India','395003'),('addr_052','cust_192','49355','Esker','Agraharam','Andhra Pradesh','India','532663'),('addr_053','cust_082','54','Mosinee','R S','Gujarat','India','395003'),('addr_054','cust_008','05196','Bonner','R S','Gujarat','India','395003'),('addr_055','cust_152','1','Thompson','R S','Gujarat','India','395003'),('addr_056','cust_127','94','Scofield','Agraharam','Andhra Pradesh','India','532663'),('addr_057','cust_153','05','Troy','Agraharam','Andhra Pradesh','India','532663'),('addr_058','cust_024','9163','Warrior','R S','Gujarat','India','395003'),('addr_059','cust_110','3','Dottie','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_060','cust_142','977','Randy','Agraharam','Andhra Pradesh','India','532663'),('addr_061','cust_181','759','Knutson','Agraharam','Andhra Pradesh','India','532663'),('addr_062','cust_038','83','Lighthouse Bay','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_063','cust_181','53094','Southridge','R S','Gujarat','India','395003'),('addr_064','cust_141','56337','Macpherson','Agraharam','Andhra Pradesh','India','532663'),('addr_065','cust_061','65','Bunting','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_066','cust_034','4','Manufacturers','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_067','cust_181','22676','Nova','R S','Gujarat','India','395003'),('addr_068','cust_065','3012','Mifflin','R S','Gujarat','India','395003'),('addr_069','cust_196','83','Everett','Agraharam','Andhra Pradesh','India','532663'),('addr_070','cust_034','83','Shasta','Agraharam','Andhra Pradesh','India','532663'),('addr_071','cust_056','4','Prairie Rose','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_072','cust_122','2','Porter','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_073','cust_175','185','Ridgeway','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_074','cust_063','14579','Towne','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_075','cust_046','53','Porter','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_076','cust_035','31172','Sachtjen','R S','Gujarat','India','395003'),('addr_077','cust_105','0600','Dryden','Agraharam','Andhra Pradesh','India','532663'),('addr_078','cust_125','39801','Hudson','R S','Gujarat','India','395003'),('addr_079','cust_046','558','Warbler','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_080','cust_164','563','Karstens','R S','Gujarat','India','395003'),('addr_081','cust_016','7517','Manley','R S','Gujarat','India','395003'),('addr_082','cust_046','57458','Hovde','R S','Gujarat','India','395003'),('addr_083','cust_137','60','Crowley','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_084','cust_045','88','Maple Wood','R S','Gujarat','India','395003'),('addr_085','cust_167','9366','Commercial','R S','Gujarat','India','395003'),('addr_086','cust_018','41','Boyd','Agraharam','Andhra Pradesh','India','532663'),('addr_087','cust_126','81704','Johnson','Agraharam','Andhra Pradesh','India','532663'),('addr_088','cust_096','661','Doe Crossing','Agraharam','Andhra Pradesh','India','532663'),('addr_089','cust_179','781','Tony','Agraharam','Andhra Pradesh','India','532663'),('addr_090','cust_159','199','Commercial','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_091','cust_150','11','Portage','Agraharam','Andhra Pradesh','India','532663'),('addr_092','cust_063','4','Southridge','R S','Gujarat','India','395003'),('addr_093','cust_109','3205','Steensland','R S','Gujarat','India','395003'),('addr_094','cust_074','69031','Almo','R S','Gujarat','India','395003'),('addr_095','cust_033','10','Lighthouse Bay','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_096','cust_158','8','Erie','Agraharam','Andhra Pradesh','India','532663'),('addr_097','cust_187','0','Lillian','R S','Gujarat','India','395003'),('addr_098','cust_133','99060','Oxford','R S','Gujarat','India','395003'),('addr_099','cust_105','0','Arkansas','Agraharam','Andhra Pradesh','India','532663'),('addr_100','cust_012','3','Anzinger','Agraharam','Andhra Pradesh','India','532663'),('addr_101','cust_072','9358','Bowman','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_102','cust_062','2','Prairie Rose','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_103','cust_169','422','Dawn','Agraharam','Andhra Pradesh','India','532663'),('addr_104','cust_036','518','Starling','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_105','cust_085','79','Magdeline','Agraharam','Andhra Pradesh','India','532663'),('addr_106','cust_157','40404','Kensington','Agraharam','Andhra Pradesh','India','532663'),('addr_107','cust_191','528','Main','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_108','cust_158','20240','Clemons','R S','Gujarat','India','395003'),('addr_109','cust_132','71977','Meadow Vale','R S','Gujarat','India','395003'),('addr_110','cust_072','3','Russell','Agraharam','Andhra Pradesh','India','532663'),('addr_111','cust_145','74078','Portage','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_112','cust_030','2605','Dakota','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_113','cust_007','1','Luster','R S','Gujarat','India','395003'),('addr_114','cust_124','33','Sloan','R S','Gujarat','India','395003'),('addr_115','cust_177','07898','Monterey','Agraharam','Andhra Pradesh','India','532663'),('addr_116','cust_141','6252','Dottie','Agraharam','Andhra Pradesh','India','532663'),('addr_117','cust_181','822','Nova','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_118','cust_067','05718','Toban','R S','Gujarat','India','395003'),('addr_119','cust_077','70228','Forest','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_120','cust_144','0495','Manley','R S','Gujarat','India','395003'),('addr_121','cust_055','63','Moland','Agraharam','Andhra Pradesh','India','532663'),('addr_122','cust_108','1','Manitowish','R S','Gujarat','India','395003'),('addr_123','cust_028','7','Larry','R S','Gujarat','India','395003'),('addr_124','cust_092','82107','Kropf','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_125','cust_066','74911','International','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_126','cust_011','2','Farmco','Agraharam','Andhra Pradesh','India','532663'),('addr_127','cust_119','44','Memorial','Agraharam','Andhra Pradesh','India','532663'),('addr_128','cust_130','4','Gina','R S','Gujarat','India','395003'),('addr_129','cust_141','29','Marcy','Agraharam','Andhra Pradesh','India','532663'),('addr_130','cust_081','2','Cody','Agraharam','Andhra Pradesh','India','532663'),('addr_131','cust_050','72','Pearson','R S','Gujarat','India','395003'),('addr_132','cust_030','0313','Stang','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_133','cust_126','610','Alpine','R S','Gujarat','India','395003'),('addr_134','cust_200','83','Leroy','R S','Gujarat','India','395003'),('addr_135','cust_019','03140','Vermont','Agraharam','Andhra Pradesh','India','532663'),('addr_136','cust_144','13','Shopko','Agraharam','Andhra Pradesh','India','532663'),('addr_137','cust_143','9','Dakota','Agraharam','Andhra Pradesh','India','532663'),('addr_138','cust_076','5','American','R S','Gujarat','India','395003'),('addr_139','cust_067','3','David','R S','Gujarat','India','395003'),('addr_140','cust_130','875','Oakridge','R S','Gujarat','India','395003'),('addr_141','cust_081','6','Arkansas','R S','Gujarat','India','395003'),('addr_142','cust_091','495','Charing Cross','Agraharam','Andhra Pradesh','India','532663'),('addr_143','cust_140','56395','7th','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_144','cust_177','482','Anniversary','R S','Gujarat','India','395003'),('addr_145','cust_070','0','Pearson','R S','Gujarat','India','395003'),('addr_146','cust_170','14','Anderson','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_147','cust_025','17398','Service','Agraharam','Andhra Pradesh','India','532663'),('addr_148','cust_070','267','Rutledge','R S','Gujarat','India','395003'),('addr_149','cust_019','5257','Reindahl','Sadar Bazar','Uttar Pradesh','India','281002'),('addr_150','cust_135','3','Dryden','R S','Gujarat','India','395003');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank`
--

DROP TABLE IF EXISTS `bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank` (
  `bank_id` char(8) NOT NULL,
  `customer_id` char(8) DEFAULT NULL,
  `account_no` varchar(100) DEFAULT NULL,
  `ifsc_code` char(11) DEFAULT NULL,
  PRIMARY KEY (`bank_id`),
  KEY `bankCustomerID` (`customer_id`),
  CONSTRAINT `bankCustomerID` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank`
--

LOCK TABLES `bank` WRITE;
/*!40000 ALTER TABLE `bank` DISABLE KEYS */;
INSERT INTO `bank` VALUES ('bank_001','cust_195','HR','LANDP'),('bank_002','cust_118','TUES','ZIOP'),('bank_003','cust_039','NSC','CNK'),('bank_004','cust_007','MDLX','UBS'),('bank_005','cust_046','ABEOW','CTXS'),('bank_006','cust_107','ATNI','WSBF'),('bank_007','cust_044','ALXN','FNSR'),('bank_008','cust_007','CI','CRBP'),('bank_009','cust_109','GEB','NEV'),('bank_010','cust_051','CBO','CGIX'),('bank_011','cust_180','AJG','LFGR'),('bank_012','cust_034','NLST','UZA'),('bank_013','cust_023','KRA','CPIX'),('bank_014','cust_001','INGR','SCON'),('bank_015','cust_162','XOG','ADRA'),('bank_016','cust_155','CRVS','WCST'),('bank_017','cust_154','CLNS^H','OIS'),('bank_018','cust_122','WFBI','BAF'),('bank_019','cust_059','NBHC','CEQP'),('bank_020','cust_093','CMO','VJET'),('bank_021','cust_085','NCLH','SYNL'),('bank_022','cust_089','VALU','LTRPA'),('bank_023','cust_057','WRB','EARN'),('bank_024','cust_033','DD','FTAG'),('bank_025','cust_189','ACXM','MRCY'),('bank_026','cust_166','DEPO','SAEX'),('bank_027','cust_090','STMP','CRY'),('bank_028','cust_028','IBN','EVA'),('bank_029','cust_116','LKFN','MSL'),('bank_030','cust_167','NESR','DHR'),('bank_031','cust_115','SGC','AFST'),('bank_032','cust_074','DXGE','CDL'),('bank_033','cust_146','GMS','BBBY'),('bank_034','cust_058','MGA','SKLN'),('bank_035','cust_032','PEB^C','SCAC'),('bank_036','cust_071','PEGA','ADOM'),('bank_037','cust_063','MTDR','APDNW'),('bank_038','cust_071','SLNO','AUPH'),('bank_039','cust_078','SONC','CVNA'),('bank_040','cust_183','CERC','QHC'),('bank_041','cust_029','MMD','NBD'),('bank_042','cust_049','LINDW','CDI'),('bank_043','cust_072','OMC','GYC'),('bank_044','cust_117','CVGI','SSW^E'),('bank_045','cust_160','ULTI','JPM^G'),('bank_046','cust_102','BSD','EGIF'),('bank_047','cust_042','CTIB','VRTS'),('bank_048','cust_128','DVAX','CM'),('bank_049','cust_083','UE','INOV'),('bank_050','cust_012','OTTW','SRT');
/*!40000 ALTER TABLE `bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `customer_id` char(8) DEFAULT NULL,
  `product_id` char(8) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  KEY `cartCustomerID` (`customer_id`),
  KEY `cartProductID` (`product_id`),
  CONSTRAINT `cartCustomerID` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`),
  CONSTRAINT `cartProductID` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `category_id` char(8) NOT NULL,
  `category_name` varchar(100) DEFAULT NULL,
  `tax` float DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('catg_001','furniture',12,'images/furniture.jpeg'),('catg_002','grocery',18,'images/grocery.jpeg'),('catg_003','electronics',12,'images/electronics.jpeg'),('catg_004','household',12,'images/household.jpeg'),('catg_005','clothes',18,'images/clothes.jpg'),('catg_006','toys',10,'images/toys.jpeg'),('catg_007','gifts',10,'images/gift.jpeg'),('catg_008','decor',10,'images/decor.jpeg');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `company_id` char(8) NOT NULL,
  `phone_no` char(10) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `category_id` char(8) DEFAULT NULL,
  PRIMARY KEY (`company_id`),
  KEY `CompanyCategoryID_idx` (`category_id`),
  CONSTRAINT `CompanyCategoryID` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES ('comp_001','7629903992','Edgetag','catg_003'),('comp_002','4618480195','Rhynoodle','catg_007'),('comp_003','9808829004','Browsetype','catg_002'),('comp_004','1306812959','Meevee','catg_003'),('comp_005','4394076325','Kwimbee','catg_002'),('comp_006','9708046947','Skyble','catg_006'),('comp_007','9453139427','Wikivu','catg_008'),('comp_008','3203109998','Devshare','catg_006'),('comp_009','6252971817','Wikido','catg_001'),('comp_010','7505563990','Latz','catg_002'),('comp_011','1018903549','Zoonder','catg_005'),('comp_012','9124099253','Zoomdog','catg_001'),('comp_013','4639358557','Oyoyo','catg_002'),('comp_014','6071221588','Livepath','catg_005'),('comp_015','3746536260','Voolith','catg_007'),('comp_016','2149796960','Tanoodle','catg_002'),('comp_017','9678341564','Devpoint','catg_004'),('comp_018','6339728217','Katz','catg_002'),('comp_019','1098534469','Meeveo','catg_005'),('comp_020','8763205065','Flipstorm','catg_006'),('comp_021','5027418600','Bubblemix','catg_003'),('comp_022','1801731960','Nlounge','catg_005'),('comp_023','9083036601','Flashdog','catg_006'),('comp_024','9652020156','Roodel','catg_004'),('comp_025','5465550481','Cogilith','catg_008'),('comp_026','4185464333','Oyope','catg_006'),('comp_027','9696121989','Edgetag','catg_006'),('comp_028','9295998602','Janyx','catg_006'),('comp_029','8829205601','Thoughtbeat','catg_002'),('comp_030','2525916734','Realbuzz','catg_008'),('comp_031','9836866524','Blognation','catg_002'),('comp_032','2951512678','Skipfire','catg_006'),('comp_033','4276736446','Twiyo','catg_001'),('comp_034','8926693078','Quimm','catg_005'),('comp_035','9801636139','Edgewire','catg_007'),('comp_036','1992050700','Jazzy','catg_007'),('comp_037','9472307917','Meevee','catg_005'),('comp_038','3777777028','Jaxnation','catg_002'),('comp_039','4327102143','Tekfly','catg_008'),('comp_040','1422770165','Kwinu','catg_004'),('comp_041','9675956710','Eamia','catg_006'),('comp_042','5251602401','Eazzy','catg_001'),('comp_043','6749944585','Photobean','catg_004'),('comp_044','9423620854','Dynabox','catg_004'),('comp_045','3742633140','Skivee','catg_007'),('comp_046','7913422697','LiveZ','catg_002'),('comp_047','1308586615','Roombo','catg_004'),('comp_048','1374740886','Skimia','catg_001'),('comp_049','9637370537','Zoonoodle','catg_007'),('comp_050','6883450585','Oyoloo','catg_001'),('comp_051','4579189573','Linklinks','catg_008'),('comp_052','3053032886','Kaymbo','catg_004'),('comp_053','8004131651','Gigabox','catg_007'),('comp_054','6825649906','Aimbu','catg_004'),('comp_055','9084220101','Skilith','catg_001'),('comp_056','7887872445','Oozz','catg_008'),('comp_057','5663277763','Talane','catg_003'),('comp_058','4285209137','Jatri','catg_002'),('comp_059','4276562009','Plajo','catg_001'),('comp_060','1762097533','Quinu','catg_007'),('comp_061','1802868725','Oyondu','catg_002'),('comp_062','1819074049','JumpXS','catg_002'),('comp_063','5366199455','Riffpedia','catg_001'),('comp_064','6577316174','Brightbean','catg_004'),('comp_065','8074511276','Rhycero','catg_006'),('comp_066','7418466760','Ntags','catg_003'),('comp_067','3531628589','Topdrive','catg_001'),('comp_068','9725461291','Katz','catg_001'),('comp_069','9309074128','Mymm','catg_004'),('comp_070','8796925983','Fanoodle','catg_001'),('comp_071','3619212838','Oyoba','catg_003'),('comp_072','7077865571','Einti','catg_004'),('comp_073','7425036334','Zava','catg_006'),('comp_074','2024958160','Mydo','catg_006'),('comp_075','9103104367','Roomm','catg_004'),('comp_076','6919261450','Vimbo','catg_008'),('comp_077','3089247463','Vimbo','catg_004'),('comp_078','4912211445','Quimm','catg_007'),('comp_079','8301082210','Gigazoom','catg_003'),('comp_080','2471543903','Gevee','catg_004'),('comp_081','2683378348','Rhyzio','catg_003'),('comp_082','4822854283','Tanoodle','catg_007'),('comp_083','5797387512','Centidel','catg_003'),('comp_084','9161306579','Brightdog','catg_005'),('comp_085','3669053833','Blogspan','catg_001'),('comp_086','5498351249','Gigashots','catg_003'),('comp_087','4264196598','Livepath','catg_005'),('comp_088','4579444075','Jatri','catg_003'),('comp_089','9916027009','Kanoodle','catg_001'),('comp_090','4256396361','Edgepulse','catg_007'),('comp_091','8288303896','Topiclounge','catg_007'),('comp_092','9124431464','Skimia','catg_004'),('comp_093','6019713496','Meetz','catg_007'),('comp_094','6125891762','Chatterpoint','catg_005'),('comp_095','2358662311','Tagpad','catg_006'),('comp_096','9373900468','Blogspan','catg_005'),('comp_097','4087381075','Tagcat','catg_005'),('comp_098','9892821249','Voonyx','catg_007'),('comp_099','9049625461','Quatz','catg_007'),('comp_100','5952384523','Eabox','catg_001'),('comp_101','4336402073','Ainyx','catg_008'),('comp_102','7384459585','Ntags','catg_007'),('comp_103','5015800517','Shufflebeat','catg_008'),('comp_104','6529190658','Wikizz','catg_008'),('comp_105','6201952330','Jazzy','catg_006'),('comp_106','6543908732','Wordware','catg_006'),('comp_107','8999334029','Chatterbridge','catg_005'),('comp_108','7654399245','Rhycero','catg_006'),('comp_109','5946106544','Devpoint','catg_002'),('comp_110','4014510957','Kazu','catg_004'),('comp_111','5046011430','Photobug','catg_006'),('comp_112','2715504780','Quatz','catg_005'),('comp_113','9725953182','Tazzy','catg_004'),('comp_114','7816378406','Yakitri','catg_007'),('comp_115','2633266931','Oba','catg_007'),('comp_116','9109914249','Divavu','catg_008'),('comp_117','3826492202','Lajo','catg_007'),('comp_118','4832932963','Jetwire','catg_001'),('comp_119','9437805356','Trilith','catg_002'),('comp_120','3129624958','Yadel','catg_006'),('comp_121','6469850952','Viva','catg_004'),('comp_122','6044162714','Skyba','catg_003'),('comp_123','8808371956','Tekfly','catg_008'),('comp_124','9148057628','Trilia','catg_003'),('comp_125','6979944616','Shufflebeat','catg_002'),('comp_126','3048942375','Jaxnation','catg_004'),('comp_127','5956483834','Jetwire','catg_008'),('comp_128','6007217578','Camimbo','catg_002'),('comp_129','7103182044','Buzzster','catg_007'),('comp_130','5542829914','Leenti','catg_008'),('comp_131','7774074091','Mycat','catg_002'),('comp_132','1946655986','Jabbersphere','catg_003'),('comp_133','4485194640','Livefish','catg_007'),('comp_134','1918982344','Ozu','catg_001'),('comp_135','1985194361','Twitternation','catg_005'),('comp_136','7586821241','Zoozzy','catg_005'),('comp_137','3632520446','Centizu','catg_006'),('comp_138','7767222608','Realpoint','catg_008'),('comp_139','5197006762','Realfire','catg_001'),('comp_140','5533612200','Fivebridge','catg_004'),('comp_141','7769207664','Leexo','catg_004'),('comp_142','7633825298','Leenti','catg_008'),('comp_143','4415772403','Thoughtworks','catg_007'),('comp_144','1941361272','Avavee','catg_008'),('comp_145','1945573689','Jamia','catg_005'),('comp_146','1235883043','Flashpoint','catg_007'),('comp_147','3048183185','Avavee','catg_006'),('comp_148','1543301327','Photobean','catg_004'),('comp_149','7924971485','Trupe','catg_004'),('comp_150','5724369045','Geba','catg_007'),('comp_151','1489182864','Leexo','catg_003'),('comp_152','8591620255','Chatterpoint','catg_006'),('comp_153','8094024512','Twiyo','catg_008'),('comp_154','8577210451','Leexo','catg_001'),('comp_155','3825698812','Ozu','catg_001'),('comp_156','2981520356','Talane','catg_008'),('comp_157','4555931509','Brightdog','catg_005'),('comp_158','1338192643','Flipopia','catg_001'),('comp_159','4233426226','Jayo','catg_003'),('comp_160','8264653194','Twitterbridge','catg_004'),('comp_161','7634201623','Camimbo','catg_008'),('comp_162','5979754584','Izio','catg_002'),('comp_163','2055930209','Topicstorm','catg_007'),('comp_164','4427874332','Tagcat','catg_008'),('comp_165','6691328805','Kimia','catg_008'),('comp_166','7244586581','Vidoo','catg_002'),('comp_167','2682248913','Jabbersphere','catg_002'),('comp_168','6859419430','Skinix','catg_003'),('comp_169','4966123484','Zoovu','catg_002'),('comp_170','9155778285','Quimm','catg_001'),('comp_171','7105168340','Babbleopia','catg_004'),('comp_172','1875713944','Babbleblab','catg_005'),('comp_173','4164862467','Babblestorm','catg_007'),('comp_174','1226089866','Vipe','catg_003'),('comp_175','8405967590','Camido','catg_006'),('comp_176','4555111844','Quire','catg_002'),('comp_177','8653616472','Zava','catg_007'),('comp_178','4318029728','Jabbercube','catg_006'),('comp_179','9935989967','Skiptube','catg_007'),('comp_180','8031977342','Twitternation','catg_005'),('comp_181','7523860522','Wordpedia','catg_002'),('comp_182','8905918208','Flipstorm','catg_002'),('comp_183','8297842994','Buzzshare','catg_004'),('comp_184','4961648034','Skimia','catg_008'),('comp_185','7492447149','Kare','catg_007'),('comp_186','2685266665','Centimia','catg_005'),('comp_187','6645453003','Gigabox','catg_002'),('comp_188','1528696145','Skimia','catg_006'),('comp_189','6973868842','Edgeblab','catg_004'),('comp_190','6891771970','Babblestorm','catg_001'),('comp_191','2917625652','Yakijo','catg_004'),('comp_192','1446271400','Skipfire','catg_007'),('comp_193','7076936164','Rhybox','catg_004'),('comp_194','2563567504','Avavee','catg_005'),('comp_195','6153182313','Agimba','catg_006'),('comp_196','9829423072','Dabjam','catg_008'),('comp_197','6393586435','Twimbo','catg_008'),('comp_198','6835391886','Demizz','catg_005'),('comp_199','5041491119','Zoomzone','catg_003'),('comp_200','8045732004','Mycat','catg_007');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customer_id` char(8) NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `phone_no` char(10) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('cust_001','Ramon Prator','1994-12-08','3809115055'),('cust_002','Caprice McCleod','2003-06-18','7196962383'),('cust_003','Brad Eisenberg','1998-12-21','1909769396'),('cust_004','Kalinda Dust','1972-06-17','9326669763'),('cust_005','Birgit Rawsthorn','1972-05-28','5212759884'),('cust_006','Carce Gatherer','1976-07-05','5231735610'),('cust_007','Petronia Robyns','1998-10-06','9182042396'),('cust_008','Burty Anespie','1989-12-19','1171979175'),('cust_009','Rees Kerbler','1981-01-18','5039573196'),('cust_010','Ambrose Dusting','1987-04-05','5836644719'),('cust_011','Margeaux Jarrette','1984-12-19','7378208486'),('cust_012','Kelly Wemm','1991-05-12','9144077740'),('cust_013','Hesther Egre','1987-11-04','3612863146'),('cust_014','Clevey Exter','1984-10-03','6669002736'),('cust_015','Marcos MacKeller','1986-01-20','4846323104'),('cust_016','Lulu D\'Aguanno','1976-03-09','3015157088'),('cust_017','Cele Hanselmann','1979-11-16','9794435357'),('cust_018','Darrin Harbron','1990-05-27','5383991203'),('cust_019','Craggy Chapelhow','1996-09-30','9673512611'),('cust_020','Shanta Inchan','1973-11-09','6996689058'),('cust_021','Tommy Kondratowicz','1984-05-05','8303945526'),('cust_022','Igor Dowbiggin','1999-09-05','4895215550'),('cust_023','Sarena Eddleston','1973-04-24','6983978222'),('cust_024','Lorain Stuckes','1993-05-09','8839721440'),('cust_025','Camile Rossbrook','1995-04-07','3821200325'),('cust_026','Thebault Tonnesen','2001-10-01','9031655327'),('cust_027','Hendrika Robberecht','1983-11-07','4231211784'),('cust_028','Shelley Winyard','1988-11-13','3072764686'),('cust_029','Kimbell Jecks','1994-06-11','1602976099'),('cust_030','Randie Minichillo','1970-01-23','6188674780'),('cust_031','Ibbie Krop','2001-08-23','4986618724'),('cust_032','Christean Reihill','1971-08-25','5457238538'),('cust_033','Eve MacGaughey','1989-02-24','7906713695'),('cust_034','Christi Pree','1984-02-11','6412583074'),('cust_035','Saul Lockhead','1983-08-10','1889302839'),('cust_036','Ash Flanaghan','1987-12-28','5897395970'),('cust_037','Opaline Durbyn','1985-09-13','8565172094'),('cust_038','Vikki Coakley','1970-11-08','3264589481'),('cust_039','Rosetta Burnard','1979-12-08','1777562299'),('cust_040','Ario Levesley','1973-12-18','6728048761'),('cust_041','Arvy Coddington','1989-02-26','1714093593'),('cust_042','Gordie Dawney','1993-12-03','3424345438'),('cust_043','Micheline Rubi','1999-07-27','7977961617'),('cust_044','Alexander Osselton','2004-03-25','2933944855'),('cust_045','Kevan Einchcombe','1979-12-09','8716993340'),('cust_046','Griffith Vernazza','1992-04-05','7391723388'),('cust_047','Rad Paulino','1986-04-14','9145754263'),('cust_048','Odey Talmadge','1979-08-26','5365430966'),('cust_049','Ruperta Milazzo','2001-07-10','8192265914'),('cust_050','Berkie McKeady','1971-11-04','2192024640'),('cust_051','Koren Nann','1989-08-24','2937667593'),('cust_052','Galvan Shaddick','1970-03-15','7824739193'),('cust_053','Noe Scattergood','1986-12-30','7855085623'),('cust_054','Paquito Kmietsch','1993-08-11','2599407807'),('cust_055','Crystie Rolin','1987-07-28','7529832236'),('cust_056','Mireielle Plak','1983-04-06','7458549504'),('cust_057','Adrianna Faill','1989-05-20','4408948936'),('cust_058','Marylou Powley','1982-09-26','6808925009'),('cust_059','Ynes Mourant','1973-01-21','2679495006'),('cust_060','Priscilla Duffield','1997-09-20','1544017791'),('cust_061','Dianemarie Dericut','1990-08-11','4782534625'),('cust_062','Eudora Gillespey','1984-12-10','6061580207'),('cust_063','Carly Sorel','1995-03-13','7072187315'),('cust_064','Codie Lotte','1981-10-04','6783046587'),('cust_065','Aluin Midford','1984-05-25','3658559964'),('cust_066','Malia O\'Mara','1996-06-18','1475438847'),('cust_067','Shirleen Loosemore','1983-12-24','3512794821'),('cust_068','Conan Berni','1996-04-06','5297076056'),('cust_069','Rhianna Verrills','1976-03-06','2978310616'),('cust_070','Milicent Leynham','2000-06-08','2915603764'),('cust_071','Brandon Ege','1998-01-08','1304162954'),('cust_072','Heather Ingerman','1990-11-16','2639808945'),('cust_073','Merilyn Luxon','1996-06-24','1148594199'),('cust_074','Bria Ferguson','1971-10-04','4211307083'),('cust_075','Neddy Ayscough','1972-09-08','7853413523'),('cust_076','Raimund Knewstub','1979-09-30','2877578243'),('cust_077','Ker Free','1972-05-14','6356173530'),('cust_078','Missy Leathard','1997-04-16','8269098522'),('cust_079','Haslett Wheowall','2000-02-28','4075199648'),('cust_080','Burton Cerro','1973-03-19','2684918267'),('cust_081','Margi Webland','1999-07-29','6845358109'),('cust_082','Keefe Roberds','1991-11-27','9466093538'),('cust_083','Arlie Gather','1994-06-08','2954380102'),('cust_084','Audi Verdon','1977-10-04','7423458399'),('cust_085','Fonz Cranstoun','1998-05-23','3432379307'),('cust_086','Arni Attac','1982-07-19','2212304579'),('cust_087','Tara McCrainor','1985-08-29','8429993018'),('cust_088','Aurora Ferron','1979-04-24','2645969285'),('cust_089','Griffie Classen','1994-11-07','5613518313'),('cust_090','Borden Gosker','1974-08-30','3824701754'),('cust_091','Lenci Donaghy','1986-11-29','8111033063'),('cust_092','Rafi Abbe','1998-05-27','2988664740'),('cust_093','Carley Worstall','1970-09-02','8846635525'),('cust_094','Dory Vest','1991-11-09','2267021948'),('cust_095','Bradly Courcey','1978-08-28','8915566679'),('cust_096','Daniel Koppelmann','1986-04-03','1963004079'),('cust_097','Arielle Dikles','1978-08-08','9634726308'),('cust_098','Hillier Dufer','1988-02-20','5152198470'),('cust_099','Gustav Connow','1980-06-06','9012441458'),('cust_100','Roxine Huish','1983-07-02','2086072964'),('cust_101','Linell Knight','1981-11-01','3087567831'),('cust_102','Louisa Ciobutaro','1993-07-23','7718075088'),('cust_103','Micheline Sudell','1997-01-15','8209481285'),('cust_104','Gail Drioli','1980-11-18','1513539816'),('cust_105','Tera Broadbent','2003-05-14','2584408161'),('cust_106','Glory Cullity','2002-03-14','4352916665'),('cust_107','Rafaellle Beers','2000-12-09','2819757161'),('cust_108','Rem Dow','1979-11-21','6318435919'),('cust_109','Barnett Aleswell','1987-03-26','5308949014'),('cust_110','Joelly Carsberg','1986-03-20','9017485123'),('cust_111','Homerus Podbury','1989-09-01','4406441250'),('cust_112','Myrtice Hearons','1989-07-01','3354880858'),('cust_113','Lil Mingauld','1996-04-19','5798915402'),('cust_114','Harbert Hargreave','1976-04-22','7107830648'),('cust_115','Nestor Rosencwaig','1991-08-25','8541956234'),('cust_116','Fae Sandal','1973-09-21','6821177744'),('cust_117','Mildred O\' Culligan','1972-10-09','1124549085'),('cust_118','Sully Vanderson','1997-03-07','5876271550'),('cust_119','Abdul Esilmon','1990-02-27','8949203252'),('cust_120','Dania Skoyles','1988-04-17','8249428831'),('cust_121','Warden Lethieulier','1997-06-22','6056480396'),('cust_122','Clari Sambles','1983-09-16','7879599747'),('cust_123','Grace Gummery','1999-09-05','2081125420'),('cust_124','Cletus Yakovl','1982-10-21','8877227840'),('cust_125','Brandise Ifill','1997-06-27','4944087103'),('cust_126','Sharity Thorrington','1985-11-30','8757504750'),('cust_127','Waite Loughead','1995-11-29','9703259903'),('cust_128','Lilla Salzberg','1998-10-28','7054469244'),('cust_129','Jeffrey Sahlstrom','1972-09-18','6195754477'),('cust_130','William Shardlow','1997-07-15','7006134155'),('cust_131','Katherine MacAulay','1977-02-22','8517526632'),('cust_132','Florie Card','1992-01-26','5252231029'),('cust_133','Brennen Whiley','1988-02-27','5633193807'),('cust_134','Kendre Mitroshinov','1973-06-02','8102553690'),('cust_135','Chico Treleaven','1983-02-02','6864842835'),('cust_136','Jerald Deakins','1997-12-19','1555307773'),('cust_137','Cthrine Mew','1984-08-03','8941843263'),('cust_138','Bridget Novacek','1980-09-28','5707592008'),('cust_139','Burnard Houlston','1996-01-01','4233002321'),('cust_140','Rayshell Pilpovic','1994-12-18','4532965632'),('cust_141','Adrea Wison','1991-08-29','6938300158'),('cust_142','Emlyn Sprigings','1975-08-25','7989764934'),('cust_143','Whit Diplock','1974-11-25','2388656795'),('cust_144','Damiano Linforth','1975-02-18','9784770200'),('cust_145','Broddie Elman','1998-02-06','1602740960'),('cust_146','Darnall Trapp','1995-05-23','2844550631'),('cust_147','Larry Hillhouse','1973-03-17','5853993289'),('cust_148','Tiffanie Wrenn','2000-12-01','4498927535'),('cust_149','Phillipp Guiducci','1984-02-15','8266948892'),('cust_150','Donna Balfre','1994-12-28','9326895479'),('cust_151','Dennison Hadlee','1984-01-26','2351519729'),('cust_152','Toni Benfield','1986-08-08','2564661375'),('cust_153','Zarah Goakes','2000-08-11','9842893096'),('cust_154','Clemmy Pointin','1986-08-11','6587883136'),('cust_155','Kelbee Vasquez','1984-02-18','6568728722'),('cust_156','Monika Reddell','1994-05-12','5489361418'),('cust_157','Massimo Coon','1983-12-03','3474728378'),('cust_158','Jereme Beales','1985-12-16','3476013180'),('cust_159','Lesley Pougher','2000-08-04','3628850837'),('cust_160','Care Yockley','1971-09-11','9073569538'),('cust_161','Sauncho Sumption','1987-11-24','2202476616'),('cust_162','Yasmeen Orbon','1996-10-27','2824011213'),('cust_163','Claudetta D\'orsay','1997-09-17','5316011223'),('cust_164','Ernie Commings','1970-04-17','9438888399'),('cust_165','Dinnie Basillon','1995-01-16','6524940423'),('cust_166','Bartholomew Mithon','1975-07-23','7286992645'),('cust_167','Jesus Luttgert','1995-12-12','2493075786'),('cust_168','Estevan Berrygun','1976-11-08','9169275212'),('cust_169','Pietrek Dreus','1981-12-11','4283591791'),('cust_170','Lyle Ladbrook','1970-09-14','7486443981'),('cust_171','Winthrop Reuven','1979-01-13','9101280540'),('cust_172','Edyth Thompson','1988-01-17','3376311256'),('cust_173','Marris Hintzer','1988-08-10','2666597388'),('cust_174','Hew Timmes','1983-02-06','8743080789'),('cust_175','Arleta Grass','2003-03-14','8544307626'),('cust_176','Marchelle Rammell','1984-05-08','7291830526'),('cust_177','Guntar Debill','2002-04-06','4725114391'),('cust_178','Barbaraanne Vina','1998-05-20','9049618124'),('cust_179','Rheta Wann','1973-01-21','1135948290'),('cust_180','Heath Stackbridge','1979-04-02','6216343389'),('cust_181','Hilde Moynham','1980-09-04','8739613211'),('cust_182','Chloris Rolance','1975-05-08','7603914881'),('cust_183','Korey Aston','1997-02-25','5095273457'),('cust_184','Estrella Zanazzi','1983-04-09','6253330842'),('cust_185','Flori Dodsworth','1972-08-15','8927637655'),('cust_186','Raine Lottrington','1975-05-28','4517422473'),('cust_187','Earle Bockmaster','1989-11-22','8872711746'),('cust_188','Merilyn Bastie','1987-08-25','8199816027'),('cust_189','Barn Start','1985-09-18','2305798225'),('cust_190','Ulrike Creegan','1975-04-06','5253446279'),('cust_191','Lorianna Lyddiard','1995-07-09','8842725955'),('cust_192','Berkly Portman','1984-06-02','1474187370'),('cust_193','Guinna Pladen','1980-11-12','8603136783'),('cust_194','Murry Castletine','1973-08-17','8886215771'),('cust_195','Phillis Thurlborn','1998-10-31','3479493876'),('cust_196','Violet Duxbarry','1988-02-11','5232713900'),('cust_197','Marketa McEttigen','1983-01-25','3347118580'),('cust_198','Orelle Caldero','1977-07-17','5457392454'),('cust_199','Addi Mix','1978-10-16','2182429654'),('cust_200','Corrine Croysdale','1998-09-26','7572445849'),('cust_201','Rahul Maddula','2002-05-01','8699699737');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `description`
--

DROP TABLE IF EXISTS `description`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `description` (
  `product_id` char(8) DEFAULT NULL,
  `additional_details` varchar(500) DEFAULT NULL,
  `best_before` date DEFAULT NULL,
  KEY `descriptionProductId` (`product_id`),
  CONSTRAINT `descriptionProductId` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `description`
--

LOCK TABLES `description` WRITE;
/*!40000 ALTER TABLE `description` DISABLE KEYS */;
/*!40000 ALTER TABLE `description` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `username` varchar(16) NOT NULL,
  `password` char(65) DEFAULT NULL,
  `customer_id` char(8) DEFAULT NULL,
  `mode` int DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `loginCustomerID` (`customer_id`),
  CONSTRAINT `loginCustomerID` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('abeedie3k','MsDCbLuf','cust_129',0),('abootland2n','zHvZz8WXL2R','cust_096',0),('aborsnall14','cVFQj0Hw5','cust_041',0),('abreaganu','NCdGNOsBBpFl','cust_031',0),('acalliss3w','mtbP2Y','cust_141',0),('adeferrari31','ul1E5Ehw','cust_110',0),('ademsey20','E3p3gL5kL87y','cust_073',0),('adimnage51','0l0uXGX07LDH','cust_182',0),('admin','admin',NULL,1),('aeade1y','s5wlM7','cust_071',0),('afalshaw1l','vY3QkTuZxgaC','cust_058',0),('afateleyd','fTPwkov','cust_014',0),('agreaser1c','tVBp2B','cust_049',0),('aknightsbridge5b','jwJwBG','cust_192',0),('aleneve29','j05SzJs','cust_082',0),('amacknockiter4k','EpXnp4y','cust_165',0),('amallabund4l','KXH9g4sWV','cust_166',0),('apetrov7','bogGLyl','cust_008',0),('asainsberry2m','ECYoRadF','cust_095',0),('asorrel4c','qtbM1vkGZWjC','cust_157',0),('atroctor57','MOX5SBC0Wgh','cust_188',0),('bbucktrout3j','Pyikyn4','cust_128',0),('beldon2x','ccLOV4XKCcj1','cust_106',0),('beliyahu1f','9T76zlRe','cust_052',0),('bingleton5i','dZVnSo','cust_199',0),('bjimmes33','40NULX','cust_112',0),('blabarre4o','OTZtY1nUc','cust_169',0),('blangabeer3f','WiT4M4','cust_124',0),('bseif4i','mltKenz8H','cust_163',0),('bspratlingp','dMM31gBQW8','cust_026',0),('bsymons3h','cyNZyp094JLU','cust_126',0),('bvinton3c','ogzXEIrGon','cust_121',0),('cbaird4d','lB8Qj02','cust_158',0),('cbearman19','ahAIvtJwv5C','cust_046',0),('cbrocking5f','GjQgkdJ','cust_196',0),('cconiam9','SJsNrYn2','cust_010',0),('ccorn2v','KiKU1h3DswE','cust_104',0),('cdayment5e','ztRvCEAnb','cust_195',0),('cdevile25','lj9E21H','cust_078',0),('cdevoiels4f','2blWCEFFR','cust_160',0),('cdurand2r','iczBG9','cust_100',0),('cfaircliffe2f','AO4Pv8GEQXK','cust_088',0),('cffrench43','TrRVABo','cust_148',0),('chulke40','PWSvbuM','cust_145',0),('clembckem','GQhpHgId','cust_023',0),('cmayoo','08i1SQ','cust_025',0),('coherlihy2p','oHJOEvf8j','cust_098',0),('cpawlik18','eKIk3XJ','cust_045',0),('cperche5a','X2zIPkHdGWFC','cust_191',0),('cstanwayy','oO0Zh2STyov','cust_035',0),('ctansley1z','EOLhrHyer','cust_072',0),('cvassano4s','LHhg9x','cust_173',0),('cwyllie55','TcvjbpIH','cust_186',0),('dbetun3v','geEmXiQO','cust_140',0),('dcastletine1t','mzEuDdsVGt','cust_066',0),('dgoldsworthy2h','tQ6UXD','cust_090',0),('dgorse45','jTbmyQrtMK8','cust_150',0),('dhundey1m','h2LQYW','cust_059',0),('djoy1q','SFkiCyw','cust_063',0),('djurickl','sRpliZRM71','cust_022',0),('dmayhou1b','JpI8TNdlpCC','cust_048',0),('dpirazzi1e','RTvZgQJ1hsCl','cust_051',0),('dsreenank','zsO2cSiI','cust_021',0),('easkell38','wFp0xWdPNU','cust_117',0),('ebalentyne58','D7QWBfQq','cust_189',0),('ecasarili2a','4ySqPPJ3rax','cust_083',0),('eelfleet4h','UiAxXe','cust_162',0),('elaval59','D3k070PGN','cust_190',0),('elondesborough2t','OhkX1rL','cust_102',0),('emilburnew','jbGp12pbp2cd','cust_033',0),('emoran1w','lim02KOnbMs2','cust_069',0),('erakestraw4z','4f25ck','cust_180',0),('esells22','Wwe5e3z2','cust_075',0),('ewebling4q','msN4YB7Ay','cust_171',0),('fallworthy3e','EWRHcci6Ur','cust_123',0),('fbrun3g','sCPjFuykb','cust_125',0),('fcrate1v','Nhm2gHbj','cust_068',0),('fdowdam2i','8Glp8MMgoTa1','cust_091',0),('ffransson37','WKMd3SWvX8','cust_116',0),('fjeavesh','TjhwrR6','cust_018',0),('flongmead4u','qO1QgrltuNJF','cust_175',0),('fvasilic1h','zRXYrN','cust_054',0),('galgate4v','hsA1RevUlb','cust_176',0),('gboarder3y','DIob2uV','cust_143',0),('gdawdary3i','s5QPS7KSj','cust_127',0),('glebrun2j','3F9mXzna1','cust_092',0),('gredgrove1','AVHqVlTs','cust_002',0),('groe23','Vem8mDtpAI','cust_076',0),('gtaveriner2o','LVz8AxGvv','cust_097',0),('hbootherstone2y','K7GpiinahxYR','cust_107',0),('hbowatere','DMGwxIWi1f','cust_015',0),('hclymo42','m9IomufiFK','cust_147',0),('hfarndale36','lEn5TCUH','cust_115',0),('hhubbersteyv','0AjaGIQZcCjp','cust_032',0),('hjohannesson4t','8JX99sqh','cust_174',0),('hpantryz','veiY5YtuqNy','cust_036',0),('hthrussell3o','M7rIyKyzS7','cust_133',0),('imerfin2b','oxyeGbRXJwF','cust_084',0),('jbeadel1u','Se1JJ7okrse','cust_067',0),('jbricknallx','zzz7ieM','cust_034',0),('jdhenin17','nVgs1fZY','cust_044',0),('jhusbandn','YMQWf6V','cust_024',0),('jlardier32','bZbkPVIlEBx','cust_111',0),('jmalyjj','bR8yklyQ','cust_020',0),('jnoot13','QpxsMuIZYwe4','cust_040',0),('jocannovanes','SQNonwtp12','cust_029',0),('jpapierz2q','3xkOEyfhjQ','cust_099',0),('jpetroff4b','EDrSHU','cust_156',0),('jthorneley44','DXgdIeWBUmBc','cust_149',0),('kgeorgi47','pXJJYUV5Dz5','cust_152',0),('kgoodricke5','G0QOgm','cust_006',0),('kheathorn8','UsvTlbnZo','cust_009',0),('kjulien15','ujK246t66hE1','cust_042',0),('klevinge4p','6B68JkOu','cust_170',0),('kmignot1a','ifwuNKrFi4o','cust_047',0),('kmortimer1p','9ZU6J7iAHwF','cust_062',0),('ksmolan4e','K8hzJMisa','cust_159',0),('kwheelan0','ZDakqki8','cust_001',0),('lbromige4r','XxGVsEP4','cust_172',0),('ldenson53','e25cs27w','cust_184',0),('ldeverick2g','wcGP24','cust_089',0),('ldowles2w','ILCH2VR','cust_105',0),('ljosefsohna','oTmFYNgHiIP','cust_011',0),('lmccomish4w','4cK7O1Qtu','cust_177',0),('lschubertc','x0HYl8','cust_013',0),('ltotterdill4','bCC6UyjR7m','cust_005',0),('mbeathem4j','lVbU3al8prA','cust_164',0),('mblaszczak1k','bmjlKQPE','cust_057',0),('mcastelletto4g','YiPZThNYuyX','cust_161',0),('mcoldman5d','4XjcmoNT1','cust_194',0),('mflack35','g7KjKCHTLaV','cust_114',0),('mgetley1s','9Qgc8x','cust_065',0),('mglassman1d','0GjyC99','cust_050',0),('mjeger1x','pDjrIUVT8','cust_070',0),('mknifton4n','WOVxBNEP8J0','cust_168',0),('mlegan1j','8lMv0Eos','cust_056',0),('mlewisham3x','fbv55mxF','cust_142',0),('mlount2c','dJYpYwX','cust_085',0),('mmcgreary1i','GZT9Cy6f','cust_055',0),('mmeeus5h','kBUzot0a','cust_198',0),('morr16','iB1Bm6Z7s','cust_043',0),('mritelli4y','kMFJo6b7n','cust_179',0),('msibbonst','HBZr2wFLJLc','cust_030',0),('mtanti3n','zAetSbY6t4r','cust_132',0),('mtesyro12','grhoDE','cust_039',0),('ncapeling1r','mZN7U9sf','cust_064',0),('npatsall3u','x3xZJXz1Z3sF','cust_139',0),('obeamand52','QYooNi','cust_183',0),('ofairbanks5j','oZYGdmkSwpGY','cust_200',0),('oswate4m','v4iTy0K','cust_167',0),('pliddyard56','1h0elPrJUlW','cust_187',0),('pmccready11','oDtV5mwiaBLu','cust_038',0),('pprovisf','sAnJ3w','cust_016',0),('pslate1g','QW6GD4JqHc','cust_053',0),('pthorsen39','KxpognF','cust_118',0),('ptrurang','IGGWiEYmexSh','cust_017',0),('qschirak2','1Z5MpCnbQS8p','cust_003',0),('rbattram3','EX7Wja4YY','cust_004',0),('rgossling5g','trjlFJ','cust_197',0),('rhowels2e','4ys6ls711E','cust_087',0),('rjudson2u','aMQ8Zs','cust_103',0),('rlapleyb','qy5wIKSl4lA','cust_012',0),('rmarcoolyn3d','PxuS41Eh','cust_122',0),('rmarris10','nxIgsHJwJc5','cust_037',0),('root','root',NULL,1),('rpedycan2k','3UBKyb','cust_093',0),('rperassi50','ZCMw8iZS','cust_181',0),('rstilliard3m','RLwty9DN8uZ9','cust_131',0),('sansell2z','t0rIlASIAeG','cust_108',0),('sbuseki','Uqy3oAXbdx4s','cust_019',0),('scarl48','xLFWGMAz','cust_153',0),('screeber2d','aIvau9','cust_086',0),('sdafforne1n','Uo2RCj','cust_060',0),('seales30','1CjzzD3Z','cust_109',0),('semanuelov3l','YhFgBh7d25z','cust_130',0),('sgethen54','YNI5uBYzY1','cust_185',0),('sjahnisch3z','fjRCoLTdSx','cust_144',0),('smatelaitis3a','1dlWEFYR','cust_119',0),('sradborne28','VDHyxnZ9','cust_081',0),('ssimmings26','4Z9wfVj','cust_079',0),('ssleath2l','wqaLuiS','cust_094',0),('ssolomon3t','FkldRrhZN','cust_138',0),('tdelleschi1o','9LiVO9P','cust_061',0),('tfirminger49','WIVOkQ','cust_154',0),('tjeannot3r','VCtpLAn','cust_136',0),('tmartinat5c','jLaMixJPmOxr','cust_193',0),('trowsel27','Wu5BJKdSWs','cust_080',0),('tshepley4a','RO2jRoo','cust_155',0),('tstrotonr','SnXp1Tihmg3q','cust_028',0),('tswadlinq','QGrwODOoQe','cust_027',0),('tswatradge3q','sBWtjU2hqp','cust_135',0),('ttoffoletto46','JOhemD','cust_151',0),('valbutt6','Kawpbzwbmt','cust_007',0),('vbarnett21','kwiqCaL8','cust_074',0),('vbestwall4x','L3OE3S','cust_178',0),('vboyes2s','TKzQ9E','cust_101',0),('vens8','Rahulmaddula','cust_201',0),('wfifield3b','mThf7peaF8','cust_120',0),('wfrensche34','Cw5x3T3','cust_113',0),('wgyves3p','huOqkl','cust_134',0),('wmurra3s','qWp2UxkVp','cust_137',0),('wsecrett41','Ba87PUakT','cust_146',0),('wsneaker24','HQ19RFYGrxq','cust_077',0);
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` char(8) NOT NULL,
  `category_id` char(8) DEFAULT NULL,
  `company_id` char(8) DEFAULT NULL,
  `current_price` float DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `tags` varchar(100) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  KEY `productCategoryID` (`category_id`),
  KEY `productCompanyID` (`company_id`),
  CONSTRAINT `productCategoryID` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`),
  CONSTRAINT `productCompanyID` FOREIGN KEY (`company_id`) REFERENCES `company` (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('prod_001','catg_005','comp_011',500,9,'#shirt',500,'shirt','images/shirt.png'),('prod_002','catg_002','comp_005',400,9,'#dals',500,'dals','images/dals.png'),('prod_003','catg_006','comp_006',400,5,'#toycar',500,'toy car','images/toy car.png'),('prod_004','catg_007','comp_002',1500,5,'#perfume',500,'perfume','images/perfume.png'),('prod_005','catg_006','comp_006',350,5,'#ludo',500,'ludo','images/ludo.png'),('prod_006','catg_007','comp_015',2000,5,'#watch',500,'watch','images/watch.png'),('prod_007','catg_001','comp_009',35000,6,'#bed',500,'bed','images/bed.png'),('prod_008','catg_005','comp_014',1000,9,'#jeans',500,'jeans','images/jeans.png'),('prod_009','catg_005','comp_019',400,9,'#skirt',500,'skirt','images/skirt.png'),('prod_010','catg_001','comp_012',10000,6,'#cupboard',500,'cupboard','images/cupboard.png'),('prod_011','catg_004','comp_017',40,6,'#broom',500,'broom','images/broom.png'),('prod_012','catg_007','comp_035',400,5,'#bracelet',500,'bracelet','images/bracelet.png'),('prod_013','catg_004','comp_024',10,6,'#soap',500,'soap','images/soap.png'),('prod_014','catg_003','comp_001',25000,6,'#mobile',500,'mobile','images/mobile.png'),('prod_015','catg_006','comp_008',200,5,'#snakes&ladders',500,'snakes & ladders','images/snakes & ladders.png'),('prod_016','catg_008','comp_007',500,5,'#mirrorart',500,'mirror art','images/mirror art.png'),('prod_017','catg_002','comp_010',50,9,'#rice',500,'rice','images/rice.png'),('prod_018','catg_004','comp_040',300,6,'#shampoo',500,'shampoo','images/shampoo.png'),('prod_019','catg_008','comp_025',2000,5,'#painting',500,'painting','images/painting.png'),('prod_020','catg_003','comp_004',50000,6,'#laptop',500,'laptop','images/laptop.png'),('prod_021','catg_004','comp_043',500,6,'#oil',500,'oil','images/oil.png'),('prod_022','catg_001','comp_033',2500,6,'#table',500,'table','images/table.png'),('prod_023','catg_001','comp_042',1000,6,'#chair',500,'chair','images/chair.png'),('prod_024','catg_008','comp_030',2500,5,'#sculpture',500,'sculpture','images/sculpture.png'),('prod_025','catg_007','comp_036',2500,5,'#bags',500,'bags','images/bags.png'),('prod_026','catg_001','comp_048',15000,6,'#sofa',500,'sofa','images/sofa.png'),('prod_027','catg_003','comp_021',25000,6,'#tablet',500,'tablet','images/tablet.png'),('prod_028','catg_003','comp_057',40000,6,'#airconditioner',500,'air conditioner','images/air conditioner.png'),('prod_029','catg_002','comp_013',30,9,'#wheat',500,'wheat','images/wheat.png'),('prod_030','catg_007','comp_045',450,5,'#bands',500,'bands','images/bands.png'),('prod_031','catg_003','comp_066',45000,6,'#washingmachine',500,'washing machine','images/washing machine.png'),('prod_032','catg_002','comp_016',10,9,'#biscuit',500,'biscuit','images/biscuit.png'),('prod_033','catg_005','comp_022',1500,9,'#coat',500,'coat','images/coat.png'),('prod_034','catg_004','comp_044',40,6,'#washingcloth',500,'washing cloth','images/washing cloth.png'),('prod_035','catg_005','comp_034',200,9,'#socks',500,'socks','images/socks.png'),('prod_036','catg_006','comp_020',300,5,'#chess',500,'chess','images/chess.png'),('prod_037','catg_002','comp_018',40,9,'#bread',500,'bread','images/bread.png'),('prod_038','catg_006','comp_023',1000,5,'#minirobot',500,'mini robot','images/mini robot.png'),('prod_039','catg_008','comp_039',1000,5,'#pottedplant',500,'potted plant','images/potted plant.png'),('prod_040','catg_008','comp_051',1500,5,'#lamp',500,'lamp','images/lamp.png');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rating`
--

DROP TABLE IF EXISTS `rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rating` (
  `product_id` char(8) NOT NULL,
  `current_rating` float DEFAULT NULL,
  `rating_count` int DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  CONSTRAINT `ratingProductID` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rating`
--

LOCK TABLES `rating` WRITE;
/*!40000 ALTER TABLE `rating` DISABLE KEYS */;
/*!40000 ALTER TABLE `rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction_info`
--

DROP TABLE IF EXISTS `transaction_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_info` (
  `transaction_id` char(8) DEFAULT NULL,
  `customer_id` char(8) DEFAULT NULL,
  `product_id` char(8) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  KEY `transactionsTransactionID` (`transaction_id`),
  KEY `transactionsCustomerID` (`customer_id`),
  KEY `transactionsProductID` (`product_id`),
  CONSTRAINT `transactionsCustomerID` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`),
  CONSTRAINT `transactionsProductID` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`),
  CONSTRAINT `transactionsTransactionID` FOREIGN KEY (`transaction_id`) REFERENCES `transactions` (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_info`
--

LOCK TABLES `transaction_info` WRITE;
/*!40000 ALTER TABLE `transaction_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `transaction_id` char(8) NOT NULL,
  `customer_id` char(8) DEFAULT NULL,
  `address_id` char(8) DEFAULT NULL,
  `bank_id` char(8) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `total` float DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `ordersCustomerID` (`customer_id`),
  KEY `ordersAddressID` (`address_id`),
  KEY `ordersBankID_idx` (`bank_id`),
  CONSTRAINT `ordersAddressID` FOREIGN KEY (`address_id`) REFERENCES `address` (`address_id`),
  CONSTRAINT `ordersBankID` FOREIGN KEY (`bank_id`) REFERENCES `bank` (`bank_id`),
  CONSTRAINT `ordersCustomerID` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'dbmsproject'
--

--
-- Dumping routines for database 'dbmsproject'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-01 11:58:53
