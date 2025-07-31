#include <iostream>
using namespace std;
int main(){
    int n = 4;
    int temp = (n*2) - 1;
    for(int i = 0;i<temp;i++){
        for(int j = 0;j<((n*2)-1);j++){
            if(i==0 || i==temp-1){
              cout<<n<<" ";
            }
            else if(j==0||j==temp-1){
                cout<<n<<" ";
            }
           
    }
    cout<<endl;
    }
}