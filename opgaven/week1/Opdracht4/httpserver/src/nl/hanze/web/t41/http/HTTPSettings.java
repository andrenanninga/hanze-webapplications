package nl.hanze.web.t41.http;

import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.HashMap;

public final class HTTPSettings {
	// Opgave 4: 1a
	// ZET HIER DE JUISTE DIRECTORY IN WAAR JE BESTANDEN STAAN.
	
	static final String DOC_ROOT = "F:/Users/Lasse/Documents/GitHub/hanze-webapplications/opgaven/week1/Opdracht4/httpserver/content/";
	static final String FILE_NOT_FOUND = "F:/Users/Lasse/Documents/GitHub/hanze-webapplications/opgaven/week1/Opdracht4/httpserver/error/404.txt";
	static final String FILE_TYPE_UNSUPPORTED = "F:/Users/Lasse/Documents/GitHub/hanze-webapplications/opgaven/week1/Opdracht4/httpserver/error/500.txt";

	
	static final int BUFFER_SIZE = 2048;	
	static final int PORT_MIN=0;
	static final int PORT_MAX=65535;
	
	static final public int PORT_NUM = 4444;
	static final HashMap<String, String> dataTypes = new HashMap<String, String>();	
	static final String SERVER_NAME = "Onze mooie server\r\n";

	static final String[] DAYS = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
	static final String[] MONTHS = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
	static final String[] ALLOWED_FILETYPES = {"html", "css", "js", "txt", "gif", "png", "jpeg", "jpg", "pdf"};
	
	static final String CODE_200 = "HTTP/1.1 200 OK\r\n";
	static final String CODE_404 = "HTTP/1.1 404 NOT FOUND\r\n";
	static final String CODE_500 = "HTTP/1.1 500 UNSUPPORTED MEDIA TYPE\r\n";

	
	
	public static String getDate() {
		GregorianCalendar cal = new GregorianCalendar();
		String rv = "";
		rv += DAYS[cal.get(Calendar.DAY_OF_WEEK) - 1] + ", ";
		rv += cal.get(Calendar.DAY_OF_MONTH) + " " + MONTHS[cal.get(Calendar.MONTH)];
		rv += " " + cal.get(Calendar.YEAR) + "\r\n";
		
		return rv;
	}
}
