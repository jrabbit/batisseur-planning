bâtisseur
==========

A build server for all.

* Language: Python
* Targets: HaikuPorts, Fink
* Traits: distributed, group verified, automatic

From a packager's viewpoint:

* Assemble package information (SrcUrl, Description...)
* git add, commit, push
* Test the package
* Repeat until error free
* Push into repo of stable packages

Things that can be done to help packagers:

* git pre-commit hook for validating the hpkg/info file
* Automatic generation of stuff like md5 from the information given (before commit)
* After package passes/fails building, report this somewhere (A custom script passed values) (Like github issues, twitter, growl, haiku notify)


User's perspective:

* A game with points.
* Every build their machine does -> points (Like BOINC projects)
* Certain interactions with the package manager yield achievements 


http://camlistore.org/