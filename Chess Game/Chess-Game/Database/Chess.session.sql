CREATE DATABASE IF NOT EXISTS chess ;
USE chess ;

-- chess.games definition

CREATE TABLE IF NOT EXISTS `games` (
  `game_id` int NOT NULL AUTO_INCREMENT,
  `player1_id` int DEFAULT NULL,
  `player2_id` int DEFAULT NULL,
  `result` varchar(10) DEFAULT NULL,
  `date_played` date DEFAULT NULL,
  PRIMARY KEY (`game_id`),
  KEY `player1_id` (`player1_id`),
  KEY `player2_id` (`player2_id`),
  CONSTRAINT `games_ibfk_1` FOREIGN KEY (`player1_id`) REFERENCES `players` (`player_id`),
  CONSTRAINT `games_ibfk_2` FOREIGN KEY (`player2_id`) REFERENCES `players` (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- chess.moves definition

CREATE TABLE IF NOT EXISTS `moves` (
  `move_id` int NOT NULL AUTO_INCREMENT,
  `game_id` int DEFAULT NULL,
  `move_number` int DEFAULT NULL,
  `move_text` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`move_id`),
  KEY `game_id` (`game_id`),
  CONSTRAINT `moves_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- chess.players definition

CREATE TABLE IF NOT EXISTS `players` (
  `player_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `rating` int DEFAULT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;