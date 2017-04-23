/*Aluno: Felipe Marinho*/

public class Condicional {
	public static void main(String[] args) {
		double minhaAltura, meuPeso, bmi;
		minhaAltura = 1.83;
		meuPeso = 76.5;
		bmi = meuPeso / Math.pow(minhaAltura,2);

		if (bmi > 25) {
			System.out.println("Faça uma avaliação médica");
		} else {
			System.out.println("Peso sob controle");
		}
	}
}