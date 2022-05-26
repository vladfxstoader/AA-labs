#include <iostream>

using namespace std;
//ifstream f ("roby.in");
//ofstream g ("roby.out");
int testOrientare(int p1, int p2, int q1, int q2, int r1, int r2) {
    if (q1*r2 + r1*p2 + p1*q2 - q1*p2 - r1*q2 - p1*r2 == 0)
        return 0;
    else if (q1*r2 + r1*p2 + p1*q2 - q1*p2 - r1*q2 - p1*r2 < 0)
        return -1;
    else
        return 1;
}

int punct11, n, i, punct12, punct21, punct22, punct31, punct32, primulPunct1, primulpunct2, nrS = 0, nrD = 0, nrF = 0;
int main()
{
    //f>>punct11;
    //f>>punct11>>punct12;
    cin>>n;
    cin>>punct11>>punct12;
    primulPunct1 = punct11;
    primulpunct2 = punct12;
    //f>>punct21>>punct22;
    cin>>punct21>>punct22;
    //while (f>>punct31>>punct32) {
    for (i=3;i<=n;++i) {
        cin>>punct31>>punct32;
        if (testOrientare(punct11, punct12, punct21, punct22, punct31, punct32) == 0)
            nrF++;
        else if (testOrientare(punct11, punct12, punct21, punct22, punct31, punct32) < 0)
            nrD++;
        else
            nrS++;
        punct11 = punct21;
        punct12 = punct22;
        punct21 = punct31;
        punct22 = punct32;
    }
    if (testOrientare(punct11, punct12, punct21, punct22, primulPunct1, primulpunct2) == 0)
        nrF++;
    else if (testOrientare(punct11, punct12, punct21, punct22, primulPunct1, primulpunct2) < 0)
        nrD++;
    else
        nrS++;
    cout<<nrS<<" "<<nrD<<" "<<nrF;
    return 0;
}