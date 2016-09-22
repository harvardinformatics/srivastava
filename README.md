## earthquake.rc website


### Install pelican and markdown (python 2.7 required)

    pip install pelican markdown beautifulsoup4 icalendar

### Clone the repository:

    git clone git@github.com:brendanjmeade/earthquake.rc.git

### From the root of the project run the conversion with the specified theme:

    cd earthquake.rc 
    pelican content -t `pwd`/theme -o output

### Then go to the output directory and start the server

    cd output && python -m pelican.server

### ..or as a one-liner

    pelican content -t `pwd`/theme -o output && (cd output && python -m pelican.server)

### Should be visible from localhost:8000


### Making live on the website

For updating the web site, check out the files, make your edits, and do a make rsync_upload
You'll want to set SSH_USER to your username

    SSH_USER=myodysseyusername make rsync_upload
