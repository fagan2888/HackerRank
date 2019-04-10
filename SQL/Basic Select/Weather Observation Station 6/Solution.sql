/*
Enter your query here.
Please append a semicolon ';' at the end of the query and enter your query in a single line to avoid error.
*/
select distinct CITY from station where LOWER(CITY) like 'a%' or LOWER(CITY) like 'e%' or LOWER(CITY) like 'i%' or LOWER(CITY) like 'o%' or LOWER(CITY) like 'u%';
