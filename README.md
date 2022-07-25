# calorie_service
A. How to request data:
  Calorie search function from main application should write 'run' to init_search.txt, when a user inputs a food keyword, and also writes the keyword to keyword.txt calorie_service listens, when it reads 'run', it will then read the user input from keyword.txt. calorie_service will then scrape ' '  with the user input, and get  calories for food from user_input    
    
 

B. How to receive data: 
   calorie_service will write found calories to calories.txt as string. To receive response, the main application should read calories.txt. If calorie_service finds no information for user input from keyword.txt, then it will write 'None' to calories.txt.  The main application should clear calories.txt after reading

![UML](https://github.com/spencerlwahlstrom/calorie_service/blob/main/UML.PNG?raw=true)

