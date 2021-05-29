#include <iostream>
using namespace std;

int main()
{
    int no_of_test_cases, test = 0, N, M, answer = 0, sum = 0;
    cin >> no_of_test_cases;
    if (no_of_test_cases >= 1 and no_of_test_cases <= 1000)
    {
        while (test < no_of_test_cases)
        {
            if (test > 0)
            {
                cout << endl;
            }
            test = test + 1;
            int a = 1, b = 2;
            cin >> N >> M;
            sum = sum + N;
            if (sum > 1000000)
            {
                exit;
            }
            int pairs = 0;
            int flag = 0;
            if (N >= 2 && N <= 1000000 && M >= 1 && M <= 500000)
            {
                while (a < b && flag == 0 && a <= N && a < b && pairs<M)
                {
                    while (b <= N && b > 1 && b > a && pairs<M)
                    {
                        if (((M % a) % b) == ((M % b) % a))
                        {
                            // cout << "(" << a << "," << b << ")";
                            pairs = pairs + 1;
                            
                        }
                        b = b + 1;
                    }
                    b = a + 2;
                    a = a + 1;
                }
                cout << pairs;
            }
        }
    }
}