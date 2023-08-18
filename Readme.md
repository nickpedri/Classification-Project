# Classification Project

## Project Goals:

* Determine what the leading factors are for churn.

* Create a model that can help predict if a customer will churn.

* Create a presentation that will detail my findings and provide possible solutions to retain more customers who would have otherwise churned



## Questions:

* How does monthly charges affect churn rate?

* How does tenure affect churn rate?

* What kind of services have the highest churn rates?

* What factors have the least impact on churn?

* What factors have the most impact on churn?



## Data Dictionary:

* payment_type_id = Shows the id number for the payment type
* internet_service_type_id = Shows the id number for the internet service type
* contract_type_id = Shows the id number for the contract type
* customer_id = Shows the id number for each customer
* gender = Shows the customer's gender
* senior_citizen = Shows if customer is a senior citizen
* partner = Shows whether or not customer has a partner (married)
* dependents = Shows if the customer has dependents like children
* tenure = Contains data indicating the number of months a customer has been with the company
* phone_service = Shows whether or not customer has phone services with company
* multiple_lines =  Shows whether or not customer has multiple lines with company
* online_security = Shows whether or not customer has online security with company
* online_backup = Shows whether or not customer has online backup with company
* device_protection = Shows whether or not customer has device protection with company
* tech_support = Shows whether or not customer has tech support with company
* streaming_tv = Shows whether or not customer has streaming tv with company
* streaming_movies = Shows whether or not customer has streaming movies with company
* paperless_billing = Shows whether or not customer has paperless billing
* monthly_charges = Shows the monthly charges of the customer
* total_charges = Shows total charges of customer
* churn = Shows if customer churned of not
* contract_type = Shows the type of contract the customer has
* internet_service_type = Shows the type of internet service the customer has
* payment_type = Shows the type of payment the customer has



## Project Plan:

1. Plan out the project. Set out some goals, ask questions about the data, create a plan for how I will acomplish these tasks.

2. Acquire the data. This will be done via SQL initially to access data and then data will be saved to local .csv file for faster access.

3. Prepare data. To prepare the data first I will handle all null values, rename/drop/combine/modify columns, and perform whatever tasks are necessary to clean my data so it is ready for exploration/modeling.

4. Explore the data. In this step I will analyze and explore my data by visualizing it and running stats tests on it. This will help identify possible patterns and driving factors influencing the target variable. The information learned in this step will be valuable for modeling.

5. Modeling. I will begin creating models that can predict my target variable. For this project I will be using classification models. This step may involve a little more data preparation doing things such as creating dummies and minmaxscaling data so that models can properly utilize the data.

6. Deploy/present model. Once modeling is done, it is time to present my model and findings to the my audience. This includes a brief summary of all my findings and my models and possible actions that can be taken to, in this case, stop customers from churning.



## Instructions:

1. You will need access to CodeUp's database of information since the information for this project is all pulled from the database.

2. Download and install Anaconda, and install Python through Anaconda so that you have all of the necessary data science libraries and tools that you will need for pyhton.

2. Query telco data from the Codeup database using SQL and then locally save a .csv copy of it so it is faster to load up.

3. Once you have Python, all of the necessary libraries, and access to CodeUp's database or the .csv file containing the telco data,  you are all set to go.



## Key Findings:

* The leading factor contributing to churn is the contract type. Customers who are on month to month contracts churn far more often.

* Tenure also has an impact on churn. The longer the tenure, the less likely someone is to churn.

* Monthly charges has a positive correlation with churn. The higher the monthly charges the higher the churn rate.

* Fiber optic has a disproportionately high churn rate. A customer with DSL internet or no internet is far more likely to not churn. 