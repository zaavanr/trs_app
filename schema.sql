/*-------Creating the Database-----*/

create database trs;
use trs;

/*----Creating the Tables----*/
create table client(
		cid int (5),
		cfname varchar(20),
		clname varchar(20),
		ccontact int(11),
    cemail varchar(17),
    cpassword varchar (20),
    cadd1 varchar (30),
    cadd2 varchar(30),
		city varchar(25),
		parish varchar(12),
		primary key(cid)
		);
create table driver(
		dtrn int(10),
		dfname varchar(20),
		dlname varchar(20),
    dcontact varchar(10),
    demail varchar (15),
    dpassword varchar(20),
    daddr1 varchar(20),
    daddr2 varchar(20),
		dcity varchar(20),
		dparish varchar(12),
		primary key(dtrn)
		);
create table operator(
		opID int (5),
		ofname varchar(20),
		olname varchar(20),
		otrn int(10),
    oadd1 varchar(20),
    oadd2 varchar(20),
    ocity varchar(20),
		oparish varchar(12),
		primary key(opID)
		);
create table vehicle(
		plateNum varchar(8),
		vmodel varchar(10),
		vmake varchar(15),
		vcolour varchar(10),
		seat_cap int(1),
		class varchar(10),
		primary key(plateNum)
		);
