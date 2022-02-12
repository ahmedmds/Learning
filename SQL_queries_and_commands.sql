SELECT *, EXTRACT (YEAR FROM AGE(birth_date)) as "age" FROM public.employees where first_name like 'M%';

select count(emp_no) from public.employees where first_name like 'A%r'

select count(customerid) from public.customers where zip::text like '%2%'

select count(customerid) from public.customers where zip::text like '2_1%'

select coalesce(state, 'No State') as state from public.customers where cast(phone as text) like '302%'






show TIMEZONE

create table public.timezones (
ts timestamp without time ZONE,
tz timestamp with time zone)

insert into public.timezones values (
timestamp without time zone '2000-05-01 10:00:00-05' ,
timestamp with time zone '2000-05-01 10:00:00-05')

select * from public.timezones


select now()::date;
select current_date;
select now()::timestamp;

select to_char(now()::date, 'dd/mm/yyyy')

select now()::date  - date '1992/09/24'

select now() - '1800/01/01'

select age(date '1992/09/24')

select age(date '1992/09/24', '1992/09/23')

select extract (day from date '2022/01/23') as day;
select extract (month from date '2022/01/23') as month;
select extract (year from date '2022/01/23') as year;
select extract (week from date '2022/01/24') as week;

select date_trunc('year', date '1992/11/13')
SELECT date_trunc('month', date '1992/11/13')

select * from public.orders where orderDate >= now() - interval '30 days'

SELECT * FROM public.employees where extract(year FROM age(birth_date))>60;

SELECT count(emp_no) FROM public.employees where extract (month from hire_date) = 2;

SELECT count(emp_no) FROM public.employees where extract (month from birth_date) = 11;

SELECT MAX(AGE(birth_date)) FROM public.employees;




SELECT count(orderid) FROM public.orders where extract (month from orderDate) = 1 and extract (year from orderDate) = 2004;
SELECT COUNT(orderid) FROM public.orders WHERE DATE_TRUNC('month', orderdate) = date '2004-01-01';




select distinct(title) from public.titles

select distinct(birth_date) from public.employees

select distinct(lifeexpectancy) from public.country where lifeexpectancy is not null order by lifeexpectancy DESC



select * from public.employees order by first_name asc, last_name DESC

select * from public.employees order by age(birth_date)

select * from public.employees where first_name ilike 'k%' order by hire_date



select a.first_name, c.dept_name from public.employees as a inner join public.dept_emp as b on b.emp_no = a.emp_no inner join public.departments as c on c.dept_no = b.dept_no

select prod.prod_id, prod.title, inv.quan_in_stock, inv.sales  from public.products as prod inner join public.inventory as inv on inv.prod_id = prod.prod_id

select cust.customerid, cust.state, ord.orderid, ord.orderdate, ord.totalamount from public.orders as ord
inner join public.customers as cust on cust.customerid = ord.customerid
where (cust.state in ('OH', 'NY', 'OR')) order by ord.orderid ASC


select e.hire_date, count(e.emp_no) from public.employees as e group by e.hire_date

select e.emp_no, count(t.title) from public.employees as e inner join public.titles as t on t.emp_no = e.emp_no
where Extract (year from e.hire_date) > 1991 group by e.emp_no order by e.emp_no 


select e.emp_no, de.from_date, de.to_date, de.dept_no from public.employees as e inner join public.dept_emp as de on de.emp_no = e.emp_no 
where de.dept_no = 'd005'
GROUP BY e.emp_no, de.from_date, de.to_date, de.dept_no
ORDER BY e.emp_no, de.to_date;


select e.emp_no, count(t.title) as "amount of titles" from public.employees as e inner join public.titles as t on t.emp_no = e.emp_no
where Extract (year from e.hire_date) > 1991 group by e.emp_no having count(t.title)>2 order by e.emp_no

 
select de.emp_no, count(s.salary) as "amount of raises" from public.dept_emp as de
inner join public.salaries as s on s.emp_no = de.emp_no
where de.dept_no = 'd005'
GROUP BY de.emp_no, de.dept_no
having count(s.salary)>15
ORDER BY de.emp_no;

select e.emp_no, count(de.dept_no) as "worked for # departments" from public.employees as e
inner join public.dept_emp as de on de.emp_no = e.emp_no
GROUP BY e.emp_no
having count(de.dept_no)>1
ORDER BY e.emp_no;

select dept_no as "dept_no", count(de.dept_no) from public.dept_emp as de
Group by grouping sets ( (), (dept_no))

select de.dept_no as "dept_no", avg(salary) from public.salaries as s inner join public.dept_emp as de on de.emp_no = s.emp_no
group by grouping sets ( () , (de.dept_no)  )


select distinct continent, sum(population) over (partition by continent) as "total population", 
concat (round( (sum(population::float4) over (partition by continent) / sum(population::float4) over ()) * 100  )  )
from public.country

select t.name as "town", r.name as "region" from public.towns as t inner join public.regions as r on r.code=t.code

SELECT 
DISTINCT r.id, 
r."name", 
COUNT(t.id) OVER (
    PARTITION BY r.id
    ORDER BY r."name"
) AS "# of towns"
FROM public.regions AS r
JOIN public.departments AS d ON r.code = d.region 
JOIN public.towns AS t ON d.code = t.department
ORDER BY r.id;


Create domain Rating smallint check (value>0 and value <=5);

create type Feedback as (
student_id UUID,
rating Rating,
feedback text);

create extension if not exists "uuid-ossp";
CREATE TABLE student ( 
student_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), 
first_name VARCHAR(255), 
date_of_birth DATE NOT NULL,
feedback Feedback);


drop table student;
select * from student;

select * from pg_available_extensions;


----------------------------------- ZTM database tables (check database model in lecture) -------------------------------------

---- creating tables -------

create extension if not exists "uuid-ossp";

create table student (
student_id UUID PRIMARy KEY default uuid_generate_v4(),
first_name varchar(255) not null,
last_name varchar(255) not null,
date_of_birth DATE not null
)

create table subject (
subject_id UUID PRIMARy KEY default uuid_generate_v4(),
subject TEXT not null,
description TEXT
)

create table teacher (
teacher_id UUID PRIMARy KEY default uuid_generate_v4(),
first_name varchar(255) not null,
last_name varchar(255) not null,
date_of_birth DATE not null,
email TEXT
)

alter table student 
add column email text;

create table course (
course_id UUID PRIMARy KEY default uuid_generate_v4(),
"name" text not null,
description text,
subject_id uuid references subject(subject_id),
teacher_id uuid references teacher(teacher_id),
feedback feedback[]
)

create table enrollment (
course_id UUID references course(course_id),
student_id uuid references student(student_id),
enrollment_date date not null,
constraint pk_enrollment primary key (course_id, student_id)
)


---- adding data -------

insert into student (
first_name,
last_name,
email,
date_of_birth )
values (
'First',
'Last',
'first@last.io',
'1992-11-13'::DATE
);

insert into teacher (
first_name,
last_name,
email,
date_of_birth )
values (
'First',
'Last',
'first@last.io',
'1992-11-13'::DATE
);

insert into subject (
subject,
description
) values (
'SQL Zero to MASTERY',
'The art of SQL mastery'
);
delete from subject where subject = 'SQL Zero to MASTERY';

insert into subject (
subject,
description
) values (
'SQL',
'A database management language'
);

insert into course (
"name",
description
) values (
'SQL zero to mastery',
'The #1 resource for sql mastery'
);
update course set subject_id = 'a3c5f7de-5a8a-4065-9de1-2f652796f0d6' where subject_id is null;

alter table course alter column subject_id set not null;

insert into course ("name", description)
values ('name', 'description');


update course set teacher_id = 'f6e7d65a-e943-4008-b14c-a77e805e18dd' where teacher_id is null;

alter table course alter column teacher_id set not null;


insert into enrollment (student_id, course_id, enrollment_date) values(
'a66f66e0-7aec-424a-b8c9-360c67e05eba',
'907a964f-c91b-43c1-aeb4-e36e8d764615',
NOW()::DATE
);

update course
set feedback = array_append( feedback,
row('a66f66e0-7aec-424a-b8c9-360c67e05eba', --student_id
5, 'great course!')::feedback )
where course_id = '907a964f-c91b-43c1-aeb4-e36e8d764615'
