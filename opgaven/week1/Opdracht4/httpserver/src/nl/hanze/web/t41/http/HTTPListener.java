package nl.hanze.web.t41.http;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

import nl.hanze.web.t41.runner.HTTPRunner;

public class HTTPListener {
	private int portnumber;	
	private HTTPHandler httpHandler;
	
	public HTTPListener(int port, HTTPHandler hh) throws Exception {
		if (port < HTTPSettings.PORT_MIN || port > HTTPSettings.PORT_MAX) 
			throw new Exception("Invalid TCP/IP port, out of range");
		this.portnumber=port;
		this.httpHandler=hh;
		
		HTTPSettings.DATATYPES.put("html", "text/html; charset=UTF-8");
		HTTPSettings.DATATYPES.put("css",  "text/css; charset=UTF-8");
		HTTPSettings.DATATYPES.put("gif",  "image/gif");
		HTTPSettings.DATATYPES.put("png",  "image/png");
		HTTPSettings.DATATYPES.put("jpg",  "image/jpeg");
		HTTPSettings.DATATYPES.put("jpeg", "image/jpeg");
		HTTPSettings.DATATYPES.put("js",   "text/javascript");
		HTTPSettings.DATATYPES.put("txt",  "text/plain");
		HTTPSettings.DATATYPES.put("pdf",  "application/pdf");
	}
	
	public void startUp() throws Exception {
		ServerSocket servsock=new ServerSocket(portnumber);
		System.out.println("Server started");
		System.out.println("Waiting requests at port " + portnumber);

		while (true) {
			Socket s=servsock.accept();
			try{
				httpHandler.handleRequest(s.getInputStream(), s.getOutputStream());
			
			}catch(Exception e){
				s.getOutputStream().write((HTTPSettings.CODE_500 + "Date: " + HTTPSettings.getDate() + "Server: " +
			HTTPSettings.SERVER_NAME + "\n" + e.getMessage()).getBytes());
			}finally{
				s.close();
			}
		}		
	}
}
