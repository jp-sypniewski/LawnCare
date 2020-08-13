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
  `username` VARCHAR(128) NOT NULL,
  `email` VARCHAR(256) NOT NULL,
  `hashed_password` VARCHAR(256) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `first_name` VARCHAR(128) NULL,
  `last_name` VARCHAR(128) NULL,
  `account_type` ENUM('user', 'admin') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `services`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `services` ;

CREATE TABLE IF NOT EXISTS `services` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128) NOT NULL,
  `category` VARCHAR(64) NOT NULL,
  `quick_description` VARCHAR(512) NOT NULL,
  `extended_description` VARCHAR(2048) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `quote_requests`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `quote_requests` ;

CREATE TABLE IF NOT EXISTS `quote_requests` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL,
  `requester_name` VARCHAR(256) NOT NULL,
  `dttm_requested` VARCHAR(512) NOT NULL,
  `contact_phone` VARCHAR(45) NULL,
  `contact_email` VARCHAR(45) NULL,
  `preference_contact` VARCHAR(45) NOT NULL,
  `completed` TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SET SQL_MODE = '';
DROP USER IF EXISTS username;
SET SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
CREATE USER 'username' IDENTIFIED BY 'password';

GRANT SELECT, INSERT, TRIGGER, UPDATE, DELETE ON TABLE * TO 'username';

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
