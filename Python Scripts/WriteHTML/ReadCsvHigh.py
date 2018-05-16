# This has created files in C:\Users\drake\Downloads\_Omori Low High Res 360 Panorama\Data\examples\2High directory.
s = '''

<!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      '''
t='''
       <link rel="stylesheet" href="../photo-sphere-viewer.min.css">
        <script src="../three.min.js"></script>
        <script src="../D.min.js"></script>
        <script src="../doT.min.js"></script>
        <script src="../uevent.min.js"></script>
        <script src="../CanvasRenderer.js"></script>
        <script src="../Projector.js"></script>
        <script src="../photo-sphere-viewer.min.js"></script>  

  </head>

<body>
 <!--This is calling the space where the photosphere will be on the page-->
<div id="photosphere"></div>

 <!--This is being called by the space where the photosphere will be on the page-->
<script type="text/template" id="lorem-content">
<a href="X1(3).jpg.html"><font color="FF00CC">Kitchen</font></a>
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
      longitude:3.2,//0.2, (0 to 2Pi=6.28)
      latitude: 0,// -0.13770,(-1.57 to 1.57 , 0 horizon)
      image: '../pin2.png',
      width: 32,
      height: 32,
      anchor: 'bottom center',
      tooltip: 'Hotlink. <b>Click me!</b>',
      content: document.getElementById('lorem-content').innerHTML
    },
    {
      // html marker with custom style
      id: 'text',
      longitude: 0,
      latitude: 0,
      html: 'CLICK <a href="X1(3).jpg.html"><font color="FF00CC"><h1>&oplus;</h1></font></a> HERE',
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

  ]
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

with open('highNew.csv') as fo:
    for x in fo.read().split("\n"):

        # X=x-.jpg
        # print(len(x))
        with open(x+ ".html", 'w')as opf:
            opf.write(s+"<title>"+x+"</title>"+t+ "panorama:'" +"./2High/"+ x + "'," + p)
            opf.close()

    fo.close()