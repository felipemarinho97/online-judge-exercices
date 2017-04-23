/*Aluno: Felipe Marinho*/

public class QuadranteCartesiano {
	public static void main(String[] args) {
		int x = 0;
		int y = 0;
		if (x > 0 && y > 0) {
			System.out.println("Primeiro Quadrante.");
		} else if (x < 0 && y > 0) {
			System.out.println("Segundo Quadrante.");
		} else if (x < 0 && y < 0) {
			System.out.println("Terceiro Quadrante.");
		} else if (x > 0 && y < 0) {
			System.out.println("Quarto Quadrante.");
		} else {
			System.out.println("Sobre os eixos.");
		}
	}
}