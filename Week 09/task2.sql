----- First Queries -----
----- 1 -----
SELECT address
  FROM STUDIO
  WHERE name = "MGM";

----- 2 -----
SELECT birthdate
  FROM MOVIESTAR
  WHERE name = "Kim Basinger";

----- 3 -----
SELECT name
  FROM MOVIEEXEC
  WHERE networth > 10000000;

----- 4 -----
SELECT name
  FROM MOVIESTAR
  WHERE gender = "M" or address = "Prefect Rd.";

----- 5 -----
INSERT INTO MOVIESTAR
  VALUES ("Zahari Baharov", "Y path", "M", "1980-08-12")

----- 6 -----
DELETE FROM STUDIO
  WHERE address LIKE "%5%";

----- 7 -----
UPDATE MOVIE
  SET studioname = "Fox"
  WHERE title LIKE "%star%";


----- Relations -----
----- 1, 2 -----
SELECT name
  FROM STARSIN
  JOIN MOVIESTAR ON STARSIN.starname = MOVIESTAR.name
  WHERE STARSIN.movietitle = "Terms of Endearment"
    AND MOVIESTAR.gender = "M";

----- 3 -----
SELECT starname
  FROM STARSIN
  JOIN MOVIE ON STARSIN.movietitle = MOVIE.title
  WHERE STARSIN.movieyear = 1995
    AND MOVIE.studioname = "MGM";

----- 4 -----
ALTER TABLE STUDIO
  ADD COLUMN presidentname VARCHAR(30);

UPDATE STUDIO
  SET presidentname = "Darcie Denkert"
  WHERE name = "MGM";
UPDATE STUDIO
  SET presidentname = "Doris Walker"
  WHERE name = "USA Entertainm.";

SELECT presidentname
  FROM STUDIO
  WHERE name = "MGM";
