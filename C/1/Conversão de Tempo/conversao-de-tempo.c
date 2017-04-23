/* Conversão de Tempo
* Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>*/

#include <stdio.h>

int main() {
	int N, hora, min, seg;
	scanf("%d", &N);
	hora = (N / 60) / 60;
	min =  (N / 60) % 60;
	seg =  (N % 60) % 60;
	printf("%d:%d:%d\n", hora, min, seg);
}