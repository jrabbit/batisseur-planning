Timeline. Include what you plan to have accomplished by the end of:
 
Community bonding period (May 23) - 
 
*   Buildbot stuff done (should take a week[end])
 
*   Hpkg-Build is in a good place with packages. (No work may need to be done, I haven't stayed on top of how well it works with the package manager implementation.)
 
 
Quarter-term (June 13) - 
 
*   I have  basic storage [via python] into camlistore or some other verifying system. [Allowing users to cryptographically "vouch"]
 
*   Package maintainer scripts start to form around this basic pushing
 
*   Beginning of a "build drone" [python] that listens on the storage mechanism for a new job, uploads results back to the storage. [Could report back to Jenkins]
 
 
Mid-term (July 11) - 
 
*   Build drone can be configured via a webUI built in python
 
*   Build drone communicates pass/failure with logs according user preference, Build drone also begins to use .bep file tests to verify other's package builds.
 
 
Three-quarter-term (August 1) - 
 
*   Wrap this up into a tight package. 
 
*   Make a global scoreboard for the haiku package manager
 
*   wrap a shell script around it like git achievements  http://thechangelog.com/post/1200486354/git-achievements-aquire-achievements-while-using-git
 
*   Build drone will report "scores" as well.
 
*   Scoreboard website will have basic user/password/avatar and groups.
 
*   the web UI for build drone notifies users based on their settings, `notify`, growl, notif.io etc
 
*   git hooks for developers are adjusted to meet feedback
 
 
Pencils down date (August 22) - 
 
*   the websites are polished, and sustainable.
 
*   Any documentation not written happens here. [I suspect there will be a bit but its good to know in advance.]
 
 
After Google Summer of Code - 
 
*   Batisseur [the user exposed parts] gets into Haiku nightlies 
 
*   we see a Haiku Alpha release.