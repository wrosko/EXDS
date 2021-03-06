/*Filename/projectname: Rosko_terwiesch_multiplication.c
*Authors: Wade Rosko,Mats Terwiesch
*Description: Prints out a given number's multiplication table. Takes
*two inputs, the number, and the max number it will be multiplied by.
*To make the command window store more lines, press alt-space, then click
*properties. Under the layout tab, change the height of the screen buffer
size.*/

#include <stdio.h>
#include <stdbool.h>

int main()
{
    int user_number;//create a new integer variable
    int last_multiple;//create a new integer variable for max in mult table
    int stilltrue = false; //create integer to use in while
    while (stilltrue == false){//initiate while loop
    printf("Please enter a positive integer you would like the table for and"
           " hit enter, then enter the max value of its multiplication "
           "table: \n");
    //takes two inputs and makes sure they are integers
    if ( ( scanf("%d %d", &user_number, &last_multiple)) == 2){
    //print the numbers that were entered
        printf("The number you typed was %d and the "
           " value was %d \n\n",user_number,last_multiple);
    //While loop performs the multiplication operation, subtracts one
    //until there are no more operations in the times table
    while (last_multiple > 0){

        int multiple;//multiple of user_number and last_multiple
        multiple = user_number * last_multiple;
        printf("%d x %d is %d \n\n", user_number,last_multiple,multiple);
        last_multiple = last_multiple - 1;//decrease the last_multiple value by 1
        stilltrue = true;
    }

    } else {
        //Print the error message if input is not an integer
        printf("That was not an integer. \nPlease input an integer next time. \n");
        stilltrue = false;
        scanf ( "%*[^\n]");//clear input buffer of all characters up to newline

        }
    }
    return 0;

}
