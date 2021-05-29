#include <iostream>
#include <list>
using namespace std;

int main()
{
    int no_of_test_cases, test=0, value_of_N, i, j;
    
    string row_one, row_two, row_three;
    string column_one[3], column_two[3], column_three[3];
    string grid[3][3];
    cin>>no_of_test_cases;
    if(no_of_test_cases>=1 && no_of_test_cases<=19683)
    {
        while(no_of_test_cases>test)
        {
            if(test>0){cout<<endl;}
            test = test + 1;
            int no_of_x = 0, no_of_o = 0, no_of_dash = 0;
            int no_of_slashes_by_x = 0, no_of_slashes_by_o = 0, total_no_of_slashes = 0;
            int flag = 0;
            //TAKING THE GRID VALUES FROM USER
            cin>>row_one;
            cin>>row_two;
            cin>>row_three;

            column_one[0]=row_one[0];
            column_one[1]=row_two[0];
            column_one[2]=row_three[0];
            column_two[0]=row_one[1];
            column_two[1]=row_two[1];
            column_two[2]=row_three[1];
            column_three[0]=row_one[2];
            column_three[1]=row_two[2];
            column_three[2]=row_three[2];

            for(i=0; i<3; i++)
            {
                // cout<<i;
                if (column_one[i]=="X"){no_of_x = no_of_x + 1;}
                if (column_one[i]=="O"){no_of_o = no_of_o + 1;}
                if (column_one[i]=="_"){no_of_dash = no_of_dash + 1;}
                if (column_two[i]=="X"){no_of_x = no_of_x + 1;}
                if (column_two[i]=="O"){no_of_o = no_of_o + 1;}
                if (column_two[i]=="_"){no_of_dash = no_of_dash + 1;}
                if (column_three[i]=="X"){no_of_x = no_of_x + 1;}
                if (column_three[i]=="O"){no_of_o = no_of_o + 1;}
                if (column_three[i]=="_"){no_of_dash = no_of_dash + 1;}            
            }
            for(i=0; i<3; i++)
            {
                // cout<<i;
                if (column_one[i]!="X" && column_one[i]!="O" && column_one[i]!="_" ){flag=1;}
                if (column_two[i]!="X" && column_two[i]!="O" && column_two[i]!="_" ){flag=1;}
                if (column_three[i]!="X" && column_three[i]!="O" && column_three[i]!="_" ){flag=1;}
            }
            if(flag==1){continue;}
            //cout<<" no of x "<<no_of_x<<" no of o "<<no_of_o<<" no of dash "<<no_of_dash;
            if ((no_of_x==no_of_o) || ((no_of_o + 1)==no_of_x))
            {                
                for(i=0;i<3;i++)
                {
                    //CHECKING SLASHES IN ROW BY X AND Y
                    if(column_one[i]==column_two[i] && column_two[i]==column_three[i] && column_two[i]=="X"){no_of_slashes_by_x = no_of_slashes_by_x + 1;}
                    if(column_one[i]==column_two[i] && column_two[i]==column_three[i] && column_two[i]=="O"){no_of_slashes_by_o = no_of_slashes_by_o + 1;}               
                }
                //CHECKING SLASHES IN COLUMN BY X AND Y
                if(column_three[0]==column_three[1] && column_three[1]==column_three[2] && column_three[0]=="X"){no_of_slashes_by_x = no_of_slashes_by_x + 1;}
                if(column_three[0]==column_three[1] && column_three[1]==column_three[2] && column_three[0]=="O"){no_of_slashes_by_o = no_of_slashes_by_o + 1;}
                if(column_two[0]==column_two[1] && column_two[1]==column_two[2] && column_two[0]=="X"){no_of_slashes_by_x = no_of_slashes_by_x + 1;}
                if(column_two[0]==column_two[1] && column_two[1]==column_two[2] && column_two[0]=="O"){no_of_slashes_by_o = no_of_slashes_by_o + 1;}
                if(column_one[0]==column_one[1] && column_one[1]==column_one[2] && column_one[0]=="X"){no_of_slashes_by_x = no_of_slashes_by_x + 1;}
                if(column_one[0]==column_one[1] && column_one[1]==column_one[2] && column_one[0]=="O"){no_of_slashes_by_o = no_of_slashes_by_o + 1;}

                //CHECKING SLASHES IN DIAGONALS BY X AND Y
                if (column_one[0]==column_two[1] && column_two[1]==column_three[2] && column_two[1]=="X"){no_of_slashes_by_x = no_of_slashes_by_x + 1;}
                if (column_one[2]==column_two[1] && column_two[1]==column_three[0] && column_two[1]=="X"){no_of_slashes_by_x = no_of_slashes_by_x + 1;}
                if (column_one[0]==column_two[1] && column_two[1]==column_three[2] && column_two[1]=="O"){no_of_slashes_by_o = no_of_slashes_by_o + 1;}
                if (column_one[2]==column_two[1] && column_two[1]==column_three[0] && column_two[1]=="O"){no_of_slashes_by_o = no_of_slashes_by_o + 1;}

                // cout<<no_of_slashes_by_x<<no_of_slashes_by_o;
                total_no_of_slashes = no_of_slashes_by_x + no_of_slashes_by_o;
                if(no_of_slashes_by_x==2 && total_no_of_slashes==2 && no_of_dash==0){cout<<"1";continue;}
                if(no_of_slashes_by_x==1){if(total_no_of_slashes==1){if(no_of_x>no_of_o){cout<<"1";continue;}else{cout<<"3";continue;}}else{cout<<"3";continue;}}
                if(no_of_slashes_by_o==1){if(total_no_of_slashes==1){if(no_of_x==no_of_o){cout<<"1";continue;}else{cout<<"3";continue;}}else{cout<<"3";continue;}}
                if(no_of_dash==0){if(total_no_of_slashes==0){cout<<"1";continue;}else{cout<<"3";continue;}}
                if(no_of_dash>0){if(total_no_of_slashes==0){cout<<"2";continue;}else{cout<<"3";continue;}}
                if(total_no_of_slashes>1){cout<<"3";continue;}
            }cout<<"3";continue;
        }
    }
}
