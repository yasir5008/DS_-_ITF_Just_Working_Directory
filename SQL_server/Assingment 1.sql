CREATE TABLE assingment1
(
 Sender_ID int,
 Receiver_ID int,
 Amount int,
 Transaction_Date date
 )
 ;


 select *
 from assingment1

 insert into assingment1(Sender_ID,Receiver_ID,Amount,Transaction_Date) 
 VALUES(55, 22, 500, '2021-05-18'),
(11, 33, 350, '2021-05-19'),
(22, 11, 650, '2021-05-19'),
(22, 33, 900, '2021-05-20'),
(33, 11, 500, '2021-05-21'),
(33, 22, 750, '2021-05-21'),
(11, 44, 300,  '2021-05-22')

Select [Sender_ID],sum(amount) as debits
from assingment1
group by Sender_ID


Select Receiver_ID,sum(amount) as credits
from assingment1
group by Receiver_ID

CREATE TABLE debits
(Select [Sender_ID],sum(amount) as debits
from assingment1
group by Sender_ID)

select a.Sender_ID as Account_ID, (b.credits - a.debits) as Net_Change
FROM (
		Select [Sender_ID],sum(amount) as debits
		from assingment1
		group by Sender_ID
		) a

full  join

		(Select Receiver_ID,sum(amount) as credits
			from assingment1
			group by Receiver_ID
			) b

on a.Sender_ID = b.Receiver_ID

select COALESCE(a.Sender_ID,b.Receiver_ID) as Account_ID,
		coalesce(b.credits, 0)-coalesce(a.debits, 0) as Net_Change
	
FROM (
		Select [Sender_ID],sum(amount) as debits
		from assingment1
		group by Sender_ID
		) a

full  join

		(Select Receiver_ID,sum(amount) as credits
			from assingment1
			group by Receiver_ID
			) b

on a.Sender_ID = b.Receiver_ID