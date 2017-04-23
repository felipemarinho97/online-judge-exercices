#include <stdio.h>
#include <math.h>

int main()
{
	double raio, pi, area;
	pi = 3.14159;
	scanf("%lf", &raio);
	area = pi*pow(raio,2.0);
	printf("A=%.4f\n", area);

	return 0;
}