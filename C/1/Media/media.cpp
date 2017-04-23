#include <iostream>

main() {
	using namespace std;
	double a, b, media, x;
	cin >> a;
	cin >> b;
	cout.precision(5);
	media = (a*3.5) + (b*7.5);
	x = media/11.0; 
	cout << "MEDIA = " << fixed << x << endl;
}