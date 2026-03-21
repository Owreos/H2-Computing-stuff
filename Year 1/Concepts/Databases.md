Databases are a type of organised collection of structure info, typically stored digitally
 It can be managed via a DBMS application 
### Types of Databases:
* *Flat file database*
	* Stores files in single table
	* Plain text
	* Each line holds one record
	* Separated using delimiters
* *Hierarchical database:*
	* Parent child type tree like database
	* Can only have one parent
	* Can have multiple children
	* includes information about parent/child relations
	* EH: binary trees
* *Network database:*
	* Similar to hierarchical databases
	* Many to many relationship:
		* Multiple children and parents
* ***Relational database:***
	* Set of tables with columns and rows:
	* Something like the base SQL
	*  Linked via primary and foreign keys
* *Object oriented databases:*
	* Database that subscribes to a model of info represented by objects
		Trees?
* *NoSQL:* 
	* non relational database 
	* unstructured/semi structured data

**DBMS** known as Database management system
* Serves as interface between database and user/program
* Allows user to retrieve update, and manage database info
* Administrative abilities:
	performance monitoring
	tuning
	backup
	recovery
* EG:
	MS Access
	MS SQL server
	MySQL
	Oracle database
	PostgreSQL(the elephant...?)
	SQLite

### Database structure:
![[Pasted image 20250307200644.png]]
Databases are a type of storage that follows the following Rules
- External level(user view)
	- Database relevant to a particular user
	- Excludes irrelevant info
- Conceptual level
	- Specifies database info:
		- What data is stored within?
		- What data is related to each other
	- However, this does not control how the data is physically stored.
- Internal level:
	- specifies database metadata:
		- How is data stored on the computer itself?

Why
- Users:
	- Users access a customised version of the data
	- Each user's view is independent of another's
	- Users should not have to care about how the database itself is stored 
- Administrators:
	- Changing storage structure will not affect user view
	- Internal layer shenanigans(as in file management stuff) will not affect physical storage
	
Database vs File based:
- Program data independence: DB file is stored separately from the file itself
- Support multiple views
- Atomic, consistent, isolated and durable
	- Atomic: changes can be done in a single operation
	- Consistency: data is in a consistent state at the start and end of operation
	- Isolation: operation should be invisible to other operations(concurrent operations are serialized)
	- Durability: changes persist after saving

Advantages and disadvantages of DBMS:
* High initial costs/hardware
- Database is simple and does not need to be changed(say a word bank for jlkm fun or something)
- no multiple access needed
- speed requirements not met by DBMS
- special operations not supported by the DBMS.
