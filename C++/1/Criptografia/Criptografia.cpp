// Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>
// Criptografia
#include <iostream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

	string 
   desloca(string
     entrada){string
      entrada2; for(int 
   	       i = 0; i < (int)
   	        entrada.size(); ++i)
   	         {if (((int) entrada[i]
   	           >= 97) && ((int) entrada[i]
   	         	 <= 122) || ((int) entrada[i] 
   	         	  >= 65 && (int) entrada[i] <= 90))
   	         	   {entrada2 += (char) (((int) entrada[i])+3);
   	         	    } else {entrada2 += entrada[i];
		};
	};
	return entrada2;
}

string inverte(string entrada) {
	int i;
	string string2;
	i = (int) entrada.size();
	for (i; i >= 0; --i) {
		string2 += entrada[i];
	};
	return string2;
}

string desloca_esquerda(string entrada) {
	int tam;
	string saida;
	tam = (int) entrada.size();
	for(int i = 0; i < tam; ++i) {
		if ((int) entrada[i] != 32) {
			if (i > floor(tam/2.0)) {
				saida += (char) (((int) entrada[i]) - 1);
			} else {
				saida += entrada[i];
			};
		} else {
			saida += entrada[i];
		}
	};
	return saida;
}

main() {
	int n;
	vector<string> saidas;
	cin >> n;
	for (int i = 0; i <= n; i++) {
		string entrada, saida;
		getline(cin,entrada);
		saida = (desloca_esquerda(inverte(desloca(entrada))));
		saidas.push_back(saida);
	};
	for (int i = 1; i <= n; i++) {
		cout << saidas[i] << endl;
	}
}