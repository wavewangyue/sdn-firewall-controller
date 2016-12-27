"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Host1_S1 = self.addHost( 'h1', ip='192.168.0.1/16')
        Host2_S1 = self.addHost( 'h2', ip='192.168.0.2/16')
        Host3_S2 = self.addHost( 'h3', ip='192.168.1.1/16')
        Host4_S2 = self.addHost( 'h4', ip='192.168.1.2/16')
        Host5_S2 = self.addHost( 'h5', ip='192.168.1.3/16')
        Host6_S3 = self.addHost( 'h6', ip='192.168.2.1/16')
        Host7_S3 = self.addHost( 'h7', ip='192.168.2.2/16')
        Host8_S3 = self.addHost( 'h8', ip='192.168.2.3/16')
        Host9_S3 = self.addHost( 'h9', ip='192.168.2.4/16')
        S1 = self.addSwitch( 's1' )
        S2 = self.addSwitch( 's2' )
        S3 = self.addSwitch( 's3' )

        # Add links
        self.addLink( Host1_S1, S1 )
        self.addLink( Host2_S1, S1 )
        self.addLink( S1, S2 )

        self.addLink( Host3_S2, S2 )
	self.addLink( Host4_S2, S2 )
	self.addLink( Host5_S2, S2 )
        self.addLink( S2, S3 )

        self.addLink( Host6_S3, S3 )
	self.addLink( Host7_S3, S3 )
	self.addLink( Host8_S3, S3 )
	self.addLink( Host9_S3, S3 )


topos = { 'mytopo': ( lambda: MyTopo() ) }

