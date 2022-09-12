CREATE TABLE Customers (
    CustomerID int,
    CustomerName varchar(255),
    ContactName varchar(255),
    Address varchar(255),
    City varchar(255),
    PostCode int,
    Country varchar(255)
);

INSERT INTO Customers
	(CustomerID, CustomerName, ContactName, Address, City, PostCode, Country)
VALUES
	(1, 'Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', 12209, 'Germany'),
    (2, 'Ana Trujillo Emparedados y helados', 'Ana Trujillo','Avda. de la Constitución 2222','México D.F.', 05021, 'Mexico'),
    (3, 'Antonio Moreno Taquería', 'Antonio Moreno', 'Mataderos 2312', 'México D.F.', 05023, 'Mexico'),
    (4, 'Around the Horn', 'Thomas Hardy', '120 Hanover Sq.', 'London', 09867, 'UK'),
    (5, 'Berglunds snabbköp', 'Christina Berglund', 'Berguvsvägen 8', 'Luleå', 08672, 'Sweden'),
    (6,'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
    (7, 'Hekkan Burger','Testing','Gateveien 15','Sandnes','4306','Norway'),
    (8,	'Bólido Comidas preparadas', 'Martín Sommer', 'C/ Araquil, 67',	'Madrid',28023, 'Spain'),
	(9,	'Bon app',	'Laurence Lebihans',	'12, rue des Bouchers',	'Marseille',	13008	,'France'),
	(10, 'Bottom-Dollar Marketse', 'Elizabeth Lincoln',	'23 Tsawassen Blvd.', 'Tsawassen', 28412, 'Canada'),
	(11, 'Bs Beverages', 'Victoria Ashworth',	'Fauntleroy Circus','London',25897,	'UK'),
	(12, 'Cactus Comidas', 'para llevar', 'Patricio Simpson	Cerrito',	'333 Buenos Aires',	1010,	'Argentina'),
	(13, 'Centro comercial Moctezuma','Francisco Chang', 'Sierras de Granada' , '9993 México D.F.',	05022,	'Mexico'),
	(14, 'Chop-suey Chinese', 'Yang Wang', 'Hauptstr 29', 'Bern', 3012,	'Switzerland'),
	(15, 'Comércio Mineiro', 'Pedro Afonso', 'Av. dos Lusíadas 23',	'São Paulo',0543043,'Brazil'),
    (16,  'Consolidated Holdings','Elizabeth Brown','Berkeley Gardens 12 Brewery','London',12346,'UK'),
	(17,  'Drachenblut Delikatessend','Sven Ottlieb','Walserweg 21','Aachen',52066,'Germany'),
	(18, 'Du monde entier',	'Janine Labrune', '67, rue des Cinquante Otages', 'Nantes',	44000,	'France'),
	(19, 'Eastern Connection',	'Ann Devon',	'35 King George',	'London',	362345,	'UK'),
	(20, 'Ernst Handel', 'Roland Mendel',	'Kirchgasse 6',	'Graz',	8010, 'Austria'),
	(21, 'Familia Arquibaldo',	'Aria Cruz', 'Rua Orós, 92', 'São Paulo', '05442030', 'Brazil'),
	(22, 'FISSA Fabrica Inter', 'Salchichas S.A.', 'Diego Roel	C/ Moralzarzal, 86', 'Madrid',28034, 'Spain'),
	(23, 'Folies gourmandes','Martine Rancé	184,','chaussée de Tournai', 'Lille',59000,'France'),
	(24, 'Folk och fä HB',	'Maria Larsson', 'Åkergatan 24', 'Bräcke', 84467, 'Sweden'),
	(25, 'Frankenversand',	'Peter Franken','Berliner Platz 43',	'München'	,80805, 'Germany'),
	(26, 'France restauration', 'Carine Schmitt','54, rue Royale', 'Nantes', 4000 ,'France'),
	(27, 'Franchi S.p.A.',	'Paolo Accorti', 'Via Monte Bianco 34',	'Torino', 10100, 'Italy'),
	(28, 'Furia Bacalhau e Frutos do Mar', 'Lino Rodriguez', 'Jardim das rosas n. 32',	'Lisboa',1675,'Portugal'),
	(29, 'Galería del gastrónomo','Eduardo Saavedra','Rambla de Cataluña, 23','Barcelona',08022,'Spain'),
	(30, 'Godos Cocina Típica','José Pedro Freyre','C/ Romero, 33','Sevilla',41101,'Spain'),
	(31, 'Gourmet Lanchonetes','André Fonseca','Av. Brasil, 442','Campinas',04786,'Brazil'),
	(32, 'Great Lakes Food Market','Howard Snyder','2732 Baker Blvd.','Eugene',97403,'USA'),
	(33, 'GROSELLA-Restaurante','Manuel Pereira','5ª Ave. Los Palos Grandes','Caracas',1081,'Venezuela'),
	(34, 'Hanari Carnes','Mario Pontes','Rua do Paço, 67','Rio de Janeiro',05454-876,'Brazil'),
	(35, 'HILARIÓN-Abastos','Carlos Hernández','Carrera 22 con Ave. Carlos Soublette #8-35','San Cristóbal',5022,'Venezuela'),
	(36, 'Hungry Coyote','Import Store Yoshi Latimer','City Center Plaza 516 Main St','Elgin',	97827,'USA'),
	(37, 'Hungry Owl All-Night Grocers', 'Patricia McKenna','8 Johnstown Road','Cork', 459023,	'Ireland'),
	(38, 'Island Trading','Helen Bennett','Garden House Crowther Way','Cowes', 0317,'UK'),
	(39, 'Königlich Essen', 'Philip Cramer', 'Maubelstr. 90', 'Brandenburg' ,14776, 'Germany'),
	(40, 'La corne d-abondance','Daniel Tonini','67 avenue de l-Europe','Versailles',	78000,	'France'),
	(41, 'La maison dAsie','Annette Roulet','1 rue Alsace-Lorraine','Toulouse',	31000,'France'),
	(42,  'Laughing Bacchus','Wine Cellars','Yoshi Tannamuri 1900 Oak St.','Vancouver',32156,'Canada'),
    (43, 'Lazy K Kountry Store','John Steel','12 Orchestra Terrace','Walla Walla',99362,'USA'),
	(44, 'Lehmanns Marktstand','Renate Messner','Magazinweg 7','Frankfurt a.M.',	60528,'Germany'),
	(45, 'Lets Stop N Shop','Jaime Yorres','87 Polk St. Suite 5','San Francisco	',94117,'USA'),
	(46, 'LILA-Supermercado','Carlos González','Carrera 52 con Ave. Bolívar #65-98 Llano Largo','Barquisimeto',3508,'Venezuela'),
	(47, 'LINO-Delicateses','Felipe Izquierdo','Ave. 5 de Mayo Porlamar	I.','de Margarita',4980,'Venezuela'),
	(48, 'Lonesome Pine Restaurant','Fran Wilson','89 Chiaroscuro Rd.','Portland' ,97219,'USA'),
	(49, 'Magazzini Alimentari', 'Riuniti Giovanni Rovelli', 'Via Ludovico il Moro 22','Bergamo', 24100, 'Italy'),
	(50, 'Maison Dewey', 'Catherine Dewey', 'Rue Joseph-Bens 532', 'Bruxelles', 1180, 'Belgium');

-- to select all customers     
select * from customers;

-- to select customer Id, name and address columns
select CustomerID, CustomerName, Address from customers;

-- to select distinct statement: return only distinct values
select distinct Country from customers;
select count(distinct Country) as number_of_countries from customers;

-- where clause
-- for string 
select * from customers where Country='Mexico';
-- for numbers 
select * from customers where CustomerId=1;

-- Operations in where clauses: 
-- IN
SELECT * FROM Customers
WHERE City IN ('Paris','London');

-- LIKE
SELECT * FROM Customers
WHERE City LIKE 's%';

-- AND
select * from customers where Country='Germany' AND City='Berlin';

-- OR 
select * from customers where Country='Brazil' OR Country='Norway';

-- NOT
SELECT * FROM Customers WHERE NOT Country='Germany';

-- ORDER BY Keyword
SELECT * FROM Customers ORDER BY Country;
-- DESC 
SELECT * FROM Customers ORDER BY Country DESC;
-- order by several columns
SELECT * FROM Customers ORDER BY Country, CustomerName;
SELECT * FROM Customers ORDER BY Country ASC, City DESC;