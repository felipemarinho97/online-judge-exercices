/* Fórmula de Bhaskara
* Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>*/

#include <stdio.h>
#include <math.h>

int main() {
	double a, b, c, delta, div, r1, r2;
	scanf("%lf %lf %lf", &a, &b, &c);
	delta = pow(b,2) - (4*a*c);
	if (a == 0 || delta < 0) {
		printf("Impossivel calcular\n");
	}
	else {
		delta = sqrt(delta);
		div = 2.0*a;
		r1 = (-b +delta)/div;
		r2 = (-b -delta)/div;
		printf("R1 = %.5lf\n", r1);
		printf("R2 = %.5lf\n", r2);
	}

}