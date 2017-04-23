/* Notas e Moedas
* Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>*/

#include <stdio.h>

double mod(double a, double b) {
	return a-(((int) (a/b))*b);
}

int main() {
	double N;
	int r1, r2, r3, r4, r5, r6, c1, c2, c3, c4, c5, c6;
	scanf("%lf", &N);
	r1 = (int) N/100;
	r2 = ((int) N % 100)/50;
	r3 = (((int) N % 100)%50)/20;
	r4 = ((((int) N % 100)%50)%20)/10;
	r5 = (((((int) N % 100)%50)%20)%10)/5;
	r6 = ((((((int) N % 100)%50)%20)%10)%5)/2;
	c1 = (((((((int) N % 100)%50)%20)%10)%5)%2)/1;
	c2 = mod(mod(mod(mod(mod(mod(mod(N,100),50),20),10),5),2),1)/0.5;
	c3 = mod(mod(mod(mod(mod(mod(mod(mod(N,100),50),20),10),5),2),1),0.5)/0.25;
	c4 = mod(mod(mod(mod(mod(mod(mod(mod(mod(N,100),50),20),10),5),2),1),0.5),0.25)/0.1;
	c5 = mod(mod(mod(mod(mod(mod(mod(mod(mod(mod(N,100),50),20),10),5),2),1),0.5),0.25),0.1)/0.05;
	c6 = (mod(mod(mod(mod(mod(mod(mod(mod(mod(mod(mod(N,100),50),20),10),5),2),1),0.5),0.25),0.1),0.05)/0.01)+0.001;
	printf("NOTAS:\n");
	printf("%d nota(s) de R$ 100.00\n", r1);
	printf("%d nota(s) de R$ 50.00\n", r2);
	printf("%d nota(s) de R$ 20.00\n", r3);
	printf("%d nota(s) de R$ 10.00\n", r4);
	printf("%d nota(s) de R$ 5.00\n", r5);
	printf("%d nota(s) de R$ 2.00\n", r6);
	printf("MOEDAS:\n");
	printf("%d moeda(s) de R$ 1.00\n", c1);
	printf("%d moeda(s) de R$ 0.50\n", c2);
	printf("%d moeda(s) de R$ 0.25\n", c3);
	printf("%d moeda(s) de R$ 0.10\n", c4);
	printf("%d moeda(s) de R$ 0.05\n", c5);
	printf("%d moeda(s) de R$ 0.01\n", c6);

	return 0;
}