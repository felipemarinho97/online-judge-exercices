/*Aluno: Felipe Marinho*/

import  java.util.Scanner;

public class Loop {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int idades = 0;
		String[] idadesStr = sc.nextLine().split(" ");
		for (String e : idadesStr) {
			int o = Integer.parseInt(e);
			idades = idades + o;
		}
		double media = idades/(double)(idadesStr.length);
		System.out.println("Média: " + media);

	}
}