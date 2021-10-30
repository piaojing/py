# Setting pyhtno web develop environment

# Setting CGI(common gateway interface) environment
open C:\Bitnami\wordpress-5.7.2-0\apache2\conf\httpd.conf
search "mod_cgi.so"
remove "#" to enable it
search "Require all granted" in "DocumentRoot"
YOU NEED CHANGE SOME SETTINGS HERE

input below command next "Require all granted"

<Files "*.py">
  Options ExecCGI # py file excuted by CGI method
  AddHandler cgi-script .py
</Files>

