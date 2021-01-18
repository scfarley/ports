--- make/configure.py.orig	2020-06-13 14:05:35 UTC
+++ make/configure.py
@@ -1409,11 +1409,11 @@ def createCLI( cross = None ):
     grp.add_argument( '--enable-ffmpeg-aac', dest="enable_ffmpeg_aac", default=not host_tuple.match( '*-*-darwin*' ), action='store_true', help=(( 'enable %s' %h ) if h != argparse.SUPPRESS else h) )
     grp.add_argument( '--disable-ffmpeg-aac', dest="enable_ffmpeg_aac", action='store_false', help=(( 'disable %s' %h ) if h != argparse.SUPPRESS else h) )
 
-    h = IfHost( 'Nvidia NVENC video encoder', '*-*-linux*', '*-*-mingw*', none=argparse.SUPPRESS).value
+    h = IfHost( 'Nvidia NVENC video encoder', '*-*-linux*', '*-*-freebsd*', '*-*-mingw*', none=argparse.SUPPRESS).value
     grp.add_argument( '--enable-nvenc', dest="enable_nvenc", default=IfHost( True, '*-*-linux*', '*-*-mingw*', none=False).value, action='store_true', help=(( 'enable %s' %h ) if h != argparse.SUPPRESS else h) )
     grp.add_argument( '--disable-nvenc', dest="enable_nvenc", action='store_false', help=(( 'disable %s' %h ) if h != argparse.SUPPRESS else h) )
 
-    h = IfHost( 'Intel QSV video encoder/decoder', '*-*-linux*', '*-*-mingw*', none=argparse.SUPPRESS).value
+    h = IfHost( 'Intel QSV video encoder/decoder', '*-*-linux*', '*-*-freebsd*', '*-*-mingw*', none=argparse.SUPPRESS).value
     grp.add_argument( '--enable-qsv', dest="enable_qsv", default=IfHost(True, "*-*-mingw*", none=False).value, action='store_true', help=(( 'enable %s' %h ) if h != argparse.SUPPRESS else h) )
     grp.add_argument( '--disable-qsv', dest="enable_qsv", action='store_false', help=(( 'disable %s' %h ) if h != argparse.SUPPRESS else h) )
 
@@ -1676,14 +1676,14 @@ try:
     options.enable_gtk_mingw  = IfHost(options.enable_gtk_mingw, '*-*-mingw*',
                                        none=False).value
     # Disable NVENC on unsupported platforms
-    options.enable_nvenc      = IfHost(options.enable_nvenc, '*-*-linux*',
+    options.enable_nvenc      = IfHost(options.enable_nvenc, '*-*-linux*', '*-*-freebsd*',
                                        '*-*-mingw*', none=False).value
     # NUMA is linux only and only needed with x265
     options.enable_numa       = (IfHost(options.enable_numa, '*-*-linux*',
                                         none=False).value
                                  and options.enable_x265)
     # Disable QSV on unsupported platforms
-    options.enable_qsv        = IfHost(options.enable_qsv, '*-*-linux*',
+    options.enable_qsv        = IfHost(options.enable_qsv, '*-*-linux*', '*-*-freebsd*',
                                        '*-*-mingw*', none=False).value
     # Disable VCE on unsupported platforms
     options.enable_vce        = IfHost(options.enable_vce, '*-*-linux*', '*-*-mingw*',
@@ -2121,9 +2121,9 @@ int main()
     stdout.write( 'Enable FFmpeg AAC:  %s' % options.enable_ffmpeg_aac )
     stdout.write( '  (%s)\n' % note_required ) if host_tuple.system != 'darwin' else stdout.write( '\n' )
     stdout.write( 'Enable NVENC:       %s' % options.enable_nvenc )
-    stdout.write( ' (%s)\n' % note_unsupported ) if not (host_tuple.system == 'linux' or host_tuple.system == 'mingw') else stdout.write( '\n' )
+    stdout.write( ' (%s)\n' % note_unsupported ) if not (host_tuple.system == 'linux' or host_tuple.system == 'freebsd' or host_tuple.system == 'mingw') else stdout.write( '\n' )
     stdout.write( 'Enable QSV:         %s' % options.enable_qsv )
-    stdout.write( ' (%s)\n' % note_unsupported ) if not (host_tuple.system == 'linux' or host_tuple.system == 'mingw') else stdout.write( '\n' )
+    stdout.write( ' (%s)\n' % note_unsupported ) if not (host_tuple.system == 'linux' or host_tuple.system == 'freebsd' or host_tuple.system == 'mingw') else stdout.write( '\n' )
     stdout.write( 'Enable VCE:         %s' % options.enable_vce )
     stdout.write( ' (%s)\n' % note_unsupported ) if not (host_tuple.system == 'linux' or host_tuple.system == 'mingw') else stdout.write( '\n' )
 
