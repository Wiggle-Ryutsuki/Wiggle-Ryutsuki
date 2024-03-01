-- Keep a log of any SQL queries you execute as you solve the mystery.


-- Check crime report for the kidnapping of CS50 Duck, let's get more details of the crime
SELECT description FROM crime_scene_reports WHERE
  MONTH = 7
  AND DAY = 28
  AND YEAR = 2021
  AND street = "Humphrey Street";
-- Result: Time given (10:15am), Place (Humphrey Street Bakery), Witnesses (3) all mention the bakery


-- Let's check the witnesses' statements
SELECT name, transcript FROM interviews WHERE
  MONTH = 7
  AND DAY = 28
  AND YEAR = 2021;
-- Result: Witness 1(Within 10 minutes, thief drove away), Witness 2(Witnessed thief on Legget Street withdrawing money earlier in the morning),
-- Witness 3(Thief called someone for less than a minute telling them of his plans to leave TOMORROW on the earliest flight, asked his accomplice to purchase tickets)


-- Status: The license place and bank account should belong to the thief, leading to his identity || accomplice identity unknown (should be the receiver of the phonecall)

--Witness 1(Within 10 minutes, thief drove away)
-- Let's check for license plates from the bakery security footage (from around 10:15 to the next 10 minutes)
SELECT license_plate FROM bakery_security_logs WHERE
  MONTH = 7
  AND DAY = 28
  AND YEAR = 2021
  AND HOUR = 10
  AND MINUTE >= 15
  AND MINUTE <= 25;
-- Result: 8 licenses


-- Let's check for suspects who match these license_plates
SELECT name FROM people WHERE
  license_plate IN (
    SELECT license_plate FROM bakery_security_logs WHERE
      MONTH = 7
      AND DAY = 28
      AND YEAR = 2021
      AND HOUR = 10
      AND MINUTE > 15
      AND MINUTE < 25
  );
-- Result: 8 names, suspects are likely the last 2 people (Kelsey, Bruce);

-- Witness 2(Witnessed thief on Legget Street withdrawing money earlier in the morning)
-- Let's check the bank information
SELECT account_number FROM atm_transactions WHERE
  atm_location = "Leggett Street"
  AND MONTH = 7
  AND DAY = 28
  AND YEAR = 2021;


-- Now check for id relating to these accounts
SELECT person_id FROM bank_accounts WHERE
  account_number IN (
    SELECT account_number FROM atm_transactions WHERE
      atm_location = "Leggett Street"
      AND MONTH = 7
      AND DAY = 28
      AND YEAR = 2021
  );


-- Now check for names relating to the license plate AND id
SELECT p.name FROM people p
JOIN bakery_security_logs b ON p.license_plate = b.license_plate AND b.MONTH = 7 AND b.DAY = 28 AND b.YEAR = 2021 AND b.HOUR = 10 AND b.MINUTE > 15 AND b.MINUTE < 25
JOIN atm_transactions a ON ba.account_number = a.account_number AND a.atm_location = "Leggett Street" AND a.transaction_type = "withdraw" AND a.MONTH = 7 AND a.DAY = 28 AND a.YEAR = 2021
JOIN bank_accounts ba ON p.id = ba.person_id;
-- Result: Suspects narrowed down to 4 people (Iman, Luca, Diana, Bruce)

-- NOTE: most recurring name -> Bruce (main suspect)


-- Now lets check phone logs that took place near 10:15am

-- Information about caller
SELECT caller FROM phone_calls WHERE
  MONTH = 7
  AND DAY = 28
  AND YEAR = 2021
  AND duration < 60;


-- Information about receiver
SELECT receiver FROM phone_calls WHERE
  MONTH = 7
  AND DAY = 28
  AND YEAR = 2021
  AND duration < 60;


-- Match caller number to identity of main thief suspects
SELECT p.name FROM people p
JOIN bakery_security_logs b ON p.license_plate = b.license_plate AND b.MONTH = 7 AND b.DAY = 28 AND b.YEAR = 2021 AND b.HOUR = 10 AND b.MINUTE > 15 AND b.MINUTE < 25
JOIN bank_accounts ba ON p.id = ba.person_id
JOIN atm_transactions a ON ba.account_number = a.account_number AND a.atm_location = "Leggett Street" AND a.transaction_type = "withdraw" AND a.MONTH = 7 AND a.DAY = 28 AND a.YEAR = 2021
JOIN phone_calls pc ON p.phone_number = pc.caller AND pc.MONTH = 7 AND pc.DAY = 28 AND pc.YEAR = 2021 AND pc.duration < 60;

-- Result: narrowed down to 2 suspects for the thief (Diana, Bruce)


-- Match receiver phone number to suspects for the accomplice
SELECT name FROM people WHERE
  phone_number IN (
    SELECT receiver FROM phone_calls WHERE
      MONTH = 7
      AND DAY = 28
      AND YEAR = 2021
      AND duration < 60
  );

-- Result: 9 suspects (James, Larry, Anna, Jack, Melissa, Jacqueline, Philip, Robin, Doris)


-- QUICK SUMMARY: Main suspects for the thief (Diana, Bruce)
--  Suspects for the accomplice (James, Larry, Anna, Jack, Melissa, Jacqueline, Philip, Robin, Doris)


-- Time to check for passports related to these suspects
-- Main thief suspects
SELECT p.passport_number FROM people p
JOIN bakery_security_logs b ON p.license_plate = b.license_plate AND b.MONTH = 7 AND b.DAY = 28 AND b.YEAR = 2021 AND b.HOUR = 10 AND b.MINUTE > 15 AND b.MINUTE < 25
JOIN bank_accounts ba ON p.id = ba.person_id
JOIN atm_transactions a ON ba.account_number = a.account_number AND a.atm_location = "Leggett Street" AND a.transaction_type = "withdraw" AND a.MONTH = 7 AND a.DAY = 28 AND a.YEAR = 2021
JOIN phone_calls pc ON p.phone_number = pc.caller AND pc.MONTH = 7 AND pc.DAY = 28 AND pc.YEAR = 2021 AND pc.duration < 60;

-- Result: 2 passport numbers (3592750733 | 5773159633 )

-- Check what the town's airport id is
SELECT id FROM airports WHERE
  city = "Fiftyville";


-- Check next days flights:
SELECT * FROM flights WHERE
  origin_airport_id IN (
    SELECT id FROM airports WHERE
      city = "Fiftyville")
  AND MONTH = 7
  AND DAY = 29
  AND YEAR = 2021;


-- Check the id for the earliest flight
SELECT id FROM flights WHERE hour = (SELECT MIN(hour) FROM flights WHERE origin_airport_id IN (
  SELECT id FROM airports WHERE
     city = "Fiftyville")
  AND MONTH = 7
  AND DAY = 29
  AND YEAR = 2021) AND MONTH = 7
  AND DAY = 29
  AND YEAR = 2021 LIMIT 1;


--Check for passengers on this plane
SELECT ps.passport_number FROM passengers ps
JOIN flights f ON ps.flight_id = f.id
JOIN airports a ON f.origin_airport_id = a.id
WHERE f.hour = (SELECT MIN(hour) FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND MONTH = 7 AND DAY = 29 AND YEAR = 2021)
  AND f.MONTH = 7
  AND f.DAY = 29
  AND f.YEAR = 2021;


-- Check for names matching to any of these passports AND our suspect passports
SELECT p.name FROM people p
JOIN passengers ps ON p.passport_number = ps.passport_number
JOIN flights f ON ps.flight_id = f.id
JOIN airports a ON f.origin_airport_id = a.id
WHERE f.hour = (SELECT MIN(hour) FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND MONTH = 7 AND DAY = 29 AND YEAR = 2021)
  AND f.MONTH = 7
  AND f.DAY = 29
  AND f.YEAR = 2021
  AND p.passport_number IN (
    SELECT p.passport_number FROM people p
    JOIN bakery_security_logs b ON p.license_plate = b.license_plate AND b.MONTH = 7 AND b.DAY = 28 AND b.YEAR = 2021 AND b.HOUR = 10 AND b.MINUTE > 15 AND b.MINUTE < 25
    JOIN bank_accounts ba ON p.id = ba.person_id
    JOIN atm_transactions a ON ba.account_number = a.account_number AND a.atm_location = "Leggett Street" AND a.transaction_type = "withdraw" AND a.MONTH = 7 AND a.DAY = 28 AND a.YEAR = 2021
    JOIN phone_calls pc ON p.phone_number = pc.caller AND pc.MONTH = 7 AND pc.DAY = 28 AND pc.YEAR = 2021 AND pc.duration < 60
  );
--RESULT: THE CULPRIT IS BRUCE


-- Where was he flying to?
SELECT destination_airport_id FROM flights WHERE id IN (SELECT id FROM flights WHERE hour = (SELECT MIN(hour) FROM flights WHERE origin_airport_id IN (
    SELECT id FROM airports WHERE
      city = "Fiftyville")
    AND MONTH = 7
    AND DAY = 29
    AND YEAR = 2021) AND MONTH = 7
    AND DAY = 29
    AND YEAR = 2021 LIMIT 1);

SELECT * FROM airports WHERE id IN (SELECT destination_airport_id FROM flights WHERE id IN (SELECT id FROM flights WHERE hour = (SELECT MIN(hour) FROM flights WHERE origin_airport_id IN (
    SELECT id FROM airports WHERE
      city = "Fiftyville")
    AND MONTH = 7
    AND DAY = 29
    AND YEAR = 2021) AND MONTH = 7
    AND DAY = 29
    AND YEAR = 2021 LIMIT 1));
-- Result: New York City


-- WHO IS THE ACCOMPLICE?

--Find Bruce's phone number
SELECT phone_number FROM people WHERE name IN (SELECT p.name FROM people p
JOIN passengers ps ON p.passport_number = ps.passport_number
JOIN flights f ON ps.flight_id = f.id
JOIN airports a ON f.origin_airport_id = a.id
WHERE f.hour = (SELECT MIN(hour) FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND MONTH = 7 AND DAY = 29 AND YEAR = 2021)
  AND f.MONTH = 7
  AND f.DAY = 29
  AND f.YEAR = 2021
  AND p.passport_number IN (
    SELECT p.passport_number FROM people p
    JOIN bakery_security_logs b ON p.license_plate = b.license_plate AND b.MONTH = 7 AND b.DAY = 28 AND b.YEAR = 2021 AND b.HOUR = 10 AND b.MINUTE > 15 AND b.MINUTE < 25
    JOIN bank_accounts ba ON p.id = ba.person_id
    JOIN atm_transactions a ON ba.account_number = a.account_number AND a.atm_location = "Leggett Street" AND a.transaction_type = "withdraw" AND a.MONTH = 7 AND a.DAY = 28 AND a.YEAR = 2021
    JOIN phone_calls pc ON p.phone_number = pc.caller AND pc.MONTH = 7 AND pc.DAY = 28 AND pc.YEAR = 2021 AND pc.duration < 60));


--Find the call receiver from yesterdays call logs during the time of theft
SELECT receiver FROM phone_calls WHERE caller in (SELECT phone_number FROM people WHERE name IN (SELECT p.name FROM people p
JOIN passengers ps ON p.passport_number = ps.passport_number
JOIN flights f ON ps.flight_id = f.id
JOIN airports a ON f.origin_airport_id = a.id
WHERE f.hour = (SELECT MIN(hour) FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND MONTH = 7 AND DAY = 29 AND YEAR = 2021)
  AND f.MONTH = 7
  AND f.DAY = 29
  AND f.YEAR = 2021
  AND p.passport_number IN (
    SELECT p.passport_number FROM people p
    JOIN bakery_security_logs b ON p.license_plate = b.license_plate AND b.MONTH = 7 AND b.DAY = 28 AND b.YEAR = 2021 AND b.HOUR = 10 AND b.MINUTE > 15 AND b.MINUTE < 25
    JOIN bank_accounts ba ON p.id = ba.person_id
    JOIN atm_transactions a ON ba.account_number = a.account_number AND a.atm_location = "Leggett Street" AND a.transaction_type = "withdraw" AND a.MONTH = 7 AND a.DAY = 28 AND a.YEAR = 2021
    JOIN phone_calls pc ON p.phone_number = pc.caller AND pc.MONTH = 7 AND pc.DAY = 28 AND pc.YEAR = 2021 AND pc.duration < 60))) AND MONTH = 7
  AND DAY = 28
  AND YEAR = 2021
  AND duration < 60;

  -- Find receivers information
  SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE caller in (SELECT phone_number FROM people WHERE name IN (SELECT p.name FROM people p
JOIN passengers ps ON p.passport_number = ps.passport_number
JOIN flights f ON ps.flight_id = f.id
JOIN airports a ON f.origin_airport_id = a.id
WHERE f.hour = (SELECT MIN(hour) FROM flights WHERE origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") AND MONTH = 7 AND DAY = 29 AND YEAR = 2021)
  AND f.MONTH = 7
  AND f.DAY = 29
  AND f.YEAR = 2021
  AND p.passport_number IN (
    SELECT p.passport_number FROM people p
    JOIN bakery_security_logs b ON p.license_plate = b.license_plate AND b.MONTH = 7 AND b.DAY = 28 AND b.YEAR = 2021 AND b.HOUR = 10 AND b.MINUTE > 15 AND b.MINUTE < 25
    JOIN bank_accounts ba ON p.id = ba.person_id
    JOIN atm_transactions a ON ba.account_number = a.account_number AND a.atm_location = "Leggett Street" AND a.transaction_type = "withdraw" AND a.MONTH = 7 AND a.DAY = 28 AND a.YEAR = 2021
    JOIN phone_calls pc ON p.phone_number = pc.caller AND pc.MONTH = 7 AND pc.DAY = 28 AND pc.YEAR = 2021 AND pc.duration < 60))) AND MONTH = 7
  AND DAY = 28
  AND YEAR = 2021
  AND duration < 60)
  AND name IN (SELECT name FROM people WHERE
  phone_number IN (
    SELECT receiver FROM phone_calls WHERE
      MONTH = 7
      AND DAY = 28
      AND YEAR = 2021
      AND duration < 60
  ));

  -- RESULT: THE ACCOMPLICE IS ROBIN

  -- SUMMARY: The thief is Bruce, he fled to New York City, His accomplice is Robin
