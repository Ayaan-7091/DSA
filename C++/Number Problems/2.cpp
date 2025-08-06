#include <iostream>
using namespace std;

int main(){
    int n = 10400;
    int reversed = 0;
    int lastDigit = 0;
    while(n!=0){
        lastDigit = n%10;
        reversed = reversed*10 + lastDigit;
        n = n/10;
    }
    cout << reversed;
}