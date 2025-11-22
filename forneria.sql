-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 22-11-2025 a las 01:00:24
-- Versión del servidor: 9.1.0
-- Versión de PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `forneria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alertas`
--

DROP TABLE IF EXISTS `alertas`;
CREATE TABLE IF NOT EXISTS `alertas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_alerta` enum('verde','amarilla','roja') CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `mensaje` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_generada` timestamp NULL DEFAULT NULL,
  `estado` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `productos_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_alertas_productos1_idx` (`productos_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=145 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
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
(25, 'Can add alertas', 8, 'add_alertas'),
(26, 'Can change alertas', 8, 'change_alertas'),
(27, 'Can delete alertas', 8, 'delete_alertas'),
(28, 'Can view alertas', 8, 'view_alertas'),
(29, 'Can add auth group', 9, 'add_authgroup'),
(30, 'Can change auth group', 9, 'change_authgroup'),
(31, 'Can delete auth group', 9, 'delete_authgroup'),
(32, 'Can view auth group', 9, 'view_authgroup'),
(33, 'Can add auth group permissions', 10, 'add_authgrouppermissions'),
(34, 'Can change auth group permissions', 10, 'change_authgrouppermissions'),
(35, 'Can delete auth group permissions', 10, 'delete_authgrouppermissions'),
(36, 'Can view auth group permissions', 10, 'view_authgrouppermissions'),
(37, 'Can add auth permission', 11, 'add_authpermission'),
(38, 'Can change auth permission', 11, 'change_authpermission'),
(39, 'Can delete auth permission', 11, 'delete_authpermission'),
(40, 'Can view auth permission', 11, 'view_authpermission'),
(41, 'Can add auth user', 12, 'add_authuser'),
(42, 'Can change auth user', 12, 'change_authuser'),
(43, 'Can delete auth user', 12, 'delete_authuser'),
(44, 'Can view auth user', 12, 'view_authuser'),
(45, 'Can add auth user groups', 13, 'add_authusergroups'),
(46, 'Can change auth user groups', 13, 'change_authusergroups'),
(47, 'Can delete auth user groups', 13, 'delete_authusergroups'),
(48, 'Can view auth user groups', 13, 'view_authusergroups'),
(49, 'Can add auth user user permissions', 14, 'add_authuseruserpermissions'),
(50, 'Can change auth user user permissions', 14, 'change_authuseruserpermissions'),
(51, 'Can delete auth user user permissions', 14, 'delete_authuseruserpermissions'),
(52, 'Can view auth user user permissions', 14, 'view_authuseruserpermissions'),
(53, 'Can add cargo', 7, 'add_cargo'),
(54, 'Can change cargo', 7, 'change_cargo'),
(55, 'Can delete cargo', 7, 'delete_cargo'),
(56, 'Can view cargo', 7, 'view_cargo'),
(57, 'Can add categorias', 15, 'add_categorias'),
(58, 'Can change categorias', 15, 'change_categorias'),
(59, 'Can delete categorias', 15, 'delete_categorias'),
(60, 'Can view categorias', 15, 'view_categorias'),
(61, 'Can add clientes', 16, 'add_clientes'),
(62, 'Can change clientes', 16, 'change_clientes'),
(63, 'Can delete clientes', 16, 'delete_clientes'),
(64, 'Can view clientes', 16, 'view_clientes'),
(65, 'Can add cuenta bancaria', 17, 'add_cuentabancaria'),
(66, 'Can change cuenta bancaria', 17, 'change_cuentabancaria'),
(67, 'Can delete cuenta bancaria', 17, 'delete_cuentabancaria'),
(68, 'Can view cuenta bancaria', 17, 'view_cuentabancaria'),
(69, 'Can add departamento', 18, 'add_departamento'),
(70, 'Can change departamento', 18, 'change_departamento'),
(71, 'Can delete departamento', 18, 'delete_departamento'),
(72, 'Can view departamento', 18, 'view_departamento'),
(73, 'Can add detalle venta', 19, 'add_detalleventa'),
(74, 'Can change detalle venta', 19, 'change_detalleventa'),
(75, 'Can delete detalle venta', 19, 'delete_detalleventa'),
(76, 'Can view detalle venta', 19, 'view_detalleventa'),
(77, 'Can add direccion', 20, 'add_direccion'),
(78, 'Can change direccion', 20, 'change_direccion'),
(79, 'Can delete direccion', 20, 'delete_direccion'),
(80, 'Can view direccion', 20, 'view_direccion'),
(81, 'Can add django admin log', 21, 'add_djangoadminlog'),
(82, 'Can change django admin log', 21, 'change_djangoadminlog'),
(83, 'Can delete django admin log', 21, 'delete_djangoadminlog'),
(84, 'Can view django admin log', 21, 'view_djangoadminlog'),
(85, 'Can add django content type', 22, 'add_djangocontenttype'),
(86, 'Can change django content type', 22, 'change_djangocontenttype'),
(87, 'Can delete django content type', 22, 'delete_djangocontenttype'),
(88, 'Can view django content type', 22, 'view_djangocontenttype'),
(89, 'Can add django migrations', 23, 'add_djangomigrations'),
(90, 'Can change django migrations', 23, 'change_djangomigrations'),
(91, 'Can delete django migrations', 23, 'delete_djangomigrations'),
(92, 'Can view django migrations', 23, 'view_djangomigrations'),
(93, 'Can add django session', 24, 'add_djangosession'),
(94, 'Can change django session', 24, 'change_djangosession'),
(95, 'Can delete django session', 24, 'delete_djangosession'),
(96, 'Can view django session', 24, 'view_djangosession'),
(97, 'Can add forma pago', 25, 'add_formapago'),
(98, 'Can change forma pago', 25, 'change_formapago'),
(99, 'Can delete forma pago', 25, 'delete_formapago'),
(100, 'Can view forma pago', 25, 'view_formapago'),
(101, 'Can add jornada', 26, 'add_jornada'),
(102, 'Can change jornada', 26, 'change_jornada'),
(103, 'Can delete jornada', 26, 'delete_jornada'),
(104, 'Can view jornada', 26, 'view_jornada'),
(105, 'Can add movimientos inventario', 27, 'add_movimientosinventario'),
(106, 'Can change movimientos inventario', 27, 'change_movimientosinventario'),
(107, 'Can delete movimientos inventario', 27, 'delete_movimientosinventario'),
(108, 'Can view movimientos inventario', 27, 'view_movimientosinventario'),
(109, 'Can add nutricional', 28, 'add_nutricional'),
(110, 'Can change nutricional', 28, 'change_nutricional'),
(111, 'Can delete nutricional', 28, 'delete_nutricional'),
(112, 'Can view nutricional', 28, 'view_nutricional'),
(113, 'Can add pago', 29, 'add_pago'),
(114, 'Can change pago', 29, 'change_pago'),
(115, 'Can delete pago', 29, 'delete_pago'),
(116, 'Can view pago', 29, 'view_pago'),
(117, 'Can add productos', 30, 'add_productos'),
(118, 'Can change productos', 30, 'change_productos'),
(119, 'Can delete productos', 30, 'delete_productos'),
(120, 'Can view productos', 30, 'view_productos'),
(121, 'Can add turno', 31, 'add_turno'),
(122, 'Can change turno', 31, 'change_turno'),
(123, 'Can delete turno', 31, 'delete_turno'),
(124, 'Can view turno', 31, 'view_turno'),
(125, 'Can add turno has jornada', 32, 'add_turnohasjornada'),
(126, 'Can change turno has jornada', 32, 'change_turnohasjornada'),
(127, 'Can delete turno has jornada', 32, 'delete_turnohasjornada'),
(128, 'Can view turno has jornada', 32, 'view_turnohasjornada'),
(129, 'Can add ventas', 33, 'add_ventas'),
(130, 'Can change ventas', 33, 'change_ventas'),
(131, 'Can delete ventas', 33, 'delete_ventas'),
(132, 'Can view ventas', 33, 'view_ventas'),
(133, 'Can add empleado', 34, 'add_empleado'),
(134, 'Can change empleado', 34, 'change_empleado'),
(135, 'Can delete empleado', 34, 'delete_empleado'),
(136, 'Can view empleado', 34, 'view_empleado'),
(137, 'Can add liquidacion', 35, 'add_liquidacion'),
(138, 'Can change liquidacion', 35, 'change_liquidacion'),
(139, 'Can delete liquidacion', 35, 'delete_liquidacion'),
(140, 'Can view liquidacion', 35, 'view_liquidacion'),
(141, 'Can add contrato', 36, 'add_contrato'),
(142, 'Can change contrato', 36, 'change_contrato'),
(143, 'Can delete contrato', 36, 'delete_contrato'),
(144, 'Can view contrato', 36, 'view_contrato');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `visible` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `visible`) VALUES
(7, 'pbkdf2_sha256$1000000$XY9fj3qPiS8njlqs3Qsch4$jZVX9RnGHmh+T00l4NzFf5orMo0o9PDSaSijpX5MEtM=', NULL, 0, 'PruebaE', 'Fue', 'Exitosa', 'prueba@dos.cl', 0, 1, '2025-11-03 17:16:05.900293', 1),
(8, 'pbkdf2_sha256$1000000$3so01Xd6QVZwkGtexmUUKa$Abz9N8FXjyf86G/588X9bEDqe6Jasu+ycRz8376CK5k=', '2025-11-22 00:09:00.125059', 1, 'Dito', 'Dito', 'Plz', 'dito@dominio.cl', 0, 1, '2025-11-03 17:43:27.541306', 1),
(11, 'pbkdf2_sha256$1000000$NmjOMZL5u4Q9IVIBFcmYO7$amBLi2vK0JbIJFTsyNMxwpwIPYk8GdIecDQW553XyHs=', NULL, 0, 'Pepino', 'Pepe Carlos', 'Cazuela Pollo', 'miau@miau.cl', 0, 0, '2025-11-21 23:41:47.005190', 0),
(12, 'pbkdf2_sha256$1000000$7AU8L2WrPoXQ45sfLc1Jsy$0EaskGCmRP4KEW/99Jz4ynA0e0XNim2KAQvLL5QBe5Y=', NULL, 0, 'Testi', 'Testeo Testin', 'Fuentes García', 'testeo@dominio.com', 0, 1, '2025-11-22 00:09:30.639569', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo`
--

DROP TABLE IF EXISTS `cargo`;
CREATE TABLE IF NOT EXISTS `cargo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `visible` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `cargo`
--

INSERT INTO `cargo` (`id`, `nombre`, `descripcion`, `visible`) VALUES
(2, 'Prueba1', 'Esta es la primera prueba para cargojhg', 1),
(3, 'Prueba2', 'Esta es para probar nombre rep', 1),
(5, 'cargo1', 'prueba de caargooo1223.$#', 1),
(6, 'Cargo Final', 'Este cargo demuestra que corre', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

DROP TABLE IF EXISTS `categorias`;
CREATE TABLE IF NOT EXISTS `categorias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rut` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `nombre` varchar(150) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `correo` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contrato`
--

DROP TABLE IF EXISTS `contrato`;
CREATE TABLE IF NOT EXISTS `contrato` (
  `id` int NOT NULL AUTO_INCREMENT,
  `detalle_contrato` varchar(45) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `empleado_id` int NOT NULL,
  `cargo_id` int NOT NULL,
  `departamento_id` int NOT NULL,
  `turno_has_jornada_id` int NOT NULL,
  `sueldo_base` int NOT NULL DEFAULT '0',
  `visible` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_contrato_empleado1_idx` (`empleado_id`),
  KEY `fk_contrato_cargo1_idx` (`cargo_id`),
  KEY `fk_contrato_departamento1_idx` (`departamento_id`),
  KEY `fk_contrato_turno_has_jornada1_idx` (`turno_has_jornada_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `contrato`
--

INSERT INTO `contrato` (`id`, `detalle_contrato`, `fecha_inicio`, `fecha_fin`, `empleado_id`, `cargo_id`, `departamento_id`, `turno_has_jornada_id`, `sueldo_base`, `visible`) VALUES
(4, 'reponedor', '2025-11-04', '2026-01-29', 4, 3, 2, 4, 600000, 1),
(5, 'reponedor', '2025-10-08', '2026-03-18', 8, 5, 4, 5, 450000, 1),
(6, 'cajero', '2025-10-16', '2026-06-25', 1, 2, 1, 1, 350000, 1),
(7, 'cajero', '2025-10-16', '2026-06-25', 1, 2, 1, 1, 350000, 1),
(8, 'cajero', '2025-09-04', '2026-01-23', 5, 5, 3, 4, 500000, 1),
(9, 'director', '2025-10-30', '2025-12-05', 9, 3, 1, 3, 500000, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta_bancaria`
--

DROP TABLE IF EXISTS `cuenta_bancaria`;
CREATE TABLE IF NOT EXISTS `cuenta_bancaria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `banco` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `tipo_cuenta` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `numero_cuenta` int NOT NULL,
  `correo` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `empleado_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_cuenta_bancaria_empleado1_idx` (`empleado_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

DROP TABLE IF EXISTS `departamento`;
CREATE TABLE IF NOT EXISTS `departamento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Marketing', 'Departamento encargado de la promoción, publi'),
(2, 'Recursos Humanos', 'Departamento encargado de la gestión del pers'),
(3, 'Contabilidad', 'Departamento encargado de la gestión financie'),
(4, 'Logística', 'Departamento encargado de la distribución, in'),
(5, 'Ventas', 'Departamento responsable de la comercializaci');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_venta`
--

DROP TABLE IF EXISTS `detalle_venta`;
CREATE TABLE IF NOT EXISTS `detalle_venta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `descuento_pct` decimal(5,2) DEFAULT NULL,
  `ventas_id` int NOT NULL,
  `productos_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_detalle_venta_ventas1_idx` (`ventas_id`),
  KEY `fk_detalle_venta_productos1_idx` (`productos_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `direccion`
--

DROP TABLE IF EXISTS `direccion`;
CREATE TABLE IF NOT EXISTS `direccion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `calle` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `numero` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `depto` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `comuna` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `region` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `codigo_postal` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `direccion`
--

INSERT INTO `direccion` (`id`, `calle`, `numero`, `depto`, `comuna`, `region`, `codigo_postal`) VALUES
(1, 'Callecita', '123', NULL, 'Coquimbo', 'Juas', 12315),
(2, 'Calle', 'ada', NULL, 'asdad', 'X - Los Lagos', 12313),
(3, 'Calle', 'ada', NULL, 'asdad', 'X - Los Lagos', 12313),
(4, 'asdsad', 'asdasda', NULL, 'asdasa', 'IX - La Araucanía', NULL),
(5, 'asd', 'asd', NULL, 'asd', 'X - Los Lagos', NULL),
(6, 'asd', 'asd', NULL, 'asd', 'IX - La Araucanía', 3),
(7, 'asd', 'asd', NULL, 'asd', 'VIII - Biobío', NULL),
(8, '1231', '1231', '3123', '1321', 'IV - Coquimbo', 1231231);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci,
  `object_repr` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'rrhh', 'cargo'),
(8, 'rrhh', 'alertas'),
(9, 'rrhh', 'authgroup'),
(10, 'rrhh', 'authgrouppermissions'),
(11, 'rrhh', 'authpermission'),
(12, 'rrhh', 'authuser'),
(13, 'rrhh', 'authusergroups'),
(14, 'rrhh', 'authuseruserpermissions'),
(15, 'rrhh', 'categorias'),
(16, 'rrhh', 'clientes'),
(17, 'rrhh', 'cuentabancaria'),
(18, 'rrhh', 'departamento'),
(19, 'rrhh', 'detalleventa'),
(20, 'rrhh', 'direccion'),
(21, 'rrhh', 'djangoadminlog'),
(22, 'rrhh', 'djangocontenttype'),
(23, 'rrhh', 'djangomigrations'),
(24, 'rrhh', 'djangosession'),
(25, 'rrhh', 'formapago'),
(26, 'rrhh', 'jornada'),
(27, 'rrhh', 'movimientosinventario'),
(28, 'rrhh', 'nutricional'),
(29, 'rrhh', 'pago'),
(30, 'rrhh', 'productos'),
(31, 'rrhh', 'turno'),
(32, 'rrhh', 'turnohasjornada'),
(33, 'rrhh', 'ventas'),
(34, 'rrhh', 'empleado'),
(35, 'rrhh', 'liquidacion'),
(36, 'rrhh', 'contrato');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-10-24 19:55:39.865852'),
(2, 'auth', '0001_initial', '2025-10-24 19:55:40.322519'),
(3, 'admin', '0001_initial', '2025-10-24 19:55:40.456943'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-10-24 19:55:40.461072'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-10-24 19:55:40.465074'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-10-24 19:55:40.515813'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-10-24 19:55:40.549521'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-10-24 19:55:40.574508'),
(9, 'auth', '0004_alter_user_username_opts', '2025-10-24 19:55:40.578087'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-10-24 19:55:40.604555'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-10-24 19:55:40.605130'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-10-24 19:55:40.608840'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-10-24 19:55:40.636469'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-10-24 19:55:40.660491'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-10-24 19:55:40.691652'),
(16, 'auth', '0011_update_proxy_permissions', '2025-10-24 19:55:40.695683'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-10-24 19:55:40.722406'),
(18, 'sessions', '0001_initial', '2025-10-24 19:55:40.752836'),
(19, 'rrhh', '0001_initial', '2025-11-17 20:58:10.125474');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('hhmt8palhohwq6fho40rxi25agbq7h0u', '.eJxVjMsOwiAQRf-FtSFAh5dL934DGWCQqoGktCvjv2uTLnR7zzn3xQJuaw3boCXMmZ2ZY6ffLWJ6UNtBvmO7dZ56W5c58l3hBx382jM9L4f7d1Bx1G8NRRuUWpNxYBK6CYTXk3ORIggBpVhJNluZjDDKAilUQnpftDOZRJHs_QHDBzb1:1vG1s7:cLd3t0nlXqlln0QNTEpT3fVyici8PlnTNySWRPXGv_U', '2025-11-17 21:13:51.940392'),
('xa1lguileam721p0s1szhppe34lnv042', '.eJxVjMsOwiAQRf-FtSFAh5dL934DGWCQqoGktCvjv2uTLnR7zzn3xQJuaw3boCXMmZ2ZY6ffLWJ6UNtBvmO7dZ56W5c58l3hBx382jM9L4f7d1Bx1G8NRRuUWpNxYBK6CYTXk3ORIggBpVhJNluZjDDKAilUQnpftDOZRJHs_QHDBzb1:1vGWId:8X33BCp95mfng8M538I54Ggdl4S9Fu9PfqJCpq1TfWE', '2025-11-19 05:43:15.704367'),
('54hzklg5xldpzth9dme6u73t7f6nh84d', '.eJxVjMsOwiAQRf-FtSFAh5dL934DGWCQqoGktCvjv2uTLnR7zzn3xQJuaw3boCXMmZ2ZY6ffLWJ6UNtBvmO7dZ56W5c58l3hBx382jM9L4f7d1Bx1G8NRRuUWpNxYBK6CYTXk3ORIggBpVhJNluZjDDKAilUQnpftDOZRJHs_QHDBzb1:1vKcdW:z-Gd3pbBhddj6EPhPcknJnidXIBdZVNz_vc_hCVuLY0', '2025-11-30 13:17:46.580590'),
('vsnohs2p9j5s9uhciw5eoq6pdelwyzch', '.eJxVjMsOwiAQRf-FtSFAh5dL934DGWCQqoGktCvjv2uTLnR7zzn3xQJuaw3boCXMmZ2ZY6ffLWJ6UNtBvmO7dZ56W5c58l3hBx382jM9L4f7d1Bx1G8NRRuUWpNxYBK6CYTXk3ORIggBpVhJNluZjDDKAilUQnpftDOZRJHs_QHDBzb1:1vL71S:GcKX5vkFMrRHhHufja9PREZLBcTc91r08RHk14lZrmo', '2025-12-01 21:44:30.083657'),
('md0utqg8sdw7igs7e7myog1hg8d1ib76', '.eJxVjMsOwiAQRf-FtSFAh5dL934DGWCQqoGktCvjv2uTLnR7zzn3xQJuaw3boCXMmZ2ZY6ffLWJ6UNtBvmO7dZ56W5c58l3hBx382jM9L4f7d1Bx1G8NRRuUWpNxYBK6CYTXk3ORIggBpVhJNluZjDDKAilUQnpftDOZRJHs_QHDBzb1:1vL7A6:0PbZ3Qrf6GUt3rCbM57cRYGHayj27Oe3ortXDEQhLxI', '2025-12-01 21:53:26.568971'),
('rq472rnphh88vi7sjg2lpsgr6oaz0gn6', '.eJxVjMsOwiAQRf-FtSFAh5dL934DGWCQqoGktCvjv2uTLnR7zzn3xQJuaw3boCXMmZ2ZY6ffLWJ6UNtBvmO7dZ56W5c58l3hBx382jM9L4f7d1Bx1G8NRRuUWpNxYBK6CYTXk3ORIggBpVhJNluZjDDKAilUQnpftDOZRJHs_QHDBzb1:1vMWoG:_BGMqMJQPWMqGVqrDoB7D2RZetBVAC7hOz7YwxdtW1k', '2025-12-05 19:28:44.943719'),
('pqiw6aizxmgfifjcz9gt68nje9uxnina', '.eJxVjMsOwiAQRf-FtSFAh5dL934DGWCQqoGktCvjv2uTLnR7zzn3xQJuaw3boCXMmZ2ZY6ffLWJ6UNtBvmO7dZ56W5c58l3hBx382jM9L4f7d1Bx1G8NRRuUWpNxYBK6CYTXk3ORIggBpVhJNluZjDDKAilUQnpftDOZRJHs_QHDBzb1:1vMbBU:yfzCM9qp6xy7qnzWdiJy1kk6M7ZA2IvjjpO87WwJolg', '2025-12-06 00:09:00.130215');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

DROP TABLE IF EXISTS `empleado`;
CREATE TABLE IF NOT EXISTS `empleado` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) NOT NULL,
  `A_paterno` varchar(45) NOT NULL,
  `A_materno` varchar(45) NOT NULL,
  `run` varchar(45) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `fono` varchar(100) NOT NULL,
  `id_direccion` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `visible` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `run_UNIQUE` (`run`),
  UNIQUE KEY `fono_UNIQUE` (`fono`),
  UNIQUE KEY `fk_id_direccion` (`id_direccion`) USING BTREE,
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id`, `nombres`, `A_paterno`, `A_materno`, `run`, `correo`, `fono`, `id_direccion`, `user_id`, `visible`) VALUES
(1, 'Testeo Testin', 'Fuentes', 'García', '20767882-1', 'testeo@dominio.com', '12345678', 0, 12, 1),
(3, 'Pepe Carlos', 'Cazuela', 'Pollo', 'sdadas', 'miau@miau.cl', 'adasda', 2, 11, 1),
(4, 'Pepe Carlos', 'Cazuela', 'Pollo', 'a', 'miau@miau.cl', 'a', 3, NULL, 1),
(5, 'Prueba', 'Uno', 'One', 'asdasda', 'miau@miau.com', 'asdsada', 4, NULL, 1),
(6, 'asd', 'asd', 'sad', 'asd', 'asd@sa.com', 'asd', 5, NULL, 1),
(7, 'asd', 'ads', 'asd', '123123123', 'asd@faadsd.cl', 'asdasd', 6, NULL, 1),
(8, 'editado', 'asd', 'asd', '1111111-4', 'asd@sdfs.cl', 'sdas', 7, NULL, 1),
(9, '123', '2123', '31232', '21990927-6', 'qewqweasd@asd.com', '123124124', 8, NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `forma_pago`
--

DROP TABLE IF EXISTS `forma_pago`;
CREATE TABLE IF NOT EXISTS `forma_pago` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `pago_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_forma_pago_pago1_idx` (`pago_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jornada`
--

DROP TABLE IF EXISTS `jornada`;
CREATE TABLE IF NOT EXISTS `jornada` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `horas_semanales` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `jornada`
--

INSERT INTO `jornada` (`id`, `nombre`, `horas_semanales`) VALUES
(1, 'Jornada Completa', 45),
(2, 'Fin de semana', 20),
(3, 'Part Time', 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `liquidacion`
--

DROP TABLE IF EXISTS `liquidacion`;
CREATE TABLE IF NOT EXISTS `liquidacion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `periodo` date NOT NULL,
  `imponible` int NOT NULL,
  `no_imponible` int NOT NULL,
  `tributable` int NOT NULL,
  `descuentos` int NOT NULL,
  `bruto` int NOT NULL,
  `liquido` int NOT NULL,
  `fecha_cierre` date NOT NULL,
  `estado` varchar(45) NOT NULL,
  `contrato_id` int NOT NULL,
  `empleado_id` int DEFAULT NULL,
  `visible` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_liquidacion_contrato1_idx` (`contrato_id`),
  KEY `liquidacion_empleado_fk` (`empleado_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `liquidacion`
--

INSERT INTO `liquidacion` (`id`, `periodo`, `imponible`, `no_imponible`, `tributable`, `descuentos`, `bruto`, `liquido`, `fecha_cierre`, `estado`, `contrato_id`, `empleado_id`, `visible`) VALUES
(2, '2025-10-30', 325323, 23526, 23523, 25352, 5235299, 23523, '2025-11-28', 'activo', 6, 1, 1),
(3, '2025-10-12', 53453, 34534, 34534, 34534, 12312, 12315, '2025-11-12', 'activo', 6, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimientos_inventario`
--

DROP TABLE IF EXISTS `movimientos_inventario`;
CREATE TABLE IF NOT EXISTS `movimientos_inventario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_movimiento` enum('entrada','salida') CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `cantidad` int NOT NULL,
  `fecha` timestamp NOT NULL,
  `productos_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_movimientos_inventario_productos1_idx` (`productos_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nutricional`
--

DROP TABLE IF EXISTS `nutricional`;
CREATE TABLE IF NOT EXISTS `nutricional` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ingredientes` varchar(300) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `tiempo_preparacion` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `proteinas` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `azucar` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `gluten` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pago`
--

DROP TABLE IF EXISTS `pago`;
CREATE TABLE IF NOT EXISTS `pago` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha_pago` date NOT NULL,
  `monto` int NOT NULL,
  `comprobante` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `estado` varchar(45) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `liquidacion_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pago_liquidacion1_idx` (`liquidacion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

DROP TABLE IF EXISTS `productos`;
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` varchar(300) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `marca` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `precio` int DEFAULT NULL,
  `caducidad` date NOT NULL,
  `elaboracion` date DEFAULT NULL,
  `tipo` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL COMMENT 'Corresponde al tipo de elaboración, por ejemplo propia o envasado.',
  `Categorias_id` int NOT NULL,
  `stock_actual` int DEFAULT NULL,
  `stock_minimo` int DEFAULT NULL,
  `stock_maximo` int DEFAULT NULL,
  `presentacion` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL COMMENT 'Unidad con la que se almacena el producto',
  `formato` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL COMMENT 'Cantidad de unidades o detalle por presentación',
  `Nutricional_id` int NOT NULL,
  `creado` timestamp NULL DEFAULT NULL,
  `modificado` timestamp NULL DEFAULT NULL,
  `eliminado` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Productos_Categorias_idx` (`Categorias_id`),
  KEY `fk_Productos_Nutricional1_idx` (`Nutricional_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turno`
--

DROP TABLE IF EXISTS `turno`;
CREATE TABLE IF NOT EXISTS `turno` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hora_entrada` time NOT NULL,
  `hora_salida` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `turno`
--

INSERT INTO `turno` (`id`, `hora_entrada`, `hora_salida`) VALUES
(1, '00:08:00', '00:16:00'),
(2, '00:09:00', '00:17:00'),
(3, '00:10:00', '00:18:00'),
(4, '00:12:00', '00:20:00'),
(5, '00:14:00', '00:22:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turno_has_jornada`
--

DROP TABLE IF EXISTS `turno_has_jornada`;
CREATE TABLE IF NOT EXISTS `turno_has_jornada` (
  `turno_id` int NOT NULL,
  `jornada_id` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `Descripcion` varchar(45) CHARACTER SET utf16 COLLATE utf16_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_turno_has_jornada_jornada1_idx` (`jornada_id`),
  KEY `fk_turno_has_jornada_turno1_idx` (`turno_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `turno_has_jornada`
--

INSERT INTO `turno_has_jornada` (`turno_id`, `jornada_id`, `id`, `Descripcion`) VALUES
(1, 1, 1, 'Turno Mañana - Jornada Completa (45 hrs)'),
(1, 2, 2, 'Turno Mañana - Fin de Semana (20 hrs)'),
(1, 3, 3, 'Turno Mañana - Part Time (30 hrs)'),
(2, 1, 4, 'Turno Tarde - Jornada Completa (45 hrs)'),
(2, 2, 5, 'Turno Tarde - Fin de Semana (20 hrs)'),
(2, 3, 6, 'Turno Tarde - Part Time (30 hrs)'),
(3, 1, 7, 'Turno Noche - Jornada Completa (45 hrs)'),
(3, 2, 8, 'Turno Noche - Fin de Semana (20 hrs)'),
(3, 3, 9, 'Turno Noche - Part Time (30 hrs)');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

DROP TABLE IF EXISTS `ventas`;
CREATE TABLE IF NOT EXISTS `ventas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha` timestamp NOT NULL,
  `total_sin_iva` decimal(10,2) NOT NULL,
  `total_iva` decimal(10,2) NOT NULL,
  `descuento` decimal(10,2) NOT NULL,
  `total_con_iva` decimal(10,2) NOT NULL,
  `canal_venta` enum('presencial','delivery') CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `folio` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `monto_pagado` decimal(10,2) DEFAULT NULL,
  `vuelto` decimal(10,2) DEFAULT NULL,
  `clientes_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ventas_clientes1_idx` (`clientes_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alertas`
--
ALTER TABLE `alertas`
  ADD CONSTRAINT `fk_alertas_productos1` FOREIGN KEY (`productos_id`) REFERENCES `productos` (`id`);

--
-- Filtros para la tabla `contrato`
--
ALTER TABLE `contrato`
  ADD CONSTRAINT `fk_contrato_cargo1` FOREIGN KEY (`cargo_id`) REFERENCES `cargo` (`id`),
  ADD CONSTRAINT `fk_contrato_departamento1` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`id`),
  ADD CONSTRAINT `fk_contrato_empleado1` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`id`),
  ADD CONSTRAINT `fk_contrato_turno_has_jornada1` FOREIGN KEY (`turno_has_jornada_id`) REFERENCES `turno_has_jornada` (`id`);

--
-- Filtros para la tabla `cuenta_bancaria`
--
ALTER TABLE `cuenta_bancaria`
  ADD CONSTRAINT `fk_cuenta_bancaria_empleado1` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`id`);

--
-- Filtros para la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD CONSTRAINT `fk_detalle_venta_productos1` FOREIGN KEY (`productos_id`) REFERENCES `productos` (`id`),
  ADD CONSTRAINT `fk_detalle_venta_ventas1` FOREIGN KEY (`ventas_id`) REFERENCES `ventas` (`id`);

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `fk_empleado_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE SET NULL;

--
-- Filtros para la tabla `forma_pago`
--
ALTER TABLE `forma_pago`
  ADD CONSTRAINT `fk_forma_pago_pago1` FOREIGN KEY (`pago_id`) REFERENCES `pago` (`id`);

--
-- Filtros para la tabla `liquidacion`
--
ALTER TABLE `liquidacion`
  ADD CONSTRAINT `liquidacion_empleado_fk` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`id`);

--
-- Filtros para la tabla `movimientos_inventario`
--
ALTER TABLE `movimientos_inventario`
  ADD CONSTRAINT `fk_movimientos_inventario_productos1` FOREIGN KEY (`productos_id`) REFERENCES `productos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
