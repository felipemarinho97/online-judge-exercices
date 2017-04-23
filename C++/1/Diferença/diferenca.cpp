// Diferença | Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>
#include <iostream>

main() {
	using namespace std;
	int a, b, c, d, prod1, prod2;

	cin >> a;
	cin >> b;
	cin >> c;
	cin >> d;

	prod1 = a*b;
	prod2 = c*d;

	cout << "DIFERENCA = " << prod1-prod2 << endl;
}