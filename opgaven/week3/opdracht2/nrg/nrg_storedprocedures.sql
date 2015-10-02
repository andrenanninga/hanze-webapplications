USE `nrg`;

DROP procedure IF EXISTS `sp_createUser`;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
	IN p_naam VARCHAR(45),
    IN p_email VARCHAR(64),
    IN p_wachtwoord VARCHAR(64),
	IN p_telefoonnummer INT(20)

)
BEGIN
    if ( select exists (select 1 from gebruiker where email = p_email) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into gebruiker
        (
			naam,
            email,
            wachtwoord,
            telefoonnummer
        )
        values
        (
			p_naam,
            p_email,
            p_wachtwoord,
            p_telefoonnummer
        );
     
    END IF;
END$$
DELIMITER ;

DROP procedure IF EXISTS `sp_validateLogin`;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_validateLogin`(
IN p_email VARCHAR(20)
)
BEGIN
    select * from gebruiker where email = p_email;
END$$
DELIMITER ;


DROP procedure IF EXISTS `sp_getHouseholdByUser`;
DELIMITER $$
CREATE PROCEDURE `sp_getHouseholdByUser` (
IN p_gebruikerID bigint
)
BEGIN
    select * from huishouden_gebruiker where gebruiker_fk = p_gebruikerID;
END$$
 
DELIMITER ;

DROP procedure IF EXISTS `sp_getHouseholdByUser`;
DELIMITER $$
CREATE PROCEDURE `sp_getHouseholdByUser` (
IN p_huishoudenID bigint
)
BEGIN
    select * from apparaat_huishouden where huishouden_fk = p_huishoudenID;
END$$
 
DELIMITER ;

DROP procedure IF EXISTS `sp_getDeviceById`;
DELIMITER $$
CREATE PROCEDURE `sp_getDeviceById` (
IN p_appraatID bigint
)
BEGIN
    select * from apparaat where id = p_apparaatID;
END$$
 
DELIMITER ;
