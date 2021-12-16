# Calories Calculation Form - App
This is a project of an Udemy course. The scope is to make an online app, which will calculate the daily needed calories.

## Design
We want the user to have a landing page (without css), which leads him to the form sheet.<br>
The form sheet has five input fields and one button:
- Weight
- Height
- Age
- City (where the user is)
- Country
- **Calculate button**

If pushed, the app will scrape the users location from the web and calculate how many calories the user needs.

Objects:
- Calorie:
  - weight
  - height
  - age
  - temperature
  - calculate()
- Temperature
  - country
  - city
  - get()