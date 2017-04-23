/*Aluno: Felipe Marinho*/

import java.util.Scanner;

public class LoopIndefinido {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int idade = sc.nextInt();
		int soma = 0;
		double count = 0;
		while (idade != 0) {
			soma += idade;
			count += 1;
			System.out.println("Média atual: " + (soma/count));
			idade = sc.nextInt();
		}

	}
}