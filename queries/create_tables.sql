CREATE TABLE Diys
(
  diyID INT NOT NULL AUTO_INCREMENT,
  diyName VARCHAR(255) NOT NULL,
  diyCategory VARCHAR(255) NOT NULL,
  lindsay BOOLEAN NOT NULL,
  lyrics BOOLEAN NOT NULL,
  PRIMARY KEY (diyID),
  UNIQUE (diyName, diyID)
);

CREATE TABLE Art
(
  artID INT NOT NULL AUTO_INCREMENT,
  artName VARCHAR(255) NOT NULL,
  artType VARCHAR(255) NOT NULL,
  lindsay BOOLEAN NOT NULL,
  lyrics BOOLEAN NOT NULL,
  PRIMARY KEY (artID),
  UNIQUE (artName, artID)
);

CREATE TABLE Bugs
(
  bugID INT NOT NULL,
  bugName VARCHAR(255) NOT NULL,
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
  altMonthEnd INT,
  PRIMARY KEY (bugID),
  UNIQUE (bugName, bugID)
);

CREATE TABLE Fish
(
  fishID INT NOT NULL,
  fishName VARCHAR(255) NOT NULL,
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
  altMonthEnd INT,
  PRIMARY KEY (fishID),
  UNIQUE (fishName, fishID)
);

CREATE TABLE SeaCreatures
(
  seaCreatureID INT NOT NULL,
  seaCreatureName VARCHAR(255) NOT NULL,
  sellPrice INT NOT NULL,
  lindsay BOOLEAN NOT NULL,
  hourStart INT NOT NULL,
  hourEnd INT NOT NULL,
  monthStart INT NOT NULL,
  monthEnd INT NOT NULL,
  altHourStart INT,
  altHourEnd INT,
  altMonthStart INT,
  altMonthEnd INT,
  PRIMARY KEY (fishID),
  UNIQUE (fishName, fishID)
);

CREATE TABLE Flowers
(
  flowerID INT NOT NULL AUTO_INCREMENT,
  flowerName VARCHAR(255) NOT NULL,
  flowerFamily VARCHAR(255) NOT NULL,
  lindsay BOOLEAN NOT NULL,
  PRIMARY KEY (flowerID),
  UNIQUE (flowerName, flowerID)
);

CREATE TABLE SaharahItem
(
  itemID INT NOT NULL AUTO_INCREMENT,
  itemName VARCHAR(255) NOT NULL,
  itemCategory VARCHAR(255) NOT NULL,
  rugSize VARCHAR(255),
  lindsay BOOLEAN NOT NULL,
  lyrics BOOLEAN NOT NULL,
  PRIMARY KEY (itemID),
  UNIQUE (itemName, itemID)
);
