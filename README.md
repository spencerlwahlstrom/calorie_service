# calorie_service
**Before Use**
**Must create the following txt files in directory locally for communication pipe with this naming scheme:** init_search.txt, keyword.txt, calories.txt 
**Must install the following packages:** requests, bs4


**A. How to request data:**
  When a user inputs a food keyword in the calorie search function from the main application, the main app should write 'run' to init_search.txt, and also writes the keyword to keyword.txt calorie_service listens, when it reads 'run', it will then read the user input from keyword.txt. calorie_service will then scrape google search  with the user input, and get  calories for food from user_input    
    
 

**B. How to receive data:**
   Calorie_service will write the found calories to line one of calories.txt, then write the corresponding serving size to line two. The response will be written as a string. To receive theresponse, the main application should read lines 1 and 2 from calories.txt. If calorie_service finds no information for user input from keyword.txt, then it will write 'None' to calories.txt.   

![UML](https://github.com/spencerlwahlstrom/calorie_service/blob/main/UML.PNG?raw=true)

