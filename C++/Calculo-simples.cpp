#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int num, num2, valor, valor2;
	float preco, preco2;
	cin >> num;
	cin >> valor;
	cin >> preco;
	cin >> num2;
	cin >> valor2;
	cin >> preco2;
	cout << "VALOR A PAGAR: R$ " << setprecision(2) << fixed << valor*preco + valor2*preco2 << endl;
}