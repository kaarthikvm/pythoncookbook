Reference : 
1) https://geekflare.com/mysql-installation-command-sample/
2) https://www.w3schools.com/sql/default.asp

mysql -u root -p


# creation of user and database with full permission (CREATE,SELECT,INSERT,UPDATE,DELETE)
create database myinventory;
create user 'vmk'@localhost IDENTIFIED BY 'jk';
GRANT ALL ON myinventory.* TO 'vmk'@"localhost";
FLUSH PRIVILEGES;

# create a table
use myinventory;
CREATE TABLE Customer (
    CID int(50) not null auto_increment primary key,
    FirstName varchar(255),
	LastName varchar(255),
    Address varchar(255),
    City varchar(255)	
);

CREATE TABLE Orders (
    OID int not null auto_increment primary key,
    CID int,
	Date DATE,
    Price int,
    FOREIGN KEY (CID) REFERENCES Customer(CID) 	
);

INSERT INTO Customer (FirstName, LastName,Address,City) VALUES ('tiger','cub','addr1','dublin');
INSERT INTO Customer (FirstName, LastName,Address,City) VALUES ('lion','cub','addr2','dublin');
INSERT INTO Customer (FirstName, LastName,Address,City) VALUES ('dog','puppy','addr3','cork');
INSERT INTO Customer (FirstName, LastName,Address,City) VALUES ('cat','kitten','addr4','cork');
INSERT INTO Customer (FirstName, LastName,Address,City) VALUES ('cow','calf','addr5','galway');
INSERT INTO Customer (FirstName, LastName,Address,City) VALUES ('rabbit','baby','addr6','galway');

INSERT INTO Orders (CID, Date, Price) VALUES (1,'2000-12-20',1000.20);
INSERT INTO Orders (CID, Date, Price) VALUES (1,'2000-12-21',200);
INSERT INTO Orders (CID, Date, Price) VALUES (2,'2000-12-22',300);
INSERT INTO Orders (CID, Date, Price) VALUES (2,'2000-12-23',400);
INSERT INTO Orders (CID, Date, Price) VALUES (3,'2000-12-24',500);
INSERT INTO Orders (CID, Date, Price) VALUES (3,'2000-12-25',600);
INSERT INTO Orders (CID, Date, Price) VALUES (5,'2000-12-26',700);
INSERT INTO Orders (CID, Date, Price) VALUES (5,'2000-12-27',800);
INSERT INTO Orders (CID, Date, Price) VALUES (6,'2000-12-28',900);
INSERT INTO Orders (CID, Date, Price) VALUES (6,'2000-12-29',950);


select FirstName as FIRSTNAME, city as CITY  from Customer;
select c.FirstName as FIRSTNAME, c.city as CITY  from Customer as c;
select FirstName as FIRSTNAME, city as CITY  from Customer where city='dublin';
select FirstName as FIRSTNAME, city as CITY  from Customer where city between 'cork' and 'dublin';
select FirstName as FIRSTNAME, city as CITY  from Customer where city like 'd%';
select count(FirstName) from Customer where city='dublin';
select avg(Price) from Orders;
select FirstName,city,LastName from Customer where city='cork' order by LastName;
select FirstName,LastName,city from Customer group by city order by city; ==> This will select only one value and duplicate is discarded. hence it is required to put COUNT
select count(CID), FirstName,LastName,city from Customer group by city order by city
select count(CID),CID,Date,Price from Orders group by CID having CID > 2 order by Price

select c.FirstName,c.LastName,o.OID,c.CID from Customer as c left join Orders as o on c.CID = o.CID;
select c.FirstName,c.LastName,c.City,o.Price,o.OID,c.CID from Customer as c right join Orders as o on c.CID = o.CID;
select * from Customer  inner  join Orders  on Customer.CID=Orders.CID;
select * from Customer c1, Customer c2  where c1.CID=c2.CID; ==> Self Join
select * from Customer cross  join Orders  on Customer.CID=Orders.CID; ==>All rows of each table is selected and compared






