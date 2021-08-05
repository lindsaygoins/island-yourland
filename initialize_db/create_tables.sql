CREATE TABLE Diys
(
  diyID SERIAL PRIMARY KEY,
  diyName VARCHAR(255) NOT NULL UNIQUE,
  diyCategory VARCHAR(255) NOT NULL,
  lindsay BOOLEAN NOT NULL,
  lyrics BOOLEAN NOT NULL
);

CREATE TABLE Art
(
  artID SERIAL PRIMARY KEY,
  artName VARCHAR(255) NOT NULL UNIQUE,
  artType VARCHAR(255) NOT NULL,
  lindsay BOOLEAN NOT NULL,
  lyrics BOOLEAN NOT NULL
);

CREATE TABLE Bugs
(
  bugID INT PRIMARY KEY,
  bugName VARCHAR(255) NOT NULL UNIQUE,
  location VARCHAR(255) NOT NULL,
  sellPrice INT NOT NULL,
  lindsay BOOLEAN NOT NULL,
  hourStart INT NOT NULL,
  hourEnd INT NOT NULL,
  monthStart INT NOT NULL,
  monthEnd INT NOT NULL,
  altHourStart INT,
  altHourEnd INT,
  altMonthStart INT,
  altMonthEnd INT
);

CREATE TABLE Fish
(
  fishID INT PRIMARY KEY,
  fishName VARCHAR(255) NOT NULL UNIQUE,
  location VARCHAR(255) NOT NULL,
  shadowSize VARCHAR(255) NOT NULL,
  sellPrice INT NOT NULL,
  lindsay BOOLEAN NOT NULL,
  hourStart INT NOT NULL,
  hourEnd INT NOT NULL,
  monthStart INT NOT NULL,
  monthEnd INT NOT NULL,
  altHourStart INT,
  altHourEnd INT,
  altMonthStart INT,
  altMonthEnd INT
);

CREATE TABLE SeaCreatures
(
  seaCreatureID INT PRIMARY KEY,
  seaCreatureName VARCHAR(255) NOT NULL UNIQUE,
  sellPrice INT NOT NULL,
  lindsay BOOLEAN NOT NULL,
  hourStart INT NOT NULL,
  hourEnd INT NOT NULL,
  monthStart INT NOT NULL,
  monthEnd INT NOT NULL,
  altHourStart INT,
  altHourEnd INT,
  altMonthStart INT,
  altMonthEnd INT
);

CREATE TABLE Flowers
(
  flowerID SERIAL PRIMARY KEY,
  flowerName VARCHAR(255) NOT NULL UNIQUE,
  flowerFamily VARCHAR(255) NOT NULL,
  lindsay BOOLEAN NOT NULL
);

CREATE TABLE SaharahItems
(
  itemID SERIAL PRIMARY KEY,
  itemName VARCHAR(255) NOT NULL UNIQUE,
  itemCategory VARCHAR(255) NOT NULL,
  rugSize VARCHAR(255),
  lindsay BOOLEAN NOT NULL,
  lyrics BOOLEAN NOT NULL
);
