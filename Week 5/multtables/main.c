/* 
 * File:   main.c
 * Author: wrosko
 *
 * Created on May 26, 2015, 12:22 PM
 */

#include <stdio.h>

#include <stdio.h>

int main()
{
    int user_number;
    
    printf("Please enter a number: ");
    scanf("%d",&user_number);
    /* 
     * The loop goes while x < 10, and x increases by one every loop*/
    /*for ( x = 0; x < 10; x++ ) {
        /* Keep in mind that the loop condition checks 
           the conditional statement before it loops again.
           consequently, when x equals 10 the loop breaks.
           x is updated before the condition is checked. */   
        //printf( "%d\n", x ); 
    //}
    printf(" the number you typed was %d",user_number);
    return 0;
   
}

