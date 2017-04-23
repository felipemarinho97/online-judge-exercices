/* Salário
* Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>*/

#include <stdio.h>

int main() {
	int num, horas;
	float salario, per_hora;
	scanf("%d", &num);
	scanf("%d", &horas);
	scanf("%f", &per_hora);
	salario = horas*per_hora;
	printf("NUMBER = %d\n", num);
	printf("SALARY = U$ %.2f\n", salario);
}
