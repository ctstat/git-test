#include<iostream>
#include<vector>

using namespace std;


double square(int x){
    return x*x;
}

int main(){
    vector<int> nums;

    for(int i = 0; i < 10 ; i++){
        nums.push_back(square(i));
    }

    for(auto& i:nums){
        cout << i <<" ";
    }cout << endl;







}