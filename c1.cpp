#include<iostream>
#include<vector>

using namespace std;

int main(){
    vector<int> nums;

    for(int i = 0; i < 10 ; i++){
        nums.push_back(i + 100);
    }

    for(auto& i:nums){
        cout << i <<" ";
    }cout << endl;







}