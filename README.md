##Daniel Lee
##Theodore Vixay
##CS587 Project


###Brief Description:
	
	The database implementation will be done with PostgreSQL. The goal of the project is to generate tables within the system and run the Wisconsin benchmark. The results will be compared with other teams that use different systems.
	
	PostgreSQL was chosen as it was free and we have a high degree of familiarity of the system and Microsoft Azure might be implemented at a later date for benchmark comparison.
	
	We designed the code in python due to the random library in python which can generate random and unique integers in a range. The number of tuples generated can be based on changing the "MAXTUPLES" variable.

	Most of the tuples are based off of the unique and random integer. The second tuple is sequential within a range of max tuples. The stringu1 and stringu2 tuples are generated from the first and second unique integer tuple respectively. which changes 'AAAAAAA' record based on the size of the tuple to the power of base 26 which changes the character of each 'A' to a different character. Then for stringu1 and stringu2 tuples have 45 'x's appended to the right of the string. The string4 tuple is a loop of the strings "AAAAxxx...", "HHHHxxx...", "OOOOxxx...", and "VVVVxxx..." which is based on using mod on the count to generate the string.

###Lessons Learned:

	Lesson's learned is to start with a language with a library that can readily create unique and random integers in a range. This is why Python was chosen as the language to generate the input data. The other lesson learned is to set a budget in the Azure platform for notification on spending. Azure also has strong firewall security and resets the IP after each use. The Azure platform also has a suite of applications that are required for the simplest of database interactions. PostgreSQL was the backup platform that is free and is a data base with high familiarity.  