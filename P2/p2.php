<?php
	if( preg_match( "/^wsdl$/i", $_SERVER['QUERY_STRING'] ) ){ 
        $wsdl = file_get_contents( 'p2.wsdl' );
		if( $wsdl )
			echo $wsdl;
	} else { 
		class PPRSrv {
			public function simpleService( $str ){
				// Redirect STDERR to file
				fclose($STDERR);
				$STDERR = fopen('/home/student/PPR_Project/P2/ppr_p2_php.err.log', 'w');
				// Write received bytes count into STDERR
				fwrite($STDERR, $str."\n");

				// TCP Server Address
				$host = '127.0.0.1';
				$port = 5003;
				
				// Socket create
                $socket = socket_create(AF_INET, SOCK_STREAM, 0);
				
				// TCP Connection
				if(socket_connect($socket, $host, $port) === false) {
                    return "Error: Socket connect: ".socket_strerror(socket_last_error());
				}
				
				// Forward data
                if(socket_send($socket, $str, strlen($str), 0) === false) {
                    return "Error: Socket send: ".socket_strerror(socket_last_error());
				}

				// Wait for server response
				if(($str = socket_read($socket, 512, 0)) === false) {
                    return "Error: Socket read: ".socket_strerror(socket_last_error());
				}
				
				// Socket close
                socket_close($socket);
				
				// Return response
				return "Response: ".$str;
			}
		}
		
		$opt = array( 'uri' => 'http://127.0.0.1/soap/php/p2.php' );
		$srv = new SoapServer( NULL, $opt );
		$srv->setClass('PPRSrv');
		$srv->handle();
	}
?>

