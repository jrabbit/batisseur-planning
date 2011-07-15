<!DOCTYPE html>
<html lang="en">
	<head>
		<!--[if lt IE 9]>
		<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
		<![endif]-->
		<meta charset="utf-8" />
		<title>{{!user}}'s achievements</title>
		<link rel="stylesheet" type="text/css" href="css/main.css" />
		<script src="js/jquery-1.5.2.min.js"></script>
		<!-- <script src="js/jquery-ui-1.8.11.custom.min.js"></script> -->
		<script src='js/main.js'></script>
	</head>
<body>
	<header>
		<h1>HaikuPoints for {{user}}</h1>
	</header>
	<article id="user-info">
		<h2>{{user}}</h2>
		
		{{!achievements}}
	</article>
</body>
</html>