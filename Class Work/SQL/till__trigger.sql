-- create database zomato;

-- show databases;

-- use zomato;

-- create table customer ( 
-- 	id int primary key auto_increment,
--     name varchar(50),
--     email varchar(50) unique key,
--     mobile bigint unique key
-- );

#INSERT INTO customer (id, name, email, mobile) values(1, "Rahul", "r@gmail.com", 8374627482);

#INSERT INTO customer (name, email, mobile) values ("Sujal", "s@gmail.com", 7346684722), ("Raj", "r1@gmail.com", 3578388357);

#SELECT * FROM customer;

#alter table customer add city varchar(30);

#update customer set city = "Ahmedabad" where id = 1;
#update customer set city = "Surat" where id = 5;

-- Retrieve Data
-- select * from customer where id = 1; 
-- select name, email from customer where id = 1;

-- select * from customer where name like 'R%';

-- create table restaurant (
-- rid int auto_increment primary key,
-- rname varchar(56),
-- rprice int,
-- rcustomer varchar(56),
-- order_date datetime
-- );

-- select * from restaurant;

-- insert into restaurant (rid, rname, rprice, rcustomer, order_date) values (1, 'restaurant1', 554, "Rahul", "26-05-25");

-- insert into restaurant (rname, rprice, rcustomer, order_date) values 
-- ('restaurant2', 343, "Raj", "26-05-22"),
-- ('restaurant3', 87, "Suyog", "26-05-21"),
-- ('restaurant4', 612, "Kushal", "26-05-11"),
-- ('restaurant5', 99, "Piyush", "26-05-21");

-- select * from customer order by name asc;

-- select * from customer order by name desc;

-- select * from restaurant where rprice = (select min(rprice) from restaurant);

-- select rname, min(rprice) from restaurant group by rname;

-- select * from restaurant where rprice > 100 and rprice < 1000;

-- select * from restaurant where rprice > 100 or rprice < 1000;

-- select * from restaurant where rprice between 100 and 500;

-- create table vendor (
-- vid int primary key auto_increment,
-- vname varchar(50),
-- vemail varchar(50) unique key,
-- vprice int,
-- fid int,
-- foreign key(fid) references customer(id)
-- )

-- select * from customer;
-- select * from vendor;

-- insert into vendor(vid, vname, vemail, vprice, fid) values
-- (1, 'java', 'java@gmail.com', 1100, 1);

-- insert into vendor(vname, vemail, vprice, fid) values
-- ('python', 'py@gmail.com', 1900, 5),
-- ('javascript', 'js@gmail.com', 1200, 6),
-- ('dotnet', 'net@gmail.com', 1100, 1);

-- select * from customer inner join vendor on customer.id = vendor.fid;

-- select * from customer left join vendor on customer.id = vendor.fid;

-- select * from customer right join vendor on customer.id = vendor.fid;

-- select * from customer full join vendor on id = fid;

-- =========================PROCEDURE===================================

-- delimiter $$
-- create procedure myfun()

-- begin
-- select * from customer;
-- end;

-- call myfun();



-- delimiter //
-- create procedure myfun2()
-- begin
-- select * from vendor;
-- end//
-- delimiter ;

-- call myfun2();

#-------------------------------Trigger----------------------
-- use zomato; 

-- create table temp_customer ( 
-- 	id int primary key auto_increment,
--     name varchar(50),
--     email varchar(50) unique key,
--     mobile bigint unique key
-- );

-- INSERT INTO temp_customer (id, name, email, mobile) values(1, "Rahul", "r@gmail.com", 8374627482);

#INSERT INTO temp_customer (name, email, mobile) values ("Sujal", "s@gmail.com", 7346684722), ("Raj", "r1@gmail.com", 3578388357);

-- drop table trigger01;

-- create table trigger01 (
-- tid int,
-- tname varchar(55),
-- temail varchar(50),
-- tmobile bigint,
-- ttime timestamp default current_timestamp,
-- action_perform varchar(50)
-- )

#==============DELETE TRIGGER===================

-- create trigger deltrigger 
-- before delete on temp_customer
-- for each row
-- insert into trigger01 (tid,tname,temail,tmobile,action_perform) values
-- (old.id, old.name, old.email, old.mobile, "Data Deleted")

-- delete from temp_customer where id = 2;

#===============INSERT TRIGGER=====================

-- create trigger addtrigger
-- after insert on temp_customer
-- for each row
-- insert into trigger01 (tid,tname,temail,tmobile,action_perform) values
-- (new.id, new.name, new.email, new.mobile, "Data Inserted")

-- INSERT INTO temp_customer (name, email, mobile) values ("Kuanl", "kk@gmail.com", 7346675522), ("Vraj", "vr@gmail.com", 3578388343);

#===============UPDATE TRIGGER=====================

-- create trigger beforeupdatetrigger
-- before update on temp_customer
-- for each row
-- insert into trigger01 (tid,tname,temail,tmobile,action_perform) values
-- (old.id, old.name, old.email, old.mobile, "Before Update")

-- create trigger Afterupdatetrigger
-- after update on temp_customer
-- for each row
-- insert into trigger01 (tid,tname,temail,tmobile,action_perform) values
-- (new.id, new.name, new.email, new.mobile, "After Update")



#==============Task=================

create database task1;

use task1;

create table customer (
cid int primary key auto_increment,
cname varchar(56),
cemail varchar(56) unique key,
cmobile bigint unique key
);


create table restaurant (
id int primary key auto_increment,
rid int,
rname varchar(56),
rprice int,
rlocation varchar(56),
fid int,
foreign key (fid) references customer (cid)
);


create table delivery (
did int,
dname varchar(56)
);

-- alter table delivery add restfid int;

-- ALTER TABLE delivery ADD CONSTRAINT restfid FOREIGN KEY (restfid) REFERENCES restaurant (id);
-- alter table delivery add column restfid int, ADD CONSTRAINT restfid FOREIGN KEY (restfid) REFERENCES restaurant (id);
 
-- alter table delivery add custfid int;

-- ALTER TABLE delivery ADD CONSTRAINT custfid FOREIGN KEY (custfid) REFERENCES customer (cid);

-- INSERT INTO customer (cid, cname, cemail, cmobile) values(1, "Rahul", "r@gmail.com", 8374627482);

-- INSERT INTO customer (cname, cemail, cmobile) values ("Sujal", "s@gmail.com", 7346684722), ("Raj", "r1@gmail.com", 3578388357);

-- alter table customer add ctime timestamp default current_timestamp;

INSERT INTO restaurant (id, rid, rname, rprice, rlocation, fid) values
(1, 101, 'rest1', 1020, 'Ahmedabad', 2);

INSERT INTO restaurant (rid, rname, rprice, rlocation, fid) values
(102, 'rest2', 3320, 'Surat', 1),
(103, 'rest3', 3542, 'Vadodara', 3),
(104, 'rest4', 950, 'Ahmedabad', 1),
(101, 'rest1', 1020, 'Ahmedabad', 3),
(102, 'rest2', 3320, 'Surat', 2);

INSERT INTO delivery (did, dname, restfid, custfid) values
(1, 'Boy1', 1, 2);

INSERT INTO delivery (dname, restfid, custfid) values
('Boy2', 2, 1),
('Boy3', 3, 3),
('Boy1', 4, 1),
('Boy3', 5, 3),
('Boy4', 6, 2);

create table custtrig (
id int,
name varchar(56),
email varchar(50),
mobile bigint,
time timestamp default current_timestamp
);

create trigger delcust
after delete on customer
for each row
insert into custtrig (id, name, email, mobile) values
(old.cid, old.cname, old.cemail, old.cmobile);

insert into customer(cname, cemail, cmobile) values
("Suyog", "suyog@123", 8874924924);

delete from customer where cid = 4;

select * from customer;

select * from customer full join restaurant on cid = fid;

select * from customer inner join restaurant on customer.cid = restaurant.fid inner join
delivery on restaurant.id = delivery.restfid;

update customer set cname = "Kush", cemail = "kush@123", cmobile = 6254859204 where cid = 3;

select * from customer where cname like 'R%';
-- ===================================================================-- 

-- ----------------WINDOWS FUNCTION-----------------------------
use zomato; 

select rid, rname, rprice, row_number() OVER (partition by rname order by rprice desc) as rest_price from restaurant;

select rid, rname, rprice, rank() over (order by rprice desc) as rest_rank from restaurant;

select rid, rname, rprice, dense_rank() over (order by rprice desc) as rest_dense from restaurant;

select rid, rname, rprice, lag(rprice) over (order by rprice) as rest_lag from restaurant;

select rid, rname, rprice, lead(rprice) over (order by rprice) as rest_lead from restaurant;

select rid, rname, rprice, sum(rprice) over (partition by rname order by rprice) as rest_sum from restaurant;


-- ===============================CTE======================================

-- WITH MyCteName AS (
--     -- Your temporary query logic goes here
--     SELECT column1, column2 
--     FROM your_table
--     WHERE condition
-- )
-- -- Your main query referencing the CTE
-- SELECT * 
-- FROM MyCteName;











