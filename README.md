# hostsPageBlocker
## Description
This simple Python script allows you to easily block URLs by rerouting them to localhost
through the addition of rules in the system's hosts file.  It was designed to provide an effective way to improve 
your **focus** and **productivity** by **blocking distracting websites**.  

## Features
- **Input**: input URLs you wish to block   
- **Support**: Automatically generates all possible URL variations to ensure blocking works (if possible using this method).

## How to run
### Prerequisites
- Python 3.6 or newer
- Administrative privileges

### Example
```sh
C:\> python main.py
Number of pages: 3
Enter URL: example.com
Enter URL: www.testsite.com
Enter URL: https://somewebsite.com

URLs have been successfully blocked!
```

## Future Enhancements
- [x] Add support for Linux
- [x] Improve error handling
- [ ] Add further support to user input
- [ ] Develop a more user-friendly GUI.
- [ ] Add more convenient options of input (e.g. pasting all URLs at once or from a txt file) 
- [ ] Implement a feature of generating larger number of entries, to make it more inconvenient to quickly unlock
 