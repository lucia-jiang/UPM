package series;

public class SeriesDatabase {

	public SeriesDatabase() {

	}

	public boolean openConnection() {
		return false;
	}

	public boolean closeConnection() {
		return false;
	}

	public boolean createTableCapitulo() {
		return false;
	}

	public boolean createTableValora() {
		return false;
	}

	public int loadCapitulos(String fileName) {
		return 0;
	}

	public int loadValoraciones(String fileName) {
		return 0;
	}

	public String catalogo() {
		return null;
	}

	public double mediaGenero(String genero) {
		return 0.0;
	}

	public boolean setFoto(String filename) {
		return false;
	}

}
