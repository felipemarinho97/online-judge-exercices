/* Salário com Bônus
* Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>*/
#include <stdio.h>

int main() {
	char nome[41];
	double salario, vendas, comisao, salario_with_bonus;
	scanf("%s", nome);
	scanf("%lf", &salario);
	scanf("%lf", &vendas);
	comisao = vendas*0.15;
	salario_with_bonus = salario + comisao;
	printf("TOTAL = R$ %.2f\n", salario_with_bonus);

}