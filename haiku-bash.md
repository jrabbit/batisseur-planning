Command Line Oddities (From my experience and research)
=======================================================

*  	`screen`
* 	all of `installoptionalpackage -l`
*	`ssh-copy-id`
*	`git gui` / `git[k|x]`
*	`pbpaste` (I made one from the Be Book example)
*	top/ps aux -- these exist but don't act how a linux/bsd/Mac user might expect, could flash usage at them.
*	`dig` ?
*	`du -h` versus `df -h` human output flag for du works in du but not in df
*	`free` -- Memory information (linux)
*	`ntp*` -- gui forthcoming but no CLI tool?

How do we tell a user to get a tool?
-------------------------------------
For now tell them to `installoptionalpackage $PACKAGE` if possible. Ubuntu does this currently and is semi useful when you don't typo a program. 

*	["There is a new builtin error-handling function named command_not_found_handle."][#1] 
*	[Information about ubunutu's implementation](https://bugs.launchpad.net/ubuntu/+source/bash/+bug/155899)

Notes
-----
Ubuntu's implementation uses Python, Haiku nightlies don't have python by default. This could change. (Unlikely)

[#1]: http://www.tldp.org/LDP/abs/html/bashver4.html