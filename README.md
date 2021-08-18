<p align="center">
<img src="https://github.com/DanielMistrik/Ethereum-Address-Mnemonic/blob/01480605b450a087d4eac6ec2d452508f42a9048/ethMnemonic/MnemGen/static/bigLogo.jpg" width="100" height="100" align="center">
</p>

# 0xD words (Ethereum-Address-Mnemonic)
Turn any Ethereum address into a recognizable and usable mnemonic.<br>
<b>Chrome Optimized</b> - no guarantee about styles in other browsers.<br>
0xd_words - Same repository but some changes to deployment paramaters and the one used by heroku.

## Preface
<p> The inspiration for 0xD words came from the inherent complexity of Ethereum addresses. To ensure availability and prevent two users having the same address the number of possible addresses is incredibly large (> 10<sup>48</sup>). To identify each address in this enormous set Ethereum utilizes the address in hexadecimal form and while this does uniquely identify it, hexadecimal is difficult to remember exactly and prone to small errors, especially when its 40 characters like in Ethereum. Improvements such as EIP-55 checksumm and ENS have improved usability but ENS is a paid service and EIP-55, being a soft fork, isn't implemented universally. </p>
<p> What was needed is a more human-friendly way to define Ethereum addresses. The project what3words were faced with a similair problem for geolocation, coordinates are unwieldy and hard to remember, and solved it with a word mnemonic and this project will as well. Words are natural, easy to remember and one can detect different words better than different characters </p>

## Project Implementation
<p> 0xD words will take an Ethereum address and convert it into a 14-word mnemonic. One might ask why the mnemonic is so large and the simple answer is the size of the set of possible Etheruem addresses.</p>
<p> The process of converting an Ethereum address into a mnemonic starts by taking its hexadecimal, without the 0x prefix, and dividing it into 14 parts of at most 3 hexadecimals. Each part is then converted to a base 10 number and then assigned a word from the wordlist with the index of the number. The wordlist has 4096, 16<sup>3</sup>, words filtered from the oxford 5000 wordlist. The words were filtered to be non-similair and randomly arranged so they aren't in alphabetical order. The words are then arranged into the order of the numbers they were converted from and returned to user seperated by dashes. To convert a mnemonic back into an ethereum address you reverse the steps described above.</p>
<p> The implementation guarantees every ethereum address has a unique and permanent mnemonic attached to it.</p>

## Technical Specification
<p>Below is a description of the files used in the project:</p>

* Proj - Master Directory of entire project
  * ethMnemonic - Django folder responsible for the actual website
    * ethMnemonic - Folder with all the standard Django files for the website as a whole, not alot of unique code added except in urls.py
    * MnemGen - Folder for the actual file app
      * migrations - Django folder the framework uses with databases. Not the projects creation and no project code added in this folder
      * static - The folder for the static images,css and js files
      * templates - The folder for the html files
      * (various Django default .py files that were only lightly edited)
      * models.py - Defines the word list table stored in Django db
      * views.py - The main .py file of the entire project, where all the urls are redirected to html files and most of the EIP-55 checking and mnemonic conversion is done
      * urls.py - Redirects the various functions in views.py to urls.
    * db.sqlite3 - The database for the Django project
    * manage.py - The manage python file for the entire Django project
    * processedWordList.json - The processed word list in Django JSON that can be used in load data on the word list table in the db.  
  * processedWordList.txt - Text file containing the 4096 words used by the project, each line has one word
  * RawWordList.txt - Text file containing the words in the Oxford 5000 word list. 
  * wordListProcessor.py - The python file responsible for filtering and processing the word list.

## External Sources
* Font Awesome

### Additional Notes
The logo was created by me in GIMP 2.10 and no external css/html template was used.
