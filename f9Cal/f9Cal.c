#include <stdio.h>
main()
     {
         /* Var Declare */
    float verion = 2.0;
    char a;
    float income, living, dControl, loans;

        /* User Input */

    printf("Enter Your Income: ");
    scanf("%f",&income);
    printf("Do You Have Any Loans To Pay?(y)");
    scanf(" %c", &a);
    system("cls");

    /* Calculation And Out Put */

    living = income /2 ;
    dControl = living /2;
    if (a == 'y') {
        loans = dControl /2;
            printf("Your Income:      %.2f",income);
            printf("\nLiving:           %.2f",living);
            printf("\nDamage Control:   %.2f",dControl);
            printf("\nloans:             %.2f",loans);
            printf("\nSavings:          %.2f",loans);
    }
    else {
        loans = dControl;
            printf("Your Income:      %.2f",income);
            printf("\nLiving:           %.2f",living);
            printf("\nDamage Control:   %.2f",dControl);
            printf("\nSavings:          %.2f",loans);
    }
    getch();
}

/* END */
