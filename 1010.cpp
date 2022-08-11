#include<bits/stdc++.h>
 
using namespace std;
 
int main() {
    
    int a,b,c,d;
    double x,y,ans;
    cin>>a>>c>>x;
    cin>>b>>d>>y;
    ans=(c*x)+(d*y);
    cout<<fixed;
    cout<<setprecision(2)<<"VALOR A PAGAR: R$ "<<ans<<endl;
    
    return 0;
}