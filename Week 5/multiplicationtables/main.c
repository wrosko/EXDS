#include <stdio.h>
#include <stdbool.h>
int main()
{
    int user_number;//create a new integer variable
    int last_multiple;//create a new integer variable for max in mult table
    int stilltrue = false; //create integer to use in while
    while (!stilltrue){//initiate while loop
    printf("Please enter a positive integer you would like the table for and"
           " hit enter, then enter the max value of its multiplication "
           "table: \n");
//takes two inputs and makes sure they are integers
    if(scanf("%d",&user_number) == 1 && scanf("%d",&last_multiple)== 1){
        printf("The number you typed was %d and the "
           " value was %d \n\n",user_number,last_multiple);

    while (last_multiple > 0){

        int multiple;//multiple of user_number and last_multiple
        multiple = user_number * last_multiple;
        printf("%d x %d is %d \n\n", user_number,last_multiple,multiple);
        last_multiple = last_multiple - 1;//decrease the last_multiple value by 1
        stilltrue = true;
    }

    } else {
        printf("That was not an integer. \n");


    }break;
    }
    return 0;

}
