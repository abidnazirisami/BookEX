-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: bookex
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.17.10.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add author',7,'add_author'),(20,'Can change author',7,'change_author'),(21,'Can delete author',7,'delete_author'),(22,'Can add boiii',8,'add_boiii'),(23,'Can change boiii',8,'change_boiii'),(24,'Can delete boiii',8,'delete_boiii'),(25,'Can add book',9,'add_book'),(26,'Can change book',9,'change_book'),(27,'Can delete book',9,'delete_book'),(28,'Can add our user',10,'add_ouruser'),(29,'Can change our user',10,'change_ouruser'),(30,'Can delete our user',10,'delete_ouruser'),(31,'Can add wishlist',11,'add_wishlist'),(32,'Can change wishlist',11,'change_wishlist'),(33,'Can delete wishlist',11,'delete_wishlist'),(34,'Can add review',12,'add_review'),(35,'Can change review',12,'change_review'),(36,'Can delete review',12,'delete_review'),(37,'Can add message',13,'add_message'),(38,'Can change message',13,'change_message'),(39,'Can delete message',13,'delete_message');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$KriN81OShpOf$WqHoF/qW4FNu+kD9h5FJnw2vcy1scoE+pOatYlDembU=','2018-05-05 07:37:52.264423',0,'abidnazirisami','abidnazirisami','','',0,1,'2018-05-05 07:37:46.363084');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(13,'mail','message'),(7,'pages','author'),(8,'pages','boiii'),(9,'pages','book'),(10,'pages','ouruser'),(12,'rating','review'),(11,'request','wishlist'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-05-05 07:36:54.387757'),(2,'auth','0001_initial','2018-05-05 07:37:01.895005'),(3,'admin','0001_initial','2018-05-05 07:37:03.648694'),(4,'admin','0002_logentry_remove_auto_add','2018-05-05 07:37:03.716522'),(5,'contenttypes','0002_remove_content_type_name','2018-05-05 07:37:04.755567'),(6,'auth','0002_alter_permission_name_max_length','2018-05-05 07:37:05.446999'),(7,'auth','0003_alter_user_email_max_length','2018-05-05 07:37:05.570678'),(8,'auth','0004_alter_user_username_opts','2018-05-05 07:37:05.628725'),(9,'auth','0005_alter_user_last_login_null','2018-05-05 07:37:06.119560'),(10,'auth','0006_require_contenttypes_0002','2018-05-05 07:37:06.152497'),(11,'auth','0007_alter_validators_add_error_messages','2018-05-05 07:37:06.215101'),(12,'auth','0008_alter_user_username_max_length','2018-05-05 07:37:07.672804'),(13,'auth','0009_alter_user_last_name_max_length','2018-05-05 07:37:08.321788'),(14,'pages','0001_initial','2018-05-05 07:37:14.809594'),(15,'mail','0001_initial','2018-05-05 07:37:16.472988'),(16,'mail','0002_auto_20180425_1503','2018-05-05 07:37:16.530885'),(17,'rating','0001_initial','2018-05-05 07:37:18.781556'),(18,'rating','0002_auto_20180423_1418','2018-05-05 07:37:19.651584'),(19,'rating','0003_review_rate_date','2018-05-05 07:37:20.279400'),(20,'rating','0004_auto_20180425_0349','2018-05-05 07:37:20.355385'),(21,'request','0001_initial','2018-05-05 07:37:21.372508'),(22,'sessions','0001_initial','2018-05-05 07:37:21.886116');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('hr7cn9bchhleajqzz2s9kdx36n4cd3te','ZDI0MGRlNGU2ODI1MTE2NWY0ZTlhNjYyOWQ0YTA4ZjNmZTljZGVkNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwN2MzMmEwODk1MmFmNDVmMTgzNjRkOGU0ZTFhYzk0NGE4ZTg0OWQyIn0=','2018-05-19 07:37:52.298537');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mail_message`
--

DROP TABLE IF EXISTS `mail_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mail_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sent_on` datetime(6) NOT NULL,
  `seen` tinyint(1) NOT NULL,
  `photo` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `from_user_id` int(11) NOT NULL,
  `to_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mail_message_from_user_id_249de744_fk_pages_ouruser_id` (`from_user_id`),
  KEY `mail_message_to_user_id_6ee8cb32_fk_pages_ouruser_id` (`to_user_id`),
  CONSTRAINT `mail_message_from_user_id_249de744_fk_pages_ouruser_id` FOREIGN KEY (`from_user_id`) REFERENCES `pages_ouruser` (`id`),
  CONSTRAINT `mail_message_to_user_id_6ee8cb32_fk_pages_ouruser_id` FOREIGN KEY (`to_user_id`) REFERENCES `pages_ouruser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mail_message`
--

LOCK TABLES `mail_message` WRITE;
/*!40000 ALTER TABLE `mail_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `mail_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_author`
--

DROP TABLE IF EXISTS `pages_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pages_author` (
  `author_id` int(11) NOT NULL AUTO_INCREMENT,
  `author_name` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `wiki_link` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `rating` double NOT NULL,
  PRIMARY KEY (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_author`
--

LOCK TABLES `pages_author` WRITE;
/*!40000 ALTER TABLE `pages_author` DISABLE KEYS */;
/*!40000 ALTER TABLE `pages_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_boiii`
--

DROP TABLE IF EXISTS `pages_boiii`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pages_boiii` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `condition` double NOT NULL,
  `photo` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `donated` tinyint(1) NOT NULL,
  `received` tinyint(1) NOT NULL,
  `id_id` int(11) NOT NULL,
  `isbn_id` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `receiver_id_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`book_id`),
  KEY `pages_boiii_id_id_2be74193_fk_pages_ouruser_id` (`id_id`),
  KEY `pages_boiii_isbn_id_e0d549a4_fk_pages_book_isbn` (`isbn_id`),
  KEY `pages_boiii_receiver_id_id_45d7764a_fk_pages_ouruser_id` (`receiver_id_id`),
  CONSTRAINT `pages_boiii_id_id_2be74193_fk_pages_ouruser_id` FOREIGN KEY (`id_id`) REFERENCES `pages_ouruser` (`id`),
  CONSTRAINT `pages_boiii_isbn_id_e0d549a4_fk_pages_book_isbn` FOREIGN KEY (`isbn_id`) REFERENCES `pages_book` (`isbn`),
  CONSTRAINT `pages_boiii_receiver_id_id_45d7764a_fk_pages_ouruser_id` FOREIGN KEY (`receiver_id_id`) REFERENCES `pages_ouruser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_boiii`
--

LOCK TABLES `pages_boiii` WRITE;
/*!40000 ALTER TABLE `pages_boiii` DISABLE KEYS */;
/*!40000 ALTER TABLE `pages_boiii` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_book`
--

DROP TABLE IF EXISTS `pages_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pages_book` (
  `isbn` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `topic_name` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `publish_year` int(11) NOT NULL,
  `publisher` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amazon_link` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL,
  `edition` int(11) NOT NULL,
  `pages` int(11) NOT NULL,
  `count` int(11) NOT NULL,
  `rating` double NOT NULL,
  `book_name` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `photo` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `author_id_id` int(11) NOT NULL,
  PRIMARY KEY (`isbn`),
  KEY `pages_book_author_id_id_4171a49a_fk_pages_author_author_id` (`author_id_id`),
  CONSTRAINT `pages_book_author_id_id_4171a49a_fk_pages_author_author_id` FOREIGN KEY (`author_id_id`) REFERENCES `pages_author` (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_book`
--

LOCK TABLES `pages_book` WRITE;
/*!40000 ALTER TABLE `pages_book` DISABLE KEYS */;
/*!40000 ALTER TABLE `pages_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pages_ouruser`
--

DROP TABLE IF EXISTS `pages_ouruser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pages_ouruser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL,
  `roll` int(11) NOT NULL,
  `mail_id` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `donate_count` int(11) NOT NULL,
  `phone` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `photo` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `pages_ouruser_user_id_45ab1090_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pages_ouruser`
--

LOCK TABLES `pages_ouruser` WRITE;
/*!40000 ALTER TABLE `pages_ouruser` DISABLE KEYS */;
INSERT INTO `pages_ouruser` VALUES (1,'abidnazirisami',21,26,'Not available',0,'Not available','dum-dum.jpg',1);
/*!40000 ALTER TABLE `pages_ouruser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rating_review`
--

DROP TABLE IF EXISTS `rating_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rating_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(10000) COLLATE utf8mb4_unicode_ci NOT NULL,
  `rating` double NOT NULL,
  `isbn_id` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id_id` int(11) NOT NULL,
  `rate_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rating_review_isbn_id_df65ed32_fk_pages_book_isbn` (`isbn_id`),
  KEY `rating_review_user_id_id_8a88b1bc_fk_pages_ouruser_id` (`user_id_id`),
  CONSTRAINT `rating_review_isbn_id_df65ed32_fk_pages_book_isbn` FOREIGN KEY (`isbn_id`) REFERENCES `pages_book` (`isbn`),
  CONSTRAINT `rating_review_user_id_id_8a88b1bc_fk_pages_ouruser_id` FOREIGN KEY (`user_id_id`) REFERENCES `pages_ouruser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rating_review`
--

LOCK TABLES `rating_review` WRITE;
/*!40000 ALTER TABLE `rating_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `rating_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request_wishlist`
--

DROP TABLE IF EXISTS `request_wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `request_wishlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `isbn` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `author_name` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `edition` int(11) NOT NULL,
  `count` int(11) NOT NULL,
  `book_name` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `isAvailable` tinyint(1) NOT NULL,
  `hasReceived` tinyint(1) NOT NULL,
  `isEmergency` tinyint(1) NOT NULL,
  `request_date` date NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `request_wishlist_user_id_1b3d0b05_fk_auth_user_id` (`user_id`),
  CONSTRAINT `request_wishlist_user_id_1b3d0b05_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_wishlist`
--

LOCK TABLES `request_wishlist` WRITE;
/*!40000 ALTER TABLE `request_wishlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `request_wishlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-05 14:58:22
