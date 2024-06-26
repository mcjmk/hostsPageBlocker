# hostsPageBlocker
## Description
This simple Python script allows you to easily block URLs by rerouting them to localhost
through the addition of rules in the system's hosts file.  It was designed to provide an effective way to improve 
your focus and productivity by blocking distracting websites.  

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
Number of pages to block: 2
url: example.com
url: testsite.com
```

## Future Enhancements
- [ ] Develop a more user-friendly GUI.
- [ ] Add more convenient options of input (e.g. pasting all URLs at once or from a txt file) 
- [ ] Implement a feature of generating larger number of entries, to make it more inconvenient to quickly unlock
- [ ] Add support for Linux
- [ ] Improve error handling
 