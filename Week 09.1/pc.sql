SELECT AVG(speed) FROM pc;

SELECT maker, AVG(screen)
  FROM (SELECT * FROM laptop
          JOIN product
            ON laptop.model = product.model)
  GROUP BY maker;

SELECT AVG(speed)
  FROM laptop
  WHERE price > 1000;

SELECT hd, AVG(price)
  FROM pc
  GROUP BY hd;

SELECT AVG(price)
  FROM pc
  WHERE speed > 500;

SELECT AVG(price)
  FROM (SELECT * FROM product
        JOIN pc ON pc.model = product.model
        WHERE maker = 'A');

SELECT AVG(price)
  FROM (SELECT * FROM product
        JOIN pc ON pc.model = product.model
        UNION
        SELECT * FROM product
        JOIN laptop ON laptop.model = product.model)
  WHERE maker = 'B';

SELECT maker
  FROM (SELECT maker, COUNT(model) AS CM
      FROM (SELECT * FROM product
            JOIN pc ON pc.model = product.model
            GROUP BY pc.model)
    GROUP BY maker)
  WHERE CM > 2;

SELECT maker
  FROM (SELECT MAX(price), maker FROM pc
        JOIN product ON pc.model = product.model);

SELECT AVG(cd)
  FROM (SELECT model
          FROM (SELECT maker FROM product
                  WHERE type = 'Printer'
                  GROUP BY maker) AS makers
          JOIN product ON makers.maker = product.maker
          WHERE type = 'PC') AS models
  JOIN pc ON pc.model = models.model;