#include <stdio.h>

void main()
        {
	long int decn,rmd,q,dn=0,m,l;
	int i=1,j,tmp;
        char s;
	printf("Input Red Value: ");
	scanf("%ld",&decn);
	q = decn;
        for(l=q;l>0;l=l/16)
               {
		tmp = l % 16;
		if( tmp < 10)
		           tmp =tmp + 48; else
		         tmp = tmp + 55;
                         dn=dn*100+tmp;
	        }
          printf("\nHexadecimal Value : ");
         for(m=dn;m>0;m=m/100)
            {
               s=m % 100;
               printf("%c",s);
            }
    printf("\n\n");
}
