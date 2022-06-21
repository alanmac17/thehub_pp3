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

## Features
    ### GUI
    * Please enter employee No
    * Validate Employee Number
    * Present Employee Summary
    * Open Main Menu

    ### View Employee Profile
    ### Get Recommended Courses
    ### Leave an employee Review
    ### Get Recommended Next Action
    ### Create a new Employee Profile
