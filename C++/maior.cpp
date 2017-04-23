#include <iostream>
#include <cmath>

using namespace std;

int maior(int a, int b) {
	return (a+b+abs(a-b))/2.0;
}

int main() {
	int a, b, c, ab;
	cin >> a;
	cin >> b;
	cin >> c;
	cout << maior(maior(a,b),c) << " eh o maior" << endl;
}