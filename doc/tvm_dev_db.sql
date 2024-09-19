-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 19 sep. 2024 à 22:36
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `tvm_dev_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

CREATE TABLE `admin` (
  `full_name` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Structure de la table `bike`
--

CREATE TABLE `bike` (
  `id` varchar(60) NOT NULL,
  `name_bike` varchar(128) NOT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `engine` varchar(128) NOT NULL,
  `batteries` varchar(128) NOT NULL,
  `amperes` varchar(128) NOT NULL,
  `temps_charger` varchar(128) NOT NULL,
  `speed_max` varchar(128) NOT NULL,
  `autonomic` varchar(128) NOT NULL,
  `detail` varchar(256) NOT NULL,
  `reserved` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `bike`
--

INSERT INTO `bike` (`id`, `name_bike`, `image_path`, `engine`, `batteries`, `amperes`, `temps_charger`, `speed_max`, `autonomic`, `detail`, `reserved`) VALUES
('189919a5-4bc7-4a21-af91-99bf292c7135', 'Vélo électrique Sloggy', 'velo-electrique-Sloggy.jpg', '350W', 'lithium 36V 15Ah', 'test', '5 heures', '40km', 'Longue Durée', 'test', 0),
('59b213a8-da69-4258-8b9c-f6726fb0f784', 'Vélo électrique Orca', 'velo-electrique-Orca.jpg', '350W', 'lithium 36V 15Ah', 'test', '5 heures', '40km', 'Longue Durée', 'test', 0),
('67eb95de-577b-43db-9cde-4787367a9d0b', 'Vélo électrique Mahi Mahi LMTDR 13L', 'Velo-electrique-enfants-Mahi-Mahi.jpg', '350W', 'lithium 36V 15Ah', 'test', '5 heures', '40km', 'Longue Durée', 'test', 0),
('f64bbcaa-fbdd-4858-94f2-8be0a4db9ad3', 'Vélo électrique KuKirin V3', 'v3-1.png', '350W', 'lithium 36V 15Ah', 'test', '5 heures', '40km', 'Longue Durée', 'test', 0);

-- --------------------------------------------------------

--
-- Structure de la table `customer`
--

CREATE TABLE `customer` (
  `id` varchar(60) NOT NULL,
  `email` varchar(50) NOT NULL,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `num_tel` varchar(60) NOT NULL,
  `cin` varchar(60) NOT NULL,
  `address` varchar(128) NOT NULL,
  `city` varchar(60) NOT NULL,
  `gender` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `customer`
--

INSERT INTO `customer` (`id`, `email`, `first_name`, `last_name`, `num_tel`, `cin`, `address`, `city`, `gender`) VALUES
('05f34609-5967-4f10-8bb3-cc5a5141e59e', 'amine@info.com', 'amine', 'test', '0632567658', 'LL7981', 'Rabat', 'Rabat', 'Male'),
('2e91ca67-cc32-4a22-bdbb-70a993cb96fb', 'achraf_test@info.com', 'achraf', 'test', '0632567589', 'FH55985', 'Rabat', 'Rabat', 'Male'),
('74d0e712-a5cf-406d-a5db-044f61c5e998', 'achraf_test@info.com', 'achraf', 'test', '0632567589', 'FH55985', 'Rabat', 'Rabat', 'Male'),
('a09a628c-52bf-4620-b967-71d018b9f5bd', 'achraf@info.com', 'achraf', 'test', '0632567589', 'FH55985', 'Rabat', 'Rabat', 'Male'),
('dcb271b4-637c-4756-8288-eb68c28cd5e8', 'achraf_test@info.com', 'achraf', 'test', '0632567589', 'FH55985', 'Rabat', 'Rabat', 'Male');

-- --------------------------------------------------------

--
-- Structure de la table `machine`
--

CREATE TABLE `machine` (
  `model` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `machine`
--

INSERT INTO `machine` (`model`, `type`, `id`, `created_at`, `updated_at`) VALUES
('Sloggy', 'bike', '189919a5-4bc7-4a21-af91-99bf292c7135', '2024-09-18 21:44:58', '2024-09-18 21:44:58'),
('Luqi 2.0', 'scooter', '312beabc-4c38-40ef-a8d9-386167eb9f73', '2024-09-18 21:44:57', '2024-09-18 21:44:57'),
('E125S', 'scooter', '4c8928bd-bce8-4052-964b-8ede18fef18e', '2024-09-18 21:44:58', '2024-09-18 21:44:58'),
('Orca', 'bike', '59b213a8-da69-4258-8b9c-f6726fb0f784', '2024-09-18 21:44:59', '2024-09-18 21:44:59'),
('Mahi LMTDR 13L', 'bike', '67eb95de-577b-43db-9cde-4787367a9d0b', '2024-09-18 21:44:58', '2024-09-18 21:44:58'),
('Luqi 3.0', 'scooter', '6b9741a0-6fd3-47b6-9640-560cd7c06b97', '2024-09-18 21:44:58', '2024-09-18 21:44:58'),
('Luqi Q3', 'scooter', '8c900b54-4c33-4d16-9fa4-f50e0e1d4972', '2024-09-18 21:44:57', '2024-09-18 21:44:57'),
('KuKirin V3', 'bike', 'f64bbcaa-fbdd-4858-94f2-8be0a4db9ad3', '2024-09-18 21:44:58', '2024-09-18 21:44:58');

-- --------------------------------------------------------

--
-- Structure de la table `motor`
--

CREATE TABLE `motor` (
  `id` varchar(60) NOT NULL,
  `name_motor` varchar(128) NOT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `maximal_moto` varchar(128) NOT NULL,
  `batteries` varchar(128) NOT NULL,
  `speed_max` varchar(128) NOT NULL,
  `autonomic` varchar(128) NOT NULL,
  `charger` varchar(128) NOT NULL,
  `temps_charger` varchar(128) NOT NULL,
  `charge_max` varchar(128) NOT NULL,
  `detail` varchar(128) NOT NULL,
  `reserved` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Structure de la table `person`
--

CREATE TABLE `person` (
  `username` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `person`
--

INSERT INTO `person` (`username`, `type`, `id`, `created_at`, `updated_at`) VALUES
(NULL, 'customer', '05f34609-5967-4f10-8bb3-cc5a5141e59e', '2024-09-19 18:55:16', '2024-09-19 18:55:16'),
(NULL, 'customer', '2e91ca67-cc32-4a22-bdbb-70a993cb96fb', '2024-09-18 21:54:22', '2024-09-18 21:54:22'),
(NULL, 'customer', '74d0e712-a5cf-406d-a5db-044f61c5e998', '2024-09-18 21:58:16', '2024-09-18 21:58:16'),
(NULL, 'customer', 'a09a628c-52bf-4620-b967-71d018b9f5bd', '2024-09-18 23:08:03', '2024-09-18 23:08:03'),
('user_achraf', 'user', 'dab80ff7-2834-4250-a389-9c1c6de84f6a', '2024-09-18 22:15:50', '2024-09-18 22:15:50'),
(NULL, 'customer', 'dcb271b4-637c-4756-8288-eb68c28cd5e8', '2024-09-18 21:51:27', '2024-09-18 21:51:27');

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

CREATE TABLE `reservation` (
  `person_id` varchar(60) NOT NULL,
  `machine_id` varchar(60) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `prix` int(11) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `reservation`
--

INSERT INTO `reservation` (`person_id`, `machine_id`, `start_date`, `end_date`, `prix`, `id`, `created_at`, `updated_at`) VALUES
('dab80ff7-2834-4250-a389-9c1c6de84f6a', '312beabc-4c38-40ef-a8d9-386167eb9f73', '2024-09-22', '2024-09-29', 490, '3288dd65-449a-4456-bac0-c06e8da0748a', '2024-09-19 21:07:00', '2024-09-19 21:07:00'),
('a09a628c-52bf-4620-b967-71d018b9f5bd', '59b213a8-da69-4258-8b9c-f6726fb0f784', '2024-09-20', '2024-09-27', 490, '3d8132fc-75e2-4248-8066-f4d2df44ef51', '2024-09-18 23:08:03', '2024-09-18 23:08:03'),
('dab80ff7-2834-4250-a389-9c1c6de84f6a', '4c8928bd-bce8-4052-964b-8ede18fef18e', '2024-09-24', '2024-10-01', 490, '565c6564-4021-4913-9b76-81078700d6bb', '2024-09-19 19:04:38', '2024-09-19 19:04:38'),
('74d0e712-a5cf-406d-a5db-044f61c5e998', '189919a5-4bc7-4a21-af91-99bf292c7135', '2024-09-20', '2024-09-27', 490, '86076c80-196e-4107-aa64-4b14596c5011', '2024-09-18 21:58:16', '2024-09-18 21:58:16'),
('05f34609-5967-4f10-8bb3-cc5a5141e59e', '67eb95de-577b-43db-9cde-4787367a9d0b', '2024-09-22', '2024-09-29', 490, 'fbfcb1ba-6487-4689-88d1-952b5fe489d6', '2024-09-19 18:55:16', '2024-09-19 18:55:16');

-- --------------------------------------------------------

--
-- Structure de la table `scooter`
--

CREATE TABLE `scooter` (
  `id` varchar(60) NOT NULL,
  `name_scooter` varchar(128) NOT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `engine` varchar(128) NOT NULL,
  `batteries` varchar(128) NOT NULL,
  `amperes` varchar(128) NOT NULL,
  `temps_charger` varchar(128) NOT NULL,
  `speed_max` varchar(128) NOT NULL,
  `autonomic` varchar(128) NOT NULL,
  `detail` varchar(256) NOT NULL,
  `reserved` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `scooter`
--

INSERT INTO `scooter` (`id`, `name_scooter`, `image_path`, `engine`, `batteries`, `amperes`, `temps_charger`, `speed_max`, `autonomic`, `detail`, `reserved`) VALUES
('312beabc-4c38-40ef-a8d9-386167eb9f73', 'Moto électrique Luqi 2.0', 'scooter-electrique-luqi2-jumpway-vert.jpg', '2000W', '60V 25Ah Amovible', 'test', '5 heures', '40km/h', 'Possibilité jusqu', 'test', 0),
('4c8928bd-bce8-4052-964b-8ede18fef18e', 'Scooter électrique E125S', 'eScooter-E125S Ruby-Red-Glossy.jpg', '2000W', '48V 30Ah Amovible', 'test', '5 heures', '45km/h', 'Possibilité jusqu', 'test', 0),
('6b9741a0-6fd3-47b6-9640-560cd7c06b97', 'Moto électrique Luqi 3.0', 'scooter-electrique-luqi-3.jpg', '2000W', '60V 25Ah Amovible', 'test', '5 heures', '40km/h', 'Possibilité jusqu', 'test', 0),
('8c900b54-4c33-4d16-9fa4-f50e0e1d4972', 'Moto électrique Luqi Q3', 'scooter-electrique-q3-rouge.jpg', '2000W', '48V 30Ah Amovible', 'test', '5 heures', '45km/h', 'Possibilité jusqu à 70km* dépend du poids du conducteur, du type de parcours et de la charge du scooter', 'test', 0);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id` varchar(60) NOT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `num_tel` varchar(60) NOT NULL,
  `cin` varchar(60) NOT NULL,
  `address` varchar(128) NOT NULL,
  `city` varchar(60) NOT NULL,
  `gender` varchar(60) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `image_path`, `email`, `first_name`, `last_name`, `num_tel`, `cin`, `address`, `city`, `gender`, `password`) VALUES
('dab80ff7-2834-4250-a389-9c1c6de84f6a', 'placeholder-avatar.jpg', 'achraf_test@info.com', 'achraf', 'test', '0632567589', 'SJ28847', 'Rabat', 'Rabat', 'Male', '123456');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Index pour la table `bike`
--
ALTER TABLE `bike`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `machine`
--
ALTER TABLE `machine`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `model` (`model`);

--
-- Index pour la table `motor`
--
ALTER TABLE `motor`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `person_id` (`person_id`),
  ADD KEY `machine_id` (`machine_id`);

--
-- Index pour la table `scooter`
--
ALTER TABLE `scooter`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cin` (`cin`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`id`) REFERENCES `person` (`id`);

--
-- Contraintes pour la table `bike`
--
ALTER TABLE `bike`
  ADD CONSTRAINT `bike_ibfk_1` FOREIGN KEY (`id`) REFERENCES `machine` (`id`);

--
-- Contraintes pour la table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`id`) REFERENCES `person` (`id`);

--
-- Contraintes pour la table `motor`
--
ALTER TABLE `motor`
  ADD CONSTRAINT `motor_ibfk_1` FOREIGN KEY (`id`) REFERENCES `machine` (`id`);

--
-- Contraintes pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`),
  ADD CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`machine_id`) REFERENCES `machine` (`id`);

--
-- Contraintes pour la table `scooter`
--
ALTER TABLE `scooter`
  ADD CONSTRAINT `scooter_ibfk_1` FOREIGN KEY (`id`) REFERENCES `machine` (`id`);

--
-- Contraintes pour la table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`id`) REFERENCES `person` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
