-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sasquatch_sightings_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `sasquatch_sightings_schema` ;

-- -----------------------------------------------------
-- Schema sasquatch_sightings_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sasquatch_sightings_schema` DEFAULT CHARACTER SET utf8 ;
USE `sasquatch_sightings_schema` ;

-- -----------------------------------------------------
-- Table `sasquatch_sightings_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sasquatch_sightings_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sasquatch_sightings_schema`.`sightings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sasquatch_sightings_schema`.`sightings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `where` VARCHAR(255) NULL,
  `description` TEXT NULL,
  `sasquatches` INT NULL,
  `date_seen` DATE NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_sightings_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_sightings_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `sasquatch_sightings_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
