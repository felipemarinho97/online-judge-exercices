/*Aluno: Felipe Marinho*/

import java.util.Scanner;

public class Leitura2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String[] nomeIdade = sc.nextLine().split(" ");
		String nome = nomeIdade[0];
		int idade = Integer.parseInt(nomeIdade[1]);
		String sobrenome = sc.nextLine();

		if (idade == 18) {
			System.out.println("\\o\\ |o/ \\o/ /o/");
		} else if (idade < 18) {
			System.out.println(nome + " " + sobrenome + ", meu bb!");
		} else {
			System.out.println(nome + " " + sobrenome + ", oi tio!");
		}
	}
}