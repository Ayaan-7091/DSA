#include <iostream>
using namespace std;

int main(){
    int n = 4554;
    int temp = n;
    int reverse = 0;
    int last_digit = 0;
    
    while(n!=0){
        last_digit = n % 10;
        reverse = reverse*10 + last_digit;
        n = n/10;
    }

    if(temp==reverse){
        cout<<"Palindrome";
    }else{
        cout<<"Not Palindrome";
    }
}