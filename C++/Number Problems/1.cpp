#include <iostream>
using namespace std;

int main(){
    int n = 532012;
    int temp;
    int count = 0;
    while(n!=0){
        temp = n%10;
        count = count + 1;
        n = n/10;
    }
    cout << count;
}
