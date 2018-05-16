#Thisd has created files in C:\Users\drake\Downloads\_Omori Low High Res 360 Panorama\Data\examples\2High directory.
s='''
<!DOCTYPE html>
<html>

	<head>
		<meta charset="utf-8" />
		
       <title>Panorama</title>
	
		<meta name="viewport" content="initial-scale=1.0" />
		<script src="three.min.js"></script>
		<script src="photo-sphere-viewer.min.js"></script>
		<style>
			html, body {
				margin: 0;
				width: 100%;
				height: 100%;
				overflow: hidden;
			}

			#container {
				width: 100%;
				height: 100%;
			}
		</style>
	</head>

	<body>
		

<div id="container"></div>
		<script>
			var div = document.getElementById('container');
			var PSV = new PhotoSphereViewer({
			
			
'''
p='''
			
					container: div,
					time_anim: 3000,
					usexmpdata: false,
					navbar: true,
					navbar_style: {
						backgroundColor: 'rgba(58, 67, 77, 0.7)'
					},
				});
		</script>
	</body>

</html>
'''

with open('lowOrig.csv') as fo:
        for x in fo.read().split("\n"):
           # print(len(x))
                with open(x+".html",'w')as opf:
                         opf.write(s+"panorama:'"+"./1Low/"+ x +"',"+p)
                         opf.close()

        fo.close()