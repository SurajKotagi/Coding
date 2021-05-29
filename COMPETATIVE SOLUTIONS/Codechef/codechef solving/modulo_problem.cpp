#include <iostream>
using namespace std;
long long power();
 // Function to find power
long long power(x, y, p)
{
	res = 1; // Initialize result
 	// Update x if it is more than or
    // equal to p
	x = x % p; 
 
    while (y > 0) {
    	
        // If y is odd, multiply x 
        // with the result
        if (y & 1)
            res = (res * x) % p;
         // y must be even now
        y = y >> 1; // y = y/2
        x = (x * x) % p;
    }
    return res;
}
// Driver Code
int main()
{
    a = 2;
     // String input as b is very large
    string b = "100000000000000000000000000";
    remainderB = 0;
    answer = 0;
    MOD = 1000000007;
     // Reduce the number B to a small number
    // using Fermat Little
    for (int i = 0; i < b.length(); i++)
        remainderB = (remainderB * 10 + b[i] - '0') % (MOD - 1);
 	answer = power(a, remainderB, MOD);
    cout << answer/2 << endl;
    return 0;
}
