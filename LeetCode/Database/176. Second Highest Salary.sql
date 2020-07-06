-- Write a SQL query to get the second highest salary from the Employee table.
-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the query should return 200 as the second highest salary. 
-- If there is no second highest salary, then the query should return null.

-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

-- # Write your MySQL query statement below

SELECT
    IFNULL(
        (SELECT DISTINCT Salary FROM Employee
         ORDER BY Salary DESC LIMIT 1 OFFSET 1), NULL)
    As SecondHighestSalary;

SELECT
    IF(
        (SELECT Count(DISTINCT salary) FROM employee) >= 2,
        (SELECT salary FROM employee ORDER  BY salary DESC LIMIT  1, 1), 
        NULL)
    As SecondHighestSalary; 