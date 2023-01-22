#!/usr/bin/perl

# P1/p1.pl

# ************************************************
# ***************** LIBRARIES ********************
use warnings;
use strict;
use SOAP::Lite;

# ************************************************
# ****************** GLOBALS *********************
my $BUFFERSIZE = 4096;

# *** SOAP CONSTS ***
my $endpoint = 'http://127.0.0.1/soap/php/p2.php';
my $soapaction = 'http://127.0.0.1/soap/php/p2.php/simpleService';
my $method = 'simpleService';

my $buffer;
my $bytes = 0;

# *************************************************
# ***************** MAIN DRIVE ********************
# SOAP client bind
my $client = SOAP::Lite->new(proxy => $endpoint);

# Main loop
while(1){
	# Get data from STDIN
	$bytes = sysread(STDIN, $buffer, $BUFFERSIZE);

	# if there are read bytes
	if ($bytes > 0) {
		# Set SOAP params
		my @params = (
			SOAP::Data->name('param1')->value($buffer)
		);

		# Send data via SOAP service
		my $response = $client->call(SOAP::Data->name($method)->attr({'xmlns' => $soapaction}), @params);

		if($response->fault){
			print("Error: ".$response->faultstring);
			die "Error: ".$response->faultstring;
		}
	} else { 
		last; 
	}
}
