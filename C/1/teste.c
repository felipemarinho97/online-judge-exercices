#include <stdio.h>
int main()
{
	int incio,fim,incr;
	float f, c;
	incio = 0;
	fim = 300;
	incr = 20;

	f = incio;
	while (incio <= fim) {
		c = (5.0/9.0) * (f-32.0);
		printf("%4.0f %6.1f\n", f,c);
		f = f + incr;
		incio = incio + incr;
	}

}
