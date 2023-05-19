-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- ホスト: db
-- 生成日時: 2023 年 4 月 20 日 11:26
-- サーバのバージョン： 5.7.41
-- PHP のバージョン: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `django_sample`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- テーブルの構造 `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- テーブルの構造 `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `auth_permission`
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
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add post', 8, 'add_post'),
(30, 'Can change post', 8, 'change_post'),
(31, 'Can delete post', 8, 'delete_post'),
(32, 'Can view post', 8, 'view_post'),
(33, 'Can add quiz', 9, 'add_quiz'),
(34, 'Can change quiz', 9, 'change_quiz'),
(35, 'Can delete quiz', 9, 'delete_quiz'),
(36, 'Can view quiz', 9, 'view_quiz'),
(37, 'Can add tag', 10, 'add_tag'),
(38, 'Can change tag', 10, 'change_tag'),
(39, 'Can delete tag', 10, 'delete_tag'),
(40, 'Can view tag', 10, 'view_tag'),
(41, 'Can add seiseki', 11, 'add_seiseki'),
(42, 'Can change seiseki', 11, 'change_seiseki'),
(43, 'Can delete seiseki', 11, 'delete_seiseki'),
(44, 'Can view seiseki', 11, 'view_seiseki'),
(45, 'Can add genre', 12, 'add_genre'),
(46, 'Can change genre', 12, 'change_genre'),
(47, 'Can delete genre', 12, 'delete_genre'),
(48, 'Can view genre', 12, 'view_genre'),
(49, 'Can add quiz', 13, 'add_quiz'),
(50, 'Can change quiz', 13, 'change_quiz'),
(51, 'Can delete quiz', 13, 'delete_quiz'),
(52, 'Can view quiz', 13, 'view_quiz'),
(53, 'Can add haiku', 14, 'add_haiku'),
(54, 'Can change haiku', 14, 'change_haiku'),
(55, 'Can delete haiku', 14, 'delete_haiku'),
(56, 'Can view haiku', 14, 'view_haiku');

-- --------------------------------------------------------

--
-- テーブルの構造 `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$62Fcm9JK3JVLCapAdqoqok$XRsHxTUPfYDCWgaVZu1TsqpZj9LhWhtPJ+xR8A+wR4M=', '2023-04-20 02:17:31.961009', 1, 'admin', '', '', '', 1, 1, '2023-04-04 15:12:25.355602'),
(2, 'pbkdf2_sha256$260000$7gPTYjm4ANgEhFkmOk4Twm$Vc/8pB3mGE4wMOWB4KjVD4l1GIXF5WLphAXuJN70apM=', '2023-04-14 10:36:08.795948', 0, 'test01', '', '', '', 0, 1, '2023-04-05 03:53:17.512315');

-- --------------------------------------------------------

--
-- テーブルの構造 `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- テーブルの構造 `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- テーブルの構造 `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_bin,
  `object_repr` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-04-05 03:53:17.587841', '2', 'test01', 1, '[{\"added\": {}}]', 4, 1),
(2, '2023-04-05 13:04:00.451491', '1', 'english', 1, '[{\"added\": {}}]', 7, 1),
(3, '2023-04-05 14:55:35.485947', '1', 'title-1', 1, '[{\"added\": {}}]', 8, 1),
(4, '2023-04-05 14:56:05.671725', '1', 'tag1', 1, '[{\"added\": {}}]', 10, 1),
(5, '2023-04-05 14:56:12.872606', '1', 'title-1', 2, '[]', 8, 1),
(6, '2023-04-05 14:58:51.721740', '2', 'sports', 1, '[{\"added\": {}}]', 7, 1),
(7, '2023-04-05 14:59:04.202455', '1', 'title-1', 2, '[{\"changed\": {\"fields\": [\"Category\"]}}]', 8, 1),
(8, '2023-04-05 14:59:20.954675', '1', 'title-1', 2, '[]', 8, 1),
(9, '2023-04-05 14:59:39.082750', '2', 'tag2', 1, '[{\"added\": {}}]', 10, 1),
(10, '2023-04-05 14:59:55.524320', '1', 'title-1', 2, '[{\"changed\": {\"fields\": [\"Tag\"]}}]', 8, 1),
(11, '2023-04-05 15:00:25.336022', '1', 'title-1', 2, '[]', 8, 1),
(12, '2023-04-05 16:01:51.547549', '2', '投稿２', 1, '[{\"added\": {}}]', 8, 1),
(13, '2023-04-05 18:12:57.424517', '1', 'title-1', 2, '[]', 8, 1),
(14, '2023-04-05 18:13:02.549783', '1', 'title-1', 2, '[]', 8, 1),
(15, '2023-04-07 07:17:39.115186', '1', 'あ', 1, '[{\"added\": {}}]', 14, 1),
(16, '2023-04-07 07:47:43.766451', '1', 'あ', 3, '', 14, 1),
(17, '2023-04-07 07:48:35.644659', '2', 'あ', 1, '[{\"added\": {}}]', 14, 1),
(18, '2023-04-07 07:56:25.878701', '1', 'english', 1, '[{\"added\": {}}]', 12, 1),
(19, '2023-04-07 07:56:36.471181', '1', 'a', 1, '[{\"added\": {}}]', 13, 1),
(20, '2023-04-09 10:13:26.482967', '1', 'aa', 2, '[{\"changed\": {\"fields\": [\"\\u554f\\u984c\"]}}]', 13, 1),
(21, '2023-04-20 02:18:09.232360', '2', '計算', 1, '[{\"added\": {}}]', 12, 1),
(22, '2023-04-20 02:18:22.377861', '3', '歴史', 1, '[{\"added\": {}}]', 12, 1),
(23, '2023-04-20 02:18:37.339381', '4', 'スポーツ', 1, '[{\"added\": {}}]', 12, 1),
(24, '2023-04-20 02:18:44.487231', '5', 'サッカー', 1, '[{\"added\": {}}]', 12, 1);

-- --------------------------------------------------------

--
-- テーブルの構造 `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'mybbs', 'category'),
(8, 'mybbs', 'post'),
(9, 'mybbs', 'quiz'),
(11, 'mybbs', 'seiseki'),
(10, 'mybbs', 'tag'),
(14, 'myhaiku', 'haiku'),
(12, 'myquiz', 'genre'),
(13, 'myquiz', 'quiz'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- テーブルの構造 `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-04-04 15:08:07.053240'),
(2, 'auth', '0001_initial', '2023-04-04 15:08:07.308018'),
(3, 'admin', '0001_initial', '2023-04-04 15:08:07.388480'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-04-04 15:08:07.395701'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-04 15:08:07.403097'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-04-04 15:08:07.449103'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-04-04 15:08:07.475297'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-04-04 15:08:07.485875'),
(9, 'auth', '0004_alter_user_username_opts', '2023-04-04 15:08:07.491054'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-04-04 15:08:07.514297'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-04-04 15:08:07.516510'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-04-04 15:08:07.522010'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-04-04 15:08:07.550131'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-04-04 15:08:07.574173'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-04-04 15:08:07.583869'),
(16, 'auth', '0011_update_proxy_permissions', '2023-04-04 15:08:07.589057'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-04-04 15:08:07.614784'),
(18, 'sessions', '0001_initial', '2023-04-04 15:08:07.638485'),
(19, 'mybbs', '0001_initial', '2023-04-05 13:03:16.677318'),
(20, 'mybbs', '0002_post_comment_count_post_like_count_post_public_range', '2023-04-05 13:03:16.758781'),
(21, 'mybbs', '0003_rename_haiku_seiseki', '2023-04-05 13:03:16.776691'),
(22, 'mybbs', '0004_user', '2023-04-05 13:03:16.937943'),
(23, 'mybbs', '0005_delete_user', '2023-04-05 13:03:16.956732'),
(24, 'mybbs', '0006_post_tag', '2023-04-05 13:03:17.018993'),
(25, 'mybbs', '0007_post_category', '2023-04-05 13:03:17.044287'),
(26, 'myhaiku', '0001_initial', '2023-04-05 13:03:17.060666'),
(27, 'myquiz', '0001_initial', '2023-04-05 13:03:17.113360'),
(28, 'mybbs', '0008_alter_post_tag', '2023-04-05 16:16:45.024597'),
(29, 'mybbs', '0009_alter_post_tag', '2023-04-05 16:20:24.157528');

-- --------------------------------------------------------

--
-- テーブルの構造 `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_bin NOT NULL,
  `session_data` longtext COLLATE utf8mb4_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0xxadydte63jm63avk4gt5wpkc9iq6uf', '.eJxVjEEOwiAQRe_C2hBgOnVw6b5nIDNApWpoUtqV8e7apAvd_vfef6nA21rC1vISpqQuyqrT7yYcH7nuIN253mYd57ouk-hd0QdtephTfl4P9--gcCvfmiQ66wQx9WZkygggxrpIpmcykM-QBC2NgB06h4y-857ZU-bEgKDeH8w0Nzc:1pjiL5:EL4cSerfZNHo6Pt2s-NMsx54GyRgFDk6KFtdD99d3iE', '2023-04-18 15:12:51.814069'),
('84lbm3l3mvuxma9bkx3uzh34ek7w6erl', '.eJxVjDsOwjAQRO_iGlnxf01JnzNYtteLA8iR4qRC3J1ESgFTznszbxbittaw9bKECdmVCXb57VLMz9IOgI_Y7jPPc1uXKfFD4SftfJyxvG6n-3dQY6_72hjS3pJWIlsvnQNLWVnIGkgK0tklBDkoJE1kYIiEYCUokB72JGKfL8iyN08:1pjuCe:9eyFzgm1nlXxY4xxenMRyN3hLZmbL4Ouy--VeL6gcH0', '2023-04-19 03:52:56.514484'),
('e64tpd1ydljt61gnyh9h17urc3lvmdt9', '.eJxVjEsOAiEQBe_C2hAIn0aX7j0D6aZBRg0kw8zKeHdDMgvdvqp6bxFx32rcR17jwuIitDj9boTpmdsE_MB27zL1tq0LyanIgw5565xf18P9O6g46qx9YvJ0ZgAb0AGi0qE4XcgwFqMQcqYE3pA31hIaDgXIGqcZSTkrPl8Lbji0:1ppJrX:4Z-50rZgEXH9sweplbFx-ygFXPv8Sr9p4eZzitfZuG8', '2023-05-04 02:17:31.967039');

-- --------------------------------------------------------

--
-- テーブルの構造 `mybbs_category`
--

CREATE TABLE `mybbs_category` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `mybbs_category`
--

INSERT INTO `mybbs_category` (`id`, `name`) VALUES
(1, 'english'),
(2, 'sports');

-- --------------------------------------------------------

--
-- テーブルの構造 `mybbs_post`
--

CREATE TABLE `mybbs_post` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `content` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `comment_count` bigint(20) NOT NULL,
  `like_count` bigint(20) NOT NULL,
  `public_range` smallint(6) NOT NULL,
  `category_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `mybbs_post`
--

INSERT INTO `mybbs_post` (`id`, `title`, `content`, `created_at`, `updated_at`, `comment_count`, `like_count`, `public_range`, `category_id`) VALUES
(1, 'title-1', 'title-1です', '2023-04-05 14:55:35.454987', '2023-04-05 18:13:02.543902', 0, 0, 1, 2),
(2, '投稿２', '投稿２です', '2023-04-05 16:01:51.540171', '2023-04-05 16:01:51.540191', 0, 0, 1, 1),
(4, 'www', 'wwwwww', '2023-04-05 18:34:58.959344', '2023-04-05 18:34:58.959408', 0, 0, 1, 2);

-- --------------------------------------------------------

--
-- テーブルの構造 `mybbs_post_tag`
--

CREATE TABLE `mybbs_post_tag` (
  `id` bigint(20) NOT NULL,
  `post_id` bigint(20) NOT NULL,
  `tag_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `mybbs_post_tag`
--

INSERT INTO `mybbs_post_tag` (`id`, `post_id`, `tag_id`) VALUES
(3, 1, 1),
(1, 1, 2),
(4, 2, 2),
(5, 4, 1),
(6, 4, 2);

-- --------------------------------------------------------

--
-- テーブルの構造 `mybbs_quiz`
--

CREATE TABLE `mybbs_quiz` (
  `id` bigint(20) NOT NULL,
  `title` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `content` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- テーブルの構造 `mybbs_seiseki`
--

CREATE TABLE `mybbs_seiseki` (
  `id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- テーブルの構造 `mybbs_tag`
--

CREATE TABLE `mybbs_tag` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `mybbs_tag`
--

INSERT INTO `mybbs_tag` (`id`, `name`) VALUES
(1, 'tag1'),
(2, 'tag2');

-- --------------------------------------------------------

--
-- テーブルの構造 `myhaiku_haiku`
--

CREATE TABLE `myhaiku_haiku` (
  `id` bigint(20) NOT NULL,
  `kaminoku` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `nakanoku` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `shimonoku` varchar(64) COLLATE utf8mb4_bin NOT NULL,
  `kami_random` longtext COLLATE utf8mb4_bin NOT NULL,
  `naka_random` longtext COLLATE utf8mb4_bin NOT NULL,
  `shimo_random` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `myhaiku_haiku`
--

INSERT INTO `myhaiku_haiku` (`id`, `kaminoku`, `nakanoku`, `shimonoku`, `kami_random`, `naka_random`, `shimo_random`, `created_at`, `updated_at`) VALUES
(2, 'あああああ', 'あああああ', 'あああああ', 'あ', 'あ', 'あ', '2023-04-07 07:48:35.641943', '2023-04-07 07:48:35.641966');

-- --------------------------------------------------------

--
-- テーブルの構造 `myquiz_genre`
--

CREATE TABLE `myquiz_genre` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `myquiz_genre`
--

INSERT INTO `myquiz_genre` (`id`, `name`, `created_at`, `updated_at`) VALUES
(1, 'english', '2023-04-07 07:56:25.874420', '2023-04-07 07:56:25.874493'),
(2, '計算', '2023-04-20 02:18:09.227208', '2023-04-20 02:18:09.227240'),
(3, '歴史', '2023-04-20 02:18:22.375456', '2023-04-20 02:18:22.375485'),
(4, 'スポーツ', '2023-04-20 02:18:37.336768', '2023-04-20 02:18:37.336855'),
(5, 'サッカー', '2023-04-20 02:18:44.483471', '2023-04-20 02:18:44.483536');

-- --------------------------------------------------------

--
-- テーブルの構造 `myquiz_quiz`
--

CREATE TABLE `myquiz_quiz` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `question` longtext COLLATE utf8mb4_bin NOT NULL,
  `choice_a` longtext COLLATE utf8mb4_bin NOT NULL,
  `choice_b` longtext COLLATE utf8mb4_bin NOT NULL,
  `choice_c` longtext COLLATE utf8mb4_bin NOT NULL,
  `answer` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `genre_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- テーブルのデータのダンプ `myquiz_quiz`
--

INSERT INTO `myquiz_quiz` (`id`, `title`, `question`, `choice_a`, `choice_b`, `choice_c`, `answer`, `created_at`, `updated_at`, `genre_id`) VALUES
(1, 'aa', 'aはどれ？', 'a', 'b', 'c', 'a', '2023-04-07 07:56:36.466788', '2023-04-09 10:13:26.456575', 1),
(4, '猫を英語で。', '猫は英語で？', 'dog', 'cat', 'catコマンド', 'cat', '2023-04-07 08:50:58.846015', '2023-04-07 08:50:58.846047', 1),
(6, '犬を英語で', '犬を英語で答えなさい', 'drag', 'doc', 'dog', 'dog', '2023-04-07 08:58:56.198805', '2023-04-07 08:58:56.198839', 1),
(7, 'サッカー', 'サッカーワールドカップ第一回は1930年に開催された。優勝国はどこ？', 'ブラジル', 'イタリア', 'ウルグアイ', 'ウルグアイ', '2023-04-20 03:01:33.456300', '2023-04-20 03:27:10.619726', 5),
(8, '2022年サッカーワールドカップ', '2022年サッカーワールドカップの開催地はどこ？', 'フランス', 'カタール', 'ダカール', 'カタール', '2023-04-20 03:02:26.710723', '2023-04-20 03:02:26.710748', 5);

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- テーブルのインデックス `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- テーブルのインデックス `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- テーブルのインデックス `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- テーブルのインデックス `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- テーブルのインデックス `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- テーブルのインデックス `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- テーブルのインデックス `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- テーブルのインデックス `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- テーブルのインデックス `mybbs_category`
--
ALTER TABLE `mybbs_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- テーブルのインデックス `mybbs_post`
--
ALTER TABLE `mybbs_post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mybbs_post_category_id_847a3879_fk_mybbs_category_id` (`category_id`);

--
-- テーブルのインデックス `mybbs_post_tag`
--
ALTER TABLE `mybbs_post_tag`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mybbs_post_tag_post_id_tag_id_5d51003c_uniq` (`post_id`,`tag_id`),
  ADD KEY `mybbs_post_tag_tag_id_f35e1bf1_fk_mybbs_tag_id` (`tag_id`);

--
-- テーブルのインデックス `mybbs_quiz`
--
ALTER TABLE `mybbs_quiz`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `mybbs_seiseki`
--
ALTER TABLE `mybbs_seiseki`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `mybbs_tag`
--
ALTER TABLE `mybbs_tag`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- テーブルのインデックス `myhaiku_haiku`
--
ALTER TABLE `myhaiku_haiku`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `myquiz_genre`
--
ALTER TABLE `myquiz_genre`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- テーブルのインデックス `myquiz_quiz`
--
ALTER TABLE `myquiz_quiz`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myquiz_quiz_genre_id_53f41ff3_fk_myquiz_genre_id` (`genre_id`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- テーブルの AUTO_INCREMENT `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- テーブルの AUTO_INCREMENT `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- テーブルの AUTO_INCREMENT `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- テーブルの AUTO_INCREMENT `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- テーブルの AUTO_INCREMENT `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- テーブルの AUTO_INCREMENT `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- テーブルの AUTO_INCREMENT `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- テーブルの AUTO_INCREMENT `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- テーブルの AUTO_INCREMENT `mybbs_category`
--
ALTER TABLE `mybbs_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- テーブルの AUTO_INCREMENT `mybbs_post`
--
ALTER TABLE `mybbs_post`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- テーブルの AUTO_INCREMENT `mybbs_post_tag`
--
ALTER TABLE `mybbs_post_tag`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- テーブルの AUTO_INCREMENT `mybbs_quiz`
--
ALTER TABLE `mybbs_quiz`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- テーブルの AUTO_INCREMENT `mybbs_seiseki`
--
ALTER TABLE `mybbs_seiseki`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- テーブルの AUTO_INCREMENT `mybbs_tag`
--
ALTER TABLE `mybbs_tag`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- テーブルの AUTO_INCREMENT `myhaiku_haiku`
--
ALTER TABLE `myhaiku_haiku`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- テーブルの AUTO_INCREMENT `myquiz_genre`
--
ALTER TABLE `myquiz_genre`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- テーブルの AUTO_INCREMENT `myquiz_quiz`
--
ALTER TABLE `myquiz_quiz`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- ダンプしたテーブルの制約
--

--
-- テーブルの制約 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- テーブルの制約 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- テーブルの制約 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- テーブルの制約 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- テーブルの制約 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- テーブルの制約 `mybbs_post`
--
ALTER TABLE `mybbs_post`
  ADD CONSTRAINT `mybbs_post_category_id_847a3879_fk_mybbs_category_id` FOREIGN KEY (`category_id`) REFERENCES `mybbs_category` (`id`);

--
-- テーブルの制約 `mybbs_post_tag`
--
ALTER TABLE `mybbs_post_tag`
  ADD CONSTRAINT `mybbs_post_tag_post_id_9cdfdce3_fk_mybbs_post_id` FOREIGN KEY (`post_id`) REFERENCES `mybbs_post` (`id`),
  ADD CONSTRAINT `mybbs_post_tag_tag_id_f35e1bf1_fk_mybbs_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `mybbs_tag` (`id`);

--
-- テーブルの制約 `myquiz_quiz`
--
ALTER TABLE `myquiz_quiz`
  ADD CONSTRAINT `myquiz_quiz_genre_id_53f41ff3_fk_myquiz_genre_id` FOREIGN KEY (`genre_id`) REFERENCES `myquiz_genre` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
