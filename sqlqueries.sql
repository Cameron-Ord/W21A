insert into item (name, description, price, created_at)
values
('Chair','This is a chair',150,'2023-11-23'),
('Table','This is a table',250,'2023-09-22'),
('Dresser','This is a dresser',300,'2022-11-20'),
('Sofa','This is a sofa',300,'2020-12-19'),
('Chair','This is a chair',250,'2021-11-13'),
('TV','This is a TV',600,'2021-02-23'),
('TV','This is a TV',300,'2023-06-17'),
('Bed','This is a bed',400,'2023-07-13'),
('Desk','This is a desk',125,'2020-07-19'),
('Stove','This is a stove',225,'2021-01-19');


insert into employee (name, `position`, hired_at, hourly_wage)
values
('Henry','Clerk','2018-10-21', 17),
('Jacob','Sales','2022-10-18', 20),
('Aaron','Clerk','2012-12-15', 22),
('Cassandra','Sales','2020-09-18',21),
('Jewel','Janitor','2012-04-19', 20);

call patch_idprice(2, 500);
call delete_item(2);
call insert_employee('Alex', 'Clerk', 15);
call return_spec_employee(4); 