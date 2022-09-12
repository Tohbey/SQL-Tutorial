CREATE TABLE Products (
    ProductID int,
    ProductName varchar(255),
    SupplierId int,
    CategoryId int ,
    Unit varchar(255),
    Price int
);

INSERT INTO Products
    (ProductID, ProductName, SupplierId, CategoryId, Unit, Price)
VALUES
    (1,'Chais', 1, 1,'10 boxes x 20 bags',18),
    (2, 'hang',	1,	1,	'24 - 12 oz bottles', 19),    
    (3, 'niseed Syrup',	1,	2,	'12 - 550 ml bottles',	10),
    (4, 'hef Antons Cajun Seasoning',	2,	2,	'48 - 6 oz jars', 22),
    (5, 'hef Antons Gumbo Mix',2,2,'36 boxes',	21.35),
    (6, 'randma Boysenberry Spread',	3,	2,	'12 - 8 oz jars',25),
    (7, 'ncle Bobs Organic Dried Pears',   3,	7,	'12 - 1 lb pkgs.',	30),
    (8, 'orthwoods Cranberry Sauce',	3,	2,	'12 - 12 oz jars',	40),
    (9, 'ishi Kobe Niku',	4,	6,	'18 - 500 g pkgs.',	97),
    (10, 'Ikura',	4,	8,	'12 - 200 ml jars',	31),
    (11, 'Queso Cabrales',	5,	4,	'1 kg pkg.',	21),
    (12, 'Queso Manchego La Pastora',	5,	4,	'10 - 500 g pkgs.',	38),
    (13, 'Konbu',	6, 8,	'2 kg box', 6),
    (14, 'Tofu',	6,	7,	'40 - 100 g pkgs.',	23.25),
    (15, 'Genen Shouyu',	6,	2,	'24 - 250 ml bottles',	15.5),
    (16, 'Pavlova',	7,	3,	'32 - 500 g boxes',	17.45),
    (17, 'Alice Mutton',	7,	6,	'20 - 1 kg tins',	39),
    (18, 'Carnarvon Tigers',	7,	8,	'16 kg pkg.',	62.5),
    (19, 'Teatime Chocolate Biscuits',	8,	3,	'10 boxes x 12 pieces',	9.2),
    (20, 'Sir Rodney Marmalade',	8,	3,	'30 gift boxes',	81),
    (21, 'Sir Rodney Scones',	8,	3,	'24 pkgs. x 4 pieces',	10),
    (22, 'Gustaf Knäckebröd',	9,	5,	'24 - 500 g pkgs.',	21),
    (23, 'Tunnbröd',	9,	5,	'12 - 250 g pkgs.',	9),
    (24, 'Guaraná Fantástica',	10,	1,	'12 - 355 ml cans',	4.5),
    (25, 'NuNuCa Nuß-Nougat-Creme',	11,	3,	'20 - 450 g glasses',	14),
    (26, 'Gumbär Gummibärchen',	11,	3,	'100 - 250 g bags',	31.23),
    (27, 'Schoggi Schokolade',	11,	3,	'100 - 100 g pieces',	43.9),
    (28, 'Rössle Sauerkraut',	12,	7,	'25 - 825 g cans',	45.6),
    (29, 'Thüringer Rostbratwurst',	12,	6,	'50 bags x 30 sausgs.',	123.79),
    (30, 'Nord-Ost Matjeshering',	13,	8,	'10 - 200 g glasses',	25.89),
    (31, 'Gorgonzola Telino',	14,	4,	'12 - 100 g pkgs',	12.5),
    (32, 'Mascarpone Fabioli',	14,	4,	'24 - 200 g pkgs.',	32),
    (33, 'Geitost',	15,	4,	'500 g',	2.5),
    (34, 'Sasquatch Ale',	16,	1,	'24 - 12 oz bottles',	14),
    (35, 'Steeleye Stout',	16,	1,	'24 - 12 oz bottles',	18),
    (36, 'Inlagd Sill',	17,	8,	'24 - 250 g jars',	19),
    (37, 'Gravad lax',	17,	8,	'12 - 500 g pkgs.',	26),
    (38, 'Côte de Blaye',	18,	1,	'12 - 75 cl bottles',	263.5),
    (39, 'Chartreuse verte',	18,	1,	'750 cc per bottle',	18),
    (40, 'Boston Crab Meat',	19,	8,	'24 - 4 oz tins',	18.4),
    (41, 'Jack New England Clam Chowder',	19,	8,	'12 - 12 oz cans',	9.65),
    (42, 'Singaporean Hokkien Fried Mee',	20,	5,	'32 - 1 kg pkgs.',	14),
    (43, 'Ipoh Coffee',	20,	1,	'16 - 500 g tins',	46),
    (44, 'Gula Malacca',	20,	2,	'20 - 2 kg bags',	19.45),
    (45, 'Røgede sild',	21,	8,	'1k pkg.',	9.5),
    (46, 'Spegesild',	21,	8,'4 - 450 g glasses',	12),
    (47, 'Zaanse koeken',	22,	3,'10 - 4 oz boxes',	9.5),
    (48, 'Chocolade',	22,	3	,'10 pkgs.',	12.75),
    (49, 'Maxilaku',	23,	3,'24 - 50 g pkgs.',	20),   
    (50, 'Valkoinen suklaa',	23,	3,	'12 - 100 g bars',	16.25);

-- BETWEEN
SELECT * FROM Products
WHERE Price BETWEEN 50 AND 60;

-- <>
SELECT * FROM Products
WHERE Price <> 18;

-- <=
SELECT * FROM Products
WHERE Price <= 30;

-- >=
SELECT * FROM Products
WHERE Price >= 30;

-- >
SELECT * FROM Products
WHERE Price > 30;

-- <
SELECT * FROM Products
WHERE Price < 30;