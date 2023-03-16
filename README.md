# Project-10-Data-Extensions-Concatenator
Concatenate Data Formats. 
Idea 1:
Only first idea, is implemented; For time sake. 
Using Data libraries and OOP principles.

Version: 0.0.1a

Dependency (will give a requirments.txt; currently none. Just python.)

# SDE  
SDE LifeCycle: Watefall Approach.

Software Design: UML Diagrams(considered, not needed in contemporary use cases.)

System Design: Musings. 
    
    - CLI interface, with relevant flags for converting one file format to another, concatenating horizontally and vertically various file formats  intuitively over a cli interface.  
    
    - Sys Design Concepts: Scaling/etc aware, consideration qualitatively and prudently done so: in process of learning. 

Implementation Guidelines: Followed Roughly.

Idea iterations. No connections, no framework, no research, just easy notions.

Program UI: CLI Interface

Programming Paradigm: OOP & Functional (little)

Conceptual notion: Various data extensions - horizontal/vertical concatenation.

Extensions: json, csv, tsv, xml conversion, more semi-structured data. (xslx Excle files to be ) 

Scalability Consideration: One Process, One Thread; No distributed systems/etc. (Other ideas, not considered; as not required for program.)

# Good Practices:
Comments: Before code block, function names; code reads easily. 

Debugging: Conducted. 

Version Control (git)

# Use Scenarios/Examples (Note: `>` (indicates unix shell prompt))
## 1 File extensions are the same (horizontal concatenation. )
> concater -o=data_file2.tsv -file data_file1.xml 
(flag becomes mandatory)
> concater -o= data_file.json -file data_file1.json data_file2.json ... 
#Same usecase, works on following extensions: csv,json,xml, tsv. xlsx(excel can work on systems with openpyxl; not tested.)  
> concater -o= data_file.xml -file data_file1.csv data_file1.json ...

# In Next Version
- Packaging for package managers. 
- Security Consideration: Encrypted Data Handling/When entered. (Other ideas, not considered as need to learn.)
- Concurrency: Multithreading/Multiprocessing/Other Language based features with context and critical tradeoffs, thinking in consideration. 
- Horizontal concatenation by default.
    > concater [ -v ] data_file1.csv datafile2.csv ...
    > concater [ --output/-o=xlsx ] data_file1.tsv data_file2.tsv ...
    > concater --join-type=left-outer

### 2 File extensions differ (2 or more)
> concater  --output/-o=xlsx [-h|-v]  data_file1.csv data_file2.tsv ...
(flag becomes mandatory)

### 3 File extensions same/differ choosing rows and columns
> concater [-col=1-10,2-5,... or 'title1','title2'... -row=100,2-102,...] --o=csv data_file1.json data_file2.csv ...
 -col (if both present last flag/option is kept; either numeric or string based,  not both. )
 -row ( numeric input ).

> concater -show=n datafile1.json datafile2.csv ...
Shows n/2 lines from top and bottom.

Options to consider:
Include-Title
 
### Improvements
    Speed: Could be much much faster. Lower level coding (c); 
    Testing -> pytest/unittest (have to mock it.)

### AIMS Analysis. 
 Purpose/why/problem: Easy Cli format/extensions conversion between different data formats. 
 
 Stakeholder: Data Scientist, Analysts, ML/Data Engineers.
 
 Result: 2 Scenarios, accomplished. 
 
 Succes Criteria: weren't established (next version)

