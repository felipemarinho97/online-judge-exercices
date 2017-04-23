/*Aluno: Felipe Marinho*/

import java.util.Scanner;

public class DiferencaArrays {
	public static String[] diferencaIdades(String[] idades1, String[] idades2) {
		String[idades1.lenght] resultado;
		for (i = 0; i < idades1.lenght; i++) {
			List<String> list = new ArrayList<String>();
			list.add((int)(idades1[i]) - (int)(idades2[i]));
		}
		return list
	}
}