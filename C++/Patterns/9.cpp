#include <iostream>
using namespace std;

int main(){
    
    int n;
    cout << "Enter N : ";
    cin >> n;

    for(int i=0;i<n;i++){

        for(int j=n;j>i;j--){
            cout << " ";
        }

        for(int j=0;j< 2*i+1;j++){
            cout << "*";
        }

          for(int j=n;j>i;j--){
            cout << " ";
        }

        cout << endl;
    }

     for(int i=n;i>=0;i--){

        for(int j=i;j<n;j++){
            cout << " ";
        }

        for(int j=0;j<2*i+1;j++){
            cout << "*";
        }

          for(int j=i;j<n;j++){
            cout << " ";
        }

        cout << endl;
    }
}