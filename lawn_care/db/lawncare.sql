-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema lawncare
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `lawncare` ;

-- -----------------------------------------------------
-- Schema lawncare
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lawncare` DEFAULT CHARACTER SET utf8 ;
USE `lawncare` ;

-- -----------------------------------------------------
-- Table `users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `users` ;

CREATE TABLE IF NOT EXISTS `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128) NULL,
  `email` VARCHAR(256) NOT NULL,
  `hashed_password` VARCHAR(256) NOT NULL,
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `email_UNIQUE` ON `users` (`email` ASC);


-- -----------------------------------------------------
-- Table `services`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `services` ;

CREATE TABLE IF NOT EXISTS `services` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128) NOT NULL,
  `category` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `name_UNIQUE` ON `services` (`name` ASC);

SET SQL_MODE = '';
DROP USER IF EXISTS username;
SET SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
CREATE USER 'username' IDENTIFIED BY 'password';

GRANT SELECT, INSERT, TRIGGER, UPDATE, DELETE ON TABLE * TO 'username';

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `services`
-- -----------------------------------------------------
START TRANSACTION;
USE `lawncare`;
INSERT INTO `services` (`id`, `name`, `category`) VALUES (1, 'mow lawn', 'lawn care');
INSERT INTO `services` (`id`, `name`, `category`) VALUES (2, 'fertilize', 'lawn care');
INSERT INTO `services` (`id`, `name`, `category`) VALUES (3, 'flea and tick control', 'weed/pest control');
INSERT INTO `services` (`id`, `name`, `category`) VALUES (4, 'fetching the finest shrubbery', 'landscaping');

COMMIT;

