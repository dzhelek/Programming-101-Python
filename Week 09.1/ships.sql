-- name; country; numguuns; launched
SELECT name, country, numguns, launched
  FROM (SELECT * FROM ships
        JOIN classes ON classes.class = ships.class);

----- -----
SELECT name, country, numguns, launched
  FROM (SELECT * FROM classes
        LEFT JOIN ships ON classes.class = ships.class)
  WHERE (SELECT COUNT(class) FROM
    (SELECT class
     FROM (SELECT * FROM classes
           LEFT JOIN ships ON classes.class = ships.class)
       AS shipsandclasses
     WHERE shipsandclasses.name IS NULL)) > 0;

----- -----
SELECT ship FROM outcomes
  WHERE battle = (SELECT name FROM battles
                    WHERE date BETWEEN '1942-01-01' AND '1942-12-31');

----- -----
SELECT name, country  FROM
  (SELECT name, class FROM ships
    LEFT JOIN outcomes ON ships.name = outcomes.ship
    WHERE outcomes.ship IS NULL) AS notbattledships
  LEFT JOIN classes ON notbattledships.class = classes.class;