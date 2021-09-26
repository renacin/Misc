/*
Name:                                            Renacin Matadeen
Date:                                               09/26/2021
Title                                      Review Of Core SQL Concepts

----------------------------------------------------------------------------------------------------------------------

Notes:
    Database Normalization
        + Redundant data can come in many forms. In the most common case, it common variables are entered multiple
        times when large form data is appended to a database. Over time data redundancy can waste precious storage
        space, as well as cripple the overall performance of an application

        + Database Normalization is the main process to combat data redundancy in databases. Put simply, Database 
        Normalization is the process of decomposing larger tables, into smaller ones in order to ensure similar
        attributes are grouped together and redundancy is removed.


        Anomalies That Normalization Tries To Avoid:
            Insertion Anomalies
                + Caused by inserting the same set of repeating information again, and again
                + Increases space complexity over time
                + Example: Having School attributes repeated over and over everytime a student is added to a database

            Deletion Anomalies
                + Causes loss of data when deleting certain information. 
                + Example: Deleting School Principle information, and removing entries that relied on complete forms with
                non-null values

            Updating Anomalies
                + Causes inconsistencies in data when updating certain attributes
                + Example: Updating School Phone-Number in a large CSV. How would you easily, quickly, confidently change
                that information?


        Database Normalization Concepts
            Keys: 
                + Column attributes that identify a database record uniquely

            Functional Dependencies: 
                + Constraints between two attributes in a relation.
                + Example: EMP_NAME, EMP_CONTACT, EMP_ADDRESS --> Depend On EMP_ID

            Partial Dependencies:
                + Is a type of functional dependency that occurs when non-prime attributes are partially
                dependent on part of candidate keys

            Normal Forms: 
                + Steps to accomplish a certain quality of a database.


        Levels Of Database Normalization [Normal Forms]:
            Unnormalized Form (UNF)
                + The state before any normalization. Redundant and complex values are present.
                + Nothing has been changes. Similar to raw CSV data with non-atomic values. 

            First Normal Form (1NF)
                + Repeating and complex values split up, making all instances atomic.
                + Do not keep multiple values under in one cell
                + Example: Magazine Subscription [Basketball, Soccer, Golf]
                + Database is considered in poor condition if 1NF not met

            Second Normal Form (2NF)
                + First 1NF conditions must be met
                + Tables should not have partial dependencies
                + Partial dependencies must be decomposed into new tables
                + All rows functionally depend on the primary key.
            
            
            
            Third Normal Form (3NF)            Transitive dependencies decompose to new tables. Non-key attributes depend on the primary key.
            Boyce-Codd Normal Form (BCNF)      Transitive and partial functional dependencies for all candidate keys decompose to new tables.
            Fourth Normal Form (4NF)           Removal of multivalued dependencies.
            Fifth Normal Form (5NF)            Removal of JOIN dependencies.


        Ex:
            School & Student Grades Database [1 Table In Database]
            Attributes: [School Name, School Location, School Principle, School Trustee, Student Number, Days Missed, Overall Grade]
            
            Table #1
            - Fletcher's Meadow, Brampton, John Doe, Jane Doe, 500123456, 2, B+
            - Fletcher's Meadow, Brampton, John Doe, Jane Doe, 500123236, 3, A+
            - Fletcher's Meadow, Brampton, John Doe, Jane Doe, 500567456, 10, B-

            School & Student Grades Database [2 Table In Database]
            Attributes: [School Name, School Location, School Principle, School Trustee, School Number(NEW)]
            Attributes: [Student Number, Days Missed, Overall Grade, School Number(NEW)]
            
            Table #1
            - 500123456, 2, B+, 0001
            - 500123236, 3, A+, 0001
            - 500567456, 10, B-, 0001

            Table #2
            - Fletcher's Meadow, Brampton, John Doe, Jane Doe, 0001

            Redundancy Removed:
                = 15 (REMOVED) + 4 (ADDED)
                = 11 (REMOVED)

*/