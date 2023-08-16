## SQL Showcase

Assuming a table A containing members, and the dates when they gained eligibility, lost eligibility and when they signed up.
Assuming a table B containing marketing outreach completed to the different members, and the dates of the outreach attempts.

**Question 1**: 
How many wasted marketing touchpoints are being sent out (wasted touchpoints = sent to either members already signed up or no longer eligible.)?
~~~~sql
-- Here I am transforming the table by making ID the unique key and transforming multiple rows for the different actions into columns.
WITH pivoted as (
SELECT id
, date AS eligible_date
, coalesce(lost_date,'3000-12-31') AS lost_date
, coalesce(signup_date,'3000-12-31') AS signup_date
FROM table_A 
  LEFT JOIN (
    SELECT id
      , date as lost_date
    FROM table_A 
    WHERE action ='eligibility lost'
  ) lost using (id)
  LEFT JOIN (
    SELECT id
      , date as signup_date
    FROM table_A 
    WHERE action ='signed up'
  ) signup using (id)
where   action ='eligibility gained'
)
-- Here I am joining together the tables and counting touchpoints
-- Since I am not counting distinct I can use user_id to count the rows
-- This is assuming that the user_id column is not empty, this should be verified and otherwise corrected.
-- I am using safe_divide to ensure downstream
SELECT COUNT(CASE WHEN table_b.date>lost_date OR table_b.date>signup_date THEN user_id ELSE null END) AS wasted_touchpoints
, count(*) AS total_touchpoints
, safe_divide(count(CASE WHEN table_b.date>lost_date OR tableb.date>signup_date THEN user_id ELSE null END),count(*)) AS perc_wasted
FROM table_b
LEFT JOIN pivoted ON table_b.user_id=pivoted.id
~~~~

Question 2: 
Churn per month (defined as members losing eligibilty in a month / members with eligibility on the last day of the previous month)
~~~~sql
     -- Here I am transforming the table by making ID the unique key and transforming multiple rows for the different actions into columns.
    WITH pivoted as (
    SELECT id
    , date AS eligible_date
    , coalesce(lost_date,'3000-12-31') AS lost_date
    FROM table_A 
      LEFT JOIN (
        SELECT id
          , date as lost_date
        FROM table_A 
        WHERE action ='eligibility lost'
      ) lost using (id)
    where   action ='eligibility gained'
    )
    -- I am creating a list of all months that this should be created for. I could have used a select distinct from the table itself instead of the GENERATE_DATE_ARRAY function, but both should work equally well.
    , date_spine as (
      GENERATE_DATE_ARRAY(min(date_trunc(eligible_date,MONTH)), max(date_trunc(eligible_date,MONTH)), INTERVAL 1 MONTH)
      from table_A
      )
      -- here I am creating the list of eligibles and churned members in each month.
    , aggregated as (
      select month
      ,count(distinct id) AS eligibles
      -- if their last date of eligibility is in this month they count as churned in this month
      , count(case when month=date_trunc(lost_date,month) then id else null end) as churned
      left join pivoted 
      -- if a member has lost eligibility in or after this month and has gained eligibility before this month, then they will be counted for this month
        on month<= lost_date and month>=date_trunc(eligible_date,month)
        group by 1
      )
      -- here I am comparing the churn in a certain month to the eligibles in the previous line as sorted by the month.
      select month, safe_divide(churned,LAG(eligibles)
    OVER (PARTITION BY month ORDER BY month ASC)) AS perc_churned
    from aggregated
    group by 1 order by 1 desc
~~~~
#### Part 2: 
Assuming a table of employee, manager and employee age. Please return a table containing each manager's team size and their team's average age. 
- In the first step assume there is only 2 levels of hierarchy.
~~~~sql
      SELECT manager
      , count(distinct employee) total_employees
      , round(avg(age,2) as average_age
      FROM base 
      GROUP BY 1 
      ORDER BY 1 desc
~~~~
- In the second step, please return all members underneath a manager including teams of other managers.
~~~~sql
      with recursive_base as (
          select employee, manager,age
          from base 
          where manager is null
      UNION ALL 
      (
          select b.employee, b.manager,b.age
          from base b
          join recursive_base rb on b.manager=rb.employee
      UNION ALL 
          select b.employee, rb.manager,b.age
          from base b
          join recursive_base rb on b.manager=rb.employee
      )
      )
      select manager, count(distinct employee) total_employees, round(avg(age,2) as average_age
      from recursive_base
      group by 1 order by 1 desc
~~~~
