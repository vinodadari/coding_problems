"""
# Asked programmers.io - 23-Jan-2024

Employee (efname, elname, salary, FK : dept_id)
Department (dept_name, PK : dept_id)
10 Departments
1000 employees
for every dept
fetch employee where their salary is second highest from every department

# get second highest salary from department
select max(salary) from employee LEFT JOIN departments as de de.dept_id =employee.dept_id DESC salary LIMIT 2


Bard:

method - 1
    SELECT e.efname, e.elname, e.salary
    FROM (
        SELECT e.*, ROW_NUMBER() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS rank
        FROM Employee e
    ) AS ranked_employees
    INNER JOIN Department d ON ranked_employees.dept_id = d.dept_id
    WHERE ranked_employees.rank = 2;

Explanation:

    We create a temporary table with a window function ROW_NUMBER().
    The function assigns a rank to each employee within their department, with the highest salary receiving rank 1.
    The main SELECT clause retrieves employee information from the temporary table.
    We use an INNER JOIN with the Department table to link departments and employees based on dept_id.
    The WHERE clause filters the main query to select employees whose rank is 2, meaning they have the second highest salary in their department.

method - 2
    SELECT efname, elname, salary
    FROM (
    SELECT e.*, DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank
    FROM Employee e
    INNER JOIN Department d ON e.dept_id = d.dept_id
    ) AS ranked_employees
    WHERE ranked_employees.rank = 2;

Explanation:

    The SELECT statement retrieves the employee names, last names, and salaries from a temporary result set.
    The subquery within the FROM clause:
    Selects all employee data and uses the DENSE_RANK() window function to assign a rank to each employee within their department based on their salary in descending order.
    Ties are handled by assigning the same rank to all employees with the same salary.
    Joins the Employee and Department tables based on the dept_id foreign key.
    The outer WHERE clause filters the temporary result set to include only employees with a rank of 2, which corresponds to the second highest salary in their department.

Method - 3
    SELECT e.efname, e.elname, e.salary
    FROM Employee e
    INNER JOIN Department d ON e.dept_id = d.dept_id
    WHERE e.salary IN (
    SELECT MAX(salary) AS second_highest
    FROM Employee e2
    WHERE e2.dept_id = e.dept_id
    AND e2.salary < (
        SELECT MAX(salary) AS highest_salary
        FROM Employee e3
        WHERE e3.dept_id = e.dept_id
    )
    );

Explanation:

    INNER JOIN Employee e ON e.dept_id = d.dept_id: This joins the Employee and Department tables on the dept_id column, ensuring we match each employee with their corresponding department.
    WHERE e.salary IN (...):: This filters the results to only include employees whose salary is within the subquery's result.
    Subquery 1: This subquery finds the highest salary for each department using MAX(salary), grouped by dept_id.
    Subquery 2: This nested subquery finds the second-highest salary for each department by filtering out the highest salary (obtained from subquery 1) using <.
    Main query: The final WHERE clause checks if the employee's salary matches the second_highest salary obtained from subquery 2 for their specific department.

----------------------------------------------

Note: Depending on your database platform and preferences, you can use alternative methods to achieve the same results. For example, some platforms offer window functions like ROW_NUMBER or DENSE_RANK to directly identify the employees within each department by rank.

"""
