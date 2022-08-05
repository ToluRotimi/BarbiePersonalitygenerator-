# **_Barbie - ERA Calculator_**
## Author - Tolu Rotimi
## Objective
* To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

### Brief Outline
* The user will be able to input their fullname , surname and birth year into the database. 
From this the application using (python and flask) will be able to calculate what barbie era the user was born
display this to the user.

## Crud Functionalities
* CREATE
  * Add - Users
  * Add - Barbie Era
* Read
  * View - All Users
  * View - All Barbie Era
  * View - User_Era - the barbie year and the birth year in the database.  
* Update
  * Update any items inputted into the database in relation with the id 
* Delete
  * Remove any items inputted into the database in relation with the id 

## Initial Planning with Designs and Tracking

###  **User Stories+Acceptance Criteria**
![image](https://user-images.githubusercontent.com/96881229/183012070-66efecc0-3ee1-4132-b8fb-40865a9755e0.png)

Intially planned on creating an additon section where the user inputted personlaity traits to access a charcacter that was suit their personality but needed to work within the timescale so I removed that section of the project but you'll see in my User Story and Acceptance Criteria how that would have played out. Overall my new aim as I progressed with the project was keep as simple as possible but remain as functional as possible.  

### **Trello Board** 
I used Trello board to act as a visual for my product backlog. It helped act as a guide as to the next steps to take and what to prioritise by adjusting the different cards.

Beginning of the project

![image](https://user-images.githubusercontent.com/96881229/183012431-3bca21e9-232a-40d4-a2b2-6d6a66c714a3.png)

End of Project

![image](https://user-images.githubusercontent.com/96881229/183012553-c2233c85-4997-4b7e-92ba-f6a1633549a8.png)

### **Risk Assessment**
Risk Assessement using excel showing the potential threats to the project. Encountered new potential threats as I progressed in the project and updated as I went along.

![image](https://user-images.githubusercontent.com/96881229/183014230-5c09d6d1-5713-485d-8b32-1ca8174d821d.png)

### **ERD**
Entity relationship diagram. 
Initial ERD

![Barbie-Era ERD](https://user-images.githubusercontent.com/96881229/183014548-256225b6-2c7a-4442-adfe-0b0310af6c78.jpg)

Final ERD
The initial didn't adhere to best practices and was over complicated so I created 3 tables. 2 tables being the user and barbie_era table with a one to many relationship and with the user_id as a foreignkey. Then related the two main tables to a join table where both id's were used as a foreign key. 

![Untitled Diagram](https://user-images.githubusercontent.com/96881229/183014924-d9f7074b-a173-45cb-9b4f-ed36872d98ee.jpg)

The aim for doing this was that an already established user in the database could just have their user_id already in the barbie_era so all they needed to do was pick their birth year to calculate what barbie era they were born. 

### **Front End**

Frontend apllication done using flask and HTML

* Create Functionality
 The user form and the Barbie era form. 
 
 The user inputs their forename and surname and then the barbie era picks up that user and asks for their birth year
 
 The user is then taken to a url where it prints out the barbie era they were born in
 
![image](https://user-images.githubusercontent.com/96881229/183045593-fba74fbb-a5eb-491a-beb8-96e5ebcec5e1.png)

![image](https://user-images.githubusercontent.com/96881229/183045798-1067ff0c-79fe-4cb6-96ce-96c254fd673f.png)

![image](https://user-images.githubusercontent.com/96881229/183046026-ab090352-2758-43b1-8c38-25253b76c495.png)

* PYTHON CODE
* 
The python code was created utilising the if statements to print out the barbie year that matched with user

![image](https://user-images.githubusercontent.com/96881229/183047029-275da948-3163-438c-8569-d9402c3c2e72.png

* Displaying the Read Functionality

sqlalchjemy - orm - interact database but without needing to manually go to the database 

### **Testing**

*Unit Testing
 *Summary on Tests


