-- MySQL Script generated by MySQL Workbench
-- Mon Dec 11 13:18:09 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Ejercicio01
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Ejercicio01` ;

-- -----------------------------------------------------
-- Schema Ejercicio01
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Ejercicio01` DEFAULT CHARACTER SET utf8 ;
USE `Ejercicio01` ;

-- -----------------------------------------------------
-- Table `Ejercicio01`.`proveedor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ejercicio01`.`proveedor` ;

CREATE TABLE IF NOT EXISTS `Ejercicio01`.`proveedor` (
  `codigo` INT UNSIGNED AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `direccion` TINYBLOB NULL,
  `ciudad` VARCHAR(45) NULL,
  `provincia` VARCHAR(45) NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ejercicio01`.`categoria`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ejercicio01`.`categoria` ;

CREATE TABLE IF NOT EXISTS `Ejercicio01`.`categoria` (
  `codigo` INT UNSIGNED  AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ejercicio01`.`pieza`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ejercicio01`.`pieza` ;

CREATE TABLE IF NOT EXISTS `Ejercicio01`.`pieza` (
  `codigo` INT UNSIGNED  AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `color` VARCHAR(45) NULL,
  `precio` DECIMAL NULL,
  `categoria_codigo` INT NOT NULL,
  PRIMARY KEY (`codigo`),
  INDEX `fk_pieza_categoria1_idx` (`categoria_codigo` ASC) VISIBLE,
  CONSTRAINT `fk_pieza_categoria1`
    FOREIGN KEY (`categoria_codigo`)
    REFERENCES `Ejercicio01`.`categoria` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Ejercicio01`.`proveedor_has_pieza`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ejercicio01`.`proveedor_has_pieza` ;

CREATE TABLE IF NOT EXISTS `Ejercicio01`.`proveedor_has_pieza` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `pieza_codigo` INT NOT NULL,
  `proveedor_codigo` INT NOT NULL,
  `fecha` DATETIME NULL,
  `cantidad` INT NULL,
  INDEX `fk_proveedor_has_pieza_pieza1_idx` (`pieza_codigo` ASC) VISIBLE,
  INDEX `fk_proveedor_has_pieza_proveedor1_idx` (`proveedor_codigo` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_proveedor_has_pieza_proveedor1`
    FOREIGN KEY (`proveedor_codigo`)
    REFERENCES `Ejercicio01`.`proveedor` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_proveedor_has_pieza_pieza1`
    FOREIGN KEY (`pieza_codigo`)
    REFERENCES `Ejercicio01`.`pieza` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
