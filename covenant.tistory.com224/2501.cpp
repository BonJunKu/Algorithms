#include <iostream>
using namespace std;
int main(){
  int n,k;
  cin>>n>>k;
  int count=0;
  for (int i =1 ; i<n+1; i++){
  if (n%i==0){
    count+=1;
  }
  if (count==k){
  cout<<i<<endl;
  break;
  }
  if (i==n){
    cout<<0<<endl;
  }
  }
  return 0;
}
