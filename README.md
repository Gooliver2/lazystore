# lazystore
Product, to make stores more 'smart'

* Docs: http://docs.lazystore.apiary.io/#
* Test server: https://floating-badlands-43654.herokuapp.com/


##Local Deploy:
##Pre installation:
* docker:
    https://docs.docker.com/install/
    
    Very nice and much easier way described here:
    * https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

* docker-compose:
     https://docs.docker.com/compose/install/#prerequisites
    * ```sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose```
    * ```sudo chmod +x /usr/local/bin/docker-compose```
    * ```docker-compose --version```


## Deploy
* open terminal in project root
* run ```docker-compose up```

If you deploying this for the first time - you have to setup superuser, to be able access Admin site.
For this after ```docker-compose up``` command you should run next command: 
* ```docker-compose exec  web python manage.py createsuperuser```
* set proper username, email and pasword values

# Admin address
Open ```localhost/admin``` address in your browser to get access Admin page. 
