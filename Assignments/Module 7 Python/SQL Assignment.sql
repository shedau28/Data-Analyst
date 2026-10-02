create database MarketCo;

use MarketCo;

create table Company (
CompanyID int primary key,
CompanyName varchar(45),
Street varchar(45),
City varchar(45),
State varchar(2),
Zip varchar(10)
);

-- 1) Statement to create the Contact table  

create table Contact (
ContactID int primary key,
CompanyID int,
FirstName varchar(45),
LastName varchar(45),
Street varchar(45),
City varchar(45),
State varchar(2),
Zip varchar(10),
IsMain boolean,
Email varchar(45),
Phone varchar(12),
foreign key (CompanyID) references Company(CompanyID)
);


-- 2) Statement to create the Employee table 

create table Employee (
EmployeeID	int primary key,
FirstName varchar(45),
LastName varchar(45),
Salary decimal(10,2),
HireDate date,
JobTitle varchar(25),
Email varchar(45),
Phone varchar(12)
);

-- 3) Statement to create the ContactEmployee table 

create table ContactEmployee (
ContactEmployeeID int,
ContactID int,
EmployeeID int,
ContactDate date,
Description varchar(100),
foreign key (ContactID) references Contact(ContactID),
foreign key (EmployeeID) references Employee(EmployeeID)
);


