# calorie_service

Communication Contract

**Before Use**


**Must create the following txt files in directory locally for communication pipe with this naming scheme, they are listed in .gitignore :** init_search.txt, keyword.txt, calories.txt 


**Must install the following packages:** requests, bs4


**A. How to request data:**
calorie_service.py should be started, and will give the message 'listening' to the terminal. When a user inputs a food keyword in the calorie search function from the main application, the main app should write 'run' to init_search.txt, and then write  the keyword to keyword.txt .   As calorie_service.py listens, when it reads 'run', it will then read the user input from keyword.txt. calorie_service will then scrape google search  with the user input, and get  calories for food from user_input    
     
**B. How to receive data:**
Calorie_service will write the found calories to line one of calories.txt, then write the corresponding serving size and unit of measurement to line two. The response will be written as a string. To receive the response, the main application should first sleep for 6 to 10 seconds to give the calorie_service time to scrape,  depending on internet connection speed for the device running the program. It then should read lines 1 and 2 from calories.txt. If calorie_service finds no information for user input from keyword.txt, then it will write 'None' to calories.txt.  Finally the main application should erase calories.txt after reading it to prevent errors. 


**Example Call to request and receive, see test.py for test call**

![examples](https://github.com/spencerlwahlstrom/calorie_service/blob/main/examples.PNG?raw=true)



**UML Diagram**

![UML](https://github.com/spencerlwahlstrom/calorie_service/blob/main/UML.PNG?raw=true)

