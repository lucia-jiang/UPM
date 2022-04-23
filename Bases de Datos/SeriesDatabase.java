package series;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Date;

public class SeriesDatabase {
	private java.sql.Connection conn;
	private static final String SEPARADOR = ";";
	
	public SeriesDatabase() {

	}
	
	/**
	 * Este método implementa la apertura de la conexión con la base de datos
	 * @return El método devuelve true si abre correctamente la conexión y false si ninguna conexión es abierta
	 */
	public boolean openConnection() {
		if (conn != null)
			return false;
		String serverAdress = "localhost:3306";
		String db = "series";
		String user = "series_user";
		String pass = "series_pass";
		String url = "jdbc:mysql://" + serverAdress + "/" + db;
		try {
			conn = DriverManager.getConnection(url, user, pass);
		} catch (SQLException e) {
			e.printStackTrace();
			return false;
		}
		System.out.println("Conectado a la base de datos!");
		return true;
	}

	/**
	 * Este método implementa el cierre de la conexión con la base de datos
	 * @return El método devuelve true si se ejecuta sin errores y false si ocurre alguna excepción.
	 */
	public boolean closeConnection() {
		try {
			conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}
	
	/**
	 * Este método implementa la creación de la tabla capitulo
	 * @return El método devuelve false si la tabla no se ha podido crear y true si la tabla se ha creado correctamente.
	 */
	public boolean createTableCapitulo() {
		openConnection();
		// Para crear la tabla capitulo, al ser una entidad débil hemos cogido la clave primaria de temporada, 
		// que a su vez es entidad débil de serie 
		String query = "CREATE TABLE capitulo ("
				+ "id_serie INT, "
				+ "n_temporada INT, "
				+ "n_orden INT, "
				+ "fecha_estreno DATE, "
				+ "titulo VARCHAR(100),"
				+ "duracion INT,"
				+ "PRIMARY KEY(id_serie,n_temporada, n_orden), "
				+ "FOREIGN KEY (id_serie, n_temporada) REFERENCES temporada(id_serie, n_temporada)"
				+ "ON DELETE CASCADE ON UPDATE CASCADE" + ");";

		try {
			Statement st = conn.createStatement();
			st.executeUpdate(query);
			st.close();
		} catch (SQLException e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}
	
	/**
	 * Este método implementa la creación de la tabla conoce
	 * @return false si la tabla no se ha podido crear y true si la tabla se ha creado correctamente.
	 */
	public boolean createTableValora() {
		openConnection();
		
		// Para crear la tabla valora, al ser una relación, hemos cogido como clave primaria 
		// las claves primarias de capitulo y usuario además de fecha 
		String query = "CREATE TABLE valora ("
				+ "id_serie INT, "
				+ "n_temporada INT, "
				+ "n_orden INT, "
				+ "id_usuario INT, "
				+ "fecha DATE,"
				+ "valor INT,"
				+ "PRIMARY KEY(id_usuario, id_serie, n_temporada, n_orden, fecha), "
				+ "FOREIGN KEY (id_serie, n_temporada, n_orden) REFERENCES capitulo(id_serie, n_temporada, n_orden)"
				+ "ON DELETE CASCADE ON UPDATE CASCADE, "
				+ "FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)"
				+ "ON DELETE CASCADE ON UPDATE CASCADE" + ");";

		try {
			Statement st = conn.createStatement();
			st.executeUpdate(query);
			st.close();
		} catch (SQLException e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}
	
	/**
	 * Este método inserta en la base de datos los capítulos de fileName
	 * @param fileName fichero csv que contiene información sobre las temporadas
	 * @return cantidad de elementos insertados en la tabla
	 */
	public int loadCapitulos(String fileName) {
		openConnection();
		
		BufferedReader bufferLectura = null;
		int res = 0;

		try {
			// Ponemos el autocommit a false para que se ejecute todo como una única transacción
			conn.setAutoCommit(false); 
			
			// Abrimos el fichero .csv pasado como parámetro, para leerlo, hemos incluido el fichero en la carpeta del proyecto
			bufferLectura = new BufferedReader(new FileReader(fileName));

			// Leemos la primera linea del archivo
			String linea = bufferLectura.readLine();
			// Separamos la linea mediante la constante SEPARADOR
			String[] campos = linea.split(SEPARADOR);
	
			String query = "INSERT INTO capitulo(" + 
								campos[0] + "," + 
								campos[1] + "," + 
								campos[2] + "," + 
								campos[3] + "," + 
								campos[4] + "," + 
								campos[5] + ")" + 
								"VALUES(?,?,?,?,?,?);";
			
			PreparedStatement pst = conn.prepareStatement(query);
			linea = bufferLectura.readLine();
			// Hacemos un bucle para ir leyendo las lineas del .csv
			while (linea != null) {
				campos = linea.split(SEPARADOR);
				pst.setInt(1, Integer.parseInt(campos[0])); 
				pst.setInt(2, Integer.parseInt(campos[1]));
				pst.setInt(3, Integer.parseInt(campos[2]));
				Date date = new Date(0);
				date = Date.valueOf(campos[3]);
				pst.setDate(4, date);
				pst.setString(5, campos[4]);
				pst.setInt(6, Integer.parseInt(campos[5]));
				res += pst.executeUpdate();
				// Volver a leer otra línea del fichero
				linea = bufferLectura.readLine();
			}	
			pst.close();
			conn.commit(); //fin de la transacción, se encarga de fijar los datos en la bbdd
			conn.setAutoCommit(true); //reestablecemos el AC=1

		} catch (IOException e) {
			e.printStackTrace();
			return 0;
		} catch (SQLException e) {
			e.printStackTrace();
			return 0;
		} finally {
			// Cerramos el buffer de lectura
			if (bufferLectura != null) {
				try {
					bufferLectura.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}

		System.out.println("Query ejecutada");

		return res;

	}
	
	/**
	 * Este método inserta en la base de datos las valoraciones de fileName
	 * @param fileName fichero csv que contiene información sobre las valoraciones
	 * @return cantidad de elementos insertados en la tabla
	 */
	public int loadValoraciones(String fileName) {
		BufferedReader bufferLectura = null;
		int res = 0;

		try {
			bufferLectura = new BufferedReader(new FileReader(fileName));
			String linea = bufferLectura.readLine();
			String[] campos = linea.split(SEPARADOR);

			String query = "INSERT INTO valora(" + 
								campos[0] + "," + 
								campos[1] + "," + 
								campos[2] + "," + 
								campos[3] + "," + 
								campos[4] + "," + 
								campos[5] + ")" + 
								"VALUES(?,?,?,?,?,?);";
			PreparedStatement pst = conn.prepareStatement(query);
			linea = bufferLectura.readLine();
			while (linea != null) {
				campos = linea.split(SEPARADOR);
				pst.setInt(1, Integer.parseInt(campos[0])); 
				pst.setInt(2, Integer.parseInt(campos[1]));
				pst.setInt(3, Integer.parseInt(campos[2]));
				pst.setInt(4, Integer.parseInt(campos[3]));
				Date date = new Date(0);
				date = Date.valueOf(campos[4]);
				pst.setDate(5, date);
				pst.setInt(6, Integer.parseInt(campos[5]));
				res += pst.executeUpdate();
				linea = bufferLectura.readLine();
			}
			pst.close();

		} catch (IOException e) {
			e.printStackTrace();
			return 0;
		} catch (SQLException e) {
			e.printStackTrace();
			return 0;
		} finally {
			if (bufferLectura != null) {
				try {
					bufferLectura.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		System.out.println("Query ejecutada");
		return res;
	}
	
	/**
	 * Este método consulta en la base de datos la lista de todas las series y la cantidad de episodios de cada temporada
	 * @return String con dicha información. Si no hay series se retorna {} y si no hay temporadas, 
	 * 		   el campo de los capitulos aparecerá vacío. En caso de excepción null
	 */
	public String catalogo() {
		this.openConnection();
		String res = "";
		try {
			Statement st = conn.createStatement();
			// Primero seleccionamos las series por el id una sola vez
			ResultSet rs = st.executeQuery("SELECT DISTINCT id_serie, titulo FROM serie;");
			while (rs.next()) {
				res += "," + rs.getString(2) + ":[";
				int idSerieAct = rs.getInt(1);
				// Contamos el número de capítulos de cada temporada para cada una de las series
				// Imprimimos el nombre de la serie junto con el número de capítulos ordenados por la temporada de forma ascendete
				Statement st2 = conn.createStatement();
				ResultSet rs2 = st2.executeQuery("SELECT n_capitulos, n_temporada FROM temporada WHERE id_Serie LIKE '"
								+ idSerieAct + "' ORDER BY n_temporada ASC;");
				if (rs2.next())
					res += rs2.getInt(1);
				while (rs2.next()) {
					res += "," + rs2.getInt(1);
				}
				rs2.close();
				st2.close();
				res += "]";
			}
			rs.close();
			st.close();
		} catch (SQLException e) {
			e.printStackTrace();
			return null;
		}
		res = res.replaceFirst(",", "{");
		return res + "}";
	}
	
	/**
	 * Este método consulta las valoraciones los capítulos del género pasado como parámetro y calcula su media
	 * @param genero descripción
	 * @return media, si no existe el género -1.0, en caso de excepción -2.0 y si existe sin capítulos 0.0
	 */
	public double mediaGenero(String genero) {
		this.openConnection();
		// De las tablas genero y pertenece calculamos la media y contamos el número de apariciones del género
		String query = "SELECT avg(valor), count(descripcion) FROM genero, pertenece, valora WHERE descripcion LIKE '"
				+ genero
				+ "' AND genero.id_genero = pertenece.id_genero AND valora.id_serie=pertenece.id_serie";	
		double res = 0;
		Statement st;
		ResultSet rs;
		try {
			st = conn.createStatement();
			rs = st.executeQuery(query);
			// Si el número de apariciones es 0 retornamos -1.0
			if(rs.next() && rs.getInt(2)==0){
				return -1.0;
			}
			res = rs.getDouble(1);
			rs.close(); 
			st.close();
		} catch (SQLException e) {
			e.printStackTrace();
			return -2.0;
		}
		return res;
	}

	/**
	 * Este método debe añadir la foto contenida en el fichero filename y cuyo primer apellido sea Cabeza en caso de que no tenga foto
	 * @param filename
	 * @return true si inserta foto y false en caso contrario (más de un usuario con apellido1 Cabeza o si ya tiene foto)
	 */
	public boolean setFoto(String filename) {
		this.openConnection();
		
		// Primero seleccionamos la foto y contamos el número de apariciones del apellido1 Cabeza
		String query = "SELECT fotografia, COUNT(apellido1) from usuario WHERE apellido1 = 'Cabeza';";
		try {
			Statement st = conn.prepareStatement(query);
			ResultSet rs = st.executeQuery(query);
			// Si el número de apariciones es distinto de 1 o ya tiene foto retornamos falso y no asignamos foto nuevamente
			if (rs.next() && (rs.getInt(2) != 1 || rs.getBlob(1) != null)) 
				return false;
			// Actualizamos la foto
			String query2 = "UPDATE usuario SET fotografia=? WHERE apellido1 = 'Cabeza';";
			PreparedStatement st2 = conn.prepareStatement(query2);
			File f = new File(filename);
			FileInputStream fis = new FileInputStream(f);
			st2.setBinaryStream(1, fis, (int) f.length());
			st2.executeUpdate();
			st2.close();
			
			rs.close();
			st.close();
			
		} catch (SQLException e) {
			e.printStackTrace();
			return false;
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}
}
