#DroidLog

DroidLog is a small Python script that displays all log & error messages produced by a PhoneGap app running on an Android device or emulator.

# How to use

To use, attach you Android device or launch the emulator, then run the script:

	python droidlog.py

The script will then listen for PhoneGap console messages and output them to the screen.
	
You could alternatively make the script executable:

	chmod u+x droidlog.py
	
Then run using:

	./droidlog.py

# License

DroidLog is Copyright &copy; 2012 [Joe Lambert](http://www.joelambert.co.uk) and is licensed under the terms of the [MIT License](http://joelambert.mit-license.org/).