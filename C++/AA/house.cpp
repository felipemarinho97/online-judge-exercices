#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int n, a, b;
	bool key;

	cin >> n;
	cin >> a;
	cin >> b;
	
	if (b >= 0) {key = true;}
	else {key = false;};

	for (int i = 1; i <= abs(b); ++i)
	{
		a++;
		if (a == n+1)
		{
			a = 1;
		}
		cout << a << endl;
	};


}
