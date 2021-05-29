#include <iostream>
using namespace std;

int main()
{
    int no_of_test_cases, test=0;
    cin>>no_of_test_cases;
    cout<<endl;
    if(no_of_test_cases>=1 && no_of_test_cases<=1000000){
        while(test < no_of_test_cases)
        {
        test = test + 1;
        int carbon_atoms;
        cin>>carbon_atoms;
        if(carbon_atoms == 0){
            continue;
        }
        if(carbon_atoms == 1){
            cout<<"1";
        }
        if(carbon_atoms == 2){
            cout<<"1";
        }
        if(carbon_atoms == 3){
            cout<<"1";
        }
        if(carbon_atoms == 4){
            cout<<"2";
        }
        if(carbon_atoms == 5){
            cout<<"3";
        }
        if(carbon_atoms == 6){
            cout<<"5";
        }
        if(carbon_atoms == 7){
            cout<<"9";
        }
        if(carbon_atoms == 8){
            cout<<"18";
        }
        if(carbon_atoms == 9){
            cout<<"35";
        }
        if(carbon_atoms == 10){
            cout<<"75";
        }
        if(carbon_atoms == 11){
            cout<<"159";
        }
        if(carbon_atoms == 12){
            cout<<"355";
        }
        if(carbon_atoms == 13){
            cout<<"802";
        }
        if(carbon_atoms == 14){
            cout<<"1858";
        }
        if(carbon_atoms == 15){
            cout<<"4347";
        }
        if(carbon_atoms == 16){
            cout<<"10359";
        }
        if(carbon_atoms == 17){
            cout<<"24894";
        }
        if(carbon_atoms == 18){
            cout<<"60523";
        }
        if(carbon_atoms == 19){
            cout<<"148284";
        }
        if(carbon_atoms == 20){
            cout<<"366319";
        }
        }
    }


    
}



