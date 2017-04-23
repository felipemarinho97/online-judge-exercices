#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int x;
	float y;
	cin >> x;
	cin >> y;
	cout << setprecision(3) << fixed << x/y << " km/l" << endl;
}