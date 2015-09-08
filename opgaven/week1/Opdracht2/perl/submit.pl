#!C:/Tools/Perl64/bin/perl

use Time::Local;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 
use CGI qw(:standard);

$name = param("name");

$birthdateDay = param("birthdate-day");
$birthdateMonth = param("birthdate-month") - 1;
$birthdateYear = param("birthdate-year");

if(not defined $name || $name eq "") {
	print "Location: http://localhost/form.html \n\n";
	exit;
}
else {
	print "content-type: text/html \n\n";
}

@today = localtime();
$time = timelocal(@today);

@birthday = (0, 0, 0, $birthdateDay, $birthdateMonth, $birthdateYear);
$birthtime = timelocal(@birthday);

$seconds = ($time - $birthtime);

$years = int($seconds / 60 / 60 / 24 / 365.25);

print "Hello <u>" . $name . "</u>. You are <strong>" . $years . " years</strong> old!";

print "<br>";
print "<a href=\"/form.html\">Back to form</a>";
