SELECT  COUNTRY.Continent, floor(avg(CITY.Population)) 
FROM CITY 
INNER JOIN COUNTRY  ON CITY.CountryCode = COUNTRY.Code 
GROUP BY 
    COUNTRY.Continent;
