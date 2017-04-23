/* Área
* Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>*/

#include <stdio.h>

int main() {
	double a, b, c, pi, triangulo, circulo, trapezio, quadrado, retangulo;
	
	scanf("%lf %lf %lf", &a, &b, &c);
	
	pi = 3.14159;
	triangulo = (a*c)/2.0;
	circulo = pi*(c*c);
	trapezio = ((a+b)*c)/2.0;
	quadrado = b*b;
	retangulo = a*b;

	printf("TRIANGULO: %.3lf\n", triangulo);
	printf("CIRCULO: %.3lf\n", circulo);
	printf("TRAPEZIO: %.3lf\n", trapezio);
	printf("QUADRADO: %.3lf\n", quadrado);
	printf("RETANGULO: %.3lf\n", retangulo);

}