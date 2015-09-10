package nl.hanze.web.t41.http;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;

public class HTTPRespons {
	private OutputStream out;
	private HTTPRequest request;

	public HTTPRespons(OutputStream out) {
		this.out = out;
	}

	public void setRequest(HTTPRequest request) {
		this.request = request;
	}

	public void sendResponse() throws IOException {
		byte[] bytes = new byte[HTTPSettings.BUFFER_SIZE];
		FileInputStream fis = null;	
		String fileName = request.getUri();
		if(fileName.equals("/")){
			fileName = "index.html";
		}

		try {		
			File file = new File(HTTPSettings.DOC_ROOT, fileName);			
			FileInputStream inputStream = getInputStream (file);
			
			out.write(getHTTPHeader(fileName, file.exists())); 
			
			int ch = inputStream.read(bytes, 0, HTTPSettings.BUFFER_SIZE);
			while (ch != -1) {
				out.write(bytes, 0, ch);
				ch = inputStream.read(bytes, 0, HTTPSettings.BUFFER_SIZE);
			}

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if (fis != null)
				fis.close();
		}

	}
	
	private FileInputStream getInputStream (File file) {		
		FileInputStream fis = null;
		
		/*
		  *** OPGAVE 4: 1b ***
		  Stuur het bestand terug wanneer het bestaat; anders het standaard 404-bestand.
		*/
		try{
		if(file.exists()){
			fis = new FileInputStream(file);			
		}else{
			fis = new FileInputStream(new File(HTTPSettings.FILE_NOT_FOUND));
		}}catch(Exception e){
			e.printStackTrace();
		}
		
	   	return fis;
		
	}

	private byte[] getHTTPHeader(String fileName, boolean exists) {
		String fileType = getFileType(fileName);		
		String header = "";
		
		if(!exists)
		{
			header = HTTPSettings.CODE_404;
		}
		else if(!Arrays.asList(HTTPSettings.ALLOWED_FILETYPES).contains(fileType)){
			header = HTTPSettings.CODE_500;
		}
		else{
			header = HTTPSettings.CODE_200;
			
		}
		
				
		
		header += "Date: " + HTTPSettings.getDate();
		header += "Server: " + HTTPSettings.SERVER_NAME;
		header += "\n";
		
		byte[] rv = header.getBytes();
		return rv;
	}

	private String getFileType(String fileName) {
		int i = fileName.lastIndexOf(".");
		String ext = "";
		if (i > 0 && i < fileName.length() - 1) {
			ext = fileName.substring(i + 1);
		}

		return ext;
	}

	private void showResponse(byte[] respons) {
		StringBuffer buf = new StringBuffer(HTTPSettings.BUFFER_SIZE);

		for (int i = 0; i < respons.length; i++) {
			buf.append((char) respons[i]);
		}
		System.out.print(buf.toString());

	}

}
