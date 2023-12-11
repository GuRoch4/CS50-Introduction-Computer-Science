-- Keep a log of any SQL queries you execute as you solve the mystery.

-- first i used the keyword "duck" to find a crime related to it
select * from crime_scene_reports
where description like "%duck%";
-- | 295 | 2021 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |


-- then I searched about the interviews that talked about "bakery"
select * from interviews
where transcript like "%bakery%";
-- | 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
-- | 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
-- | 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
-- | 192 | Kiana   | 2021 | 5     | 17  | I saw Richard take a bite out of his pastry at the bakery before his pastry was stolen from him.


-- I got to security seeing all the exits
select * from bakery_security_logs
where day = 28 and hour = 10 and activity = "exit";
-- +-----+------+-------+-----+------+--------+----------+---------------+
-- | id  | year | month | day | hour | minute | activity | license_plate |
-- +-----+------+-------+-----+------+--------+----------+---------------+
-- | 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
-- | 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
-- | 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
-- | 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
-- | 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
-- | 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
-- | 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
-- | 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
-- | 268 | 2021 | 7     | 28  | 10   | 35     | exit     | 1106N58       |
-- +-----+------+-------+-----+------+--------+----------+---------------+
-- Identify the plates
select people.name, b.license_plate
from bakery_security_logs b
join people on people.license_plate = b.license_plate
where b.day = 28 and b.hour = 10 and b.activity = "exit";
-- +---------+---------------+
-- |  name   | license_plate |
-- +---------+---------------+
-- | Vanessa | 5P2BI95       |--
-- | Bruce   | 94KL13X       |
-- | Barry   | 6P58WS2       |--
-- | Luca    | 4328GD8       |--
-- | Sofia   | G412CB7       |--
-- | Iman    | L93JTIZ       |--
-- | Diana   | 322W7JE       |
-- | Kelsey  | 0NTHK55       |--
-- | Taylor  | 1106N58       |..
-- +---------+---------------+


-- I got the transactions made on the day
select * from atm_transactions
where atm_location = "Leggett Street" and day = 28;
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+
-- | id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+
-- | 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     |
-- | 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
-- | 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     |
-- | 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     |
-- | 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     |
-- | 275 | 86363979       | 2021 | 7     | 28  | Leggett Street | deposit          | 10     |
-- | 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
-- | 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     |
-- | 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     |
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+
--identified the account_number
select atm.account_number,ba.account_number, p.name
from atm_transactions atm
join bank_accounts ba on ba.account_number = atm.account_number
join people p on p.id = ba.person_id
where atm.atm_location = "Leggett Street" and day = 28;
-- +----------------+----------------+---------+
-- | account_number | account_number |  name   |
-- +----------------+----------------+---------+
-- | 49610011       | 49610011       | Bruce   |
-- | 86363979       | 86363979       | Kaelyn  |--
-- | 26013199       | 26013199       | Diana   |
-- | 16153065       | 16153065       | Brooke  |--
-- | 28296815       | 28296815       | Kenny   |--
-- | 25506511       | 25506511       | Iman    |--
-- | 28500762       | 28500762       | Luca    |--
-- | 76054385       | 76054385       | Taylor  |..
-- | 81061156       | 81061156       | Benista |--
-- +----------------+----------------+---------+



-- list of calls made in less than 60 minutes
select * from phone_calls
where duration < 60 and day = 28;
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | id  |     caller     |    receiver    | year | month | day | duration |
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       |
-- | 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       |
-- | 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
-- | 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       |
-- | 254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7     | 28  | 43       |
-- | 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
-- | 261 | (031) 555-6622 | (910) 555-3251 | 2021 | 7     | 28  | 38       |
-- | 279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7     | 28  | 55       |
-- | 281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7     | 28  | 54       |
-- +-----+----------------+----------------+------+-------+-----+----------+
-- calls made with the name of the caller
select pc.caller, pc.receiver, p.name
from phone_calls pc
join people p on p.phone_number = pc.caller
where pc.duration < 60 and day = 28;
-- +----------------+----------------+---------+
-- |     caller     |    receiver    |  name   |
-- +----------------+----------------+---------+
-- | (130) 555-0289 | (996) 555-8899 | Sofia   |--
-- | (499) 555-9472 | (892) 555-8872 | Kelsey  |--
-- | (367) 555-5533 | (375) 555-8161 | Bruce   |
-- | (499) 555-9472 | (717) 555-1342 | Kelsey  |--
-- | (286) 555-6063 | (676) 555-6554 | Taylor  |..
-- | (770) 555-1861 | (725) 555-3243 | Diana   |
-- | (031) 555-6622 | (910) 555-3251 | Carina  |--
-- | (826) 555-1652 | (066) 555-9701 | Kenny   |--
-- | (338) 555-6650 | (704) 555-2131 | Benista |--
-- +----------------+----------------+---------+



-- I checked the airport fiftyville that have id (8)
select * from airports;
-- flights from fifty
select * from flights
where origin_airport_id = 8 and day = 29 order by hour ;
--selecting passengers from the earlier flight with the destination of(destination 4)LaGuardia Airport
select * from passengers
where flight_id = 36;
-- passengers with the name
select p.name, p.passport_number, ps.passport_number
from passengers ps
join people p on p.passport_number = ps.passport_number
where ps.flight_id = 36;
-- +--------+-----------------+-----------------+
-- |  name  | passport_number | passport_number |
-- +--------+-----------------+-----------------+
-- | Doris  | 7214083635      | 7214083635      |--
-- | Sofia  | 1695452385      | 1695452385      |--
-- | Bruce  | 5773159633      | 5773159633      |
-- | Edward | 1540955065      | 1540955065      |--
-- | Kelsey | 8294398571      | 8294398571      |--
-- | Taylor | 1988161715      | 1988161715      |--
-- | Kenny  | 9878712108      | 9878712108      |--
-- | Luca   | 8496433585      | 8496433585      |--
-- +--------+-----------------+-----------------+

-- I didn't select to discovery the thief, but analyzing the lists I realized that Bruce stole it, because he is in all the selects


-- now i found out who helped him
select pc.receiver, p.name
from phone_calls pc
join people p on p.phone_number = pc.receiver
where pc.caller = (
    select p.phone_number
    from people p
    where p.name = "Bruce")
    and pc.duration < 60 and day = 28;