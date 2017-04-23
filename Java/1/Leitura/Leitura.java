/*Aluno: Felipe Marinho*/

import java.util.Scanner;

public class Leitura {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int idade = sc.nextInt();

		if (idade == 18) {
			System.out.println("\\o\\ |o/ \\o/ /o/");
		} else if (idade < 18) {
			System.out.println("Meu bb!");
		} else {
			System.out.println("Oi tio!");
		}
	}
}