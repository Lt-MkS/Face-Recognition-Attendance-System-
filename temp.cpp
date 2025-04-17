#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
int main(){
  vector<int> a = { 1, 2, 3};
  vector<int> b = { 4 , 5 };
  int a1 = a.size() ;
  int b1 = b.size() ;
  int mini =  min(a[0],b[0]);
  int maxi = max( a[a1-1],b[b1-1]);
  cout<<mini<<maxi<<endl;
  


}