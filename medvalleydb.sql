-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2023 at 04:32 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medvalleydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add customer', 7, 'add_customer'),
(26, 'Can change customer', 7, 'change_customer'),
(27, 'Can delete customer', 7, 'delete_customer'),
(28, 'Can view customer', 7, 'view_customer'),
(29, 'Can add customer_ info', 8, 'add_customer_info'),
(30, 'Can change customer_ info', 8, 'change_customer_info'),
(31, 'Can delete customer_ info', 8, 'delete_customer_info'),
(32, 'Can view customer_ info', 8, 'view_customer_info'),
(33, 'Can add user payment', 9, 'add_userpayment'),
(34, 'Can change user payment', 9, 'change_userpayment'),
(35, 'Can delete user payment', 9, 'delete_userpayment'),
(36, 'Can view user payment', 9, 'view_userpayment'),
(37, 'Can add product', 10, 'add_product'),
(38, 'Can change product', 10, 'change_product'),
(39, 'Can delete product', 10, 'delete_product'),
(40, 'Can view product', 10, 'view_product'),
(41, 'Can add admin', 11, 'add_admin'),
(42, 'Can change admin', 11, 'change_admin'),
(43, 'Can delete admin', 11, 'delete_admin'),
(44, 'Can view admin', 11, 'view_admin'),
(45, 'Can add cart', 12, 'add_cart'),
(46, 'Can change cart', 12, 'change_cart'),
(47, 'Can delete cart', 12, 'delete_cart'),
(48, 'Can view cart', 12, 'view_cart'),
(49, 'Can add payment', 13, 'add_payment'),
(50, 'Can change payment', 13, 'change_payment'),
(51, 'Can delete payment', 13, 'delete_payment'),
(52, 'Can view payment', 13, 'view_payment'),
(53, 'Can add invoice', 14, 'add_invoice'),
(54, 'Can change invoice', 14, 'change_invoice'),
(55, 'Can delete invoice', 14, 'delete_invoice'),
(56, 'Can view invoice', 14, 'view_invoice'),
(57, 'Can add order', 15, 'add_order'),
(58, 'Can change order', 15, 'change_order'),
(59, 'Can delete order', 15, 'delete_order'),
(60, 'Can view order', 15, 'view_order'),
(61, 'Can add blog post', 16, 'add_blogpost'),
(62, 'Can change blog post', 16, 'change_blogpost'),
(63, 'Can delete blog post', 16, 'delete_blogpost'),
(64, 'Can view blog post', 16, 'view_blogpost'),
(65, 'Can add blog_comment', 17, 'add_blog_comment'),
(66, 'Can change blog_comment', 17, 'change_blog_comment'),
(67, 'Can delete blog_comment', 17, 'delete_blog_comment'),
(68, 'Can view blog_comment', 17, 'view_blog_comment'),
(69, 'Can add contact_message', 18, 'add_contact_message'),
(70, 'Can change contact_message', 18, 'change_contact_message'),
(71, 'Can delete contact_message', 18, 'delete_contact_message'),
(72, 'Can view contact_message', 18, 'view_contact_message');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$lC8YZ4tyoldq7XEyTrGD2u$c4nn42X1EkoG9MBh97j6IDjIj4y23mvReqf4g23LSeY=', '2023-07-10 16:03:02.149331', 1, 'Tirzi', '', '', 'md.tirzi98@gmail.com', 1, 1, '2023-07-10 16:00:56.659926');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(11, 'myapp', 'admin'),
(16, 'myapp', 'blogpost'),
(17, 'myapp', 'blog_comment'),
(12, 'myapp', 'cart'),
(18, 'myapp', 'contact_message'),
(7, 'myapp', 'customer'),
(8, 'myapp', 'customer_info'),
(14, 'myapp', 'invoice'),
(15, 'myapp', 'order'),
(13, 'myapp', 'payment'),
(10, 'myapp', 'product'),
(6, 'sessions', 'session'),
(9, 'user_payment', 'userpayment');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-07-09 19:21:28.066828'),
(2, 'auth', '0001_initial', '2023-07-09 19:21:36.303287'),
(3, 'admin', '0001_initial', '2023-07-09 19:21:38.377803'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-07-09 19:21:38.422980'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-07-09 19:21:38.473067'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-07-09 19:21:39.322812'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-07-09 19:21:40.584657'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-07-09 19:21:40.726469'),
(9, 'auth', '0004_alter_user_username_opts', '2023-07-09 19:21:40.772840'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-07-09 19:21:41.324007'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-07-09 19:21:41.354087'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-07-09 19:21:41.394973'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-07-09 19:21:41.501948'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-07-09 19:21:41.632965'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-07-09 19:21:41.740013'),
(16, 'auth', '0011_update_proxy_permissions', '2023-07-09 19:21:41.778019'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-07-09 19:21:41.881910'),
(18, 'sessions', '0001_initial', '2023-07-09 19:21:42.394671'),
(19, 'myapp', '0001_initial', '2023-07-11 14:03:20.758511'),
(20, 'myapp', '0002_alter_customer_customer_id', '2023-07-18 20:57:45.272055'),
(21, 'user_payment', '0001_initial', '2023-08-19 20:56:40.292758'),
(22, 'myapp', '0003_product', '2023-09-15 19:57:27.235716'),
(23, 'myapp', '0004_admin_blogpost_cart_order_payment_invoice_and_more', '2023-10-22 14:29:23.479828'),
(24, 'myapp', '0005_customer_account_status_customer_address_and_more', '2023-10-22 19:32:20.050699'),
(25, 'myapp', '0006_contact_message', '2023-10-31 13:12:14.216923'),
(26, 'myapp', '0007_contact_message_message_posted', '2023-10-31 18:36:32.887471'),
(27, 'myapp', '0008_cart_order_id_payment_order_id', '2023-11-03 11:18:54.269988'),
(28, 'myapp', '0009_alter_invoice_invoice_id', '2023-11-03 12:08:56.669284');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0fpy7jvmvgzpf3j7db90olrugy9vxcl2', '.eJxVjDsOwjAQBe_iGlnabPwJJT1nsNbeNQ4gW4qTCnF3iJQC2jcz76UCbWsJW5clzKzOCtTpd4uUHlJ3wHeqt6ZTq-syR70r-qBdXxvL83K4fweFevnWjifxgxkjejs4A2KRY0KBbDPASOJsSmwlMopzyWBGEA8UnZ-QRlTvD-VuOBA:1qItLq:zyXXalZIivoUVs54MHFEX_3J_ENz-l4dJGJbN3tWPNw', '2023-07-24 16:03:02.201135'),
('nmh7l229775e62h65w5s13hattepmz4p', '.eJx9jEEKgCAQAP-y5wiyTp76iSzuElu6iuYp-nviAzoOM8wDHFECWCjsOafNLGY_MTTFS2afIkyAFEVdSIdo7wZlrJWpu1a5OF-YWG_B_89ohcCa9f0A0LgpYg:1rAArZ:Uh-q7DeFfXyW0zKP_5dIIUldu-SAlG3BE4hVY9d70sU', '2023-12-18 15:28:01.143537'),
('qf3o80oc1azyq4flv8h7rae057k64l0p', '.eJyrVspLzE1VslIKzkjMKMpMLFJwzM3MU9JRSs1NzMwBihsaGBgaGls6pCSmpeWnZOboJSYDZQsSi4vL84tSgAock5INjYyBYsnx2ERz8tMz8-KLSxJLSouVrAxrAd7VI6Y:1qYQxO:5vemU55LOLPYtD57iLZ1wPd8twsXmd1OPKoJHyShooY', '2023-09-05 12:58:02.677694');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_admin`
--

CREATE TABLE `myapp_admin` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_admin`
--

INSERT INTO `myapp_admin` (`id`, `name`, `email`, `password`) VALUES
(1, 'michael Doe', 'admin@example.com', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_blogpost`
--

CREATE TABLE `myapp_blogpost` (
  `id` bigint(20) NOT NULL,
  `author_name` varchar(100) DEFAULT NULL,
  `blog_title` varchar(200) DEFAULT NULL,
  `user_image` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `writing` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_blogpost`
--

INSERT INTO `myapp_blogpost` (`id`, `author_name`, `blog_title`, `user_image`, `date`, `writing`) VALUES
(8, 'Christian John', 'Ovarian Cysts and Pregnancy: Could A Cyst Stop Me from Having a Baby?', 'uploads/blogs/internal_medicine_blogs.jpg', '2023-11-14', 'Ovarian cysts are fluid-filled sacs that form on the ovaries. Simple ovarian cysts usually are not cancerous. Most cysts are diagnosed through ultrasound or other imaging tests, which will also let your physician see the size of the cysts. While most cysts do not cause symptoms, if a cyst ruptures you may feel sudden pain and discomfort. '),
(9, 'Anne Marie', 'Why Men Should Stay on Top of Health Screenings?', 'uploads/blogs/Screenshot_98.png', '2023-11-14', 'During the pandemic, many patients delayed their annual examinations. This number was especially high in our male population. Unfortunately, this delay in screenings has resulted in more advanced prostate cancer diagnoses. \"We\'re concerned because we\'re seeing fewer patients come in for their annual screenings,\" says Daniel Lee, MD, MS, a urologist at Penn Medicine. \"So when we discover prostate cancers, they\'re more advanced than they were or could have been. The more advanced these cancers are when they are diagnosed, the more difficult they are to treat and have a successful outcome.\"'),
(10, 'Dr. Stephen Andrew', 'The COVID-19 Vaccine Can Impact Mammograms. What You Should Do (and Why You Shouldn’t Worry!).', 'uploads/blogs/Screenshot_97.png', '2023-11-14', 'In early 2021, a team of Penn Medicine radiologists began to notice a rise in axillary lymphadenopathy (swollen lymph nodes in the armpits) on multiple types of breast imaging (mammography, ultrasound and MRI).\r\n\r\nAxillary lymphadenopathy can be a sign of breast cancer. In most of the women, though, the swelling subsided within weeks. Subsequent tests and scans showed no evidence of breast cancer.\r\n\r\nGood news, ultimately – but why was this happening? Why the sudden rise in enlarged lymph nodes in the arm pit?'),
(12, 'Shahriar', 'Medicine', 'uploads/blogs/360_F_206607046_ERDw7gg52DUEjuJyGNu8NNG0YmvFnBZr_X3ee4QH.jpg', '2023-11-20', 'jklnelkrfn;weklrfkerkfwrrk');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_blog_comment`
--

CREATE TABLE `myapp_blog_comment` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `user_name` varchar(100) DEFAULT NULL,
  `comment` longtext DEFAULT NULL,
  `comment_date` date DEFAULT NULL,
  `blog_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_blog_comment`
--

INSERT INTO `myapp_blog_comment` (`id`, `user_id`, `user_name`, `comment`, `comment_date`, `blog_id_id`) VALUES
(4, 9, 'Shahriar Amin', 'The Information is Absoluteply correct.', '2023-11-14', 9),
(6, 9, 'Shahriar Amin', 'How are you?\r\n', '2023-11-29', 9),
(9, 22, 'Nazmul Sir', 'erfef', '2023-12-04', 9);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_cart`
--

CREATE TABLE `myapp_cart` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `item_price` varchar(100) DEFAULT NULL,
  `total` double DEFAULT NULL,
  `cart_session` double DEFAULT NULL,
  `order_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_cart`
--

INSERT INTO `myapp_cart` (`id`, `email`, `item_name`, `item_price`, `total`, `cart_session`, `order_id_id`) VALUES
(6, '1001139@daffodil.ac', 'Adlock', '5', 12.5, NULL, 5942),
(7, '1001139@daffodil.ac', 'Amdocal', '7.5', 12.5, NULL, 5942),
(8, '1001139@daffodil.ac', 'Aristoplex', '10', 25, NULL, 89),
(9, '1001139@daffodil.ac', 'Calbo-D', '15', 25, NULL, 89),
(10, '1001139@daffodil.ac', 'Adlock', '5', 12.5, NULL, 4820),
(11, '1001139@daffodil.ac', 'Amdocal', '7.5', 12.5, NULL, 4820),
(12, '1001139@daffodil.ac', 'Amdocal', '7.5', 17.5, NULL, 9647),
(13, '1001139@daffodil.ac', 'Aristoplex', '10', 17.5, NULL, 9647),
(14, '1001139@daffodil.ac', 'Amdocal', '7.5', 7.5, NULL, 1315),
(15, '1001139@daffodil.ac', 'Kilbac', '17', 17, NULL, 7303),
(16, '1001139@daffodil.ac', 'Adlock', '25', 77.5, NULL, 1760),
(17, '1001139@daffodil.ac', 'Amdocal', '22.5', 77.5, NULL, 1760),
(18, '1001139@daffodil.ac', 'Aristoplex', '30', 77.5, NULL, 1760),
(19, '1001139@daffodil.ac', 'Amdocal', '7.5', 7.5, NULL, 5038),
(20, 'jetor67307@eachart.com', 'Adlock', '5', 114.5, NULL, 2457),
(21, 'jetor67307@eachart.com', 'Amdocal', '7.5', 114.5, NULL, 2457),
(22, 'jetor67307@eachart.com', 'Kilbac', '102', 114.5, NULL, 2457),
(23, 'livane8347@nexxterp.com', 'Adlock', '15', 56.5, NULL, 7558),
(24, 'livane8347@nexxterp.com', 'Amdocal', '7.5', 56.5, NULL, 7558),
(25, 'livane8347@nexxterp.com', 'Kilbac', '34', 56.5, NULL, 7558),
(26, '1001139@daffodil.ac', 'Adlock', '5', 29.5, NULL, 9058),
(27, '1001139@daffodil.ac', 'Amdocal', '7.5', 29.5, NULL, 9058),
(28, '1001139@daffodil.ac', 'Kilbac', '17', 29.5, NULL, 9058),
(29, '1001139@daffodil.ac', 'Asynta-Plus', '15', 48, NULL, 1286),
(30, '1001139@daffodil.ac', 'Bantovet-Ointment', '12', 48, NULL, 1286),
(31, '1001139@daffodil.ac', 'Coralcal-D', '13', 48, NULL, 1286),
(32, '1001139@daffodil.ac', 'Windel-Plus', '8', 48, NULL, 1286),
(33, '1001139@daffodil.ac', 'Adlock', '5', 22.5, NULL, 6408),
(34, '1001139@daffodil.ac', 'Amdocal', '7.5', 22.5, NULL, 6408),
(35, '1001139@daffodil.ac', 'Aristoplex', '10', 22.5, NULL, 6408);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_contact_message`
--

CREATE TABLE `myapp_contact_message` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `message` longtext DEFAULT NULL,
  `message_posted` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_contact_message`
--

INSERT INTO `myapp_contact_message` (`id`, `name`, `email`, `phone`, `subject`, `message`, `message_posted`) VALUES
(1, 'Shahriar Amin', '1001139@daffodil.ac', '01622668685', 'jrnkejrnfkjnfknkrnf', 'kjnknfdknknkcvndskcvkdc', NULL),
(2, 'Shahriar Amin', '1001139@daffodil.ac', '01622668685', 'jrnkejrnfkjnfknkrnf', 'wefdwfwfwfw', NULL),
(3, 'Shahriar Amin', '1001139@daffodil.ac', '01622668685', 'jrnkejrnfkjnfknkrnf', 'drfsdfsdfsdsdf', NULL),
(4, 'Khandakar Arraf', '1001140@daffodil.ac', '09141704603', 'jrnkejrnfkjnfknkrnf', 'wdeasdcascasdcsd', '2023-11-01'),
(5, 'TAYAN TASFIN TANHA', 'pijek53429@rdluxe.com', '09141704603', 'Updates about new arrival', 'Please notify me', '2023-11-11'),
(7, 'Shahriar Amin', '1001139@daffodil.ac', '01622668685', 'jrnkejrnfkjnfknkrnf', 'oijenirkwk', '2023-11-20');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_customer`
--

CREATE TABLE `myapp_customer` (
  `Customer_ID` int(11) NOT NULL,
  `Customer_Name` varchar(30) NOT NULL,
  `Customer_Email` varchar(50) NOT NULL,
  `Customer_Password` varchar(255) NOT NULL,
  `Customer_Confirm_Password` varchar(255) NOT NULL,
  `account_status` varchar(10) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `role` varchar(15) DEFAULT NULL,
  `user_image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_customer`
--

INSERT INTO `myapp_customer` (`Customer_ID`, `Customer_Name`, `Customer_Email`, `Customer_Password`, `Customer_Confirm_Password`, `account_status`, `address`, `age`, `dob`, `gender`, `phone_number`, `role`, `user_image`) VALUES
(9, 'Shahriar Amin', '1001139@daffodil.ac', 'pbkdf2_sha256$600000$h17Wdx0VuiJ6yztmRQiESd$QFAyeRo38NN7Ku/rxD+C9nrcV94h5eat359PIrav8rE=', 'pbkdf2_sha256$600000$4jKJeezV7ulai3MHjaoX1o$jA/ReScjdQl2skrxUMaeFfmFyQRFzNK2DgqoqETwVZY=', 'active', 'h-8, w-50, Tongi,Gazipur. Gazipur Mohanogor', NULL, '2023-10-06', 'male', '01622668685', '', 'uploads/90.png'),
(19, 'Shahriar Amin Tirzi', 'livane8347@nexxterp.com', 'pbkdf2_sha256$600000$Eo7EJ2cKgFrokGQVrUcHvg$XaILVgbonChW5+gzA+uotbYE9yerV032+HjwkU8FmFE=', 'pbkdf2_sha256$600000$DZYnJixGycBQuXIhVcsZOQ$NoKWTm7XTiE2gxLjtHwdxqDKRDkf6oFG/fnXweBtPVk=', 'active', 'h-8, w-50, Tongi,Gazipur. City', NULL, '2023-11-02', 'male', '01622668685', '', 'uploads/360_F_206607046_ERDw7gg52DUEjuJyGNu8NNG0YmvFnBZr_GRRTId0_36ZCVKi.jpg'),
(20, 'TAYAN TASFIN TANHA', 'bacidim266@nasmis.com', 'pbkdf2_sha256$600000$nYUo3tK0n0qaZZ4ukXQZu8$pfdm10SX5OIE85LiN/MnKuK2btDg0poCY9s/bAoTYlw=', 'pbkdf2_sha256$600000$BJuCvazHZuVIpGhpr4sIqi$9IshNobTWXCgJkE4PwkSmH4DTQFV23aSoKjwcRSCxNo=', 'active', 'h-8, w-50, Tongi,Gazipur.', NULL, '2023-12-02', 'male', '09141704603', '', ''),
(21, 'TAYAN TASFIN TANHA', 'bacidim266@nasmis.com', 'pbkdf2_sha256$600000$RtJfkU7RZIthu1Wj6ZN8JO$6rI2X6Iv0PBmRPzuo8hdTrQt2fJ4GHnmPkD9er47iDw=', 'pbkdf2_sha256$600000$YsGleHUvMq1cDhuXTRgidT$p/iWE2MTxBmFCXjNCHQNnYnnE9Ktjq5YXrL+piRh2tU=', 'active', 'h-8, w-50, Tongi,Gazipur.', NULL, '2023-12-02', 'male', '09141704603', '', ''),
(22, 'Nazmul Sir', 'nazmulmunaz@gmail.com', 'pbkdf2_sha256$600000$wrLuV05bOHjNbGGX36zOWD$QtGgO6bmP5mGqEgcN99rQDf8tbPelrm8OaZy3C+az+M=', 'pbkdf2_sha256$600000$O6OFIIXC98ALRb19N9ePLR$BeGxaikX6OXK3hVCctG9uFKr6/Q+TFiM+BvukH11p+E=', 'active', 'h-8, w-50, Tongi,Gazipur.', NULL, '2023-12-01', 'male', '01622668685', '', ''),
(23, 'Paracetamol', 'recepo4212@jalunaki.com', 'pbkdf2_sha256$600000$v7xfqKvqavJ4qg9CEMLrgp$vFwFElN19JyMuRLym0xl17pUM+s/9AR3P9R0VZ+6N+Y=', 'pbkdf2_sha256$600000$aPOw6yCFuIHeT3vR9aeEpD$WSpYxKqPi2Hr9z62eegAtnkRx1ZHcuXnhpL4VbqJ7fU=', 'active', 'h-8, w-50, Tongi,Gazipur.', NULL, '2023-12-01', 'male', '01923649180', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_customer_info`
--

CREATE TABLE `myapp_customer_info` (
  `Phone_Number` varchar(20) NOT NULL,
  `Facebook` varchar(30) NOT NULL,
  `Twitter` varchar(30) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Gender` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_invoice`
--

CREATE TABLE `myapp_invoice` (
  `invoice_id` varchar(10) NOT NULL,
  `order_date` date DEFAULT NULL,
  `customer_name` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `gateway` varchar(100) DEFAULT NULL,
  `order_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_invoice`
--

INSERT INTO `myapp_invoice` (`invoice_id`, `order_date`, `customer_name`, `email`, `gateway`, `order_id_id`) VALUES
('D79297', '2023-11-20', 'Shahriar Amin Tirzi', 'livane8347@nexxterp.com', 'Nagad', 7558),
('I97297', '2023-12-04', 'Shahriar Amin', '1001139@daffodil.ac', 'Nagad', 6408),
('K84868', '2023-12-01', 'Shahriar Amin', '1001139@daffodil.ac', 'Rocket', 4820),
('N44688', '2023-11-03', 'Shahriar Amin', '1001139@daffodil.ac', 'Nagad', 89),
('O79284', '2023-11-14', 'Shahriar Amin', '1001139@daffodil.ac', 'Rocket', 1760),
('T79640', '2023-11-11', 'Shahriar Amin', '1001139@daffodil.ac', 'Nagad', 9647),
('V62620', '2023-11-03', 'Shahriar Amin', '1001139@daffodil.ac', 'Bkash', 5942);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_order`
--

CREATE TABLE `myapp_order` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `customer_name` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `total` double DEFAULT NULL,
  `gateway` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_order`
--

INSERT INTO `myapp_order` (`order_id`, `order_date`, `customer_name`, `email`, `status`, `total`, `gateway`) VALUES
(89, '2023-11-03', 'Khandaker Arraf', '1001139@daffodil.ac', 'approved', 25, 'Nagad'),
(1286, '2023-12-02', 'Shahriar Amin', '1001139@daffodil.ac', 'pending', 48, 'Nagad'),
(1315, '2023-11-11', 'Shahriar Amin', '1001139@daffodil.ac', 'pending', 7.5, 'Rocket'),
(1760, '2023-11-14', 'Khandaker Arraf', '1001139@daffodil.ac', 'declined', 77.5, 'Rocket'),
(2457, '2023-11-20', 'Shahriar Amin Tirzi', 'jetor67307@eachart.com', 'pending', 114.5, 'Nagad'),
(4820, '2023-11-07', 'Shahriar Amin', '1001139@daffodil.ac', 'approved', 12.5, 'Rocket'),
(5038, '2023-11-19', 'Shahriar Amin', '1001139@daffodil.ac', 'pending', 7.5, 'Rocket'),
(5942, '2023-11-03', 'Shahriar Amin', '1001139@daffodil.ac', 'approved', 12.5, 'Bkash'),
(6408, '2023-12-04', 'Shahriar Amin', '1001139@daffodil.ac', 'declined', 22.5, 'Nagad'),
(7303, '2023-11-11', 'Arraf', '1001139@daffodil.ac', 'pending', 17, 'Rocket'),
(7558, '2023-11-20', 'Shahriar Amin Tirzi', 'livane8347@nexxterp.com', 'declined', 56.5, 'Nagad'),
(9058, '2023-11-29', 'Shahriar Amin', '1001139@daffodil.ac', 'pending', 29.5, 'Rocket'),
(9647, '2023-11-11', 'Shahriar Amin', '1001139@daffodil.ac', 'approved', 17.5, 'Nagad');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_payment`
--

CREATE TABLE `myapp_payment` (
  `payment_id` int(11) NOT NULL,
  `transaction_number` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `order_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_payment`
--

INSERT INTO `myapp_payment` (`payment_id`, `transaction_number`, `phone_number`, `email`, `order_id_id`) VALUES
(5, '6t78t867677', '01622668685', '1001139@daffodil.ac', 5942),
(6, '8494jfirrjr', '01622668685', '1001139@daffodil.ac', 89),
(7, '6t78t867677', '01622668685', '1001139@daffodil.ac', 4820),
(8, '6t78t867677', '01622668685', '1001139@daffodil.ac', 9647),
(9, '6t78t867677', '019283744745', '1001139@daffodil.ac', 1315),
(10, '03945038jf', '03948548389', '1001139@daffodil.ac', 7303),
(11, '8494jfirrjr', '01622668685', '1001139@daffodil.ac', 1760),
(12, '6t78t867677', '019283744745', '1001139@daffodil.ac', 5038),
(13, 'kjndfknerjfe8', '09141704603', 'jetor67307@eachart.com', 2457),
(14, 'kjrkfejrfjeofier', '09141704603', 'livane8347@nexxterp.com', 7558),
(15, '45gt4g54wey6', '03948548389', '1001139@daffodil.ac', 9058),
(16, 'jrhjnekjrfkljn5t4', '01923649180', '1001139@daffodil.ac', 1286),
(17, '45gt4g54wey6', '01622668685', '1001139@daffodil.ac', 6408);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_product`
--

CREATE TABLE `myapp_product` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `price` double NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_product`
--

INSERT INTO `myapp_product` (`id`, `name`, `description`, `image`, `price`, `quantity`, `status`) VALUES
(2, 'Adlock', 'Antibiotic', 'uploads/Adlock_BqY7Yzb.png', 5, 5, NULL),
(3, 'Ambrox', 'Antibiotic', 'uploads/Ambrox.jpg', 5.5, 10, NULL),
(4, 'Amdocal', 'Pain killer', 'uploads/Amdocal.png', 7.5, 5, NULL),
(5, 'Aristoplex', 'Cough Syrup', 'uploads/Aristoplex.png', 10, 4, NULL),
(6, 'Asynta-Plus', 'Gastric Syrup', 'uploads/Asynta.png', 15, 17, NULL),
(7, 'Bantovet-Ointment', 'Antiseptic Cream', 'uploads/Bantovet.jpg', 12, 29, NULL),
(8, 'Betaloc', 'Cardiac Tablet', 'uploads/Betaloc.png', 20, 24, NULL),
(9, 'Bizoran', 'Antibiotic', 'uploads/Bizoran.png', 15, 17, NULL),
(10, 'Calbo-D', 'Calcium Tablet', 'uploads/Calbo-D.png', 15, 49, NULL),
(11, 'Candibiotic', 'Ear Drop', 'uploads/Candibiotic.jpg', 12, 25, NULL),
(12, 'Cholcut', 'Sleeping Pill', 'uploads/Cholcut.png', 15, 21, NULL),
(13, 'Clopid', 'Pain Killer', 'uploads/Clopid.png', 12, 15, NULL),
(14, 'Clopilet', 'Diabetes', 'uploads/Clopilet.png', 17, 35, NULL),
(15, 'Coralcal-D', 'Calcium Tablet', 'uploads/Coralcal-D.jpg', 13, 21, NULL),
(16, 'Domperidone', 'Contraceptive Pill', 'uploads/Domperidone.jpg', 15, 33, NULL),
(17, 'Ecosprin', 'Sleeping Pill', 'uploads/Ecosprin.jpg', 13.5, 30, NULL),
(18, 'Famotid', 'Cardiac Tablet', 'uploads/Famotid.jpg', 25, 25, NULL),
(19, 'Fexo', 'Antibiotic', 'uploads/Fexo.jpg', 10, 30, NULL),
(20, 'Gavilac', 'Gastric Syrup', 'uploads/Gavilac.png', 12.5, 25, NULL),
(21, 'Gaviscon', 'Cough Syrup', 'uploads/Gaviscon.jpg', 17, 35, NULL),
(22, 'Gavisol', 'Gastric Syrup', 'uploads/Gavisol.jpg', 16, 25, NULL),
(23, 'Imucort', 'Sleeping Pill', 'uploads/Imucort.png', 17, 25, NULL),
(24, 'Indever', 'Cardiac Medicine', 'uploads/Indever.png', 22, 30, NULL),
(25, 'Kilbac', 'Diabetes Injection', 'uploads/Kilbac.png', 17, 15, NULL),
(26, 'Lanso', 'Contraceptive Pill', 'uploads/Lanso.jpg', 13, 27, NULL),
(27, 'Lopirel', 'Cardiac Medicine', 'uploads/Lopirel.png', 18, 27, NULL),
(28, 'Mebolin', 'Paracetamol', 'uploads/Mebolin.jpg', 7, 24, NULL),
(29, 'Mirtaz', 'Pain Killer', 'uploads/Mirtaz.png', 8, 18, NULL),
(30, 'Montair', 'Antiseptic Tablet', 'uploads/Montair.png', 12, 30, NULL),
(31, 'Motigut', 'Antibiotic', 'uploads/Motigut.jpg', 17, 20, NULL),
(32, 'Nervalin', 'Contraceptive Pill', 'uploads/Nervalin.png', 15, 25, NULL),
(33, 'Nintoin', 'Anti-depresant Pill', 'uploads/Nintoin.png', 30, 30, NULL),
(34, 'Odmon', 'Anti-depresant Pill', 'uploads/Odmon.png', 22, 25, NULL),
(35, 'Odrel', 'Antibiotic', 'uploads/Odrel.png', 12, 25, NULL),
(36, 'Olicare-Lotion', 'Body Lotion', 'uploads/Olicare_lotion.jpg', 35, 30, NULL),
(37, 'Omedon', 'Gastric Tablet', 'uploads/Omedon.png', 9, 30, NULL),
(38, 'Paricel', 'Antibiotic', 'uploads/Paricel.png', 14.5, 25, NULL),
(39, 'Prazopress', 'Diabetes Tablet', 'uploads/Prazopress.png', 18, 30, NULL),
(40, 'Progut', 'Gastric tablet', 'uploads/Progut.png', 15, 35, NULL),
(41, 'Providac', 'Cough Syrup', 'uploads/Providac.jpg', 20, 20, NULL),
(42, 'Rabeprazole', 'Cardiac Medicine', 'uploads/Rabeprazole.png', 25, 30, NULL),
(43, 'Replet', 'Sleeping Pill', 'uploads/Replet.jpg', 17, 25, NULL),
(44, 'Rolip', 'Pain Killer', 'uploads/Rolip.jpg', 22, 30, NULL),
(45, 'Rosuva', 'Antibiotic', 'uploads/Rosuva.jpeg', 12, 25, NULL),
(46, 'Silodosin', 'Pain Killer', 'uploads/Silodosin.jpg', 7.5, 25, NULL),
(47, 'Tekast', 'Cardiac Medicine', 'uploads/Tekast.png', 15, 30, NULL),
(48, 'Telmilok', 'Anti-depressant Pill', 'uploads/Telmilok.png', 20, 25, NULL),
(49, 'Telpromax', 'Cardiac Medicine', 'uploads/Telpromax.png', 25, 20, NULL),
(50, 'Ticarel', 'Neuro Medicine', 'uploads/Ticarel.png', 24, 25, NULL),
(51, 'Tofen ', 'Pain Killer', 'uploads/Tofen.png', 13, 30, NULL),
(52, 'Vergon', 'Contraceptive Pill', 'uploads/Vergon.jpg', 14, 25, NULL),
(53, 'Viscotin', 'Cardiac Medicine', 'uploads/Viscotin.png', 23, 25, NULL),
(55, 'Vitabion', 'Antibiotic', 'uploads/Vitabion_sVvmmix.jpg', 13.5, 25, NULL),
(56, 'Adovas', 'Syrup', 'uploads/Efz6FYUV8jFiMUGdNbM9EwrpRwW1GvEYioLSxn2Y.jpg', 10, 25, NULL),
(57, 'Vesteral', 'Anti-Depressant Pills', 'uploads/Vesteral.png', 5.5, 20, NULL),
(58, 'Xinc', 'Antibiotic', 'uploads/61dff00f4044f.20220113.png', 15, 15, NULL),
(59, 'Windel-Plus', 'Nebulizer ', 'uploads/2018-04-07_143704.167906windelplus3mlnebulisersolution_5ac620305fa03-.68348.jpg', 8, 24, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user_payment_userpayment`
--

CREATE TABLE `user_payment_userpayment` (
  `id` bigint(20) NOT NULL,
  `payment_bool` tinyint(1) NOT NULL,
  `stripe_checkout_id` varchar(500) NOT NULL,
  `Customer_ID_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `myapp_admin`
--
ALTER TABLE `myapp_admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_blogpost`
--
ALTER TABLE `myapp_blogpost`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_blog_comment`
--
ALTER TABLE `myapp_blog_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_blog_comment_blog_id_id_209aa0a7_fk_myapp_blogpost_id` (`blog_id_id`);

--
-- Indexes for table `myapp_cart`
--
ALTER TABLE `myapp_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_cart_order_id_id_c3b5b6f5_fk_myapp_order_order_id` (`order_id_id`);

--
-- Indexes for table `myapp_contact_message`
--
ALTER TABLE `myapp_contact_message`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_customer`
--
ALTER TABLE `myapp_customer`
  ADD PRIMARY KEY (`Customer_ID`);

--
-- Indexes for table `myapp_customer_info`
--
ALTER TABLE `myapp_customer_info`
  ADD PRIMARY KEY (`Phone_Number`);

--
-- Indexes for table `myapp_invoice`
--
ALTER TABLE `myapp_invoice`
  ADD PRIMARY KEY (`invoice_id`),
  ADD KEY `myapp_invoice_order_id_id_3a22260f_fk_myapp_order_order_id` (`order_id_id`);

--
-- Indexes for table `myapp_order`
--
ALTER TABLE `myapp_order`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `myapp_payment`
--
ALTER TABLE `myapp_payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `myapp_payment_order_id_id_70d622f8_fk_myapp_order_order_id` (`order_id_id`);

--
-- Indexes for table `myapp_product`
--
ALTER TABLE `myapp_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_payment_userpayment`
--
ALTER TABLE `user_payment_userpayment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_payment_userpay_Customer_ID_id_c7528c34_fk_myapp_cus` (`Customer_ID_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `myapp_admin`
--
ALTER TABLE `myapp_admin`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myapp_blogpost`
--
ALTER TABLE `myapp_blogpost`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `myapp_blog_comment`
--
ALTER TABLE `myapp_blog_comment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `myapp_cart`
--
ALTER TABLE `myapp_cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `myapp_contact_message`
--
ALTER TABLE `myapp_contact_message`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `myapp_customer`
--
ALTER TABLE `myapp_customer`
  MODIFY `Customer_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `myapp_order`
--
ALTER TABLE `myapp_order`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9648;

--
-- AUTO_INCREMENT for table `myapp_payment`
--
ALTER TABLE `myapp_payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `myapp_product`
--
ALTER TABLE `myapp_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `user_payment_userpayment`
--
ALTER TABLE `user_payment_userpayment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `myapp_blog_comment`
--
ALTER TABLE `myapp_blog_comment`
  ADD CONSTRAINT `myapp_blog_comment_blog_id_id_209aa0a7_fk_myapp_blogpost_id` FOREIGN KEY (`blog_id_id`) REFERENCES `myapp_blogpost` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `myapp_cart`
--
ALTER TABLE `myapp_cart`
  ADD CONSTRAINT `myapp_cart_order_id_id_c3b5b6f5_fk_myapp_order_order_id` FOREIGN KEY (`order_id_id`) REFERENCES `myapp_order` (`order_id`);

--
-- Constraints for table `myapp_invoice`
--
ALTER TABLE `myapp_invoice`
  ADD CONSTRAINT `myapp_invoice_order_id_id_3a22260f_fk_myapp_order_order_id` FOREIGN KEY (`order_id_id`) REFERENCES `myapp_order` (`order_id`);

--
-- Constraints for table `myapp_payment`
--
ALTER TABLE `myapp_payment`
  ADD CONSTRAINT `myapp_payment_order_id_id_70d622f8_fk_myapp_order_order_id` FOREIGN KEY (`order_id_id`) REFERENCES `myapp_order` (`order_id`);

--
-- Constraints for table `user_payment_userpayment`
--
ALTER TABLE `user_payment_userpayment`
  ADD CONSTRAINT `user_payment_userpay_Customer_ID_id_c7528c34_fk_myapp_cus` FOREIGN KEY (`Customer_ID_id`) REFERENCES `myapp_customer` (`Customer_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
