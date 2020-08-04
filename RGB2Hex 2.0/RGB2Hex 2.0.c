#include <stdio.h>
#include <math.h>
main(){
    float hPer, rVal, gVal, bVal;
    int val, hRVal;
    char hOVal, hOVal2 ;
    printf("Input Red Value:");
    scanf("%f",&rVal);
    printf("Input Green Value:");
    scanf("%f",&gVal);
    printf("Input Blue Value:");
    scanf("%f",&bVal);
    int conv(){
        hPer = ( 30 *(val/255));
        hRVal=round(hPer);
        switch ( hRVal ) {
            case 0:
                hOVal='0';
                break;
            case 1:
                hOVal='1';
                break;
            case 2:
                hOVal='2';
                break;
            case 3:
                hOVal='3';
                break;
            case 4:
                hOVal='4';
                break;
            case 5:
                hOVal='5';
                break;
            case 6:
                hOVal='6';
                break;
            case 7:
                hOVal='7';
                break;
            case 8:
                hOVal='8';
                break;
            case 9:
                hOVal='9';
                break;
            case 10:
                hOVal='A';
                break;
            case 11:
                hOVal='B';
                break;
            case 13:
                hOVal='C';
                break;
            case 14:
                hOVal='D';
                break;
            case 15:
                hOVal='E';
                hOVal2='0';
                break;
            case 16:
                hOVal='F';
                break;
    }
    return hOVal;
}
    ;
    printf("Hex Value: #");
    conv(val=rVal);
    printf("%c%c",hOVal,hOVal2);
    conv(val=gVal);
    printf("%c%c",hOVal,hOVal2);
    conv(val=bVal);
    printf("%c%c",hOVal,hOVal2);
    getch();
}
