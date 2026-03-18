# Smart-Transaction-Risk-Detector
## Problem Understanding

This program analyzes a set of transaction amounts entered by the user. It groups the transactions based on their value and evaluates the overall financial risk. Finally, it displays categorized data along with a summary report.

## Logic Used

The program uses a list to store transaction values. A loop is used to iterate through each transaction. Using conditional statements, transactions are grouped into categories.

Categories:

* Invalid (≤ 0)
* Normal (≤ 500)
* Large (≤ 2000)
* High (> 2000)

Another loop is used to calculate:

* Total of valid transactions
* Count of valid transactions

Risk is determined using conditions:

* If number of transactions is more than 5 → Moderate Risk
* If total amount is greater than 5000 → Moderate Risk
* If there are 3 or more high-value transactions → High Risk



## Personalization Applied

The program evaluates risk based on transaction behavior:

* Many transactions condition
* High total amount condition
* High-value transaction count

These conditions help in dynamically assigning the risk level.



## Features

* Uses list to store data
* Uses loops for processing
* Uses conditional statements for classification
* Categorizes transactions into multiple groups
* Calculates total and count
* Determines risk level
* Displays structured output

## Learning Outcome

This program helps in understanding how to work with lists, loops, and conditions. It also shows how multiple conditions can be combined to make decisions. The project improves logical thinking and basic data processing skills.
