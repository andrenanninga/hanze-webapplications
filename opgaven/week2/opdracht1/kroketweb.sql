SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `kroketweb`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE IF NOT EXISTS `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `omschrijving` varchar(72) NOT NULL,
  `voorraad` int(11) NOT NULL,
  `prijs` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=36 ;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `omschrijving`, `voorraad`, `prijs`) VALUES
(1, 'Garnalenkroket ', 18, 1.20),
(2, 'Broodje Garnalenkroket ', 18, 1.80),
(3, 'Kroket', 20, 1.00),
(4, 'Broodje Kroket', 20, 1.80),
(5, 'Goulashkroket', 0, 1.40),
(6, 'Broodje Goulashkroket', 0, 1.80),
(7, 'Portie patat', 3000, 1.50),
(8, 'Portie raspatat', 240, 1.75),
(9, 'Portie bittelballen', 32, 4.00),
(10, 'Coca Cola zero 50cl', 66, 1.65),
(11, 'Coca Cola 50cl', 37, 1.65),
(12, 'Coca Cola light 50cl', 12, 1.65),
(13, 'Pepsi 33cl', 0, 0.95),
(14, 'Pepsi Light 33cl', 0, 0.95),
(15, 'Pepsi Max 50cl', 0, 2.00),
(16, 'Broodje hamburger', 35, 3.00),
(17, 'Broodje hamburger super speciaal', 38, 3.50),
(18, 'Broodje tartaar', 3, 3.00),
(19, 'Broodje warm vlees', 27, 3.90),
(20, 'Tosti ham/kaas', 30, 2.10),
(21, 'Tosti hawaii', 7, 2.40),
(22, 'Wiener Schnitzelschotel', 9, 9.90),
(23, 'Ei salade', 9, 1.90),
(24, 'Spa rood 50cl', 55, 1.65),
(25, 'Spa blauw 50cl', 0, 1.65),
(26, 'Portie mayonaise', 366, 0.50),
(27, 'Portie speciaal', 38, 0.75),
(28, 'Portie joppie', 90, 0.50),
(29, 'Portie satesaus', 36, 0.80),
(30, 'Portie oorlog', 44, 1.00),
(31, 'Fanta 50cl', 80, 1.90),
(32, '7Up 50cl', 34, 1.80),
(33, 'Snickers', 45, 0.60),
(34, 'Mars', 45, 0.60),
(35, 'Bounty', 45, 0.55);
