--CREAR TABLAS
-- Regiones
CREATE TABLE IF NOT EXISTS Regiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

--  Categorias
CREATE TABLE IF NOT EXISTS Categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

-- Clientes
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT,
    region_id INTEGER,
    FOREIGN KEY (region_id) REFERENCES Regiones(id)
);

-- Productos
CREATE TABLE IF NOT EXISTS Productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
);

-- Ventas
CREATE TABLE IF NOT EXISTS Ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    fecha TEXT,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);

-- DetalleVentas
CREATE TABLE IF NOT EXISTS DetalleVentas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    venta_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (venta_id) REFERENCES Ventas(id),
    FOREIGN KEY (producto_id) REFERENCES Productos(id)
);

-- INSERTAR DATOS
INSERT INTO Regiones (nombre) VALUES ('Metropolitana'), ('Valparaíso'), ('Biobío');
INSERT INTO Categorias (nombre) VALUES ('Electrónica'), ('Hogar'), ('Ropa');

INSERT INTO Clientes (nombre, correo, region_id) VALUES
('Ana Torres', 'ana@correo.com', 1),
('Luis Soto', 'luis@correo.com', 2);

INSERT INTO Productos (nombre, precio, categoria_id) VALUES
('Smartphone', 299990, 1),
('Lavadora', 199990, 2),
('Polera', 12990, 3);

INSERT INTO Ventas (cliente_id, fecha) VALUES
(1, '2025-08-14'),
(2, '2025-08-15');

INSERT INTO DetalleVentas (venta_id, producto_id, cantidad) VALUES
(1, 1, 2),
(2, 3, 5);


--Select para mostrar venta detallada