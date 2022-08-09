#include <bits/stdc++.h>
using namespace std;

const long long divideBy = 1e9 + 7;

int main()
{
    int n;
    cin>>n;
    vector<int> array(n + 1);
    for (int i = 1;i<=n;i++)cin>>array[i];
    vector<int> M(1e6 + 1);

    // casos base
    M[0] = 1;
    M[1] = 1;

    for (int i = 2;i<=n;i++){

        vector<int> indexesToUpdate;

        for (int j = 1;j<=sqrt(array[i]);j++){
            if (array[i] % j == 0){
                indexesToUpdate.push_back(j);
                if (array[i] / j != j){
                    indexesToUpdate.push_back(array[i] / j);
                }
            }
        }

        sort(indexesToUpdate.begin(),indexesToUpdate.end());
        reverse(indexesToUpdate.begin(),indexesToUpdate.end());

        for (int j : indexesToUpdate){
            M[j] += M[j - 1];
            M[j] %= divideBy;
        }
    }

    int count = 0;
    for (int i = 1;i<=n;i++) count = (count + M[i])% divideBy;
    cout<<count;
    return 0;
}
