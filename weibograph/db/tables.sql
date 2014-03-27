DROP TABLE if exists user;
DROP TABLE if exists relation;

CREATE TABLE user (
	uid			varchar(20) PRIMARY KEY,
	nick		varchar(30) NOT NULL,
	follows		integer NOT NULL,
	fans		integer NOT NULL,
	db_follows	integer NOT NULL DEFAULT 0,
	db_fans		integer NOT NULL DEFAULT 0,
	create_time	timestamp NOT NULL,
	modify_time	timestamp NOT NULL
);

CREATE TABLE relation (
	source varchar(20),
	target varchar(20),
	PRIMARY KEY(source, target)
);

