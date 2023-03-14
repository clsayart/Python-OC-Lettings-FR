PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

INSERT INTO lettings_address VALUES(1,7217,'Bedford Street','Brunswick','GA',31525,'USA');
INSERT INTO lettings_address VALUES(2,4,'Military Street','Willoughby','OH',44094,'USA');
INSERT INTO lettings_address VALUES(3,340,'Wintergreen Avenue','Newport News','VA',23601,'USA');
INSERT INTO lettings_address VALUES(4,9230,'E. Joy Ridge Street','Marquette','MI',49855,'USA');
INSERT INTO lettings_address VALUES(5,9606,'Harvard Street','Aliquippa','PA',15001,'USA');
INSERT INTO lettings_address VALUES(6,588,'Argyle Avenue','East Meadow','NY',11554,'USA');

INSERT INTO lettings_letting VALUES(1,'Joshua Tree Green Haus /w Hot Tub',1);
INSERT INTO lettings_letting VALUES(2,'Oceanview Retreat',2);
INSERT INTO lettings_letting VALUES(3,'''Silo Studio'' Cottage',3);
INSERT INTO lettings_letting VALUES(4,'Pirates of the Caribbean Getaway',4);
INSERT INTO lettings_letting VALUES(5,'The Mushroom Dome Retreat & LAND of Paradise Suite',5);
INSERT INTO lettings_letting VALUES(6,'Underground Hygge',6);
COMMIT;
