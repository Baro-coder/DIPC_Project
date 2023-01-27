import org.apache.xmlrpc.*;

public class p4 {
	private static int PORT = 5004;
	private static int CODE_SUCCESS = 0;

	public int deliver(byte[] data) {
		// Conver bytes array to String
		String new_data = new String(data);

		// forward decoded data to STDOUT
		System.out.print(new_data);

		return p4.CODE_SUCCESS;
	}

	public static void main (String [] args) {
		try {
            System.err.println("Attempting to start server...");

            // Server Register
			WebServer server = new WebServer( p4.PORT );
			server.addHandler( "Server", new p4() );
            server.start();

            System.err.println("Server started successfully.");
            System.err.println("Accepting requests.\n");

		}catch (Exception exception) {
			System.err.println( "Server: " + exception );
		}
	}
}
