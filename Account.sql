create database atmdb;
use atmdb;
create table account(
C_id int primary key auto_increment,
Name varchar(40),
Pin int,
Balance int,
Mobile_no bigint,
Account_type varchar(15))
;
alter table account auto_increment=1;
SELECT * FROM atmdb.account;

select * from account;
desc account;
update account set balance = 7000 where C_id = 1;