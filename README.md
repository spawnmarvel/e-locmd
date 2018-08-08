# e-lo the chatbot cmd with NLP using TextBlob
# v 1.1
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
<br>
Mke a env, install requirements.txt
<br>
### Build
First thing to know about cmd.Cmd: you subclass it and customize the subclass to be your command prompt.The methods of this subclass that begin with do_ are now your prompt commands.
<br>
Interface for NLP e-lo
```
class MyCommand(Cmd):

def do_math(self, args):
def do_talk(self, args):
def do_q(self, args):
def do_txt_delete(self, args):
def do_txt_get(self, args):
def do_txt_files(self, args):
def do_txt_index(self, args):
def do_txt_search(self, args):
def do_txt_data(self, args):
```


## ToDo

* Feed e-lo text data: 95%
* Analyze it / NLP: 30%
* Report of data: 30%
* Talk about it: 0%
* Learn about it: 10%


### Prerequisites

TBD

### Code choices

### Installing

Create a virtual env and install all the packets from requirements.txt
## Running the tests
Explain how to run the automated tests for this system
### Break down into end to end tests
Explain what these tests test and why

```
Give an example
```
### And coding style tests
Explain what these tests test and why
```
Give an example
```
## Deployment
Add additional notes about how to deploy this on a live system:


## Built With

*
*
*


## Versioning
Branch: master and test.


## Authors

* **spawnmarvel** - *Initial work* - 


## License


## Acknowledgments

* http://pythontesting.net/framework/unittest/unittest-introduction/
* https://www.analyticsvidhya.com/blog/2018/02/natural-language-processing-for-beginners-using-textblob/














