#include<stdio.h>
#include<stdlib.h>

int main()
{
    int N,M,a=1,b=2,answer=0,t,test=0;
    scanf("%d",&t);
    if(1<=t&&t<=1000)
    {
        while(test<t)
        {
            scanf("%d%d",&N,&M);
            if(1<=M && M<=5000000 && N>=2 && N<=1000000)
            {
                answer = 0;
                while(a>=1 && a<=N && a<b)
                {
                    while(b>=1 && b>a && b<=N)
                    {
                        if(((M%a)%b)==((M%b)%a))
                        {
                            answer = answer + 1;
                            printf(answer);
                        }
                        b++;
                    }
                    b=a+2;
                    a++;
                }
            // printf("%d\n",answer);
            }
        test++;
        }
    }
}
