CREATE TABLE Horno (
numero_serie INT AUTO_INCREMENT, 
modelo VARCHAR(50) NOT NULL,
marca VARCHAR(50) NOT NULL,
año_fabricacion YEAR,
INDEX idx_modelo_marca (modelo, marca),
CONSTRAINT Id_Horno PRIMARY KEY (numero_serie)
);
CREATE TABLE modos_de_coccion (
id_modos_coccion INT AUTO_INCREMENT PRIMARY KEY,
nombre_modo_coccion VARCHAR(50) NOT NULL
);
CREATE TABLE ciclos_de_coccion (
id_ciclo INT AUTO_INCREMENT PRIMARY KEY,
horno_id INT,
hora_inicio TIME,
duracion_estimada TIME,
temperatura_inicial INT,
temperatura_final INT,
modo_coccion_id INT,
FOREIGN KEY (horno_id) REFERENCES Horno(numero_serie),
FOREIGN KEY (modo_coccion_id) REFERENCES modos_de_coccion(id_modos_coccion)
);
INSERT INTO Horno (modelo, marca, año_fabricacion)
VALUES
  ('Electrolux EOC3540X', 'Electrolux', 2020),
  ('Bosch HBG675BS1', 'Bosch', 2021),
  ('Whirlpool AKZ9850/1', 'Whirlpool', 2022)
  ;
INSERT INTO modos_de_coccion (nombre_modo_coccion)
VALUES
  ('Hornear'),
  ('Conveccion'),
  ('Descongelar'),
  ('Cocción al vapor')
  ;
INSERT INTO ciclos_de_coccion (horno_id, hora_inicio, duracion_estimada, temperatura_inicial, temperatura_final, modo_coccion_id)
VALUES
  (1, '10:00:00', '01:30:00', 180, 200, 1),
  (2, '15:30:00', '00:45:00', 220, 250, 2),
  (3, '19:00:00', '01:00:00', 100, 120, 4)
  ;
  SELECT * FROM Horno WHERE numero_serie = 1;
  SELECT * FROM ciclos_de_coccion WHERE horno_id = 2;
  SELECT * FROM ciclos_de_coccion c
INNER JOIN modos_de_coccion m ON c.modo_coccion_id = m.id_modos_coccion
WHERE m.nombre_modo_coccion = 'Conveccion';
  SELECT numero_serie, modelo FROM Horno WHERE año_fabricacion = 2021;
  SELECT SUM(TIME_TO_SEC(duracion_estimada)) / 3600 AS total_horas
FROM ciclos_de_coccion;


  

