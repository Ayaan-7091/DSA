#include <iostream>
using namespace std;
int main(){
    int n = 4;
    int size = (2*n)-1;
  for(int i = 0; i < size; i++) {
    for(int j = 0; j < size; j++) {
        int min_dist = min(min(i, j), min(size - 1 - i, size - 1 - j));
        cout << n - min_dist << " ";
    }
    cout << endl;
}
}
