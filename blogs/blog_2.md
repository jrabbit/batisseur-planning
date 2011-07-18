Some of the clearly amazing things that got done during the community bonding period were:

* [Get Haiku logo](https://github.com/jrabbit/batisseur-planning/blob/master/gethaikudraft-a3.png)
* [Pasteboard (not good yet) Based heavily on examples in BeBook and guidance from Rene Gollent "DeadYak"](https://github.com/jrabbit/batisseur-planning/blob/master/pasteboard.cpp)
* [command not found, trying to make Haiku's bash more user friendly. Will be ready for Alpha 3.](https://github.com/jrabbit/haiku-command-not-found/blob/master/haiku_cnf.py)
* [Haiku trove classifier TBA upon haiku-specific python packages!](https://sourceforge.net/tracker/?func=detail&aid=3306479&group_id=66150&atid=513504)


I also discovered that [Buildbot](http://trac.buildbot.net/) [Mostly its dependency: Twisted] don't play nice on FreeBSD, the platform which currently builds Haiku nightlies on [Matt Madia's server](http://dev.osdrawer.net/projects/haikubuildomatic/). It's not a huge priority to me at this point but it appears a bug still exists and will have to be filed (on my list).

On my list for the first quarter is finishing Command Not Found, and beginning work on the git tools and web services for package developers.[My actual project.] These tools can be developed while the package-fs work is in limbo or hpkgs mature. Command Not Found is a little script (if the install has python) or message that hooks into Bash's command not found system and informs the user of ways to get this software. (i.e. you type in `ruby` but haven't installed it or know that we have `installoptionalpackage ruby`, it will kindly tell you we have it.) Ubuntu has this feature in recent releases, and has an optional feature that may be interesting to use, spelling correction. It will be optional.

Command not found will be a way for users to be educated about Haiku even if they dive straight into the Terminal like a Unix user without reading any documentation [Like me!].
