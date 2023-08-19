
## <p style="text-align: center;">Excel Showcase</p>


![Dashboard](https://github.com/julia-schmidt-lademann/julia-schmidt-lademann.github.io/blob/main/_includes/Budget.JPG?raw=true)

**Background:**
- I am interested in creating a zero-based budgeting file. 
- The Setup mirror the setup of the popular Budgeting app YNAB.

**Visuals:**
- The visuals mirror the setup of the popular Budgeting app YNAB.
- The top figure shows money available in the accounts that has not yet been budgeted out to a category. 
- Each category shows the amount assigned in the current month, the money spent in the current month and money left over considering spending and assignments in past months. 
- For each category it shows the goal and the amount still required to reach that goal. 
- There are a number of aggregate statistics summing all categories. 
- Special highlighting shows if within a category group there is a category with more spent than available. This ensures that even when the category is collapsed overspending is visible and can easily be adressed.

**Functionalities:**

- Transactions are added to the relevant accounts and are attributed to the relevant spending categories. To do this I use a VBA script to ensure the necessary formulas are added when a new transaction appears.
- It allows the user to assign funds to categories based on inflows and transactions. The report then tracks the funds currently available in each category at a certain point in time.
- It allows the user the ability to set goals for every category and track progress against the goal. This could be a monthly goal or a longerterm goal including multiple months of assignments and spending
- Recurring transactions are automatically added based on their frequency and the Account they are steup against
- It allows the ability to report on spending over time. 
    - This could be to compare spending at the same point in the month compared to another month by category or account
    - This could be comparing inflows and outflows to monitor Savings rate and Net worth changes over time
    - This could be identifying payees that a lot of money has been spent at over a period of time
- The file allows accounts to be classified as being included or excluded in the budget to allow Networth tracking.
    - Changes in investment Accounts should be easily trackable but should not impact the money available for spending on everyday expenses.

<sub>This Report for example shows the monthly spending in a certain category for the current month and 2 prior months. The Category is variable, and the same can be run over a multi-select of Accounts.</sub>
![Dashboard](https://github.com/julia-schmidt-lademann/julia-schmidt-lademann.github.io/blob/main/_includes/budget_reporting.JPG?raw=true)


**Technical Details:**
- The bulk of the functionalities lie in the Power Query that allows for the transactions on the different accounts to be combined into a single master datasource. 
- The transactions are then presented split by category 
- Formulas to create a unique list of sheet names power the ability to quickly jump between tabs allowing the bulk of the sheets to remain hidden for a quicker and cleaner layout
- Using the Excel Currency Financial Market Information the file allows for mutliple currencies to be combined in a single report

----------------------------------------------------------------------------------------------------

