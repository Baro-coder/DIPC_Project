import org.apache.xmlrpc.*;

public class p4 {
	private static int port = 5004;
	
	// udostepniana metoda ---------------------------------------------
	public int store(String str) {
		System.out.println(str);
        return 0;
	}

	public static void main (String [] args) {
		try {
            System.out.println("Attempting to start server...");

			WebServer server = new WebServer( p4.port );
			server.addHandler( "Server", new p4() );
            server.start();

            System.out.println("Server started successfully.");
            System.out.println("Accepting requests.\n");

		}catch (Exception exception) {
			System.err.println( "Server: " + exception );
		}
	}
}
