// In the first code i tried to find out the percent of RGB value
// counting 255 = 100% and then rounded the percent of RGB Value
// to covert it to HEX value. EX: if RGB Value is 100% then
// Hex is also 100% so Hex Value = F
// How FUCKING stupid i was.. i should kill myself FF times FUCK!!
// It should be just a fucking simple DECIMAL TO HEXADECIMAL CONVERSION!!!!
// Back to sanity i putted 2 logic to make this a proper RGB to HEXA converter
// 1. RGB Value Can not be more than 255
// 2. Id RGB value is equal to 0 then HEX out put goes directly char '0'
// NOW I CAN DIE PEACEFULLY

#include <stdio.h>
void main()
{
int rVal, gVal, bVal, decn;
char faulCoder(decn){
        int rmd,q,dn=0,m,l,i=1,j,tmp;
        char s;
        if (decn == 0 ) {
                s = '0';
                printf("%c",s);
                printf("%c",s);
            }
        else {
            q = decn;
            for(l=q;l>0;l=l/16)
                {
                    tmp = l % 16;
                    if( tmp < 10)
                        tmp =tmp + 48;
                    else
                        tmp = tmp + 55;
                    dn=dn*100+tmp;
                }
            for(m=dn;m>0;m=m/100)
                {
                s=m % 100;
                printf("%c",s);
                }
            }
        }
    printf("Input Red Value: ");
	scanf("%ld",&rVal);
	printf("Input Green Value: ");
	scanf("%ld",&gVal);
	printf("Input Blue Value: ");
	scanf("%ld",&bVal);
	if (( rVal > 255 ) || ( gVal > 255) || ( bVal > 255 ))
    {
        printf("RGB VALUE MUST BE EQUEL OR LESS 255 ");
    }
    else {
        printf("\nHexa Value: #");
        faulCoder(decn = rVal);
        faulCoder(decn = gVal);
        faulCoder(decn = bVal);
        printf("\n\n");
    }
}
