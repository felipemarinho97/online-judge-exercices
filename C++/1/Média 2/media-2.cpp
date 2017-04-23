// Média 2 | Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>
#include <iostream>

main() {
	using namespace std;
	double a, b, c, media;
	cin >> a;
	cin >> b;
	cin >> c;
	
	media = (a*0.2) + (b*0.3) + (c*0.5);
	cout.precision(1);
	cout << "MEDIA = " << fixed << media << endl;
}