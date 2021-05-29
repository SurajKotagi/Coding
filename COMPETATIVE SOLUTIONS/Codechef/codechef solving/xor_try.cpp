#include <iostream>
using namespace std;

int main() 
{
    int power(long long x, unsigned int y, int p);
	int no_of_test_cases;
	int test=0;
    cin>>no_of_test_cases;
    
    while (test<no_of_test_cases)
    {
        
        if(test>0){cout<<endl;}
    	unsigned int N;
        long long res=1;
        test = test + 1;
        cin>>N;
        if (N>=1 && N<=100000)
        {
            res = power(2,(N-1),1000000007);
        }
        cout << res%1000000007;
    }
    return 0;
}
// int power(int a)
// {
//     int p = 1000000007;
//     long long x = 2;
//     int ans = 1;     // Initialize result
 
//     x = x % p; // Update x if it is more than or
//                 // equal to p
  
//     if (x == 0) return 0; // In case x is divisible by p;
 
//     while (a > 0)
//     {
//         // If y is odd, multiply x with result
//         if (a & 1)
//             ans = (ans*x) % p;
 
//         // y must be even now
//         a = a>>1; // y = y/2
//         // cout<<"hi";
//         x = (x*x) % p;
//     }
//     return ans;
// }
int power(long long x, unsigned int y, int p)
{
    int res = 1;     // Initialize result
 
    x = x % p; // Update x if it is more than or
                // equal to p
  
    if (x == 0) return 0; // In case x is divisible by p;
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;
 
        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;
    }
    return res;
}
