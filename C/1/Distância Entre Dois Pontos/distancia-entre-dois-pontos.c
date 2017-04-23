/* Distância Entre Dois Pontos
* Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>*/

#include <stdio.h>
#include <math.h>

int main() {
	float x1, x2, y1, y2;
	double dis, powx, powy;
	
	scanf("%f %f", &x1, &y1);
	scanf("%f %f", &x2, &y2);
	
	powx = pow((x2 - x1),2);
	powy = pow((y2 - y1),2);
	dis = sqrt(powx+powy);

	printf("%.4lf\n", dis);
}