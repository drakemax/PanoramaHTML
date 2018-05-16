# This has created files in C:\Users\drake\Downloads\_Omori Low High Res 360 Panorama\Data\examples\2High directory.
import logging
logging.basicConfig(filename='logfile1.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
s = '''
<!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      '''

t='''
      <link rel="stylesheet" href="../photo-sphere-viewer.min.css">
	  
	    <!--   These are for Spot image on plan     -->
		<script type="text/javascript" src="../jquery-3.3.1.min.js"></script> 
		<script type="text/javascript" src="../jquery.maphilight.js"></script>
		
		 <!-- Main photosphere setup -->
        <script  src="../three.min.js"></script>
        <script type="text/javascript" src="../D.min.js"></script>
        <script type="text/javascript" src="../doT.min.js"></script>
        <script type="text/javascript" src="../uevent.min.js"></script>
        <script type="text/javascript" src="../CanvasRenderer.js"></script>
        <script type="text/javascript" src="../Projector.js"></script>
        <script type="text/javascript" src="../photo-sphere-viewer.min.js"></script> 
		
		<!-- These below are for tabs-->
		 <link  rel="stylesheet" href="../jquery-ui-1.12.1/jquery-ui.css">
		<script type="text/javascript" src="../jquery-ui-1.12.1/jquery-ui.js"></script>


   <!-- This funcrtion for hotspots on plan- -->
 <script type="text/javascript">$(function() {
        $('.map').maphilight();
        $('#squidheadlink').mouseover(function(e) {
            $('#squidhead').mouseover();
        }).mouseout(function(e) {
            $('#squidhead').mouseout();
        }).click(function(e) { e.preventDefault(); });
    });</script>

<!-- This funcrtion for TABS-->
  <script>
  $( function() {
    $( "#tabs" ).tabs().addClass( "ui-tabs-vertical ui-helper-clearfix" );
    $( "#tabs li" ).removeClass( "ui-corner-top" ).addClass( "ui-corner-left" );
  } );
  </script>
  <style>
  .ui-tabs-vertical { width: 100%; }
  .ui-tabs-vertical .ui-tabs-nav { padding: .2em .1em .2em .2em; float: left; width: 12em; }
  .ui-tabs-vertical .ui-tabs-nav li { clear: left; width: 100%; border-bottom-width: 1px !important; border-right-width: 0 !important; margin: 0 -1px .2em 0; }
  .ui-tabs-vertical .ui-tabs-nav li a { display:block; }
  .ui-tabs-vertical .ui-tabs-nav li.ui-tabs-active { padding-bottom: 0; padding-right: .1em; border-right-width: 1px; }
  .ui-tabs-vertical .ui-tabs-panel { padding: 1em; float: left; width: 80%;}
  </style>
</head>
<body>


 <!--This IS TABS-->
<div id="tabs">
  <ul>
  <li><a href="#tabs-1">Panorama</a></li>
    <li><a href="#tabs-2">Ground Floor Plan</a></li>
	<li><a href="#tabs-3">First Floor Plan</a></li>
	  </ul>
  
    <!--This IS TAB 1-->
	<div id="tabs-1">
		  <div id="photosphere"></div>
		  <p>360/180 photosphere of room. Click on hotlinks to move to 
		  another room photosphere or use tab to select plan and hover on room code. If there is a red dot then 
		  there is a room photosphere associated with that room.</p>
	 </div>			  

	<!--This IS TAB 2-->
   <div id="tabs-2">
			<H1>  Ground Floor plan of site. </H1>
			 <h2>Click on <strong>Room Name</strong> to go to panorama view.</h2>
			 
			 <div id="box1">
			<img src="OmoriPlanGround.jpg" width="1000" class="map" usemap="#simple">
						<map name="simple">
				 
					  <area  href="Ground Dining.html" shape="circle" coords="727,506,40" alt="Dining" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					  <area   href="Ground Living.html" shape="circle" coords="335,506,40" alt="Living" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}'  title="Click HERE to go to Panorama">
						<area  href="Stairwell landing.html" shape="circle" coords="158,172,40"  alt="Stair" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					  <area  href="Ground Kitchen.html" shape="circle" coords="745,196,40"  alt="Living" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					   <area  href="Ground WC.html" shape="circle" coords="273,143,40"  alt="WC" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					  <area  href="Ground Utility.html" shape="circle" coords="435,169,40"  alt="Utility" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					 
					 </map>
			</div>
    
  </div>
  
  <!--This IS TAB 3-->
   <div id="tabs-3">
			<H1>  First Floor plan of site. </H1>
			 <h2>Click on <strong>Room Name</strong> to go to panorama view.</h2>
			 
			 <div id="box2">
			<img src="OmoriPlanFirst.jpg" width="1000" class="map" usemap="#simple1">

					<map name="simple1">

					   <area  id="squidhead" href="Staiwell Landing 2.html" shape="circle" coords="130,207,40" alt="Dining" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					 <!-- <area   href="Upper HWC Cupd.html" shape="circle" coords="423,230,40" alt="Living" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}'  title="Click HERE to go to Panorama">  -->
						<area   href="Upper HWC Cupd.html" shape="circle" coords="303,103,40"  alt="Stair" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					  <area  href="Upper WC.html"shape="circle" coords="415,112,40"  alt="Living" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					   <area  href="Upper Bathroom.html" shape="circle" coords="581,96,40"  alt="WC" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					  <area  href="Upper Bed 1.html" shape="circle" coords="707,322,40"  alt="Utility" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					  <area   href="Upper Deck.html" shape="circle" coords="446,698,40" alt="Living" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}'  title="Click HERE to go to Panorama">
						<area  href="Upper Bed 2.html" shape="circle" coords="389,432,40"  alt="Stair" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					  <area  href="Upper Bed 3.html" shape="circle" coords="170,420,40"  alt="Living" data-maphilight='{"stroke":false,"fillColor":"ff0000","fillOpacity":0.6}' title="Click HERE to go to Panorama">
					 
					 </map>
			</div>
    
  </div>
 
</div>

 <!--This is being called by the space where the photosphere will be on the page-->
<script type="text/template" id="lorem-content">
<a href="0Ground Kitchen.jpg.html"><font color="FF00CC">Kitchen</font></a><br/>
<p> The above text is a hyperlink to the kitchen. 
Kitchen joinery 20 years old </p> 
</script>

<script>
/**
 * Initialize the viewer
 */
var PSV = new PhotoSphereViewer({
  // main configuration

'''
p = '''

container: 'photosphere',
  usexmpdata: false,  // This is code that allows it to work in IE11
  loading_img:  '../photosphere-logo.gif',
  time_anim: false,
  caption: 'Wellington City Council Building XXX X XX ',
  default_fov: 90,//70,
  default_lat: 0.1,//0.3,
  mousewheel: true,//false,
  size: {
    height: 1000 //was 500
  },

  // list of markers
  markers: [
    {
      // image marker that opens the panel when clicked
      id: 'image',
      //longitude:3.2,//0.2, (0 to 2Pi=6.28)
      //latitude: 0,// -0.13770,(-1.57 to 1.57 , 0 horizon)
	  x: 3135,
	  y: 1493,
      image: '../pin2.png',
      width: 32,
      height: 32,
      anchor: 'bottom center',
      tooltip: 'Kitchen <b>Click me!</b>',
      content: document.getElementById('lorem-content').innerHTML
    },
    {
      // html marker living
      id: 'text1',
      x: 1829,
	  y: 1513,
      html: 'CLICK <a href="0Ground Living.jpg.html"><font color="FF00CC"><h1>&oplus;</h1></font></a> HERE',
      anchor: 'bottom right',
      scale: [0.5, 1.5],
      style: {
        maxWidth: '100px',
        color: 'white',
        fontSize: '20px',
        fontFamily: 'Helvetica, sans-serif',
        textAlign: 'center'
      },
      tooltip: {
        content: 'An HTML marker',
        position: 'right'
      }
    },
    {
      // html marker utility
      id: 'text2',
      x: 2181,
	  y: 1475,
      html: 'CLICK <a href="0Ground Utility.jpg.html"><font color="FF00CC"><h1>&oplus;</h1></font></a> HERE',
      anchor: 'bottom right',
      scale: [0.5, 1.5],
      style: {
        maxWidth: '100px',
        color: 'white',
        fontSize: '20px',
        fontFamily: 'Helvetica, sans-serif',
        textAlign: 'center'
      },
      tooltip: {
        content: 'An HTML marker',
        position: 'right'
      }
    },
  ],
});

/**
 * Create a new marker when the user clicks somewhere
 */
PSV.on('click', function(e) {
  PSV.addMarker({
    id: '#' + Math.random(),
    longitude: e.longitude,
    latitude: e.latitude,
    image:'../pin3.png',
    width: 32,
    height: 32,
    anchor: 'bottom center',
    tooltip: 'Generated pin',
    data: {
      generated: true
    }
  });
});

/**
 * Delete a generated marker when the user clicks on it
 */
PSV.on('select-marker', function(marker) {
  if (marker.data && marker.data.generated) {
    PSV.removeMarker(marker);
  }
});
</script>
</body>
</html>
'''

with open('OmoriGroundHighNew.csv') as fo:
    for x in fo.read().split("\n"):
        with open(x+ ".html", 'w')as opf:
            opf.write(s+"<title>"+x+"</title>"+t+"panorama:'"+"./2High/"+x+".jpg',"+p)
            opf.close()

    fo.close()
    logging.info(fo)