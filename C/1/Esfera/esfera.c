/* Esfera
* Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>*/
#include <stdio.h>
#include <math.h>

int main() {
	double raio, pi, volume;
	pi = 3.14159;
	scanf("%lf", &raio);
	volume = (4/3.0) * pi * pow(raio,3);
	printf("VOLUME = %.3lf\n", volume);
}