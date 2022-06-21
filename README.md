# The Hub

The Hub is an employee management tool for people managers. The idea is to gather and use information about the employee to help managers take the right actions at the right times. Information like when is my next performance review, how many new hires do we have in training. What should resouces can I offer in a performance review.
The hub is a place to make business rules and automate emails, content and next actions so that employees get the engagement they need and managers can spend less time on administation and more time on people.

## User Stories
**(Desired User Experience)

* As a new employee I want to receive information about my role so that I can be successful
* As a new employee I want to upskill in my role so that I can get do my work more efficiently
* As a new employee I want to have access to content relevant to my job so that I know what is expected of me
* As a Manager I want new employees to receive training material relevant to their role 
* As a Manager I want an easy way of setting up employees for success when they first start in the company
* As a Manager I want to log reviews for every stage of the employment journey
* Ad an Manager I want to know what the next best action for all employees

### Current Use Case 

* Title: See next action for an employee
* Actor: Manager
* Use Case:
	1. * A Manager enters an employee number
	2. * The number is used to retrieve information about the employee, their role and employment type
	3. * The manager then views the next recommended action
	4. * The system checks that they are passed probation so the next review is a performance review

* Title: Log a performance review
* Actor: Manager
* Use Case:
	1. * A Manager enters an employee number
	2. * The number is open a menu allowing them to select create employee review
	3. * The manager then inputs details about the review and rating
	4. * The system logs the review and feeds in to the business BI


### Future Use Case
* Title: Read information about my new company, my role
* Actor: New Starter
* Scenario:
	1. * The new starter opens the onboarding email in their email client
	2. * The new starter sees information about their team, their role and links to relevant training content.
	3. * The new stater clicks on the links to view more information
	4. * The links open to the company and training sites.

## Functional Requirements
* Retrieve data about employees
* Create an employee profile
* Create and log an employee review
* Search relevant training content for the employee's role

## Future Functionality
* Query the database and create business rules to notify managers and employees of when a review is due. 
* For example if the employee type is a 'new hire' and a training review is completed with a status of pass.
* Then update the employee type to 'probation' and next review date to 3 months from the last review date

* Format relevant onboarding content for the new starter in to an email
* Utilise API connecting to linkedin learning and populate the email with curated courses
* Send an email to the new starter and their manager

## Functions
* Start (main)
* Request employee id (get_id)
* Create an employee profile (get_profile)
* Confirm id is valid (validate_id)
* Main Menu (main_menu)
* Get the next recommended action for an employee (next_action)
* Retrieve Role Training Material (get_course)
* Add an employee review (add_review)
* Employee Profile Class (EmployeeProfile)
* Get full profile details (get_full_profile)
* Provide short employee summary (get_profile)
* Create an employee profile (add_employee)

## Process Flow

## Features
### Welcome Screen
    * Please enter employee No
    * Validate Employee Number
    * Present Employee Summary
    * Open Main Menu

### View Employee Profile
### Get Recommended Courses
### Leave an employee Review
### Get Recommended Next Action
### Create a new Employee Profile

## Technologies In Use
    - ### [Github](https://github.com/)
    - ### [Gitpod](https://gitpod.io/)
    - ### [Heroku](heroku.com)
    - ### [Lucid](https://lucid.app/)
    - ### [PEP8](http://pep8online.com/)
    - ### [Pandas] 

